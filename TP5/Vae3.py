from PIL import Image
from numpy import asarray
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import tensorflow as tf
import gzip
from tensorflow import keras
import sys
sys.modules['keras'] = keras
from keras.layers import Input, Dense, Lambda, Reshape
from keras.models import Model
from keras import backend as K
from keras import metrics
from keras.datasets import mnist
from tensorflow.python.framework.ops import disable_eager_execution
disable_eager_execution()





# Load de las imagenes
files = ['/home/augusto/Desktop/yalefaces/subject01.gif',
'/home/augusto/Desktop/yalefaces/subject01.happy',
'/home/augusto/Desktop/yalefaces/subject01.sad',
'/home/augusto/Desktop/yalefaces/subject01.sleepy',
'/home/augusto/Desktop/yalefaces/subject01.surprised',
'/home/augusto/Desktop/yalefaces/subject01.wink']

# Parametros de la imagen
base_width = 64
base_height = None
img = Image.open(files[0])
wpercent = (base_width/float(img.size[0]))
base_height = int((float(img.size[1])*float(wpercent)))

x_train = np.zeros((len(files), base_width * base_height))


i=0
for f in files:
    img = Image.open(f)
    img = img.resize((base_width,base_height), Image.ANTIALIAS)
    numpydata = asarray(img).astype('float32') / 255.
    x_train[i] = numpydata.ravel()
    i += 1

# Parametros de la red
batch_size = 100
original_dim = base_height * base_width
latent_dim = 2
intermediate_dim = 1024
epochs = 500
epsilon_std = 1.0



### Encoder ####

# H(z) --> Funcion que genera z a partir de la media y varianza
def sampling(args: tuple):
    # we grab the variables from the tuple
    z_mean, z_log_var = args
    print(z_mean)
    print(z_log_var)
    epsilon = K.random_normal(shape=(K.shape(z_mean)[0], latent_dim), mean=0.,
                              stddev=epsilon_std)
    return z_mean + K.exp(z_log_var / 2) * epsilon  # h(z)

# input to our encoder
x = Input(shape=(original_dim,), name="input")
# intermediate layer
h = Dense(intermediate_dim, activation='relu', name="encoding")(x)
# defining the mean of the latent space
z_mean = Dense(latent_dim, name="mean")(h)
# defining the log variance of the latent space
z_log_var = Dense(latent_dim, name="log-variance")(h)
# note that "output_shape" isn't necessary with the TensorFlow backend
z = Lambda(sampling, output_shape=(latent_dim,))([z_mean, z_log_var])
# defining the encoder as a keras model
encoder = Model(x, [z_mean, z_log_var, z], name="encoder")
# print out summary of what we just did
# encoder.summary()

### Decoder ###

# Input to the decoder
input_decoder = Input(shape=(latent_dim,), name="decoder_input")
# taking the latent space to intermediate dimension
decoder_h = Dense(intermediate_dim, activation='relu', name="decoder_h")(input_decoder)
# getting the mean from the original dimension
x_decoded = Dense(original_dim, activation='sigmoid', name="flat_decoded")(decoder_h)
# defining the decoder as a keras model
decoder = Model(input_decoder, x_decoded, name="decoder")
# decoder.summary()


### Red completa ###

# grab the output. Recall, that we need to grab the 3rd element our sampling z
output_combined = decoder(encoder(x)[2])
# link the input and the overall output
vae = Model(x, output_combined)
# print out what the overall model looks like
# vae.summary()

# Fucnion de costo
def vae_loss(x: tf.Tensor, x_decoded_mean: tf.Tensor):
  # Aca se computa la cross entropy entre los "labels" x que son los valores 0/1 de los pixeles, y lo que salió al final del Decoder.
  xent_loss = original_dim * metrics.binary_crossentropy(x, x_decoded_mean) # x-^X
  kl_loss = - 0.5 * K.sum(1 + z_log_var - K.square(z_mean) - K.exp(z_log_var), axis=-1)
  vae_loss = xent_loss +  kl_loss
  return vae_loss


# Define la funcion de costo
vae.compile( loss=vae_loss,experimental_run_tf_function=False)
# vae.summary()



### Training ###




vae.fit(x_train, x_train,
        shuffle=True,
        epochs=epochs,
        batch_size=batch_size)







### Resultados ###
x_test_encoded = encoder.predict(x_train, batch_size=batch_size)[0]
labels = ['normal', 'happy', 'sad', 'sleepy', 'surprised', 'wink']
plt.figure(figsize=(6, 6))
plt.scatter(x_test_encoded[:,0], x_test_encoded[:,1])
for i, txt in enumerate(labels):
    plt.annotate(txt, (x_test_encoded[i][0] + 0.01, x_test_encoded[i][1] + 0.01))
plt.show()


n =  6
figure = np.ones((base_height * n, base_width * n))
# linearly spaced coordinates on the unit square were transformed through the inverse CDF (ppf) of the Gaussian
# to produce values of the latent variables z, since the prior of the latent space is Gaussian
grid_x = norm.ppf(np.linspace(0.05, 0.95, n))
grid_y = norm.ppf(np.linspace(0.05, 0.95, n))

for i, yi in enumerate(grid_x):
    for j, xi in enumerate(grid_y):
        z_sample = np.array([[xi, yi]])
        x_decoded = decoder.predict(z_sample)
        # print(fonts.printLetter(x_decoded[0]))
        digit = x_decoded[0].reshape(base_height, base_width)
        figure[i * base_height: (i + 1) * base_height,
               j * base_width: (j + 1) * base_width] = digit

# figure[0][0] = 0

plt.figure(figsize=(10, 10))
plt.imshow(figure , cmap='Greys_r')
plt.show()
