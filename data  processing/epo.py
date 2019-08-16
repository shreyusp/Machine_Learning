from keras.models import Sequential
from keras.layers import Dense,Convolution2D,MaxPooling2D,Flatten

cModel=Sequential()

cModel.add(Convolution2D(32,(3,3),input_shape=(64,64,3),activation='relu'))
cModel.add(MaxPooling2D(pool_size=(2,2)))

cModel.add(Convolution2D(32,(3,3),activation='relu'))
cModel.add(MaxPooling2D(pool_size=(2,2)))
cModel.add(Flatten())
cModel.add(Dense(units=128,activation='relu'))
cModel.add(Dense(units=1,activation='sigmoid'))

cModel.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])


from keras.preprocessing.image import ImageDataGenerator

trainDataGen=ImageDataGenerator(rescale=1./255,shear_range=0.2,zoom_range=0.2,horizontal_flip=True)

testDataGen=ImageDataGenerator(rescale=1./255)

trainingData=trainDataGen.flow_from_directory('cnndataset/dataset/training_set',target_size=(64,64),batch_size=32,class_mode='binary')

testData=testDataGen.flow_from_directory('cnndataset/dataset/training_set',target_size=(64,64),batch_size=32,class_mode='binary')

cModel.fit_generator(trainingData,steps_per_epoch=2000,epochs=5)

cModel.save('CatDog5epoch')

