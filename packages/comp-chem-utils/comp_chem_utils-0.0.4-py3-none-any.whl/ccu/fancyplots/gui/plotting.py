"""Functions for plotting free energy diagrams.

The main function is :func:`ccu.fancyplots.gui.plotting.generate_figure`.

Examples:
    >>> from ccu.fancyplots.data import DEFAULT_PARAMETERS
    >>> from ccu.fancyplots.data import FEDData
    >>> from ccu.fancyplots.gui.plotting import generate_figure
    >>> energy_data = [[0.0, 1.5, 0.5]]
    >>> data = FEDData(
    ...     energy_data=energy_data,
    ...     mechanism=["*", "*H", "H2"],
    ...     legend_labels=["Cu(111)"],
    ... )
    >>> generate_figure(data, DEFAULT_PARAMETERS, visual=True)

"""

import logging
from typing import TYPE_CHECKING

import matplotlib

from ccu.fancyplots.data import DEFAULT_PARAMETERS
from ccu.fancyplots.data import Annotation
from ccu.fancyplots.data import FEDData
from ccu.fancyplots.gui.utils import print_easter_egg

matplotlib.use("Agg")

from matplotlib import axes
from matplotlib import figure
from matplotlib import rc
from matplotlib.legend_handler import HandlerLine2D
import matplotlib.lines
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib.ticker import FormatStrFormatter
import numpy as np

if TYPE_CHECKING:
    from ccu.fancyplots.data import FormattingParameters

logger = logging.getLogger(__name__)


_INVALID_TS_PATHWAY_MSG = (
    "Unable to bracket the transition step. There is "
    "no elementary reaction step defined {0} the reaction step."
)
_DEFAULT_COLOR = "k"


# TODO? what does this mean?
# This fixes the legend's vertical space issue - where when subscripts are used and 2 or more columns, white space between lines are not consistent.
# One has to change the ration of the height (xx) in case it is not properly aligned for some specific case.
# This class is not being used anywhere yet. Usage example : plt.legend(handler_map={matplotlib.lines.Line2D: SymHandler()},
#                                                            fontsize='xx-large', ncol=2,handleheight=2.4, labelspacing=0.05)
class SymHandler(HandlerLine2D):  # noqa: D101
    def create_artists(  # noqa: D102
        self,
        legend,
        orig_handle,
        xdescent,
        ydescent,  # noqa: ARG002
        width,
        height,
        fontsize,
        trans,
    ):
        xx = 0.6 * height
        return super().create_artists(
            legend, orig_handle, xdescent, xx, width, height, fontsize, trans
        )


def create_axes(
    parameters: "FormattingParameters", *, visual: bool = True
) -> tuple[axes.Axes, figure.Figure]:
    """Create the primary axes for plotting free energy diagrams.

    Args:
        parameters: The formatting parameters to use to plot the diagram
        visual: Whether or not to display the image. If True, the figure will
            be saved to file instead of displayed.

    Returns:
        A 2-tuple (``ax``, ``fig``) whose first and second elements are the
        primary axes and figure used to plot the diagram, respectively.

    """
    if visual:
        matplotlib.use("TkAgg")
        fig = figure.Figure(figsize=parameters["boxsize"], dpi=120)

        rc("font", family=parameters["font"], size=parameters["fontsize"])
        rc("legend", fontsize=parameters["fontsize"])
        rc("xtick", labelsize=parameters["fontsize"])

        ax1 = fig.add_subplot(111)
    else:
        print_easter_egg()
        plt.rcParams["font.family"] = parameters["font"]
        plt.rcParams.update({"font.size": parameters["fontsize"]})
        plt.rcParams.update({"legend.fontsize": parameters["fontsize"]})
        plt.rcParams.update({"xtick.labelsize": parameters["fontsize"]})
        fig, ax1 = plt.subplots()
        fig.set_size_inches(*parameters["boxsize"])

    return ax1, fig


