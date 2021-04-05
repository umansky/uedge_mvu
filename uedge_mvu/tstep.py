from uedge import bbb

def uestep(dtnow, depth_max=10, nrefine=3, debug=False, reset=False):
# Usage example, to integrate by deltat=1.0 s, do:
# uestep(1.0, reset=True)
#======================================================#
        
    if (debug):
        print("In uedge_step() depth, depth_max, total time:", uestep.depth, depth_max, uestep.deltat)

    if (reset):
        uestep.abort=False
        uestep.depth=0
        uestep.deltat=0.0        

    if (uestep.abort):
        print("aborting")
        return
    else:
        if (uestep.depth>depth_max):
            print("Too many recursions")
            uestep.abort=True
            pass
            #return
        else:

            print("Trying time step: ", dtnow)
            bbb.dtreal=dtnow
            bbb.exmain()

            if (bbb.iterm!=1):
                #-previous step failed, try substeps now
                uestep.depth += 1
                dtnew=dtnow/nrefine
                for i in range(1,nrefine+1):
                    uestep(dtnew, depth_max, nrefine, debug)
                #-on completion of all substeps return to previous level
                uestep.depth -= 1                
            else:
                print("Successful time step with dt=", dtnow)
                uestep.deltat=uestep.deltat+dtnow
                print("Cumulative deltat=", uestep.deltat)
                print("\n")
                pass
        
    #return ##-this one does not matter?

#-attributes for the function, used as static variables
uestep.abort=False
uestep.depth=0
uestep.deltat=0.0
