# 🎮 Cuatro en Raya — Juego de consola en Python
¡Bienvenido a **Cuatro en Raya**! Este proyecto es una simulación del clásico juego de mesa, desarrollada completamente en **Python** y pensada para ejecutarse desde la consola.

---

## ✨ ¿Qué hace este proyecto especial?
Este juego no solo funciona: está diseñado con una estructura clara y modular. La lógica del juego está separada de la interfaz, lo que permite:

- ✅ Código más limpio y fácil de mantener
- ✅ Posibilidad de escalar a una interfaz gráfica real (como tkinter, pygame o web)
- ✅ Mayor claridad para quienes están aprendiendo programación

---

## 🧩 Estructura del proyecto
- **CuatroEnRaya** → Clase principal que contiene toda la lógica del juego (tablero, reglas, turnos, verificación de ganador).
- **mostrar_tablero(tablero)** → Función externa que imprime el tablero en consola.
- **juego_cuatro_en_raya** → Función que simula una interfaz gráfica dentro de la consola. Se encarga de mostrar mensajes, recibir entradas del jugador y coordinar el flujo del juego.

---

## 🛠️ ¿Cómo ejecutar el juego?
### ✅ Requisitos
Solo necesitas tener Python 3 instalado. Puedes verificarlo con:
```bash
python --version
```

### ▶ Ejecutar el juego
1. Guarda el código en un archivo llamado `cuatro_en_raya.py`.
2. Abre tu terminal en la carpeta donde guardaste el archivo.
3. Ejecuta el siguiente comando:
```bash
python cuatro_en_raya.py
```

El juego te pedirá:
- Número de filas
- Número de columnas
- Tu ficha (X o Y)

¡Y listo! A jugar 😄

---

## 👨‍💻 Autor
Jesús — interesado en el aprendizaje de la programación
