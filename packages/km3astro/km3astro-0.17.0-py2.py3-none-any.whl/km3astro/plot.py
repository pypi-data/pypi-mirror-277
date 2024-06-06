"""Plotting utilities.
"""
from astropy.units import degree

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import healpy as hp
from datetime import timedelta
import warnings

import astropy.units as u
from astropy.coordinates import SkyCoord
from astropy.coordinates import ICRS, Galactic, FK4, FK5  # Low-level frames

from astropy.time import Time

from km3net_testdata import data_path

import km3astro.coord as kc
import km3astro.frame as kf
import km3astro.toolbox as kt
import km3astro.extras as ke
import tempfile
import os


def ra_dec(skycoord):
    """Take (ra, dec) from skycoord in matplotlib-firendly format.

    This wraps the ra because astropy's convention differs from matplotlib.
    """
    ra = skycoord.ra.wrap_at(180 * degree).radian
    dec = skycoord.dec.radian
    return ra, dec


def projection_axes(projection="aitoff", **figargs):
    fig = plt.figure(**figargs)
    ax = fig.add_subplot(111, projection=projection)
    ax.grid(color="lightgrey")
    return fig, ax


def plot_equatorial(
    evts,
    projection="aitoff",
    ax=None,
    marker="o",
    markersize=4,
    alpha=0.8,
    adjust_subplots=True,
    **kwargs,
):
    ra, dec = ra_dec(evts)
    if ax is None:
        _, ax = projection_axes(projection=projection)
    ax.plot(ra, dec, marker, markersize=markersize, alpha=alpha, **kwargs)
    if adjust_subplots:
        plt.subplots_adjust(top=0.95, bottom=0.0)
    return ax


def get_coord_from_skycoord(SC, frame, detector):
    """Return the coordinate of a SkyCoord object for aitoff or mollweide projection

    Parameters
    ----------
    SC : astropy.SkyCoord
        The sky coordinate.
    frame : str
        The frame of the coordinate, either "ParticleFrame" or "UTM" or "altaz" or "equatorial" or "galactic"
    detector : str [default = "antares"]
        Detector of the coordinate, either "orca", "arca" or "antares".

    Returns
    -------
    (phi, theta)/(az, ze)/(alt, az)/(ra, dec)/(l, b) : (float, float)
        The set of coordinate.

    """
    SC_copy = kc.transform_to(SC, frame, detector)

    if frame == "ParticleFrame":
        phi = SC_copy.phi.wrap_at(180 * u.deg).radian

        theta = SC_copy.theta.radian

        if type(theta) == np.float64:
            if theta > np.pi / 2:
                theta = theta - np.pi

        if type(theta) == np.ndarray:
            print(len(theta))
            for idx, t in enumerate(theta):
                if t > np.pi / 2:
                    theta[idx] = t - np.pi

        return phi, theta

    elif frame == "UTM":
        az = SC_copy.azimuth.wrap_at(180 * u.deg).radian
        ze = SC_copy.alt_utm.radian
        return az, ze

    elif frame == "altaz":
        alt = SC_copy.alt.radian
        az = SC_copy.az.wrap_at(180 * u.deg).radian
        return alt, az

    elif frame == "equatorial":
        ra = SC_copy.ra.wrap_at(180 * u.deg).radian
        dec = SC_copy.dec.radian
        return ra, dec

    elif frame == "galactic":
        l = SC_copy.l.wrap_at(180 * u.deg).radian
        b = SC_copy.b.radian
        return l, b

    else:
        raise ValueError("Error: Wrong Frame input frame")
        return None


def get_alert_color(alert_type):
    """Return the color for a specific alert_type
    Based on color list tab:Palette 10
    """

    Alert_color_dict = {
        "GRB": "tab:blue",
        "GW": "tab:orange",
        "Neutrino": "tab:green",
        "NuEM": "tab:red",
        "SK_SN": "tab:purple",
        "SNEWS": "tab:brown",
        "Transient": "tab:pink",
    }

    if alert_type in Alert_color_dict.keys():
        return Alert_color_dict[alert_type]
    else:
        return "c"


def get_alert_marker(alert_type):
    """Return the marker style for a specific alert_type"""

    Alert_marker_dict = {
        "GRB": "o",
        "Neutrino": "^",
        "NuEM": "v",
        "SK_SN": "*",
        "SNEWS": "*",
        "Transient": "s",
    }

    if alert_type in Alert_marker_dict.keys():
        return Alert_marker_dict[alert_type]
    else:
        return "."


