import os
import datetime
import copy
import numpy as np
from scipy.optimize import curve_fit
from scipy.special import erfc
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection, LineCollection
from matplotlib.backends.backend_pdf import PdfPages
import h5py
from uedge import bbb, com, api
from uedge import __version__ as uedgeVersion



def plotmesh(iso=True, zshift=0.0, xlim=None, ylim=None, yinv=False, show=True):

    fig,ax = plt.subplots(1)

    if (iso):
        plt.axes().set_aspect('equal', 'datalim')
    else:
        plt.axes().set_aspect('auto', 'datalim')

    for iy in np.arange(0,com.ny+2):
        for ix in np.arange(0,com.nx+2):
            plt.plot(com.rm[ix,iy,[1,2,4,3,1]],
                     com.zm[ix,iy,[1,2,4,3,1]]+zshift, 
                     color="black", linewidth=0.5)
            
    plt.xlabel('R [m]')
    plt.ylabel('Z [m]')
    fig.suptitle('UEDGE grid')
    plt.grid(False)

    if xlim:
        plt.xlim(xlim)
    if ylim:
        plt.ylim(ylim)

    if yinv:
        plt.gca().invert_yaxis()
        
    if show:
        plt.show()



def plotvar(var, zshift=0.0, iso=True, grid=False, label=None, vmin=None, vmax=None, yinv=False, title="UEDGE data"):
    
    patches = []

    for iy in np.arange(0,com.ny+2):
        for ix in np.arange(0,com.nx+2):
            rcol=com.rm[ix,iy,[1,2,4,3]]
            zcol=com.zm[ix,iy,[1,2,4,3]]+zshift
            rcol.shape=(4,1)
            zcol.shape=(4,1)
            polygon = Polygon(np.column_stack((rcol,zcol)), True)
            patches.append(polygon)

    #-is there a better way to cast input data into 2D array?
    vals=np.zeros((com.nx+2)*(com.ny+2))

    for iy in np.arange(0,com.ny+2):
        for ix in np.arange(0,com.nx+2):
            k=ix+(com.nx+2)*iy
            vals[k] = var[ix,iy]


     # Set vmin and vmax disregarding guard cells
    if not vmax:
        vmax = np.max(var)
    if not vmin:
        vmin = np.min(var)


    
    norm = matplotlib.colors.Normalize(vmin=vmin, vmax=vmax)
    ###p = PatchCollection(patches, cmap=cmap, norm=norm)
    p = PatchCollection(patches, norm=norm)
    p.set_array(np.array(vals))




    fig,ax = plt.subplots(1)

    ax.add_collection(p)
    ax.autoscale_view()
    plt.colorbar(p, label=label)

    if iso:
        plt.axis('equal')  # regular aspect-ratio
    
    fig.suptitle(title)
    plt.xlabel('R [m]')
    plt.ylabel('Z [m]')

    if grid:
        plt.grid(True)

    if yinv:
        plt.gca().invert_yaxis()
        
    #if (iso):
    #    plt.axes().set_aspect('equal', 'datalim')
    #else:
    #    plt.axes().set_aspect('auto', 'datalim')

    plt.show()




def plotrprof(var, ixcut=-1, title="UEDGE data", lines=True, dots=False, xlim=None, ylim=None, xlog=False, ylog=False):
    # Plotting radial profiles of UEDGE data
    #
    # Usage example:
    # plotrprof(bbb.te/ev, title="Te [eV]")
    # plotrprof(ni[:,:,1], title="Nn [m-3]")
    #==================================#
    
    fig,ax = plt.subplots(1)

    if (ixcut<0):
        ix0=bbb.ixmp
    else:
        ix0=ixcut

        

    if (lines):
        plt.plot(com.rm[ix0,:,0]-com.rm[ix0,com.iysptrx,0],var[ix0,:])
    
    if (dots):
        plt.plot(com.rm[ix0,:,0]-com.rm[ix0,com.iysptrx,0],var[ix0,:],"o")
        
    if xlim:
        plt.xlim(xlim)

    if ylim:
        plt.ylim(ylim)

    if ylog:
        plt.yscale('log')

    if xlog:
        plt.xscale('log')
        
    plt.xlabel('R-Rsep [m]')
    fig.suptitle(title)
    plt.grid(True)
 
    plt.show()
