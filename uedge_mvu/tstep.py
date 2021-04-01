irecurse=0 #-global variable
from uedge import bbb

def uestep(dtnow, irecurse=0, irecurse_max=10, nrefine=3):
    #
    
    print("Trying time step: ", dtnow)
    bbb.dtreal=dtnow
    bbb.exmain()

    if (irecurse<irecurse_max):
        if (bbb.iterm!=1):
            irecurse=irecurse+1
            print("Inside uedge_step() recursion:", irecurse)
            dtnew=dtnow/nrefine
            for i in range(1,nrefine+1):
                uestep(dtnew, irecurse, irecurse_max, nrefine)
    else:
        print("Too many recursions, exiting...")
	#stop

# Usage example:
# uestep(1.0)