def bracket_ts_step(
    ts_step_index: int, energies: dict[str, float | None]
) -> tuple[int, int]:
    """Determine the indices of the nearest mechanism steps to a TS.

    Args:
        ts_step_index: The index of the transition state step.
        energies: A list of free energies. The ith entry in ``energies``
            corresponds to the ith step in ``pathway``.

    Raises:
        RuntimeError: Unable to bracket the transition step. Either there is
            no elementary reaction step defined prior to the reaction step or
            there is no elementary reaction step defined after the reaction
            step.

    Returns:
        A 2-tuple (``index_before``, ``index_after``) indicating the indices
        of the nearest, defined reaction steps before and after the transition
        state, respectively.

    """
    index_check_before = index_check_after = 1
    index_before = ts_step_index - index_check_before
    index_after = ts_step_index + index_check_after
    no_left_bracket = no_right_bracket = True

    while no_left_bracket or no_right_bracket:
        if index_before < 0:
            raise RuntimeError(_INVALID_TS_PATHWAY_MSG.format("before"))

        if index_after > len(energies) - 1:
            raise RuntimeError(_INVALID_TS_PATHWAY_MSG.format("after"))

        if energies[index_before] is None:
            index_check_before += 1
            index_before = ts_step_index - index_check_before
        else:
            no_left_bracket = False

        if energies[index_after] is None:
            index_check_after += 1
            index_after = ts_step_index + index_check_after
        else:
            no_right_bracket = False

    return index_before, index_after


# TODO: add options for other interpolation functions (e.g., quadratic, cubic)
def interpolate(
    x0: tuple[float, float, float], y0: tuple[float, float, float]
) -> tuple[list[float], list[float]]:
    """Interpolate between three points with a sinusoidal function.

    Args:
        x0: The x-coordinates of the start, mid-, and end points.
        y0: The y-coordinates of the start, mid-, and end points.

    Returns:
        The x- and y-coordinates of the interpolation.

    """
    xx = list(np.linspace(x0[0], x0[1], 50))
    xx2 = list(np.linspace(x0[1], x0[2], 50))
    xx += xx2

    prefac1 = y0[1] - y0[0]

    yy = [
        y0[0] + prefac1 * np.sin(0.5 * np.pi * (x - x0[0]) / (x0[1] - x0[0]))
        for x in xx
    ]
    prefac2 = y0[2] - y0[1]
    yy += [
        y0[2] - prefac2 * np.sin(0.5 * np.pi * (x - x0[0]) / (x0[2] - x0[1]))
        for x in xx2
    ]
    return xx, yy


def create_ts_curve(
    ts_step_index: int,
    energies: list[float | None],
    step_count: int,
) -> tuple[list[float], list[float]]:
    """Create the plotting data for a transition state curve.

    Args:
        ts_step_index: The index of the transition state step.
        energies: A list of free energies. The ith entry in ``energies``
            corresponds to the ith step in ``pathway``.
        step_count: A weighted index for mechanism steps. Elementary steps
            increment the index by 2 while steps corresponding
            to transition states increment the index by 1.

    Returns:
        A 2-tuple (``xx``, ``yy``) whose first and second elements are the x
        and y values to be plotted on the free energy diagram.

    """
    before, after = bracket_ts_step(
        ts_step_index=ts_step_index,
        energies=energies,
    )
    x = (step_count - 0.99, step_count, step_count + 0.99)
    y = (energies[before], energies[ts_step_index], energies[after])
    return interpolate(x, y)


def plot_solid_lines(
    ax: axes.Axes,
    x: list[int],
    y: list[list[float]],
    color: str,
    zorder: int,
    linewidth: float,
    label: str,
) -> None:
    """Plot the solid lines connecting mechanism steps.

    Args:
        ax: The :class:`matplotlib.axes.Axes` on which the lines will be
            plotted.
        x: A list of floats indicating the x values for the lines.
        y: A list of lists of floats indicating the y values for the lines.
        color: The matplotlib color to be used to plot the lines.
        zorder: The zorder for the line. Lines with lower zorder values are
            drawn first.
        linewidth: A width of the plotted lines.
        label: The legend label for the line.

    """
    if label:
        _ = ax.plot(
            x,
            y,
            "-",
            color=color,
            linewidth=linewidth,
            zorder=zorder,
            label=label,
        )
    else:
        _ = ax.plot(x, y, "-", color=color, linewidth=linewidth, zorder=zorder)


def plot_dashed_lines(
    ax: axes.Axes,
    x: list[int],
    y: list[list[float]],
    color: str,
    zorder: int,
    linewidth: float,
) -> None:
    """Plot the dashed lines connecting mechanism steps.

    Args:
        ax: The :class:`matplotlib.axes.Axes` on which the lines will be
            plotted.
        x: A list of floats indicating the x values for the lines.
        y: A list of lists of floats indicating the y values for the lines.
        color: The matplotlib color to be used to plot the lines.
        zorder: The zorder for the line. Lines with lower zorder values are
            drawn first.
        linewidth: A width of the plotted lines.

    """
    dashedline_width = linewidth * 0.7
    ax.plot(x, y, "--", color=color, linewidth=dashedline_width, zorder=zorder)


