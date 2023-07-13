
from pymol.cgo import *
from pymol import cmd
import numpy as np
from chempy.brick import Brick

        

Points_0 = [
        
COLOR,1.0,0.0,0.0,1.0,SPHERE,4.965339376844304,2.756870426460817,9.4507031748626,0.3,COLOR,1.0,0.0,0.0,1.0,SPHERE,1.7408082281453063,1.3545847514603282,4.414392438416101,0.3,COLOR,1.0,0.0,0.0,1.0,SPHERE,1.0460064868269825,3.142922979920253,6.322657743000134,0.3,COLOR,1.0,0.0,0.0,1.0,SPHERE,9.078676661201378,7.390462980723724,3.26272040652979,0.3,COLOR,1.0,0.0,0.0,1.0,SPHERE,2.410422635339453,9.984325800970197,7.640425383213221,0.3,COLOR,1.0,0.0,0.0,1.0,SPHERE,8.504502090205454,5.412938663280766,7.952826173041753,0.3,COLOR,1.0,0.0,0.0,1.0,SPHERE,1.9656195351608485,6.981180593446837,4.457728353664979,0.3,COLOR,1.0,0.0,0.0,1.0,SPHERE,3.1238511289923077,9.636611675917706,3.9587002565201668,0.3,COLOR,1.0,0.0,0.0,1.0,SPHERE,8.861842355001082,8.844030670846287,3.8295880986114783,0.3,COLOR,1.0,0.0,0.0,1.0,SPHERE,4.517567122121559,2.3394000425501913,4.215061167676836,0.3

            ]
cmd.load_cgo(Points_0, "Points_0", state=1)
cmd.set("cgo_transparency", 0, "Points_0")
        