import numpy as np

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
