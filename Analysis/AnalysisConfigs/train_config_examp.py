import os

batch_size = 50#256
# The number of epochs to train for
n_epochs = 200 #200
# The size of the images in the training set
img_size = (160,160,1)
# A random seed to use
random_seed = 2
# The list of learning parameters to use
learning_params = ['main_deflector_parameters_theta_E',
	'main_deflector_parameters_gamma1','main_deflector_parameters_gamma2',
	'main_deflector_parameters_gamma','main_deflector_parameters_e1',
	'main_deflector_parameters_e2','main_deflector_parameters_center_x',
	'main_deflector_parameters_center_y',
	 'subhalo_parameters_sigma_sub']
# Which parameters to consider flipping
flip_pairs = None
# Which terms to reweight
weight_terms = None
# The path to the folder containing the npy images
# for training
npy_folders_train = ['/opt/miniconda3/lib/python3.8/site-packages/paltas/systems2']
# The path to the tf_record for the training images
tfr_train_paths = [
	os.path.join(path,'data.tfrecord') for path in npy_folders_train]
metadata_paths_train = [
	os.path.join(path,'metadata.csv') for path in npy_folders_train]
# The path to the folder containing the npy images for validation
npy_folder_val = ('/opt/miniconda3/lib/python3.8/site-packages/paltas/systems2_val')
# The path to the tf_record for the validation images
tfr_val_path = os.path.join(npy_folder_val,'data.tfrecord')
# The path to the training metadata
# The path to the validation metadata
metadata_path_val = os.path.join(npy_folder_val,'metadata.csv')
# The path to the csv file to read from / write to for normalization
# of learning parameters.
input_norm_path = npy_folders_train[0] + 'norms.csv'
# The detector kwargs to use for on-the-fly noise generation
kwargs_detector = None
# Whether or not to normalize the images by the standard deviation
norm_images = True
# A string with which loss function to use.
loss_function = 'full'
# A string specifying which model to use
model_type = 'xresnet34'
# A string specifying which optimizer to use
optimizer = 'Adam'
# Where to save the model weights
#model_weights = ('model_weights/model_weights_{epoch:02d}-{val_loss:.2f}.h5')
model_weights = ('model_weights/model_weights2.h5')
model_weights_init = ('/initial_weights/initial_weights.h5')
# The learning rate for the model
learning_rate = 5e-3
# Whether or not to use random rotation of the input images
random_rotation = True
# Only train the head
train_only_head = False
