# 🧠 Algoritmos de Búsqueda y Ordenamiento en Python

## 📚 Descripción del proyecto

Este proyecto fue desarrollado como trabajo integrador para la materia **Programación I** de la **Tecnicatura Universitaria en Programación (UTN)**. El objetivo fue investigar, implementar y comparar distintos algoritmos de búsqueda y ordenamiento en el lenguaje de programación Python, aplicándolos a un caso práctico funcional.

Se desarrolló un sistema que simula un negocio con productos, permitiendo:

- Generar una lista de productos con campos `código`, `nombre` y `precio`.
- Ordenar la lista utilizando el algoritmo **Merge Sort**.
- Buscar productos utilizando **búsqueda binaria**, incluyendo opción de buscar “uno solo” o “todos” los elementos coincidentes.
- Medir tiempos de ejecución para evaluar la eficiencia de los algoritmos.

## 👥 Participantes

- **Rodrigo Daniel Montes Sare** – [rodrii.montesrms@gmail.com](mailto:rodrii.montesrms@gmail.com)
- **Gabriel Maximiliano Montaña** – [gabriel.m.montana@gmail.com](mailto:gabriel.m.montana@gmail.com)

## 🏫 Materia

- **Programación I**  
- **Tecnicatura Universitaria en Programación (UTN)**
- Año lectivo: 2024–2025

## 💻 Instrucciones de uso

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/usuario/tp-busqueda-ordenamiento.git
   ```
   *(Reemplazar por el enlace real)*

2. Ingresar al proyecto:
   ```bash
   cd tp-busqueda-ordenamiento
   ```

3. Ejecutar el archivo principal:
   ```bash
   python tp-2.py
   ```

4. Seguir las instrucciones en pantalla:
   - Elegir cuántos productos generar.
   - Seleccionar el campo por el cual se desea ordenar.
   - Visualizar los productos ordenados (opcional).
   - Seleccionar el campo para realizar una búsqueda.
   - Elegir si se desea buscar un solo resultado o todos los que coincidan.

> Requisitos:
> - Python 3.x instalado
> - Consola con soporte para entrada de texto

## 🧪 Funcionalidades implementadas

- Generación automática de listas con productos simulados.
- Ordenamiento eficiente por campo (`nombre`, `precio` o `código`) usando **Merge Sort**.
- Búsqueda binaria optimizada con control de orden previo.
- Medición de tiempos para evaluar eficiencia algorítmica.
- Validación del funcionamiento y control de errores.

## 📈 Resultados y eficiencia

- **Merge Sort** ordenó 10.000 elementos en menos de **0.05 segundos**.
- Otros métodos como Bubble Sort o Selection Sort tardaron entre **7 y 26 segundos**.
- **Búsqueda binaria** respondió en milisegundos, siempre que la lista estuviera ordenada.
- La variante “buscar todos” también demostró gran eficiencia.

> Nota: Al intentar generar una lista de 50.000 productos, el sistema colapsó debido a los límites de recursos disponibles, lo que permitió entender la importancia de ajustar el procesamiento a la capacidad del entorno.

## 🔍 Reflexión del equipo

El desarrollo de este trabajo nos permitió:

- Comprender en profundidad los algoritmos de búsqueda y ordenamiento, no solo en teoría sino aplicándolos en un contexto real.
- Valorar la importancia de la eficiencia algorítmica para mejorar el rendimiento de una aplicación.
- Aprender a trabajar colaborativamente usando herramientas como GitHub, Visual Studio Code e Intellij.
- Identificar y resolver errores comunes relacionados con estructura de datos y validaciones.

Entre las posibles mejoras futuras se encuentran:

- Agregar una interfaz gráfica para hacerlo más amigable al usuario.
- Exportar los resultados y estadísticas a archivos externos.
- Implementar ordenamiento múltiple y otros algoritmos como Timsort.

## 📁 Estructura del repositorio

```
├── tp-2.py                # Archivo principal del proyecto
├── README.md              # Descripción y guía del proyecto
├── capturas/              # Capturas de pantalla de pruebas (opcional)
├── informe.pdf            # Trabajo práctico completo (opcional)
```

## 📎 Enlace al informe

📝 Versión PDF del trabajo práctico disponible en el repositorio.  
📹 El video presentación con demostración práctica será compartido por la cátedra.

## 📚 Bibliografía

- [DataCamp – Linear Search in Python](https://www.datacamp.com/es/tutorial/linear-search-python)  
- [EIPOS Grados – Tipos de algoritmos de ordenación en Python](https://eiposgrados.com/blog-python/tipos-de-algoritmos-de-ordenacion-en-python/)

---

© 2024 - UTN – Programación I – Rodrigo y Gabriel
