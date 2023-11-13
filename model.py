import numpy as np
from PIL import Image
from keras.models import load_model

modelo = load_model('modelo.h5')


def clasificar_imagen(imagen):
    imagen = procesar_imagen(imagen)
    resultado = modelo.predict(imagen)
    clasificacion = np.argmax(resultado)

    return clasificacion


def procesar_imagen(imagen):
    imagen = Image.open(imagen)
    # Asegúrate de que la imagen tenga el tamaño esperado por el modelo (28x28)
    imagen = imagen.resize((28, 28))
    # Convierte a escala de grises
    imagen = imagen.convert('L')
    imagen = np.array(imagen)
    imagen = imagen / 255.0
    # Asegura que la imagen tenga las dimensiones correctas para el modelo
    imagen = imagen.reshape(1, 28, 28, 1)  # Ajusta las dimensiones a 28x28
    return imagen
