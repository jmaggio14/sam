from scipy import interpolate

def interp2D(newShape,data,kind="linear"):
	r,c = newShape
	x = np.arange(c)
	y = np.arange(r)
	interpolated = interpolate.interp2D(x,y,data,kind)
	return interpolated