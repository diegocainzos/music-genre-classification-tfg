# Clasificación de Géneros Musicales Usando Redes Neuronales

Este proyecto implementa un sistema de clasificación de géneros musicales mediante redes neuronales convolucionales (CNNs) que usa espectrogramas de archivos de audio como entrada. El modelo permite preprocesar archivos de audio, crear espectrogramas, y entrenar una red neuronal para la clasificación de diferentes géneros musicales.

![Predicción Demo](gráficas/test.gif)


## Contenido del Repositorio

- **`music_genre_classifier.py`**: Script para clasificar archivos de audio en géneros musicales usando un modelo previamente entrenado.
- **`music-spectrograms.ipynb`**: Notebook para generar espectrogramas a partir de archivos de audio, con opciones de aumentación de datos.
- **`train_network.ipynb`**: Notebook para entrenar la red neuronal usando espectrogramas generados y dividir los datos en conjuntos de entrenamiento, validación y prueba.
- La carpeta gráficas contiene las figuras incluidas en la memoria del proyecto. En ella podemos conocer más en detalle la distribución, resultados y conclusiones del trabajo.
## Requisitos Previos

- **Python** >= 3.7
- Bibliotecas requeridas: `librosa`, `tensorflow`, `keras`, `matplotlib`, `PIL`, `tkinter`, `audiomentations`, `numpy`, `sklearn`
