# SIA - TP2

## Instrucciones para Configuracion

El sistema se podra configurar mediante el archivo `config.json`, el mismo cuenta con los campos necesarios para ejecutar cualquiera de los algoritmos implementados. Se deben completar todos los campos aunque los valores no sean utilizados por el algoritmo elegido.

Un ejemplo de archivo de configuración es el siguiente:
```
{
    "populationSize": 400,
    "crossing": "ANULAR",
    "mutation": "GENE",
    "selector1": "TOURNAMENT_D",
    "selector2": "UNIVERSAL",
    "selector3": "TOURNAMENT_D",
    "selector4": "UNIVERSAL",
    "selectorA": 0.5,
    "selectorB": 0.5,
    "endingCondition": "TIME",
    "character": "INFILTRADO",
    "pm": 0.5,
    "selectionChilds": 200,
    "fillMethod": "FILL_ALL",


    "t0_temp" : 3,
    "tc_temp" : 1.0,
    "k_temp" : 0.1,
    "tp_threshold": 0.75,
    "td_m": 5,

    "endingGenerationsCompared": 5,  
    "endingFitnessLimit": 20    ,
    "endingDeltaFitness": 1,
    "endingGenerationsLimit": 100,
    "endingStructureDh": 1,
    "endingStructureDad": 1,
    "endingStructureDf": 1,
    "endingStructurePp": 1,
    "endingTimeLimit": 30.0

}
```

Los personajes para al campo `character` pueden ser: **GUERRERO, ARQUERO, DEFENSOR, INFILTRADO**

Los valores válidos para `crossing` son: **ONE-POINT, TWO-POINT, ANULAR, UNIFORM**

Los valores válidos para `mutation` son: **GENE, LIMITED-MULTIGENE, UNIFORM, GENE-COMPLETE**

Los 4 `selector` pueden ser: **BOLTZMANN, ELITE, RANKING, ROULETTE, TOURNAMENT_D, TOURNAMENT_P, UNIVERSAL**

El campo `fillMethod`solo puede tener dos valores: **FILL_ALL, FILL_PARENT**

Los valores para parametrizar **BOLTZMANN** son:
- `t0_temp`: temperatura inicial
- `tc_temp`: temperatura de corte
-` k_temp`: parametro de la exponencial

Los valores para parametrizar **TOURNAMENT_P** son:
-`tp_threshold`: indica el threshold.

Los valores para parametrizar **TOURNAMENT_D** son:
-`td_m`: indica la cantidad de individuos a elegir

En cuanto al campo `endingCondition` podrá tomar los siguientes valores: **ACC_SOL, CONTENT, GEN_AMMOUNT, STRUCTURE, TIME**.
Los valores para su parametrizacion son:
- `endingGenerationsCompared`:  Cantidad de generaciones utilizada para comparar: utilizado por STRUCTURE Y CONTENT
- `endingFitnessLimit`: Fitness limite, utilizado por ACC_SOL
- `endingDeltaFitness`: Variacion minima del fitness, utilizado por CONTENT
- `endingGenerationsLimit`: Limite de generaciones, utilizado por GEN_AMMOUNT
- `endingStructureDh`: Utilizado por STRUCTURE
- `endingStructureDad`: Utilizado por STRUCTURE
- `endingStructureDf`: Utilizado por STRUCTURE
- `endingStructurePp`: Utilizado por STRUCTURE
- `endingTimeLimit`: Tiempo limite, utilizado por TIME


Cada una de estas condiciones de corte tambien tienen sus respectivas configuraciones, todas ellas pueden tomar como valores numeros enteros o float's.



## Instrucciones para incorporacion del Dataset

El Dataset debe estar en formato `.tsv` y para que el sistema lea de dicho Dataset se debe agregar el path al mismo en el archivo `Constants.py` (en el lugar **BOTAS_PATH, GUANTES_PATH, ARMAS_PATH, PECHERA_PATH, CASCOS_PATH**) ubicado en la carpeta `TP2/Utilities`.

## Instrucciones para la Ejecución

Situados en la carpeta `TP2` del proyecto, se puede ejecutar el sistema mediante el comando:

```bash
python3 __main__.py
```

Se podrá ver mediante un grafico en tiempo real el Fitness Mínimo, Fitness Promedio y el Fitness Máximo por cada Generación.


## Integrantes
- Augusto Henestrosa
- Francisco Choi
- Nicolás de la Torre