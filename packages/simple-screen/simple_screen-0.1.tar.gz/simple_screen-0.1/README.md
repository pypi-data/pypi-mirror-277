# Simple Screen

Provee una serie de funciones basadas en curses, para permitir usar print e input de forma posicionada y jugar con colores.

La idea es poder crear programas que vayan enfrentando a situaciones algo mas reales que con print e input, pero sin necesitar librerias que metan ruido a la hora de enseñar. Es un paso previo.

## Funciones que aporta

Aquí tienes un listado de las funciones públicas del archivo proporcionado junto con una breve explicación de cada una:

1. **pause(ms)**
   - Pausa la ejecución del programa durante una cantidad de milisegundos especificada.

2. **init()**
   - Inicializa la pantalla de curses y configura los parámetros básicos como dimensiones, colores y pares de colores.

3. **finish()**
   - Finaliza el uso de curses y restaura la configuración del terminal a su estado original.

4. **cls(refresh=False)**
   - Limpia la pantalla y opcionalmente refresca la pantalla para mostrar los cambios inmediatamente.

5. **locate(x, y)**
   - Mueve el cursor a la posición (x, y) especificada en la pantalla.

6. **Print(cadena, refresh=False)**
   - Imprime una cadena en la pantalla en la posición actual del cursor y opcionalmente refresca la pantalla para mostrar los cambios inmediatamente.

7. **Input(mensaje="")**
   - Muestra un mensaje en la pantalla y espera la entrada del usuario. Devuelve la cadena de entrada del usuario.

8. **pair(fg, bg, refresh=False)**
   - Configura el par de colores activo con los colores de primer plano (fg) y fondo (bg) especificados, y opcionalmente refresca la pantalla para mostrar los cambios inmediatamente.

9. **pen(fg, refresh=False)**
   - Cambia el color del "bolígrafo" (texto) al color de primer plano especificado y opcionalmente refresca la pantalla para mostrar los cambios inmediatamente.

10. **paper(bg, refresh=False)**
    - Cambia el color del "papel" (fondo) al color de fondo especificado y opcionalmente refresca la pantalla para mostrar los cambios inmediatamente.

Estas funciones permiten interactuar con la pantalla usando la biblioteca `curses`, manejando colores y posiciones del cursor para una interfaz de texto avanzada.