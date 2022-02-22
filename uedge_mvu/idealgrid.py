from fortranformat import FortranRecordWriter
import re
import numpy as np
from uedge import bbb, grd


def import_field(fp,nxm,nym):

    nvals=(nxm+2)*(nym+2)*5
    buffer=np.zeros(nvals)

    #-how many lines to read
    nlines=int(np.ceil(float(nvals)/3.))

    #-skip a blank line
    line=fp.readline()

    #-read data
    for i in range(0,nlines):
        line=fp.readline()
        columns=line.split()
        str=columns[0]; buffer[i*3]=float(re.sub('[dD]', 'e', str))
        str=columns[1]; buffer[i*3+1]=float(re.sub('[dD]', 'e', str))
        str=columns[2]; buffer[i*3+2]=float(re.sub('[dD]', 'e', str))

    #-convert data to 3D array
    fdata=np.zeros((nxm+2,nym+2,5))

    i=0
    for k in range(5):
        for jy in range(0,nym+2):
            for ix in range(0,nxm+2):
                fdata[ix,jy,k]=buffer[i]
                i=i+1

    return fdata


def export_field(fp, nxm, nym, fdata):

    #-skip a line                                                                                             
    fp.write("\n")

    nvals=(nxm+2)*(nym+2)*5
    buffer=np.zeros(nvals)
    nlines=int(np.ceil(float(nvals)/3.))


    i=0
    for k in range(5):
        for jy in range(0,nym+2):
            for ix in range(0,nxm+2):
                buffer[i]=fdata[ix,jy,k]
                i=i+1

    frw = FortranRecordWriter('(3e23.15)')


    for m in range(nlines):
        line = frw.write(buffer[3*m:3*m+3])+"\n"
        fp.write(line)




def idlg_read(fname="gridue"):

    print("In idealgrid: idlg_read()")
    print("Importing data from ", fname)

    f = open(fname, 'r')
     
    #-read headerline
    line=f.readline()
    columns=line.split()
    nxm=int(columns[0])
    nym=int(columns[1])
    

    #import data, one field at a time
    rm=import_field(f,nxm,nym)
    zm=import_field(f,nxm,nym)
    psi=import_field(f,nxm,nym)
    br=import_field(f,nxm,nym)
    bz=import_field(f,nxm,nym)
    bpol=import_field(f,nxm,nym)
    bphi=import_field(f,nxm,nym)
    b=import_field(f,nxm,nym)

    #import runid
    line=f.readline()
    print("runid:",line)

    f.close()

    return rm,zm,psi,br,bz,bpol,bphi,b


def idlg_write(rm,zm,psi,br,bz,bpol,bphi,b, fname="gridue.cp", runid="runid", nxm=0, nym=0):
    print("In idealgrid: idlg_write()")

    print("Exporting data to ", fname)
    f = open(fname, 'w')

    frw = FortranRecordWriter('(I15,I15)')
    headerline = frw.write([nxm,nym])+"\n"

    f.write(headerline)

    export_field(f,nxm,nym,rm)
    export_field(f,nxm,nym,zm)
    export_field(f,nxm,nym,psi)
    export_field(f,nxm,nym,br)
    export_field(f,nxm,nym,bz)
    export_field(f,nxm,nym,bpol)
    export_field(f,nxm,nym,bphi)
    export_field(f,nxm,nym,b)

    f.write("\n"+runid)

    f.close()
