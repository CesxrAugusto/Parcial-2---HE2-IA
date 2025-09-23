# Parcial-2---HE2-IA
*Universidad de los Andes - Facultad de Economia*

## 📋 Información del Proyecto

En este repositorio se encuentra el desarrollo del segundo parcial de la materia "IA aplicada a la Economia", en el cual evaluará el mejor hiperparametro mediante herramientas del Deep Learning sobre el dataset Adult Census Income

## 🎯 Objetivos

Desarrollar una red neuronal que prediga si una persona gana mas de $50,000 anuales basandose en caracteristicas demograficas y socioeconomicas

## 📊 Dataset

- Fuente: https://archive.ics.uci.edu/dataset/2/adult
- Dimensiones: 16281 filas x 15 columnas
- Variable objetivo: *income*

## Variables

- Variables numericas: *age*, *fnlwgt*, *education-num*, *capital-gain*, *capital-loss*, *hours-per-week*
- Variables categoricas: *workclass*, *education*, *marital-status*, *occupation*, *relationship*, *race*, *sex*, *native-country*

## Librerias Principales

- pandas
- seaborn
- torch

## Desarrollo y Metodologia

### 1. Recoleccion y exploracion de datos

- Carga del dataset proporcionado de las instrucciones del parcial
- Realizacion de split 50/50
- Realizacion de EDA

### 2. Desarrollo de Algoritmos

- Realizacion de modelo de regresion logistica
- Creacion de MLP
- Definir funcion de perdida y optimizador
- Realizacion de experimentos con hiperparametros

## Ejecución
1. Clonar el repositorio
2. Abrir el notebook en Google Colab o Jupyter
3. Ejecutar las celdas secuencialmente
4. Los resultados se guardarán automáticamente

## Hiperparametros

## 📈 Resultados

## 👥 Contribuidores

- Equipo de desarrollo: Adrian Montenegro Zamora, Cesar Augusto 
- Profesor: Camilo Vega Barbosa
- Profesor complementario: Daniel Aguirre

## 📚 Referencias

- Curso "IA para la Economía" - Universidad de los Andes
- Becker, B. & Kohavi, R. (1996). Adult. https://archive.ics.uci.edu/dataset/2/adult

## 📄 Licencia

Este proyecto se desarrolla con fines académicos para la Universidad de los Andes.