def get_visibility_map(frame, detector):
    """Get the visibility map for a given frame ('equatorial' or 'galactic') and a given detector ('antares', 'orca' or 'arca')."""

    path = f"{os.path.dirname(os.path.abspath(__file__))}/data/visibility_map_{frame}_{detector}.npy"

    if os.path.isfile(path):
        visibility_map = np.load(path)
    else:
        nside = 128
        npix = hp.nside2npix(nside)
        t0, t1 = Time("2022-01-01T00:00:00"), Time("2022-01-02T00:00:00")
        visibility_map = np.zeros(npix)
        lon, lat = hp.pix2ang(nside, range(npix), lonlat=True)
        if frame == "equatorial":
            coords = SkyCoord(ra=lon * u.deg, dec=lat * u.deg, frame="icrs")
        elif frame == "galactic":
            coords = SkyCoord(l=lon * u.deg, b=lat * u.deg, frame="galactic")
        t = t0
        dt = u.Quantity("10 minute")
        ntimes = 0
        while t < t1:
            frame = kc.local_frame(time=t, location=detector)
            coords_loc = coords.transform_to(frame)
            visibility_map[coords_loc.alt.deg > 0] += 1
            t += dt
            ntimes += 1
        visibility_map /= ntimes
        np.save(path, visibility_map)

    return visibility_map


def skymap_hpx(
    skymap_url: str = None,
    obstime: str = None,
    nside: int = 128,
    detector: str = "antares",
    outfile: str = None,
    **old_kwargs,
):
    """Method to plot a skymap from an FITS url.

    Parameters
    ----------
    skymap_url : str
        URL of the FITS skymap.
    obstime : str
        Alert time in ISOT format.
    nside : int
        Resolution of the map to be drawn (higher = more precise but slower).
    detector : str
        The detector to use for horizon definition. Choices are antares, orca, and arca.
    outfile : str
        Path to the output file. If None, no file is written.
    **old_kwards: dict
        [TO BE DEPRECATED] Arguments used by the old function: (file0, save=False, path="", name="")

    Returns:
    Fig : file.png
       A png file of the skymap.
    """

    # === SECTION TO BE DEPRECATED ===
    # Handling of old plotting function
    if len(old_kwargs) > 0:
        warnings.warn(
            "The old 'skymap_hpx' method will be replaced, see documentation.",
            DeprecationWarning,
        )

        file0 = old_kwargs.get("file0")
        save = old_kwargs.get("save", False)
        path = old_kwargs.get("path", "")
        name = old_kwargs.get("name", "")

        projection = "mollweide"
        fig, ax = projection_axes(projection=projection, figsize=[40 / 2.54, 30 / 2.54])

        gw_map = hp.read_map(file0)
        hp.mollview(map=gw_map, fig=fig)
        hp.graticule()

        if save:
            if path != "":
                if name == "":
                    name = os.path.join(path.name, f"skymap_hpx_test.png")
                else:
                    name = os.path.join(path.name, f"{name}.png")
            else:
                path = tempfile.TemporaryDirectory()
                if name == "":
                    name = "hpx_skymap_maker_test.png"
                plt.savefig(name)

        return fig
    # === END OF SECTION TO BE DEPRECATED ===

    assert skymap_url is not None and obstime is not None
    io, postprocess = ke.ligoskymap()
    obstime = Time(obstime, format="isot")

    skymap = io.fits.read_sky_map(skymap_url, nest=False)[0]
    # downgrade a bit the resolution to make it quicker
    skymap = hp.ud_grade(skymap, nside)
    npix = hp.nside2npix(nside)

    # Prepare contours
    cls_skymap = 100 * postprocess.find_greedy_credible_levels(skymap / np.sum(skymap))

    # Prepare horizon (darkens the half of the sky that is above horizon)
    ra, dec = hp.pix2ang(nside, range(npix), lonlat=True)
    coords = SkyCoord(ra=ra * u.deg, dec=dec * u.deg, frame="icrs")
    frame = kc.local_frame(time=obstime, location=detector)
    coords = coords.transform_to(frame)
    horizon = -1 * np.ones_like(skymap)
    horizon[np.sin(coords.alt.rad) > 0] = 1

    # Prepare the figure
    fig = plt.figure(figsize=(9, 5.3))
    ax = plt.axes([0.00, 0.15, 1, 0.78], projection="astro degrees mollweide")
    # Plot skymap and its contour
    ax.imshow_hpx(skymap, cmap=plt.get_cmap("Blues"))
    ax.contour_hpx(
        (cls_skymap, "ICRS"),
        colors=["blue", "blue"],
        linewidths=[1, 1],
        linestyles=[":", "-"],
        levels=(50, 90),
    )
    # Plot horizon
    ax.imshow_hpx(
        horizon,
        cmap=matplotlib.colors.ListedColormap(["white", "grey"]),
        vmin=0.0,
        vmax=1.0,
        alpha=0.3,
    )
    # Axis configuration
    ax.grid()
    ax.set_facecolor("none")
    for key in ["ra", "dec"]:
        ax.coords[key].set_auto_axislabel(False)

    # Draw custom legend
    handles = []
    handles.append(
        matplotlib.lines.Line2D(
            [], [], color="blue", linewidth=1, linestyle=":", label="50% contour"
        )
    )
    handles.append(
        matplotlib.lines.Line2D(
            [], [], color="blue", linewidth=1, linestyle="-", label="90% contour"
        )
    )
    handles.append(
        matplotlib.patches.Patch(
            edgecolor="black",
            facecolor="grey",
            alpha=0.30,
            label=r"Region above horizon at $t_{alert}$",
        )
    )
    fig.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.50, 0.10), ncol=3)
    fig.suptitle("Equatorial coordinates", fontsize=16)
    if outfile is not None:
        fig.savefig(outfile, dpi=300)

    return fig


