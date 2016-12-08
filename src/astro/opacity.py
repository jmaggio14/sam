
def opacity(otype="bf", rho=None, T=None, X=None, Z=None, t=None, g=1.0):
	try:
	
		if otype in ["bf","bound-free","bound_free"]:
			opacity,units = bound_free_opacity(rho=rho,T=T,X=X,Z=Z,t=t,g=g)

		elif otype in ["ff","free-free","free_free"]:
			opacity,units = free_free_opacity(rho=rho,T=T,X=X,Z=Z,t=t,g=g)

		elif otype in ["es","electron-scattering","electron_scattering"]:
			opacity,units = electron_scattering_opacity(X=X)

		elif otype in ["H-","h-","hydrogen-ion"]:
			opacity,units = H_ion_opacity(rho=rho,T=T,Z=Z)

		return opacity,units
	
	except Exception as e:
		sam.debug(e)

def bound_free_opacity(rho,T,X,Z,t,g=1):
	units = "[m^2/kg]"

	if t == None:
		 t = 2.82 * ( rho * (1 + X) )**.2
	k_bf = sam.CONSTANT_Abf * (g/t) * Z * (1 + X) * (rho / T**3.5)
	return k_bf,units

def free_free_opacity(rho,T,X,Z,t,g):
	units = "[m^2/kg]"
	k_ff = (sam.CONSTANT_Aff * g * (1-Z) * (1+X) * rho) / T**3.5 

	return k_ff,units

def electron_scattering_opacity(X):
	units = "[m^2/kg]"
	k_es = 0.02 * (1+X)

	return k_es, units

def H_ion_opacity(rho,T,Z):
	units = "[m^2/kg]"
	k_Hion = 7.9e-34 * (Z/0.02) * rho**.5 * T**9

	return k_Hion, units