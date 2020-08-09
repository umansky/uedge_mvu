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



def plotmesh(iso=True, xlim=None, ylim=None, show=True):
    fig,ax = plt.subplots(1)
    if (iso):
        plt.axes().set_aspect('equal', 'datalim')
    else:
        plt.axes().set_aspect('auto', 'datalim')
    for iy in np.arange(0,com.ny+2):
        for ix in np.arange(0,com.nx+2):
            plt.plot(com.rm[ix,iy,[1,2,4,3,1]],
                     com.zm[ix,iy,[1,2,4,3,1]], 
                     color="black", linewidth=0.5)
    plt.xlabel('R [m]')
    plt.ylabel('Z [m]')
    fig.suptitle('UEDGE mesh')
    plt.grid(False)
    if xlim:
        plt.xlim(xlim)
    if ylim:
        plt.ylim(ylim)
    if show:
        plt.show()
