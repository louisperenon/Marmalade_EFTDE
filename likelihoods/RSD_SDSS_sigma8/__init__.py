import sys
import os
import numpy as np

require = [
	'sigma8',
]

path_to_data = os.path.dirname(os.path.realpath(sys.argv[0])) + '/likelihoods/RSD_SDSS_sigma8'
x, y, erry = np.loadtxt(path_to_data+'/data.txt', comments='#', unpack=True)

def get_loglike(Engine_input, Engine):
	return -0.5*((y-Engine.sigma8(x))/erry)**2.
