"""

NOTES::
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
	>>> opacityValue = OP.value( rho=1e5, T=1e5)  # returns closest opacity value in table for rho = 1e5,T=1e5
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
		
		#interpolates the logR and logT
		interp = interpolate.interp2d(x,y,rawOpacity)
		newX = np.arange(0,x.size,x.size/cols)
		newY = np.arange(0,y.size,y.size/rows)
		self._opacity = interp( newX,newY )

		self._logR = output[1]
		self._logT = output[2]

		self._logR = self.interp1( newX.size,self._logR )
		self._logT = self.interp1( newY.size,self._logT )


	def convert_units(self,array):
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
		unLogged =  base**array
		return unLogged


	def closest_index(self,value,x):
		absoluteDifference = np.abs(value - x)
		closest = np.argmin(absoluteDifference)
		return closest


	def value(self,rho,T):
		logR = np.log10(  (rho * 1e-3)/(1e-18 * T**3)  )
		logT = np.log10(T)
		logR_index = self.closest_index(logR,self._logR)
		logT_index = self.closest_index(logT,self._logT)

		opacity_value = 10**self._opacity[ logT_index, logR_index ] * .1
		return opacity_value 

	def interp1(self,newSize,array):
		currentX = np.arange(array.size)
		newX = np.arange(0,array.size,array.size/newSize)
		interpolated = np.interp(newX,currentX,array)
		return interpolated

if __name__ == "__main__":
	OP = Opacity('../../opacity.txt',80,7)
	print(OP._rho.size,OP._T.size)


	print(OP.value( 1e3,3e4 ) )
	print(OP.value( 1e-2,4.3e5) )

	
	rhoStack = np.vstack(( OP._rho, OP._opacity ) )
	Tcols = np.vstack( ([0], OP._T.reshape( (OP._T.size,1) )) )
	fullStack = np.hstack(  (Tcols,rhoStack) )
	np.savetxt('interpolated_opacity.txt',fullStack)

