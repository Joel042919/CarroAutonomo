# Auto Genético: Algoritmo de Aprendizaje para Conducir

Este proyecto utiliza un **algoritmo genético** para enseñar a un auto (simulado en un entorno de juego) a manejar. El objetivo es crear un sistema donde el auto aprenda a navegar por un circuito, tomando decisiones en función de su entorno, usando un algoritmo evolutivo basado en **NEAT** (Neuroevolution of Augmenting Topologies).

## Descripción

El proyecto emplea el algoritmo de **NEAT** para evolucionar una población de redes neuronales que controlan a un vehículo en un entorno simulado con **Pygame**. A medida que el vehículo interactúa con el entorno, el algoritmo genético selecciona los individuos más exitosos y genera nuevas generaciones para mejorar la capacidad del auto para conducir de manera eficiente.

## Requisitos

Este proyecto requiere de las siguientes librerías para funcionar correctamente:

- **pygame==2.5.2**
- **neat-python==0.92**

## Instalación

Para instalar las dependencias necesarias, primero asegúrate de tener **Python 3** y **pip** instalados. Luego, sigue estos pasos:

### 1. Crear un entorno virtual (opcional, pero recomendado)

Es recomendable crear un entorno virtual para manejar las dependencias del proyecto sin afectar la instalación global de Python.

#### En Windows:

```bash
python -m venv venv
.\venv\Scripts\activate
```

### 2. Instalar las dependencias
Una vez dentro del entorno virtual, instala las librerías necesarias:

```bash
pip install -r requirements.txt
```

Este comando instalará las versiones correctas de pygame y neat-python especificadas en el archivo requirements.txt.

### 3. Ejecutar
```bash
python main.py
```