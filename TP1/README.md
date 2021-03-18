# SIA - TP1

## Instrucciones para Configuracion

El sistema se podra configurar mediante el archivo `config.json`, el mismo cuenta con los campos necesarios para ejecutar cualquiera de los algoritmos implementados. Se deben completar todos los campos aunque los valores no sean utilizados por el algoritmo elegido. 

Un ejemplo de configuración para utilizar el algoritmo `greedy` con la heurística `1` => boxObjDistance y el mapa `map1` con la visualización desactivada:

```
{
    "algorithm": "greedy",
    "heuristic": 1,
    "level_map": "map1",
    "iddfs_max_depth": 1000,
    "visual" : false
}
```

Los valores validos para `algorithm` son:
- bfs
- dfs
- iddfs
- greedy
- a*
- ida

Los valores para `heuristic` son enteros positivos del 1 al 5.

Mientras que para `level_map` puede tomar el valor cualquier nombre de los archivos `.txt` que se encuentren en la carpeta ubicada en `TP1/maps` (Si desea crear nuevos mapas, estos deben ser cuadrados de NxN). El campo `iddfs_max_depth` debe tener como valor un número entero positivo. Y `visual` puede ser `true` o `false`.


## Instrucciones para la Ejecución

### Requerimientos

Para la ejecución del sistema, se requiere tener instalado `python3` y `matplotlib`. Dicha libreria se puede instalar mediante el comando:

```bash
pip install -r requirements.txt
```
o
```bash
sudo python3 -m pip install -r requirements.txt
```

### Ejecución

Situados en la carpeta `TP1` del proyecto, se puede ejecutar el sistema mediante el comando:

```bash
python3 __main__.py
```

Por `stdout` se visualizara el nombre del mapa, el nombre del algoritmo, la heuristica y la máxima profundidad de nodos de iddfs.
También se podrá ver si el mapa fue resuelto o no, la profundidad, el costo, la cantidad de nodos expandidos, la cantidad de nodos frontera y el tiempo de la solución.

### Resultados

Luego de ejecutar el sistema, se generara un archivo `.txt` en la carpeta `results` con el formato [MAP]-[ALGORITHM]-[HEURISTIC].txt donde se podrá ver, ademas de lo mostrado por `stdout`, el camino realizado hasta llegar al objetivo.

Si la configuración del sistema tenia la visual activa, ademas de generar el archivo con estadisticas y resultados, se mostrara en pantalla, graficado cada paso del jugador hasta llegar al objetivo.


## Integrantes
- Augusto Henestrosa
- Francisco Choi
- Nicolás de la Torre

