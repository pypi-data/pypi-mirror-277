"""
"""

import numpy as np


def draw_from_hist(bins, hh, size=1):
    """draw random values that follow the distribution defined by the histogram

    Args:
        bins (ndarray of floats): the histogram bin edges
        hh (ndarray of floats): bin contents
        size (int): number of values to draw

    Returns:
        ndarray of floats: random values

    Examples:
        >>> x = np.random.normal(size=1000000)
        >>> hh,bins = np.histogram(x, bins=100)
        >>> v = draw_from_hist(bins, hh, size=1000000)
    """
    F = np.hstack(([0.], np.cumsum(hh))) 
    F /= np.sum(hh)
    x = np.random.uniform(0., 1., size=size)
    return np.interp(x, F, bins)
    
def draw_from_pdf(pdf, rng, size=1, bins=100):
    """draw random values from an arbitrary pdf

    Args:
        pdf (callable): PDF 
        rng (tuple of 2 floats): pdf range
        size (int): number of values to draw

    Returns:
        ndarray of floats: random values        
    """
    xbins = np.linspace(rng[0], rng[1], bins)
    hval = pdf(xbins)
    assert np.any(hval >= 0.)
    # should check that all the hvals >= 0.
    return draw_from_hist(xbins, hval[1:], size=size)

    
    