def plot_fed(
    ax: axes.Axes,
    energies: list[float | None],
    mechanism: list[str],
    color: str,
    zorder: int,
    linewidth: float,
    legend_label: str,
) -> int:
    """Plot the free energy diagram of a pathway.

    Args:
        ax: The :class:`.axes.Axes` on which to plot the free energy diagram.
        energies: A list of free energies. The ith entry in ``energies``
            corresponds to the ith step in ``pathway``.
        mechanism: A list of strings corresponding to the steps of a reaction
            mechanism.
        color: A string corresponding to a matplotlib colour.
        zorder: The zorder for the lines for the pathway. A lower zorder
            indicates that the line will be drawn first.
        linewidth: The width of the line to use to plot the free energy
            diagram.
        legend_label: The legend label for the pathway.

    Returns:
        A weighted index for mechanism steps. Elementary steps increment the
        index by 2 while steps corresponding to transition states increment
        the index by 1.

    """
    step_count = -1
    x_dash = []
    y_dash = []
    for i, step in enumerate(mechanism):
        x = []
        y = []
        step_count += 1 if (step.split("_")[0].upper() == "TS") else 2

        if energies[i] is None:
            logger.warning("%s not defined for pathway.", step)
        else:
            if step.split("_")[0].upper() == "TS":
                xx, yy = create_ts_curve(i, energies, step_count)
            else:
                energy = energies[i]
                xx = [step_count - 1, step_count]
                yy = [energy, energy]

            x.extend(xx)
            y.extend(yy)
            x_dash.extend(xx)
            y_dash.extend(yy)
            plot_solid_lines(ax, x, y, color, zorder, linewidth, legend_label)

    plot_dashed_lines(ax, x_dash, y_dash, color, zorder, linewidth)
    return step_count


def plot_energy_data(
    ax: axes.Axes,
    data: FEDData,
    parameters: "FormattingParameters",
) -> int:
    """Plot the free energy diagrams of all pathways.

    Args:
        ax: The :class:`.axes.Axes` on which to plot the Gibbs plot.
        data: The free energy data to plot.
        parameters: The formatting parameters to use to plot the free energy
            diagram.

    Returns:
        The number steps in the final pathway. Steps corresponding to
        transition states contribute 1 to the total count. Steps corresponding
        to ordinary intermediates contribute 2 to the total count.

    """
    for i, energies in enumerate(data["energy_data"]):
        legend_label = data["legend_labels"][i]

        try:
            color = parameters["colors"][i]
        except IndexError:
            color = _DEFAULT_COLOR
            msg = (
                "WARNING: Number of colors defined are not sufficient for "
                "the pathways defined. Taking the default color "
                f"({_DEFAULT_COLOR})."
            )
            logger.warning(msg)

        count = plot_fed(
            ax=ax,
            energies=energies,
            mechanism=data["mechanism"],
            color=color,
            zorder=10 - i,
            linewidth=parameters["linewidth"],
            legend_label=legend_label,
        )
    return count


def format_primary_axes(
    ax: axes.Axes,
    parameters: "FormattingParameters",
    count: int,
    *,
    visual: bool = True,
) -> None:
    """Format the primary axis.

    Args:
        ax: The primary :class:`matplotlib.axes.Axes`.
        parameters: The :class:`.formatting.FormattingParameters` to use for
            the axes.
        count: A weighted index for mechanism steps. Elementary steps
            increment the index by 2 while steps corresponding
            to transition states increment the index by 1.
        visual: Whether or not to display the image. If True, the figure will
            be saved to a file. If False, the figure will be displayed.
            Defaults to True.

    """
    ax.set_xlim([-0.05, count + 0.05])
    # ax.set_ylim(parameters["yscale"])

    for axis in ["top", "bottom", "left", "right"]:
        ax.spines[axis].set_linewidth(parameters["linewidth"])
        ax.spines[axis].set_zorder(100)

    ax.set_xlabel(
        parameters["xlabel"],
        fontsize=parameters["fontsize"],
        fontfamily=parameters["font"],
    )
    ax.set_ylabel(
        parameters["ylabel"],
        fontsize=parameters["fontsize"],
        fontfamily=parameters["font"],
    )

    ax.yaxis.set_minor_locator(
        AutoMinorLocator(int(parameters["tick_min"]) + 1)
    )
    ax.yaxis.set_major_formatter(
        FormatStrFormatter(f"%.{parameters['tick_dec']}f")
    )
    ax.tick_params(
        which="both",
        direction=parameters["tick_loc"],
        labelsize=parameters["fontsize"],
        width=parameters["linewidth"],
    )
    ax.tick_params(which="major", length=4 * parameters["linewidth"])
    ax.tick_params(which="minor", length=2.5 * parameters["linewidth"])
    ax.xaxis.set_ticklabels([])
    ax.xaxis.set_ticks([])

    if parameters["title"]:
        if visual:
            plt.title(
                parameters["title"],
                fontsize=parameters["fontsize"] + 1,
                fontfamily=parameters["font"],
            )
        else:
            ax.set_title(
                parameters["title"],
                fontsize=parameters["fontsize"] + 1,
                fontfamily=parameters["font"],
            )

    if parameters["xscale"]:
        ax.set_xscale(parameters["xscale"])

    if parameters["yscale"]:
        ax.set_yscale(parameters["yscale"])


