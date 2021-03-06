"""

NOTES::

	input data must be in this format: https://github.com/jmaggio14/sam/blob/master/src/sig_proc/opacity_data_example.txt
	
	-as of now:
		does scale for logs
		does convert values to mkg
		does scale for T_6

	-if anyone can check my math in the 'value()' method, that would be dandy.

	-example for how to use it is below

	-Feel free to email me at jxm9264@rit.edu or contact me via facebook: https://www.facebook.com/jeff.a.maggio
	

PURPOSE:: Generates system to easily retrieve opacity values

EXAMPLE::

	#create Opacity object instance
	>>> OP = Opacity(filename='opacity.txt',rows=100,cols=100) 	# interpolates opacity table to 100x100 grid
									# rho is indexed along columns
									# T is indexed along rows 
									# more rows & cols --> more resolution

	#retrieve opacity value for any given rho & T
	>>> opacityValue1 = OP.value( rho=1e5, T=1e5)  
	
	>>> opacityValue2 = OP.value( rho=1.2e5, T=1.2e5)  
		#repeat with N opacityValues
		# returns closest opacity value in table for rho,T
	 	# does scale for logs
	  	# does convert values to mkg
		# does scale for T_6
"""

import numpy as np
from scipy import interpolate 


class Opacity(object):

	def __init__(self,filename,rows=1e2,cols=1e2):
		#Retrieves raw opacity data
		output = self.load_opacity(filename)
		rawOpacity = output[0]

		r,c = rawOpacity.shape
		x = np.arange(c)
		y = np.arange(r)
		
		#interpolates the opacity table to specified rows/cols
		interp = interpolate.interp2d(x,y,rawOpacity)
		newX = np.arange(0,x.size,x.size/cols)
		newY = np.arange(0,y.size,y.size/rows)
		self._opacity = interp( newX,newY )

		#interpolates logR and logT to the same range as opacity table
		self._logR = output[1]
		self._logT = output[2]
		self._logR = self.interp1( newX.size,self._logR )
		self._logT = self.interp1( newY.size,self._logT )


	def convert_units(self,array):
		#THIS METHOD IS NO LONGER USED
		converted = array * 1e3
		return converted
	
	
	def load_opacity(self,filename):
		#retrieving opacity values
		opacity = np.genfromtxt(filename)
		#retrieving arrays that correspond to logR & logT
		logR = opacity[0,:][1:]
		logT = opacity[:,0][1:]
		#removing logR & logT from array
		without_logR = np.delete(opacity,0,0)
		without_logT = np.delete(without_logR,0,1)
		rawOpacities = without_logT
		return rawOpacities,logR,logT


	def remove_log(self,array,base=10):
		#THIS FUNCTION IS NO LONGER USED
		unLogged =  base**array
		return unLogged


	def closest_index(self,value,x):
		#Retrieves closest index to input value
		absoluteDifference = np.abs(value - x)
		closest = np.argmin(absoluteDifference)
		return closest


	def value(self,rho,T):
		#calculates logR and logT --> also *should* convert units properly
		logR = np.log10(  (rho * 1e-3)/(1e-18 * T**3)  )
		logT = np.log10(T)
		logR_index = self.closest_index(logR,self._logR)
		logT_index = self.closest_index(logT,self._logT)
		#de-logs the retrieved value and *should* convert to mkg
		opacity_value = 10**self._opacity[ logT_index, logR_index ] * .1
		return opacity_value 

	def interp1(self,newSize,array):
		currentX = np.arange(array.size)
		newX = np.arange(0,array.size,array.size/newSize)
		interpolated = np.interp(newX,currentX,array)
		return interpolated

if __name__ == "__main__":
	OP = Opacity('../../opacity.txt',80,7)
	print(OP._logR.size,OP._logT.size)


	print(OP.value( 1e3,3e4 ) )
	print(OP.value( 1e-2,4.3e5) )

	
	Rstack = np.vstack(( OP._logR, OP._opacity ) )
	Tcols = np.vstack( ([0], OP._logT.reshape( (OP._logT.size,1) )) )
	fullStack = np.hstack(  (Tcols,Rstack) )
	np.savetxt('interpolated_opacity.txt',fullStack)

