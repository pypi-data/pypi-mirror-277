#!/usr/bin/env python3
"""Example of data analysis with python readin hdf5 data."""
import os
import sys
import traceback

from vdaq_ana.cmmds import fit_utils
import matplotlib.pyplot as plt
import numpy as np
from vdaq_ana import VDaqData
from vdaq_ana import Progress
from scipy import stats


def read_data(vdaq, options, evt_E=None, evt_CH=None):
    """Iterates on all the events."""
    if options.nevts is None:
        max_evts = vdaq.nevts
    else:
        max_evts = options.nevts

    prg = Progress.ShowProgress(max_evts)
    prg.start()

    # now we iterate on all the data
    # for that we use vdaq as iterable
    if evt_E is None:
        evt_E = {}

    if evt_CH is None:
        evt_CH = {}

    print("\nIterating over all data in the file")
    try:
        for ievt, evt in enumerate(vdaq):
            if ievt == 0:
                continue

            if ievt > max_evts:
                break

            mid = evt.mod_id
            md = vdaq.modules[mid]
            data = md.process_event(evt)
            # get the array to store the event energy
            if data is not None:
                e_list = evt_E.setdefault(mid, [])
                e_ch = evt_CH.setdefault(mid, [])
                for channel, E in data:
                    if E > options.thrs:
                        e_list.append(E)
                        e_ch.append(channel)

            # monitor progress
            prg.increase()
            if prg.timer.mark() > 0.1:
                prg.timer.set_mark()
                prg.show()

    except RuntimeError:
        print("\n\nSomething very bad happened...")
        print('-'*60)
        traceback.print_exc(file=sys.stdout)
        print('-'*60)

    except KeyboardInterrupt:
        print("\nArrrrggggg !!!!")
        raise KeyboardInterrupt

    print("\nDone: ", ievt)
    return evt_E, evt_CH


def do_analyze_data(file_list, options):
    """Main routine."""

    evt_E = {}
    evt_CH = {}
    for fname in file_list:
        # Open the file
        if not os.path.exists(fname):
            print("Input file", fname, "does not exist")
            continue

        print("\n+++Reading file {}".format(fname))

        # We open here the file
        vdaq = VDaqData(fname)
        for m in list(vdaq.modules.values()):
            m.set_debug(options.debug)
            m.do_cluster = options.cluster
            m.polarity = options.polarity

        vdaq.show_info(True)
        # and read the data
        evt_E, evt_CH = read_data(vdaq, options,
                                  evt_E=evt_E,
                                  evt_CH=evt_CH)

    # Create the figure
    n_mod = len(evt_E)
    fig, ax = plt.subplots(nrows=2, ncols=n_mod)
    dax = {}   # Spectrum axes
    daxc = {}  # Hitmap axes
    try:
        for iax, k in enumerate(evt_E.keys()):
            dax[k] = ax[0, iax]
            daxc[k] = ax[1, iax]

    except Exception:
        key = list(evt_E.keys())[0]
        dax[key] = ax[0]
        daxc[key] = ax[1]

    print("")

    # Do the fit
    for mid, E in evt_E.items():
        #  bit of statistics. Find out the optimal binwidth based on average noise
        vmin = np.min(E)
        vmax = np.max(E)
        range = vmax - vmin
        noise = stats.mode(vdaq.modules[mid].noise, keepdims=True).mode[0]
        if noise < 5.0:
            noise = 5.0

        if options.nbin < 0:
            nbin = int(range/(1.0*noise)/5.0 + 0.5) * 5
        else:
            nbin = options.nbin

        # Create and draw the histogram
        ax = dax[mid]
        n, bins, patches = ax.hist(E, nbin, range=(vmin, vmax), facecolor='g', alpha=0.75)
        if options.logy:
            ax.set_yscale("log")
            
        step = 0.5 * (bins[1] - bins[0])
        X = bins[:-1] + step

        # Do the fits
        if options.fit == "landau":
            mu = np.mean(E)
            sigma = np.std(E)
            result, out, legend = fit_utils.fit_landau_model(mu, sigma, n, bins, options.debug)

        elif options.fit == "gauss":
            result, out, legend = fit_utils.fit_peak_model(n, bins, debug=options.debug)

        if options.fit != "none":
            if options.debug:
                print(result.fit_report())

            fit_utils.draw_best_fit(ax, result, bins)
            ax.legend([legend], loc=1)

        ax.set_title('Module %d' % mid)

        # Hit map
        for mid, CH in evt_CH.items():
            ax = daxc[mid]
            m = vdaq.modules[mid]
            X = np.arange(m.ntot+1)
            n, bins, patches = ax.hist(CH, facecolor='g', bins=m.ntot, alpha=0.75)
            ax.set_xlabel('Channel')
            ax.set_ylabel('Occupancy')

    plt.show()


def analyze_data():
    """Main entry."""
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('files', nargs='+', help="Input files")
    parser.add_argument("--fit", choices=["none", "gauss", "landau"],
                        help="It will try a Landau-like fit to the data (default)",
                        default="none"
                        )
    parser.add_argument("--debug", action="store_true", help="Debug", default=False)
    parser.add_argument("--logy", action="store_true", help="Log Scale for spectrum", default=False)
    parser.add_argument("--cluster", action="store_true",
                        help="Will try to find clusters in sparse",
                        default=False)
    parser.add_argument("--nevts", help="Read at most nevts events", default=None)
    parser.add_argument("--thrs", help="Signal Threshold", default=-9999, type=float)
    parser.add_argument("--polarity", help="Signal polarity", default=1)
    parser.add_argument("--nbin", default=-1, type=int, help="Number of bins in histogram.")
    

    options = parser.parse_args()

    if len(options.files) == 0:
        print("I need an input file")
        sys.exit()

    do_analyze_data(options.files, options)
    sys.exit()


if __name__ == "__main__":
    analyze_data()
