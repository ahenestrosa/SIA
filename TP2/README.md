# SIA - TP2

## Instrucciones para Configuracion

El sistema se podra configurar mediante el archivo `config.json`, el mismo cuenta con los campos necesarios para ejecutar cualquiera de los algoritmos implementados. Se deben completar todos los campos aunque los valores no sean utilizados por el algoritmo elegido.

Un ejemplo de archivo de configuración es el siguiente:
```
{
    "populationSize": 400,
    "crossing": "UNIFORM",
    "mutation": "UNIFORM",
    "selector1": "TOURNAMENT_P",
    "selector2": "ROULETTE",
    "selector3": "ELITE",
    "selector4": "RANKING",
    "selectorA": 0.75,
    "selectorB": 0.25,
    "endingCondition": "GEN_AMMOUNT",
    "character": "GUERRERO",
    "pm": 0.25,
    "selectionChilds": 200,
    "fillMethod": "FILL_ALL",

    "endingGenerationsCompared": 10,  
    "endingFitnessLimit": 50,
    "endingDeltaFitness": 3,
    "endingGenerationsLimit": 50,
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

En cuanto al campo `endingCondition` podrá tomar los siguientes valores: **ACC_SOL, CONTENT, GEN_AMMOUNT, STRUCTURE, TIME**.
Cada una de estas condiciones de corte tambien tienen sus respectivas configuraciones, todas ellas pueden tomar como valores numeros enteros.

## Instrucciones para incorporacion del Dataset

El Dataset debe estar en formato `.tsv` y para que el sistema lea de dicho Dataset se debe agregar el path al mismo en el archivo `Constants.py` (en el lugar **BOTAS_PATH, GUANTES_PATH, ARMAS_PATH, PECHERA_PATH, CASCOS_PATH**) ubicado en la carpeta `TP2/Utilities`.

***Completar***

## Instrucciones para la Ejecución

Situados en la carpeta `TP2` del proyecto, se puede ejecutar el sistema mediante el comando:

```bash
python3 __main__.py
```

Se podrá ver mediante un grafico en tiempo real el Fitness Mínimo, Fitness Promedio y el Fitness Máximo por cada Generación.

***Completar***


## Integrantes
- Augusto Henestrosa
- Francisco Choi
- Nicolás de la Torre