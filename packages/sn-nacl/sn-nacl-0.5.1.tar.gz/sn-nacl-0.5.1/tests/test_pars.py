import pylab as pl

def compare_pars(tds, pars):
    """
    compares the parameters found in the sncosmo and after the NaCl fit
    """
    
    x0_tds = tds.sn_data.x0
    x1_tds = tds.sn_data.x1
    c_tds = tds.sn_data.col
    tmax_tds = tds.sn_data.tmax
    z = tds.sn_data.z
    
    x0_mod = pars['X0'].full[tds.sn_data.sn_index]
    x1_mod = pars['X1'].full[tds.sn_data.sn_index]
    c_mod = pars['col'].full[tds.sn_data.sn_index]
    tmax_mod = pars['tmax'].full[tds.sn_data.sn_index]
    
    pl.figure()
    pl.scatter(x0_tds, x0_mod)
    pl.title('X0 NaCl vs X0 sncosmo')
    pl.xlabel('X0 sncosmo')
    pl.ylabel('X0 NaCl')
    pl.show()
    
    pl.figure()
    pl.scatter(x1_tds, x1_mod)
    pl.title('X1 NaCl vs X1 sncosmo')
    pl.xlabel('X1 sncosmo')
    pl.ylabel('X1 NaCl')
    pl.show()
    
    pl.figure()
    pl.scatter(c_tds, c_mod)
    pl.title('col NaCl vs col sncosmo')
    pl.xlabel('col sncosmo')
    pl.ylabel('col NaCl')
    pl.show()
    
    pl.figure()
    pl.scatter(tmax_tds, tmax_mod)
    pl.title('tmax NaCl vs tmax sncosmo')
    pl.xlabel('tmax sncosmo')
    pl.ylabel('tmax NaCl')
    pl.show()
    
    pl.figure()
    pl.scatter(z, x0_mod/x0_tds, color='red')
    pl.title('X0 NaCl/X0 sncosmo vs z')
    pl.xlabel('z')
    pl.ylabel('X0 NaCl/X0 sncosmo')
    pl.show()

    pl.figure()
    pl.scatter(z, x1_mod/x1_tds, color='red')
    pl.title('X1 NaCl/X1 sncosmo vs z')
    pl.xlabel('z')
    pl.ylabel('X1 NaCl/X1 sncosmo')
    pl.show()
    
    pl.figure()
    pl.scatter(z, c_mod/c_tds, color='red')
    pl.title('col NaCl/col sncosmo vs z')
    pl.xlabel('z')
    pl.ylabel('col NaCl/col sncosmo')
    pl.show()
    
    pl.figure()
    pl.scatter(z, tmax_mod/tmax_tds, color='red')
    pl.title('tmax NaCl/tmax sncosmo vs z')
    pl.xlabel('z')
    pl.ylabel('tmax NaCl/tmax IDR')
    pl.show()

    pl.figure()
    pl.scatter(z, x1_mod-x1_tds, color='red')
    pl.title('X1 NaCl-X1 sncosmo vs z')
    pl.xlabel('z')
    pl.ylabel('X1 NaCl-X1 sncosmo')
    pl.show()
    
    pl.figure()
    pl.scatter(z, c_mod-c_tds, color='red')
    pl.title('col NaCl-col sncosmo vs z')
    pl.xlabel('z')
    pl.ylabel('col NaCl-col sncosmo')
    pl.show()
    
def compare_all_pars(old_pars, new_pars, block_name=['X0', 'X1', 'col', 'tmax', 'M0', 'M1', 'CL']):
    """
    """
    for block in block_name:
        fig, axes = pl.subplots(nrows=1, ncols=2, figsize=(10,10))
        fig.suptitle(f'parameter ' + block + ' before and after fit')
        axes[0].plot(old_pars[block].full, new_pars[block].full, 'k.')
        axes[0].set_xlabel(block + ' before fit')
        axes[0].set_ylabel(block + ' after fit')

        axes[1].plot(old_pars[block].full, (old_pars[block].full - new_pars[block].full)/old_pars[block].full, 'k.')
        axes[1].set_xlabel(block + ' before fit')
        axes[1].set_ylabel(block + ' before - after / before')
