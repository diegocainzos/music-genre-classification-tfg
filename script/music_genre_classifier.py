import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import time
import io

from collections import Counter
from PIL import Image  
import tkinter as tk
from tkinter import filedialog, messagebox
from tensorflow.keras.models import load_model

# Cargar el modelo solo una vez, optimizando la carga
MODEL_PATH = "/Users/diego/UValencia/TFG/notebook/model/modelo90%.h5"
model = load_model(MODEL_PATH)

# Diccionario para la conversión de id a género, mejorando la legibilidad
GENRE_DICT = {
    0: "blues", 1: "classical", 2: "country", 3: "disco", 4: "hiphop",
    5: "jazz", 6: "metal", 7: "pop", 8: "reggae", 9: "rock"
}

def id_to_string(genre_id):
    """Convierte un ID de género a su nombre"""
    return GENRE_DICT.get(genre_id, "unknown")

def create_spectrograms(audio_file, segment_duration=5):
    """Crea una lista de espectrogramas a partir de un archivo de audio."""
    lista = []
    try:
        y, sr = librosa.load(audio_file)
    except (FileNotFoundError, librosa.util.exceptions.ParameterError) as e:
        print(f"Error loading {audio_file}: {e}")
        return lista

    duration = len(y) / sr
    for i in range(0, int(duration / segment_duration)):
        segment = y[i * segment_duration * sr:(i + 1) * segment_duration * sr]
        
        mel = librosa.feature.melspectrogram(y=segment, sr=sr, n_mels=224)
        mel_db = librosa.power_to_db(mel)
        
        fig, ax = plt.subplots(figsize=(2.16, 2.24))
        ax.axis('off')
        librosa.display.specshow(mel_db, sr=sr, cmap='magma', ax=ax)
        
        buf = io.BytesIO()
        plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0)
        buf.seek(0)
        
        img = Image.open(buf).rotate(180).resize((224, 216)).convert('RGB')
        lista.append(np.array(img) / 255)
        
        plt.close(fig)
    return lista

def classify_audio():
    """Función para cargar un archivo de audio, crear sus espectrogramas, y clasificar el género mediante el modelo cargado."""
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    start_time = time.perf_counter()
    spectrograms = create_spectrograms(file_path, segment_duration=5)
    
    if not spectrograms:
        messagebox.showerror("Error", "No se pudieron generar espectrogramas.")
        return

    predictions = [np.argmax(model.predict(np.expand_dims(spec, axis=0), verbose=0)) for spec in spectrograms]
    elapsed_time = time.perf_counter() - start_time
    
    genre_counts = Counter(predictions)
    most_common_genre, repetitions = genre_counts.most_common(1)[0]

    result = f"Genero: {id_to_string(most_common_genre)}, Repeticiones: {repetitions}\n"
    result += f"Tiempo transcurrido: {elapsed_time:.2f} segundos\n"
    result += "Conteo de las predicciones:\n" + ''.join(f" {id_to_string(genre)}: {count}\n" for genre, count in genre_counts.items())
    
    messagebox.showinfo("Resultado de la Clasificación", result)

def setup_gui():
    """Configura la interfaz gráfica para cargar y clasificar un archivo de audio."""
    root = tk.Tk()
    root.title("Clasificador de Géneros Musicales")

    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    label = tk.Label(frame, text="Clasificador de Géneros Musicales\n\nPor Diego García Caínzos - TFG 2024", font=("Helvetica", 16))
    label.pack(pady=10)

    btn_classify = tk.Button(frame, text="Cargar y Clasificar Audio", command=classify_audio, font=("Helvetica", 14))
    btn_classify.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    setup_gui()
