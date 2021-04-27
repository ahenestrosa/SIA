# SIA - TP3

## Instrucciones para la Ejecución

Situados en la carpeta `TP3` del proyecto, se puede ejecutar el ejercicio deseado mediante los comandos:

**EJECUCION Del Ejercicio 1**
```bash
python3 ej1.py 
```
En la salida se mostrará que operador logico se esta ejecutando, la salida esperada y la salida obtenida luego de ejecutar el **Perceptrón Simple**.

**EJECUCION Del Ejercicio 2**
```bash
python3 ej2.py [-linear|-nonlinear|-multipleNonLinear] true
```

Por ejemplo: 
```bash
python3 ej2.py -nonlinear true
```
Ejecuta el ejercicio 2, con el **Perceptrón Simple No Lineal**, en la salida se podra visualizar cada preducción y el valor deseado. Además se mostrará un grafico de Época vs Error.

El flag `-linear` realizará lo mismo que con el flag mostrado en el ejemplo pero con el **Perceptrón Simple Lineal**.

En cuanto al flag `-multipleNonLinear` tambien ejecutará el  **Perceptrón Simple No Lineal** variando el rango de aprendizaje y la cantidad de épocas. En este caso, la salida serán 3 plots, uno por cada rango de aprendizaje.

**EJECUCION Del Ejercicio 3**
```bash
python3 ej3a.py 
```
o
```bash
python3 ej3b.py 
```

Se podrá visualizar en la salida como evoluciona el error al transcurrir las etapas, los resultados obtenidos y un plot de Epoca vs Error en el caso del `ej3a`.

## Integrantes
- Augusto Henestrosa
- Francisco Choi
- Nicolás de la Torre