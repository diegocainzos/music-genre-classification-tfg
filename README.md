# 🎵 Clasificación de Géneros Musicales Usando Redes Neuronales

Este proyecto implementa un sistema de clasificación de géneros musicales mediante redes neuronales convolucionales (CNNs) que usa espectrogramas de archivos de audio como entrada. El modelo permite preprocesar archivos de audio, crear espectrogramas, y entrenar una red neuronal para la clasificación de diferentes géneros musicales.

---

## 🎯 Predicción Demo
¡Mira la demo de predicción en acción! 
<br>

<img src="gráficas/test.gif" alt="Predicción Demo" width="500" style="display: block; margin: 0 auto; border-radius: 10px;" />

---

## 📂 Estructura del Repositorio

La estructura del proyecto es la siguiente:

- **`script/`**: Scripts para lanzar la interfaz.
- **`aumento de datos y procesado de audio/`**: Notebooks relacionados con la gestión y preprocesamiento de datos.
- **`model/`**: Modelos entrenados y definiciones de arquitectura.
- **`entrenamiento y pruebas/`**: Notebooks para exploración de datos y experimentación.
- **`gráficas/`**: Resultados obtenidos durante los experimentos, como métricas y gráficos.
- **`tfg_diego_garcia.pdf/`**: Memoria LibText de la tesis.

---

## 🛠 Instalación

Sigue estos pasos para configurar el proyecto en tu entorno local:

### 1️⃣ Clonar el repositorio
Primero, clona este repositorio en tu máquina local:
```bash
git clone https://github.com/tu-usuario/nombre-repositorio.git
cd nombre-repositorio
```

### 2️⃣ Instalar las librerías requeridas
```bash
pip install -r requirements.txt
```

### 3️⃣ Ejecutar el script
```bash
cd script
python music_genre_classifier.py
```

---

## 💡 Motivación y Objetivo del Proyecto

- La proliferación de plataformas de streaming como Spotify y YouTube Music ha aumentado el número de artistas y canciones disponibles, dificultando el etiquetado manual de géneros musicales.
- Este proyecto busca desarrollar un clasificador automático de géneros musicales mediante CNNs, utilizando espectrogramas de Mel generados a partir de fragmentos de canciones de 30 segundos pertenecientes a 10 géneros diferentes.

---

## 🔬 Metodología y Estado del Arte

### 📊 Conjunto de Datos y Técnicas Usadas:
- El dataset principal utilizado fue **GTZAN**, con fragmentos de audio divididos en géneros.
- Se procesaron los datos para generar espectrogramas de Mel, una representación visual del audio en función del tiempo y la frecuencia.

### 🧠 Redes Neuronales Convolucionales (CNNs):
- Las CNNs, inspiradas en la corteza visual del cerebro, son ideales para tareas de clasificación visual, como analizar espectrogramas.
- Se analizaron distintas arquitecturas, ventajas y desventajas de CNNs frente a otros modelos como LSTM, RNN o híbridos.

### 🔧 Herramientas y Tecnologías:
- Librerías como TensorFlow y Keras fueron fundamentales en el desarrollo y entrenamiento de la red neuronal.
- **Librosa** se utilizó para el procesamiento de audio, mientras que **Audiomentations** ayudó a aumentar los datos con técnicas como cambios en el tono, velocidad y ruido.

---

## 🏆 Resultados y Conclusiones

-  El sistema alcanzó una precisión superior al 90% en la clasificación de géneros musicales.
-  Los espectrogramas de Mel demostraron ser una herramienta efectiva para representar características musicales.

### 📈 Visualización de Resultados:
<br>
<div style="display: flex; justify-content: center; gap: 20px;">
  <img src="https://i.imgur.com/Q2qfaBN.jpeg" alt="Gráfico de ROC" width="400" style="border-radius: 10px;" />
  <img src="https://i.imgur.com/kLEVNT4.jpeg" alt="Gráfico de Precisión" width="400" style="border-radius: 10px;" />
</div>
<br>
  <img src="https://i.imgur.com/DnAHcBP.jpeg" alt="Loss" width="800" style="border-radius: 10px;" />

---

## 🌟 Impacto y Trabajo Futuro

### Impacto:
-  Esta herramienta puede ser útil en plataformas de streaming para etiquetado automático, ofreciendo recomendaciones más personalizadas.

### Trabajo Futuro:
-  Ampliar el dataset para incluir subgéneros musicales.
-  Incorporar modelos más avanzados como Transformers para mejorar aún más la precisión.
-  Extender la aplicación a dispositivos móviles.

---

¡Gracias por explorar este proyecto! 🚀
