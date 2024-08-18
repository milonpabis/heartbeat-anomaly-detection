import numpy as np
import matplotlib.pyplot as plt



def plot_signal_data(ax, x: np.array, y: np.array, annot_sample: int = None, plot_kws: dict = {}):
    """
    Plots the signal data on the given axis. Uses np.ndarray for x and y.
    Can also plot the annotation sample on the signal.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The axis to plot the data on.
    x : np.array
        The x-axis data.
    y : np.array
        The y-axis data.
    annot_sample : int, optional
        The index of the annotation in the signal. The default is None.
    plot_kws : dict, optional
        Keyword arguments to pass to the plot function. The default is {}.

    Returns
    -------
    ax : matplotlib.axes.Axes
        The axis with the plotted data.
    """

    if "c" not in plot_kws.keys():
        plot_kws["c"] = "green"
    
    ax.plot(x, y, **plot_kws)
    ax.set_ylabel("Signal Strength [mV]")
    ax.set_xlabel("Seconds [s]")

    if annot_sample is not None:
        ax.plot(x[annot_sample], y[annot_sample], 'ro', alpha=0.5)
        ax.annotate("A", [x[annot_sample] + 0.02, y[annot_sample]], c="white")

    ax.set_facecolor((0.1, 0.1, 0.1))

    ax.set_title("MLII Signal Part")
    ax.grid()
    
    return ax



def plot_signal(ax, signal: np.array, annot_sample: int, annot_symbol: str, fs=360):
    """
    Plots the signal data with the annotation on the given axis. Needs only the signal y-axis data.
    
    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The axis to plot the data on.
    signal : np.array
        The y-axis data.
    annot_sample : int
        The index of the annotation in the signal.
    annot_symbol : str
        The annotation symbol.
    fs : int, optional
        The sampling frequency of the signal. The default is 360.

    Returns
    -------
    ax : matplotlib.axes.Axes
        The axis with the plotted data.
    """

    ax.plot(np.arange(signal.shape[0]) / fs, signal, c="springgreen")
    ax.plot(annot_sample / fs, signal[annot_sample], 'ro', alpha=0.5)
    ax.annotate(annot_symbol, [annot_sample / fs + 0.02, signal[annot_sample]], c="white")
    ax.set_ylabel("Signal Strength [mV]")
    ax.set_xlabel("Seconds [s]")

    ax.set_facecolor((0.1, 0.1, 0.1))

    ax.set_title("MLII Signal Part")
    ax.grid()
    
    return ax