def format_secondary_axes(
    ax: axes.Axes, parameters: "FormattingParameters"
) -> None:
    """Format the secondary axis.

    Args:
        ax: The secondary :class:`matplotlib.axes.Axes`.
        parameters: The :class:`.formatting.FormattingParameters` to use for
            the axes.

    """
    ax.yaxis.set_minor_locator(
        AutoMinorLocator(int(parameters["tick_min"]) + 1)
    )
    ax.yaxis.set_major_formatter(
        FormatStrFormatter(f"%.{parameters['tick_dec']}f")
    )
    ax.tick_params(
        which="both",
        direction="in",
        labelsize=parameters["fontsize"],
        width=parameters["linewidth"],
    )
    ax.tick_params(which="major", length=4 * parameters["linewidth"])
    ax.tick_params(which="minor", length=2.5 * parameters["linewidth"])
    ax.yaxis.set_ticklabels([])


def add_annotations(
    ax: axes.Axes,
    annotations: list[Annotation],
    visual: bool,
    fontsize: float,
    font: str,
) -> None:
    """Add the annotations to the free energy diagram.

    Args:
        ax: The :class:`matplotlib.axes.Axes` on which to place the
            annotations.
        annotations: The annotations to add.
        visual: Whether or not the diagram is being shown.
        fontsize: The font size to use for the annotations.
        font: The matplotlib font family to use to write the annotations.

    """
    fontsize_label = fontsize - 2
    for annotation in annotations:
        engine = ax if visual else plt

        engine.text(
            x=annotation.x,
            y=annotation.y,
            s=annotation.text,
            color=annotation.color,
            fontsize=fontsize_label,
            fontfamily=font,
        )


def save_fed_plot(savename: str, dpi: int) -> None:
    """Save the free energy diagram.

    Args:
        savename: The filename to use when saving the file
        dpi: The resolution in dots-per-inch.

    """
    if savename.split(".")[-1].lower() == "png":
        plt.savefig(
            savename,
            bbox_inches="tight",
            dpi=dpi,
            transparent=True,
        )
    else:
        plt.savefig(savename, bbox_inches="tight", transparent=True)
    plt.close()


def generate_figure(
    diagram_data: FEDData,
    parameters: "FormattingParameters" = DEFAULT_PARAMETERS,
    annotations: list[Annotation] | None = None,
    *,
    visual: bool = True,
) -> tuple[axes.Axes, axes.Axes, figure.Figure]:
    """Generate the free energy diagram figure.

    Args:
        diagram_data: The data for the free energy diagram.
        parameters: The formatting parameters to use to create the free energy
            diagram.
        annotations: Annotations for the free energy data. Defaults to an
            empty list.
        visual: Whether or not to display the image. If True, the figure will
            be saved to file instead of displayed.

    Returns:
        A 3-tuple (``ax1``,``ax2``, ``figure``). ``ax1`` is the primary axes
        containing the free energy diagram. ``ax2`` is the secondary axes; it
        is None unless the "tick_double" parameter is True in ``parameters``.
        ``figure`` is the :class:`matplotlib.figure.Figure` containing all
        plot elements.

    """
    logger.info("Generating free energy diagram")
    annotations = annotations or []

    for key, value in parameters.items():
        logger.debug("%s=%s", key, value)

    ax1, fig = create_axes(parameters)
    ax2 = None
    count = plot_energy_data(ax1, diagram_data, parameters)
    format_primary_axes(ax=ax1, parameters=parameters, count=count)

    if parameters["tick_double"]:
        ax2 = ax1.secondary_yaxis("right")
        format_secondary_axes(ax=ax2, parameters=parameters)

    engine = ax1 if visual else plt

    engine.legend(
        loc=parameters["legend_loc"],
        frameon=False,
        fontsize=parameters["fontsize"] - 2,
    )
    add_annotations(
        ax=ax1,
        annotations=annotations,
        visual=visual,
        fontsize=parameters["fontsize"],
        font=parameters["font"],
    )

    if not visual:
        save_fed_plot(parameters["savename"], parameters["dpi"])

    return ax1, ax2, fig
