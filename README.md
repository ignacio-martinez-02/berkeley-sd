# Berkeley - Simulación de sincronización de relojes

Proyecto desarrollado para la materia "Sistemas Distribuidos" de la carrera Ingeniería en Sistemas de Información (UTN-FRCU).

- Profesores: Ulises Rapallini y Ernesto Ledesma
- Autor: Ignacio Gabriel Martínez

## Descripción

Esta pequeña práctica implementa una simulación del algoritmo de Berkeley para sincronizar relojes en un sistema maestro-esclavo. Está pensada como un ejercicio pedagógico para la materia.

El repositorio contiene un maestro que coordina la sincronización y dos esclavos que reportan su tiempo local y reciben el tiempo ajustado.

## Estructura de archivos

- `master.py` — Script que actúa como el servidor maestro. Escucha conexiones de los esclavos, recibe sus tiempos, calcula el ajuste promedio según el algoritmo de Berkeley y envía el tiempo sincronizado a los esclavos.
- `slave1.py` — Cliente/esclavo que se conecta al maestro. Envía su hora local (se ingresa por consola) y recibe el nuevo tiempo sincronizado.
- `slave2.py` — Segundo cliente/esclavo (idéntico en funcionamiento a `slave1.py`).

> Nota: los tres scripts usan la librería estándar `socket` de Python. No hay dependencias externas.

## Requisitos

- Python 3.x
- Sistema operativo con sockets (Linux, macOS, Windows)

## Objetivo

Demostrar el funcionamiento básico del algoritmo de Berkeley: el maestro colecta los tiempos de los esclavos, calcula un ajuste promedio (considerando también su propio reloj) y difunde el nuevo tiempo sincronizado para que todos los nodos queden alineados.

## Cómo usar

1. Abrir tres terminales (o pestañas).
2. En la primera terminal, ejecutar el maestro:

```bash
python3 master.py
```

3. En la segunda terminal, ejecutar el primer esclavo:

```bash
python3 slave1.py
```

Al ejecutar, `slave1.py` pedirá por consola que ingreses el tiempo actual del esclavo (valor numérico en segundos). Ingresa, por ejemplo, `98.5`.

4. En la tercera terminal, ejecutar el segundo esclavo:

```bash
python3 slave2.py
```

También se pedirá el tiempo local del segundo esclavo (por ejemplo, `101.2`).

Importante: el maestro espera exactamente dos esclavos (`server.listen(2)`), por lo que debes iniciar ambos esclavos después o mientras el maestro está esperando conexiones.

## Resultado esperado

- El maestro imprimirá mensajes indicando la recepción de las conexiones de los esclavos y los tiempos recibidos.
- Se calculará el ajuste promedio teniendo en cuenta las diferencias entre los relojes de los esclavos y el reloj del maestro. El maestro mostrará el ajuste y el nuevo tiempo sincronizado.
- El maestro enviará el nuevo tiempo a cada esclavo. Cada esclavo imprimirá la hora local antes de sincronizar y la hora sincronizada recibida.

Ejemplo (salida simplificada):

```
🕒 Maestro iniciado. Esperando conexiones de esclavos...
✅ Conectado esclavo desde ('127.0.0.1', 54612)
✅ Conectado esclavo desde ('127.0.0.1', 54616)
⏱️  Hora recibida del esclavo: 98.50s
⏱️  Hora recibida del esclavo: 101.20s

🧮 Ajuste promedio: -0.10s
🕓 Nuevo tiempo sincronizado: 99.90s

Tiempos finales sincronizados:
   Maestro: 99.90s
   Esclavo 1: 99.90s
   Esclavo 2: 99.90s

✅ Sincronización completada correctamente.
```

Y en cada esclavo se verá algo como:

```
Conectado al maestro. Hora del maestro: 100.0s
Mi hora local (antes de sincronizar): 98.5s
Hora sincronizada recibida: 99.9s
✅ Sincronización exitosa.
```

## Notas y consideraciones

- El puerto por defecto es `5000` y la IP `127.0.0.1` (localhost). Si quieres probar en distintas máquinas modifica `HOST` y `PORT` acorde a la red.
- Esta implementación es una simulación simplificada. No considera retardos de red (latencia), fallos de comunicación, o realidades del reloj del sistema (se usan valores simulados ingresados manualmente).
- Para experimentar, puedes modificar los valores iniciales del reloj del maestro en `master.py` o automatizar los relojes de los esclavos.

## Autor y créditos

Ignacio Gabriel Martínez

Trabajo realizado para la materia "Sistemas Distribuidos" (UTN-FRCU), profesores Ulises Rapallini y Ernesto Ledesma.

