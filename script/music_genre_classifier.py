import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import time
import io
import os
from collections import Counter
from scipy import ndimage
from PIL import Image  
import tkinter as tk
from tkinter import filedialog, messagebox

# Definir la función id_to_string
def id_to_string(id):
    genres = ["blues", "classical", "country", "disco", "hiphop", "jazz", "metal", "pop", "reggae", "rock"]
    return genres[id] if 0 <= id < len(genres) else "unknown"

# Cargar el modelo desde el archivo .h5
from tensorflow import keras
from keras.models import load_model
model = load_model("/Users/diego/UValencia/TFG/notebook/model/modelo90%.h5")

# Función para crear espectrogramas
def create_spectrograms(audio_file, segment_duration=5):
    lista = []
    try:
        y, sr = librosa.load(audio_file)
    except:
        print(f"Error loading {audio_file}")
        return lista

    start_sec = 0
    duration = len(y) / sr
    for i in range(0, int(duration / segment_duration)):
        fig = plt.figure(figsize=(216 / 100, 224 / 100))  # Tamaño en pulgadas
        ax = fig.add_subplot(1, 1, 1)
        fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
        mel = librosa.feature.melspectrogram(y=y[int(start_sec * sr):int((start_sec + segment_duration) * sr)], sr=sr, n_mels=224)
        start_sec += segment_duration
        mel = librosa.power_to_db(mel)
        librosa.display.specshow(mel, sr=sr, cmap='magma')
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        img = Image.open(buf)
        img = img.rotate(180)
        img = img.resize((224, 216))
        img_rgb = img.convert('RGB')
        lista.append(np.array(img_rgb) / 255)
        plt.clf()
        plt.close(fig)
    return lista

# Función para cargar y clasificar un archivo de audio
def classify_audio():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    start_time = time.perf_counter()
    fotos = create_spectrograms(file_path, 5)
    indices = []

    for foto in fotos:
        foto = np.expand_dims(foto, axis=0)
        indices.append(np.argmax(model.predict(foto, verbose=0)))

    elapsed_time = time.perf_counter() - start_time
    conteo = Counter(indices)
    valor_mas_repetido, repeticiones = conteo.most_common(1)[0]

    result = f"Genero: {id_to_string(valor_mas_repetido)}, Repeticiones: {repeticiones}\n"
    result += f"Tiempo transcurrido: {elapsed_time:.2f} segundos\n"
    result += "Conteo de las predicciones:\n"
    for clase, conteo in conteo.items():
        result += f" {id_to_string(clase)}: {conteo} \n"
    
    messagebox.showinfo("Resultado de la Clasificación", result)

# Configuración de la interfaz gráfica con Tkinter
root = tk.Tk()
root.title("Clasificador de Géneros Musicales")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Clasificador de Géneros Musicales", font=("Helvetica", 16))
label.pack(pady=10)

btn_classify = tk.Button(frame, text="Cargar y Clasificar Audio", command=classify_audio, font=("Helvetica", 14))
btn_classify.pack(pady=20)

root.mainloop()
