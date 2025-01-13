# Clasificación de Géneros Musicales Usando Redes Neuronales

Este proyecto implementa un sistema de clasificación de géneros musicales mediante redes neuronales convolucionales (CNNs) que usa espectrogramas de archivos de audio como entrada. El modelo permite preprocesar archivos de audio, crear espectrogramas, y entrenar una red neuronal para la clasificación de diferentes géneros musicales.

### Predicción Demo
Puedes ver una demo de predicción a continuación:

<img src="gráficas/test.gif" alt="Predicción Demo" width="500" style="display: block; margin: 0 auto;" />


## Estructura del Repositorio

La estructura del proyecto es la siguiente:

- **`script/`**: Script que lanza la interfaz.
- **`aumento de datos y procesado de audio/`**: Notebooks relacionados con la gestión y preprocesamiento de datos.
- **`model/`**: Modelos entrenados y definiciones de arquitectura.
- **`entrenamiento y pruebas/`**: Notebooks para exploración de datos y experimentación.
- **`gráficas/`**: Resultados obtenidos durante los experimentos, como métricas y gráficos.
- **`tfg_diego_garcia.pdf/`**: Memoria LibText de la tesis.

## Instalación

Sigue estos pasos para configurar el proyecto en tu entorno local:

### 1. Clonar el repositorio
Primero, clona este repositorio en tu máquina local:
```bash
git clone https://github.com/tu-usuario/nombre-repositorio.git
cd nombre-repositorio
```
### 2. Instalar las librerias requeridas
```bash
pip install -r requirements.txt
```
### 3. Ejecutar el script

```bash
cd script
python music_genre_classifier.py
```
