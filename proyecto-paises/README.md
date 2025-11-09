# Proyecto Integrador Programación 1 - 2025  
## Gestión de Datos de Países en Python: filtros, ordenamientos y estadísticas  
**Tecnicatura Universitaria en Programación – Universidad Tecnológica Nacional**

---

## Información General

- **Materia:** Programación I  
- **Año:** 2025  
- **Profesor Titular:** Sebastián Bruselario  
- **Docente Tutor:** Virginia Cimino  
- **Integrantes del grupo:** Pablo Mazuquin / Marcos Mardones  

---

## Descripción del Proyecto

Este proyecto corresponde al Trabajo Práctico Integrador (TPI) de la asignatura **Programación I**.

El objetivo es desarrollar un sistema en Python capaz de gestionar información de países utilizando:

- Listas  
- Diccionarios  
- Funciones  
- Modularización  
- Lectura desde archivos CSV  
- Filtros  
- Ordenamientos  
- Estadísticas básicas  

El sistema se ejecuta por consola e incorpora un **menú interactivo** que permite realizar búsquedas, filtrados, ordenamientos, actualizaciones y obtener indicadores estadísticos del conjunto de países cargados.

---

## Objetivos del Trabajo

- Aplicar los conceptos fundamentales de Programación 1.  
- Leer y procesar datos desde un archivo CSV.  
- Organizar el proyecto mediante módulos independientes.  
- Implementar funciones robustas con validaciones y manejo de errores.  
- Generar estadísticas relevantes a partir del dataset.  
- Fortalecer el trabajo colaborativo utilizando GitHub.

---

## Características del Sistema

### Gestión de países
- Agregar un nuevo país (con validación de campos)  
- Actualizar población o superficie de un país existente  

### Búsquedas
- Buscar por nombre (coincidencia exacta o parcial)

### Filtros
- Filtrar por continente  
- Filtrar por rango de población  
- Filtrar por rango de superficie  

### Ordenamientos
- Ordenar por nombre  
- Ordenar por población  
- Ordenar por superficie (ascendente o descendente)

### Estadísticas
- País con mayor población  
- País con menor población  
- Promedio de población  
- Promedio de superficie  
- Cantidad de países por continente  

---

## Estructura del Proyecto

El proyecto se encuentra modularizado siguiendo buenas prácticas:

```
 proyecto-paises
 ├── main.py
 ├── paises.csv
 ├── README.md
```

---

## Dataset Utilizado

Los datos se leen y escriben en un archivo CSV **paises.csv**, que contiene los campos:

- nombre  
- población  
- superficie  
- continente  


---

## Requerimientos Técnicos

- Python **3.x**
- No usa librerías externas (solo `csv` y `os`).

---

## Instrucciones de Ejecución

```bash
python main.py
```

El programa se ejecuta por consola mostrando un menú interactivo.

---

## Ejemplo de registro de país

```
Ingrese el nombre del país: argentina
Ingrese su población: 45000000
Ingrese su superficie: 2780000
Ingrese el continente del país: america
```

---

## Autores: 

- *Pablo Mazuquin / Marcos Mardones*
- UTN – Tecnicatura Universitaria en Programación


