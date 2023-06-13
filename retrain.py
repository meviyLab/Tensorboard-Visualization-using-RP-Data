# -*- coding: utf-8 -*-

import os,cv2
import numpy as np
import matplotlib.pyplot as plt
import pickle
import tensorflow as tf
from tensorboard.plugins import projector
tf.__version__

PATH = os.getcwd()

LOG_DIR = PATH+ '/embedding-logs'

#%%
data_path = PATH + '/rapidprotypedata'
data_dir_list = os.listdir(data_path)

img_data=[]
for dataset in data_dir_list:
    img_list=os.listdir(data_path+'/'+ dataset)
    print ('Loaded the images of dataset-'+'{}\n'.format(dataset))
    for img in img_list:
        input_img=cv2.imread(data_path + '/'+ dataset + '/'+ img )
        input_img_resize=cv2.resize(input_img,(100,100))
        img_data.append(input_img_resize)
    
                
img_data = np.array(img_data)

#%%

feature_vectors = np.loadtxt('featurevectors_rapidprototype.txt')
print ("feature_vectors_shape:",feature_vectors.shape)
print ("num of images:",feature_vectors.shape[0])
print ("size of individual feature vector:",feature_vectors.shape[1])

num_of_samples=feature_vectors.shape[0]
num_of_samples_each_class = 100

features = tf.Variable(feature_vectors, name='features')


y = np.ones((num_of_samples,),dtype='int64')

y[0:100]=0
y[100:200]=1
y[200:300]=2
y[300:400]=3
y[400:]=4

names = ['01','02','03','04','05']

metadata_file = open(os.path.join(LOG_DIR, 'metadata_meviy_classes.tsv'), 'w')
metadata_file.write('Class\tName\n')
k=100 # num of samples in each class
j=0

for i in range(num_of_samples):
    c = names[y[i]]
    if i%k==0:
        j=j+1
    metadata_file.write('{}\t{}\n'.format(j,c))
    #metadata_file.write('%06d\t%s\n' % (j, c))
metadata_file.close()
       

def images_to_sprite(data):
    """Creates the sprite image along with any necessary padding

    Args:
      data: NxHxW[x3] tensor containing the images.

    Returns:
      data: Properly shaped HxWx3 image with any necessary padding.
    """
    if len(data.shape) == 3:
        data = np.tile(data[...,np.newaxis], (1,1,1,3))
    data = data.astype(np.float32)
    min = np.min(data.reshape((data.shape[0], -1)), axis=1)
    data = (data.transpose(1,2,3,0) - min).transpose(3,0,1,2)
    max = np.max(data.reshape((data.shape[0], -1)), axis=1)
    data = (data.transpose(1,2,3,0) / max).transpose(3,0,1,2)
    # Inverting the colors seems to look better for MNIST
    #data = 1 - data

    n = int(np.ceil(np.sqrt(data.shape[0])))
    padding = ((0, n ** 2 - data.shape[0]), (0, 0),
            (0, 0)) + ((0, 0),) * (data.ndim - 3)
    data = np.pad(data, padding, mode='constant',
            constant_values=0)
    
    # Tile the individual thumbnails into an image.
    data = data.reshape((n, n) + data.shape[1:]).transpose((0, 2, 1, 3)
            + tuple(range(4, data.ndim + 1)))
    data = data.reshape((n * data.shape[1], n * data.shape[3]) + data.shape[4:])
    data = (data * 255).astype(np.uint8)
    return data
#%%
sprite = images_to_sprite(img_data)
cv2.imwrite(os.path.join(LOG_DIR, 'sprite_meviy_classes.png'), sprite)

#%%
saver = tf.compat.v1.train.Saver([features])
saver.save(LOG_DIR, 'images_meviy_classes.ckpt')  # Assumes LOG_DIR is './logs/'

# checkpoint_path = os.path.join(LOG_DIR, 'images_4_classes.ckpt')
# saver = tf.train.Checkpoint(features=features)
# saver.save(checkpoint_path)

# config = tf.compat.v1.ConfigProto()
config = projector.ProjectorConfig()

# One can add multiple embeddings.
embedding = config.embeddings.add()

embedding.tensor_name = features.name
embedding.metadata_path = os.path.join(LOG_DIR, 'metadata_meviy_classes.tsv')
embedding.sprite.image_path = os.path.join(LOG_DIR, 'sprite_meviy_classes.png')
embedding.sprite.single_image_dim.extend([img_data.shape[1], img_data.shape[1]])

projector.visualize_embeddings(LOG_DIR, config)
