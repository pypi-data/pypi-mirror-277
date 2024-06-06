"""test of the new bandpass system (a la sncosmo)
"""

import numpy as np
from nacl.lib.bspline import BSpline
import nacl.bandpasses



def test_filterdb_insertion():
    """
    """
    grid = np.arange(2000., 11010., 10.)
    basis = BSpline(grid)
    db = nacl.bandpasses.FilterDb(basis)

    g = nacl.bandpasses.get_bandpass('megacampsf::g', 12.)
    db.insert(g)
    db.insert(g, 0.325)
    r = nacl.bandpasses.get_bandpass('megacampsf::r', 1.233)
    db.insert(r, 0.766)
    db.insert(r)

    assert len(db) == 4
    a = db[(g.name, 0.325)]
    b = db[g.name]
    c = db[r.name]


def test_filterdb_pickle():
    """
    """
    grid = np.arange(2000., 11010., 10.)
    basis = BSpline(grid)
    db = nacl.bandpasses.FilterDb(basis)

    g = nacl.bandpasses.get_bandpass('megacampsf::g', 12.)
    db.insert(g)
    db.insert(g, 0.325)
    r = nacl.bandpasses.get_bandpass('megacampsf::r', 1.233)
    db.insert(r, 0.766)
    db.insert(r)

    import pickle
    with open('fdb.pkl', 'wb') as f:
        pickle.dump(db, f)

    with open('fdb.pkl', 'rb') as f:
        ddb = pickle.load(f)

    # compare the contents of the two databases
    # TODO
    