def skymap_list(
    dataframe: pd.DataFrame = pd.DataFrame(),
    frame: str = "equatorial",
    frame_input: str = "equatorial",
    detector: str = "antares",
    outfile: str = None,
    **old_kwargs,
):
    """Method to plot a skymap from a list of alert in a csv file.

    Parameters
    ----------
    dataframe = pd.DataFrame()
        The dataframe containing the list of alert.
    frame : str [default = "equatorial"]
        The frame of the skymap, either "equatorial" or "galactic".
    frame_input : str [default = "equatorial"]
        The frame of the input data, either "equatorial" or "galactic".
    detector : str [ default = "antares"]
        The detector to be used for eventual input and for horizon.
    outfile : str
        Path to the output file. If None, no file is written.
    **old_kwards: dict
        [TO BE DEPRECATED] Arguments used by the old function: (file0, plot_frame, detector_to, alt_cut, title, save, path, name)

    Returns:
    Fig : file.png
       A png file of the skymap.
    """

    # === SECTION TO BE DEPRECATED ===
    # Handling of old plotting function
    if len(old_kwargs) > 0:
        warnings.warn(
            "The old 'skymap_list' method will be replaced, see documentation.",
            DeprecationWarning,
        )

        file0 = old_kwargs.get("file0", "")
        plot_frame = old_kwargs.get("plot_frame", "equatorial")
        detector_to = old_kwargs.get("detector_to", "antares")
        alt_cut = old_kwargs.get("alt_cut", 5.7)
        title = old_kwargs.get("title", "")
        save = old_kwargs.get("save", False)
        path = old_kwargs.get("path", "")
        name = old_kwargs.get("name", "")

        projection = "aitoff"
        fig, ax = projection_axes(projection=projection, figsize=[40 / 2.54, 30 / 2.54])

        if file0 != "":
            table_read = pd.read_csv(file0, comment="#")
            table_skycoord = kt.build_skycoord_list(table_read, frame, detector)

        elif dataframe.empty == False:
            table_skycoord = kt.build_skycoord_list(dataframe, frame_input, detector)
            if "Alert_type" in dataframe.columns:
                extracted_column = dataframe["Alert_type"]
                table_skycoord = table_skycoord.join(extracted_column)

        else:
            file0 = data_path("astro/antares_coordinate_systems_benchmark.csv")
            table_skycoord = kt.build_skycoord_list(table_read, frame, detector)

        plot_pd_skycoord(table_skycoord, plot_frame, detector_to, projection, ax)
        plot_visibility(ax=ax, frame=plot_frame, detector=detector_to)

        if title == "":
            title = detector + " Alert List " + plot_frame + " frame skymap"
        ax.set_title(title, fontsize=20, y=1.1)
        xlabel, ylabel = get_label(plot_frame)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        if "Alert_type" in table_skycoord.columns:

            h = []
            check_list = []

            for it in table_skycoord["Alert_type"]:

                if it not in check_list:
                    check_list.append(it)

                    alert = mlines.Line2D(
                        [],
                        [],
                        color=get_alert_color(it),
                        marker=".",
                        markersize=10,
                        label=it,
                    )

                    h.append(alert)

            plt.legend(handles=h, bbox_to_anchor=(1.1, 1.2), loc="upper right")

        if save:
            if path != "":
                if name == "":
                    name = os.path.join(
                        path.name, f"skymap_list_{detector}_test_{plot_frame}.png"
                    )
                else:
                    name = os.path.join(path.name, f"{name}.png")
            else:
                path = tempfile.TemporaryDirectory()
                if name == "":
                    name = "skymap_list_" + detector + "_test_" + plot_frame + ".png"
            plt.savefig(name)
        return fig
    # ===END OF SECTION TO BE DEPRECATED ===

    if not dataframe.empty:
        detector = "antares"
        table_skycoord = kt.build_skycoord_list(dataframe, frame_input, detector)
        if "Alert_type" in dataframe.columns:
            extracted_column = dataframe["Alert_type"]
            table_skycoord = table_skycoord.join(extracted_column)
        table_skycoord["SkyCoord_base"] = table_skycoord["SkyCoord_base"].map(
            lambda x: kc.transform_to(x, frame, detector)
        )
    else:
        table_read = pd.read_csv(
            data_path("astro/antares_coordinate_systems_benchmark.csv"), comment="#"
        )
        table_skycoord = kt.build_skycoord_list(table_read, frame_input, detector)
        table_skycoord["SkyCoord_base"] = table_skycoord["SkyCoord_base"].map(
            lambda x: kc.transform_to(x, frame, detector)
        )

    ke.ligoskymap()

    if frame not in ["galactic", "equatorial"]:
        raise RuntimeError(f"Unknown frame type {frame}")
    aframe = "icrs" if frame == "equatorial" else "galactic"

    # Prepare figure
    fig = plt.figure(figsize=(9, 5.3))
    ax = plt.axes(
        [0.00, 0.15, 1, 0.78],
        projection="%s degrees mollweide"
        % ("astro" if frame == "equatorial" else "geo"),
    )
    # Plot point-source
    for _, alert in table_skycoord.iterrows():
        if frame == "equatorial":
            ax.scatter(
                alert["SkyCoord_base"].ra.deg,
                alert["SkyCoord_base"].dec.deg,
                s=100,
                marker=get_alert_marker(alert.get("Alert_type", ".")),
                color=get_alert_color(alert.get("Alert_type", "black")),
                transform=ax.get_transform("icrs"),
            )
        elif frame == "galactic":
            ax.scatter(
                alert["SkyCoord_base"].l.deg,
                alert["SkyCoord_base"].b.deg,
                s=50,
                marker=get_alert_marker(alert.get("Alert_type", ".")),
                color=get_alert_color(alert.get("Alert_type", "black")),
                transform=ax.get_transform("itrs"),
            )

    # Axis configuration
    ax.grid()
    ax.set_facecolor("none")
    for key in ["ra", "dec", "longitude", "latitude"]:
        if key in ax.coords:
            ax.coords[key].set_auto_axislabel(False)

    # Draw custom legend
    if "Alert_type" in table_skycoord:
        handles = []
        for alert_type in np.unique(table_skycoord["Alert_type"]):
            handles.append(
                matplotlib.lines.Line2D(
                    [],
                    [],
                    color=get_alert_color(alert_type),
                    marker=get_alert_marker(alert_type),
                    markersize=10,
                    linewidth=0,
                    label=alert_type,
                )
            )
        fig.legend(
            handles=handles, loc="upper center", bbox_to_anchor=(0.50, 0.13), ncol=4
        )

    fig.suptitle(frame.capitalize() + " coordinates", fontsize=16)
    if outfile is not None:
        fig.savefig(outfile, dpi=300)

    return fig


