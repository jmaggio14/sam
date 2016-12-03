import scipy.integrate as integ

def integrate(array,dx,culmative=True):
	if culmative:
		integral = integ.cumtrapz(array,dx=dx)
	else:
		integral = integ.trapz(array,dx=dx)

	return integral


def numerical_integration(iterate,terms,var,lam):
	for value in iterate:
		lam(  )






func = lambda d : d[""]