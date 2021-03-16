# SIA - TP1

## Instrucciones para Configuracion

El sistema se podra configurar mediante el archivo `config.json`, el mismo cuenta con los campos necesarios para ejecutar cualquiera de los algoritmos implementados. Se deben completar todos los campos aunque los valores no sean utilizados por el algoritmo elegido. 

Un ejemplo de configuración para utilizar el algoritmo `greedy` con la heurística `boxObjDistance` y el mapa `map1.txt` con la visualización desactivada:

```
{
    "algorithm": "greedy",
    "heuristic": "boxObjDistance",
    "level_map": "maps/map1.txt",
    "iddfs_max_depth": 1,
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

Los valores para `heuristic` son:
- boxObjDistance
- playerBoxDistance
- playerBoxObjDistance

Mientras que para `level_map` puede tomar el valor del path de cualquiera de los archivos que se encuentren en la carpeta ubicada en `TP1/maps`. El campo `iddfs_max_depth` debe tener como valor un número entero positivo. Y `visual` puede ser `true` o `false`.


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

Por `stdout` se visualizara el nombre del algoritmo, la heuristica (si se eligio un algoritmo informado) y la máxima profundidad (solo para el algoritmo IDDFS).
También se podrá ver si el mapa fue resuelto o no, el costo, la cantidad de nodos expandidos, la cantidad de nodos frontera y el tiempo de la solución.


***COMPLETAR DICIENDO COMO VA A SER LA VISUALIZACION***

## Integrantes
- Augusto Henestrosa
- Francisco Choi
- Nicolás de la Torre