def skymap_alert(
    ra: float = None,
    dec: float = None,
    obstime: str = None,
    error_radius: float = None,
    frame: str = "equatorial",
    detector: str = "antares",
    outfile: str = None,
    **old_kwargs,
):
    """Method to plot a skymap from an alert in a csv file or by giving RA, DEC and obstime.

    Parameters
    ----------

    ra, dec : (float,float)
        The ra and dec coordinate of the alert.
    obstime : str
        The observation time of the alert. Format is "YYYY-MM-DDTHH:MM:SS"
    error_radius : float [default = None]
        The radius of the error circle around the alert coordinate.
    frame : str [default = "equatorial"]
        The frame of the map.
    detector : str [default = "antares"]
        The detector to use for horizon definition and coordinate transformation. Choices are antares, orca, and arca.
    outfile : str
        Path to the output file. If None, no file is written.
    **old_kwards: dict
        [TO BE DEPRECATED] Arguments used by the old function: (file0, plot_frame, detector_to, alt_cut, title, save, path, name)

    Returns:
    Fig : file.png
       A png file of the skymap.
    """

    # === SECTION TO BE DEPRECATED ===
    # Handling of old plotting function
    if len(old_kwargs) > 0:
        warnings.warn(
            "The old 'skymap_alert' method will be replaced, see documentation.",
            DeprecationWarning,
        )

        file0 = old_kwargs.get("file0", "")
        plot_frame = old_kwargs.get("plot_frame", "equatorial")
        detector_to = old_kwargs.get("detector_to", "antares")
        alt_cut = old_kwargs.get("alt_cut", 5.7)
        title = old_kwargs.get("title", "")
        save = old_kwargs.get("save", False)
        path = old_kwargs.get("path", "")
        name = old_kwargs.get("name", "")

        use_coord = False
        use_file = False
        if file0 != "":
            use_file = True
        if ra != None and dec != None and obstime != None:
            use_coord = True
        if use_coord == False and use_file == False:
            file0 = data_path("astro/antares_moon_sun_position_benchmark.csv")
            ra = 80
            dec = 15
            obstime = "2022-06-15T03:03:03"
            use_coord = True
            use_file = True

        projection = "aitoff"
        fig, ax = projection_axes(projection=projection, figsize=[40 / 2.54, 30 / 2.54])

        if use_file == True:
            table_read = pd.read_csv(file0, comment="#")
            table_skycoord = kt.build_skycoord_list(table_read, frame, detector)
            obstime = get_obstime(table_skycoord)
            plot_file(file0, ax, projection, frame, detector, plot_frame, detector_to)

        if use_coord == True:
            alert = SkyCoord(
                ra=ra * u.degree, dec=dec * u.degree, obstime=obstime, frame="icrs"
            )
            if error_radius is not None:
                theta = np.linspace(0, 2 * np.pi, 360)
                ra = ra + error_radius * np.cos(theta)
                dec = np.fmax(-90, np.fmin(90, dec + error_radius * np.sin(theta)))
                error = SkyCoord(
                    ra=ra * u.degree, dec=dec * u.degree, obstime=obstime, frame="icrs"
                )
                plot_SkyCoord(
                    error,
                    frame=plot_frame,
                    detector=detector_to,
                    projection=projection,
                    ax=ax,
                    marker=".",
                    markersize=1,
                    color="royalblue",
                )

            plot_SkyCoord(
                alert,
                frame=plot_frame,
                detector=detector_to,
                projection=projection,
                ax=ax,
                marker=".",
                markersize=10,
                linewidth=0,
                color="royalblue",
                label=get_Sky_label(alert, plot_frame, detector_to, time=False),
            )

        horizon = get_horizon(
            detector=detector_to, time=obstime, frame=plot_frame, alt_cut=alt_cut
        )

        plot_SkyCoord(
            horizon,
            frame=plot_frame,
            detector=detector_to,
            projection=projection,
            ax=ax,
            marker=".",
            markersize=10,
            linewidth=0,
            color="darkgreen",
        )

        gal_plan = get_galactic_plan(
            detector=detector_to, time=obstime, frame=plot_frame
        )
        plot_SkyCoord(
            gal_plan,
            frame=plot_frame,
            detector=detector_to,
            projection=projection,
            ax=ax,
            marker=".",
            markersize=10,
            linewidth=0,
            color="darkred",
        )

        date, time = str(obstime).split("T", 1)

        if title == "":
            title = (
                detector + " Alert " + plot_frame + " frame skymap " + date + " " + time
            )
        ax.set_title(title, fontsize=20, y=1.1)
        xlabel, ylabel = get_label(plot_frame)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        horizon_line = mlines.Line2D(
            [], [], color="lime", marker=".", markersize=1, label="Horizon"
        )
        gal_line = mlines.Line2D(
            [], [], color="red", marker=".", markersize=1, label="Galactic plan"
        )

        h, l = ax.get_legend_handles_labels()
        h.append(horizon_line)
        h.append(gal_line)

        plt.legend(handles=h, bbox_to_anchor=(1.1, 1.2), loc="upper right")

        if save:
            if path != "":
                if name == "":
                    name = os.path.join(
                        path.name, f"skymap_alert_{detector}_test_{plot_frame}.png"
                    )
                else:
                    name = os.path.join(path.name, f"{name}.png")

            else:
                path = tempfile.TemporaryDirectory()
                if name == "":
                    name = "skymap_alert_" + detector + "_test_" + plot_frame + ".png"

            plt.savefig(name)

        return fig
    # ===END OF SECTION TO BE DEPRECATED ===

    assert ra is not None and dec is not None and obstime is not None

    ke.ligoskymap()

    if frame not in ["galactic", "equatorial"]:
        raise RuntimeError(f"Unknown frame type {frame}")
    aframe = "icrs" if frame == "equatorial" else "galactic"

    obstime = Time(obstime, format="isot")
    skycoord_eq = SkyCoord(ra=ra * u.deg, dec=dec * u.deg, frame="icrs")
    skycoord_frame = kc.transform_to(skycoord_eq, frame, detector)

    # Prepare horizon (darkens the half of the sky that is above horizon)
    nside = 512
    npix = hp.nside2npix(nside)
    p_frame, t_frame = hp.pix2ang(nside, range(npix), lonlat=True)
    coords = SkyCoord(p_frame * u.deg, t_frame * u.deg, frame=aframe)
    coords_loc = coords.transform_to(kc.local_frame(time=obstime, location=detector))
    horizon = -1 * np.ones(npix)
    horizon[np.sin(coords_loc.alt.rad) > 0] = 1
    # Prepare error circle
    if error_radius is not None:
        dist = coords.separation(skycoord_frame)
        mapcircle = np.zeros(hp.nside2npix(nside))
        mapcircle[dist.deg <= error_radius] = 1
    # Prepare galactic plane
    coords_gal = kc.transform_to(coords, "galactic", detector)
    galplane = -1 * np.ones(npix)
    galplane[np.abs(coords_gal.b.deg) < 2] = 1

    # Prepare figure
    fig = plt.figure(figsize=(9, 5.3))
    ax = plt.axes(
        [0.00, 0.15, 1, 0.78],
        projection="%s degrees mollweide"
        % ("astro" if frame == "equatorial" else "geo"),
    )
    # Plot horizon
    ax.imshow_hpx(
        horizon,
        cmap=matplotlib.colors.ListedColormap(["white", "grey"]),
        vmin=0.0,
        vmax=1.0,
        alpha=0.3,
    )
    # Plot galactic plane
    ax.imshow_hpx(
        galplane,
        cmap=matplotlib.colors.ListedColormap(["white", "red"]),
        vmin=0.0,
        vmax=1.0,
        alpha=0.4,
    )
    # Plot point-source
    if frame == "equatorial":
        ax.scatter(
            skycoord_frame.ra.deg,
            skycoord_frame.dec.deg,
            marker="+",
            color="blue",
            transform=ax.get_transform("icrs"),
        )
    elif frame == "galactic":
        ax.scatter(
            skycoord_frame.l.deg,
            skycoord_frame.b.deg,
            marker="+",
            color="blue",
            transform=ax.get_transform("itrs"),
        )
    if error_radius is not None:
        ax.imshow_hpx(
            mapcircle,
            cmap=matplotlib.colors.ListedColormap(["white", "blue"]),
            alpha=0.4,
            vmin=0,
            vmax=1,
        )
    # Axis configuration
    ax.grid()
    ax.set_facecolor("none")
    for key in ["ra", "dec", "longitude", "latitude"]:
        if key in ax.coords:
            ax.coords[key].set_auto_axislabel(False)

    # Draw custom legend
    handles = []
    handles.append(
        matplotlib.lines.Line2D(
            [], [], color="blue", linewidth=0, marker="+", label="Alert position"
        )
    )
    if error_radius is not None:
        handles.append(
            matplotlib.patches.Patch(facecolor="blue", alpha=0.4, label="Error radius")
        )
    handles.append(
        matplotlib.patches.Patch(
            edgecolor="black",
            facecolor="grey",
            alpha=0.3,
            label=r"Region above horizon at $t_{alert}$",
        )
    )
    handles.append(
        matplotlib.patches.Patch(
            edgecolor="darkred", facecolor="red", alpha=0.4, label="Galactic plane"
        )
    )
    fig.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.50, 0.13), ncol=2)
    fig.suptitle(frame.capitalize() + " coordinates", fontsize=16)
    if outfile is not None:
        fig.savefig(outfile, dpi=300)

    return fig
