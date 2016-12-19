#sam is the entire module
import sam
import matplotlib.pyplot as plt
import numpy as np

#Configs are configuration settings from config.yaml
configs = sam.Config()._configs

myStar = sam.astro.Star(configs)



#retreiving stellar properties
# myStar._radii = np.flipud(myStar._radii)
dMdr = np.asarray( [myStar._radii, myStar._mGrad] )
dPdr = np.asarray([myStar._radii, myStar._pGrad] )
dLdr = np.asarray([myStar._radii, myStar._lGrad] )
dTdr = np.asarray([myStar._radii, myStar._tGrad] )

Mr = [myStar._radii,myStar._MrArray]
Pr = [myStar._radii,myStar._PrArray]
Lr = [myStar._radii,myStar._LrArray]
Tr = [myStar._radii,myStar._TrArray]

rho = np.asarray( [myStar._radii,myStar._rhoArray]  ) 
#plotting methods

# plt.plot( dMdr )
# plt.show()

sam.sig_proc.quickplot(values=(rho,),xLabel="stellar radius [meters]",yLabel="rho [kg/m^3]",filename="rho.pdf",save=True,display=False,clearFig=True )
sam.sig_proc.quickplot(values=(Mr,),xLabel="stellar radius [meters]",yLabel="Mass [kg]",filename="Mr.pdf",save=True,display=False,clearFig=True )
sam.sig_proc.quickplot(values=(Pr,),xLabel="stellar radius [meters]",yLabel="Pressure [N/m^2]",filename="Pr.pdf",save=True,display=False,clearFig=True )
sam.sig_proc.quickplot(values=(Lr,),xLabel="stellar radius [meters]",yLabel="Luminosity [W]",filename="Lr.pdf",save=True,display=False,clearFig=True )
sam.sig_proc.quickplot(values=(Tr,),xLabel="stellar radius [meters]",yLabel="Temperature [k]",filename="Tr.pdf",save=True,display=False,clearFig=True )

