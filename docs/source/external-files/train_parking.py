#!/usr/bin/env python
# coding: utf-8

# In[6]:


from keras.layers import Conv2D, MaxPooling2D, ZeroPadding2D
from keras.layers import Dense, Activation, Dropout, Flatten
from keras import optimizers
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator
import numpy as np 


# In[7]:


# étape1: charger les données
img_width = 150
img_height = 150


# In[8]:


DATA_train = "/Users/mosbahhachem/Documents/git/StageCerema/code/data/train"
DATA_valid = "/Users/mosbahhachem/Documents/git/StageCerema/code/data/valid"


# In[9]:


datagen = ImageDataGenerator(rescale = 1./255)


# In[27]:


train_generator = datagen.flow_from_directory(directory=DATA_train,target_size=(img_width,img_height), 
classes=['paking','non_parking'],class_mode='binary',batch_size=16)


# In[22]:


validation_generator = datagen.flow_from_directory(directory=DATA_valid,target_size=(img_width,img_height),
classes=['parking','non_parking'], class_mode='binary',batch_size=16)


# In[33]:


model =Sequential()

model.add(Conv2D(32,(3,3), input_shape=(img_width, img_height, 3)))
#model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.5))

model.add(Conv2D(32,(3,3), input_shape=(img_width, img_height, 3)))
#model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.5))

model.add(Flatten())
model.add(Dense(100))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.summary()

model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])

print('model compler!!')

print('train start....')
training = model.fit_generator(generator=train_generator, steps_per_epoch=5000 // 16,epochs=25
,validation_data=validation_generator,validation_steps=832//16)

print('training finished!!')

print('sauvgarde parking_non_parking_test.h5')
# saisir le chemin où seront stockés les poids et modèle du modèle qui vient d'être entraîné
model.save_weights('/Users/mosbahhachem/Documents/git/StageCerema/code/model/parking_non_parking_test.h5')
model.save('/Users/mosbahhachem/Documents/git/StageCerema/code/model/parking_non_parking_test.model')

print('Toutes les sauvgardes avec succées !!')



# In[ ]:




