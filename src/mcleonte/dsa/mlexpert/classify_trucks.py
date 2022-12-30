"""
Create and return a convolutional neural network (CNN) to classify images
produced by a traffic-camera feed based on whether or not a truck is in the
images.

Note that :

• You should use TensorFlow 2 Keras APIs to create a CNN that expects images of
dimensions 224x224 with 3 channels (Red, Green, and Blue).

• The CNN should consist of 8 ordered layers : 1. A convolutional layer with 16
filters, each with a kernel of dimensions 3x3 and a Rectified Linear Unit (ReLU)
activation function. 2. A max pooling layer with dimensions 2x2. 3. A
convolutional layer with 32 filters, each with a kernel of dimensions 3x3 and a
ReLU activation function. 4. Another max pooling layer with dimensions 2x2. 5. A
convolutional layer with 64,filters each with a kernel of dimensions 3x3 and a
ReLU activation function. 6. A layer to flatten the values of the previous
layer. 7. A dense layer (fully connected) with 20 neurons and a ReLU activation
function. 8. Finally, a dense layer with a single neuron and sigmoid activation.
This layer will output the prediction.

• Each convolutional and pooling layer should use valid padding, each layer with
a ReLU activation should use He normal initialization, and the layer with a
sigmoid activation should use Glorot normal initialization.

• The CNN should use Adam as the optimizer with a learning rate of .01. As well,
binary cross-entropy should be used as the loss function, since the label of
each frame is 1 when there's a truck in the image and when there isn't a truck
in the image.
"""

from tensorflow.keras import Sequential, layers, optimizers, losses, metrics


def classify_trucks():
  model = Sequential([
      layers.Conv2D(
          16,
          (3, 3),
          padding='valid',
          activation='relu',
          kernel_initializer='he_normal',
          input_shape=(224, 224, 3),
          data_format='channels_last',
      ),
      layers.MaxPool2D(
          (2, 2),
          padding='valid',
      ),
      layers.Conv2D(
          32,
          (3, 3),
          padding='valid',
          activation='relu',
          kernel_initializer='he_normal',
      ),
      layers.MaxPool2D(
          (2, 2),
          padding='valid',
      ),
      layers.Conv2D(
          64,
          (3, 3),
          padding='valid',
          activation='relu',
          kernel_initializer='he_normal',
      ),
      layers.Flatten(),
      layers.Dense(
          20,
          activation='relu',
          kernel_initializer='he_normal',
      ),
      layers.Dense(
          1,
          activation='sigmoid',
          kernel_initializer='glorot_normal',
      ),
  ])
  model.compile(
      optimizer=optimizers.Adam(1e-2),
      loss=losses.BinaryCrossentropy(),
      metrics=[
          metrics.BinaryAccuracy(),
      ],
  )
  return model
