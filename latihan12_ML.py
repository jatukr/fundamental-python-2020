import tensorflow as tf
import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
from keras_preprocessing import image
import matplotlib.pyplot as plt
# import matplotlib.image as mpimg

base_dir = 'images'
train_dir = os.path.join(base_dir, 'train')
validation_dir = os.path.join(base_dir, 'val')

# Membuat direktori ruangan rapi pada direktori data training
train_clean_dir = os.path.join(train_dir, 'clean')

# Membuat direktori ruangan berantakan pada direktori data training
train_messy_dir = os.path.join(train_dir, 'messy')

# membuat direktori ruangan rapi pada direktori data validasi
validation_clean_dir = os.path.join(validation_dir, 'clean')

# membuat direktori ruangan berantakan pada direktori data validasi
validation_messy_dir = os.path.join(validation_dir, 'messy')

# membuat sebuah objek ImageDataGenerator untuk data training dan data testing
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    horizontal_flip=True,
    shear_range=0.2,
    fill_mode='nearest'
)

test_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    horizontal_flip=True,
    shear_range=0.2,
    fill_mode='nearest'
)

# Mempersiapkan data latih yang akan dipelajari oleh model
train_generator = train_datagen.flow_from_directory(
    train_dir,  # Direktori data latih
    target_size=(150, 150),  # Mengubah resolusi seluruh gambar menjadi 150x150 piksel
    batch_size=4,  # karena kita merupakan masalah klasifikasi 2 kelas maka menggunakan class_mode='binary'
    class_mode='binary'
)

validation_generator = test_datagen.flow_from_directory(
    validation_dir,  # Direktori data validasi
    target_size=(150, 150),  # Mengubah resolusi seluruh gambar menjadi 150x150 piksel
    batch_size=4,  # karena kita merupakan masalah klasifikasi 2 kelas maka menggunakan class_mode='binary'
    class_mode='binary'
)

# Membangun arsitektur sebuah CNN
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile model dengan 'adam' optimizer loss function 'binary_crossentropy'
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# Latih model dengan fit
model.fit(
    train_generator,
    steps_per_epoch=25,  # berapa batch yang akan dieksekusi pada setiap epoch
    epochs=20,  # tambahkan epoch jika akurasi model belum optimal
    validation_data=validation_generator,  # Menampilkan akurasi pengujian data validasi
    validation_steps=5,  # berapa batch yang akan dieksekusi pada setiap epoch
    verbose=2
)

# File
fn = 'images/images/test/8.png'

# Predicting image
path = fn
img = image.load_img(path, target_size=(150, 150))
imgplot = plt.imshow(img)
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)

images = np.vstack([x])
classes = model.predict(images, batch_size=10)

print(fn)
if classes == 0:
    print('clean')
else:
    print('messy')
