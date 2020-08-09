irecurse=0 #-global variable
from uedge import bbb

def uestep(dtnow, nrefine=3, irecurse_max=10, reset=False):
    #
    global irecurse
    if (reset):
        irecurse=0

    irecurse=irecurse+1
    print("Inside uedge_step():", irecurse)

    print("Trying time step: ", dtnow)
    bbb.dtreal=dtnow
    bbb.exmain()

    if (irecurse<irecurse_max):
        if (bbb.iterm!=1):
            dtnew=dtnow/nrefine
            for i in range(1,nrefine+1):
                uestep(dtnew)
    else:
        print("Too many recursions, exiting...")

# Usage example:
# uestep(1.0, reset=True)
