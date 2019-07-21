"""
Feldman-Cousins prescription for the construction of
frequentist confidence limits.
"""

import numpy as np
from scipy.stats import norm, poisson, rankdata


def find_acceptance_interval_poisson(mean, background, x_bins, alpha):
    """Acceptance interval for Poisson process with known background.

    Parameters:
        mu (float)           : Mean of the signal
        background (float)   : Mean of the background
        x_bins (array-like)  : Bins in x
        alpha (float)        : Desired confidence level
    Returns:
        x_min, x_max (float) : Confidence interval
    """

    dist = poisson(mu=mu + background)

    x_bin_width = x_bins[1] - x_bins[0]

    p = []
    r = []

    for x in x_bins:
        p.append(dist.pmf(x))
        # Implementing the boundary condition at zero
        muBest = max(0, x - background)
        probMuBest = poisson.pmf(x, mu=muBest + background)
        # probMuBest should never be zero. Check it just in case.
        if probMuBest == 0.0:
            r.append(0.0)
        else:
            r.append(p[-1] / probMuBest)

    p = np.asarray(p)
    r = np.asarray(r)

    if sum(p) < alpha:
        raise ValueError(
            "X bins don't contain enough probability to reach "
            "desired confidence level for this mu!"
        )

    rank = rankdata(-r, method="dense")

    index_array = np.arange(x_bins.size)

    rank_sorted, index_array_sorted = zip(*sorted(zip(rank, index_array)))

    index_min = index_array_sorted[0]
    index_max = index_array_sorted[0]

    p_sum = 0

    for i in range(len(rank_sorted)):
        if index_array_sorted[i] < index_min:
            index_min = index_array_sorted[i]
        if index_array_sorted[i] > index_max:
            index_max = index_array_sorted[i]
        p_sum += p[index_array_sorted[i]]
        if p_sum >= alpha:
            break

    return x_bins[index_min], x_bins[index_max] + x_bin_width


def construct_confidence_intervals_poisson
