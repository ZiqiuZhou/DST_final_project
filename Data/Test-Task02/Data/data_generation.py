"""
Generates a test sinoidal time series for task 2.

run in /Data/Test-Task02/Data directory: python3 data_generation.py

"""

import numpy as np


# Sinusoidal time series:
N_data = 100000 # number of series points
dt = 0.5 # time step size
A = 2 # Amplitude
freq = 0.1 # Frequency
phi0 = 0 # Phase Offset for training data
phi0_test = 0.5 # -||- for testing data
c = 0.5 # Offset

t = np.arange(0, N_data, dt)
training_data = A*np.sin(2*np.pi*freq*t+phi0)+c

# generate training data
data_dict_train = {}
data_dict_train['train_input_sequence'] = training_data
data_dict_train['dt'] = dt

np.save('training_data_N{}.npy'.format(N_data), data_dict_train)


testing_data = A*np.sin(2*np.pi*freq*t+phi0_test)+c

# generate testing data
data_dict_test = {}
data_dict_test['test_input_sequence'] = testing_data

# random Initial condition (by random index)
# this ensures that the model draws a random initial condition when testing
dl_max = 20000
pl_max = 20000
max_idx = len(testing_data) - pl_max
min_idx = dl_max
idx = np.arange(min_idx, max_idx)
np.random.shuffle(idx)
testing_ic_indexes = idx

data_dict_test['testing_ic_indexes'] = testing_ic_indexes
data_dict_test['dt'] = dt
np.save('testing_data_N{}.npy'.format(N_data), data_dict_test)

"""
# code of vlachas-repo ...



project_dir = "/home/dietrich/final_project_LSTM"

train_data_raw = np.load(project_dir + '/lorenz96_data_train.npy')
test_data_raw = np.load(project_dir + '/lorenz96_data_test.npy')
training_data = np.vstack(([data_segment for data_segment in train_data_raw]))
testing_data = np.vstack(([data_segment for data_segment in test_data_raw]))

# generate training data
data_dict_train = {}
data_dict_train['train_input_sequence'] = training_data
data_dict_train['dt'] = 1
np.save(project_dir + '/Data/Lorenz-96/Data/training_data_N100000.npy', data_dict_train)

# generate testing data
data_dict_test = {}
data_dict_test['test_input_sequence'] = testing_data

dl_max = 20000
pl_max = 20000
max_idx = len(testing_data) - pl_max
min_idx = dl_max
idx = np.arange(min_idx, max_idx)
np.random.shuffle(idx)
testing_ic_indexes = idx

data_dict_test['testing_ic_indexes'] = testing_ic_indexes
data_dict_test['dt'] = 1
np.save(project_dir + '/Data/Lorenz-96/Data/testing_data_N100000.npy', data_dict_test)
"""
