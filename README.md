
# Proyecto: Análisis de Partidas y MVPs

Este proyecto analiza los resultados de varias partidas de un juego tipo shooter, contabilizando estadísticas por jugador como kills, asistencias, muertes y MVPs. También se genera una tabla final con los puntajes acumulados.

##  Estructura del Proyecto

```
Practica2Entregar/
│
├── notebooks/           # Notebooks para probar y visualizar los resultados
│   └── ejercicio_10.ipynb
│
├── src/                 # Código fuente del proyecto
│   └── __init__.py      # Contiene la función principal `contabilizar`
│
├── main.py              # Ejecuta el análisis desde consola
├── requirements.txt     # Lista de dependencias del proyecto
└── README.md            # Este archivo
```

##  ¿Cómo ejecutar el proyecto?

Podés trabajar de dos formas:

###  Opción 1: Usando el notebook

1. Asegurate de estar en la raíz del proyecto.
2. Activá tu entorno virtual si tenés uno.
3. Abrí Jupyter:
   ```bash
   jupyter notebook
   ```
4. Entrá a la carpeta `notebooks/` y abrí `ejercicio_10.ipynb`.

---

###  Opción 2: Usando el archivo main.py

1. Estando en la raíz del proyecto, simplemente corré:
   ```bash
   python main.py
   ```

Este archivo llama a las funciones definidas en `src/__init__.py` para procesar las rondas, calcular resultados y mostrar estadísticas.

---

##  Instalación de Dependencias

Se recomienda usar un entorno virtual:

### 1. Crear entorno virtual (opcional)
```bash
python -m venv venv
```

### 2. Activarlo:
- En Windows:
  ```bash
  venv\Scripts\activate
  ```
- En macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### 3. Instalar las dependencias necesarias
```bash
pip install -r requirements.txt
igual, como solo tiene la dependencia notebook seria solo este comando
  pip install notebook





##  Notas

- Las funciones de análisis están en `src/__init__.py`, en particular en `contabilizar`
- Las rondas de prueba están cargadas en el notebook y en el `main.py`.

---

