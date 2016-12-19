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

sam.sig_proc.quickplot(values=(rho,),xLabel="stellar radius [meters]",yLabel="rho [kg/m^3]",filename="rho.pdf",save=True )
sam.sig_proc.quickplot(values=(dMdr,),xLabel="stellar radius [meters]",yLabel="dMdr [kg/m]",filename="dMdr.pdf",save=True )
sam.sig_proc.quickplot(values=(dPdr,),xLabel="stellar radius [meters]",yLabel="dPdr [N/m^2/m]",filename="dPdr.pdf",save=True )
sam.sig_proc.quickplot(values=(dLdr,),xLabel="stellar radius [meters]",yLabel="dLdr [W/m]",filename="dLdr.pdf",save=True )
sam.sig_proc.quickplot(values=(dTdr,),xLabel="stellar radius [meters]",yLabel="dTdr [k/m]",filename="dTdr.pdf",save=True )

