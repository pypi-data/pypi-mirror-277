Función **IGUALAR_COLUMNAS**
==============================
<p1>Esta función requiere como entrada dos Dataframes, realiza el cruce y retorna las columnas comunes de ambos Dataframes, esto con el objetivo de tener Dataframes con las mismas columnas.</p1>

**<h2>Parámetros</h2>**
<p> Esta función cuenta con dos parámetros principales</p>

```Python
helper_dataframe.igualar_columnas(X_test, X_t_eval_)
```

<p1><strong>X_test</strong> (Requerido): Dataframe del cual se considera como referencia las columnas que se buscaran en el Dataframe X_T_EVAL_.</p1>

<p1><strong>X_t_eval_</strong> (Requerido): Dataframe sobre el cual se realizara la operación de extracción de columnas iguales.</p1>

**<h2>Retornos</h2>**

<p1><strong>X_t_eval</strong> : Dataframe resultado del cruce entre los dos Dataframes ingresados, esta se construye a partir del X_T_EVAL_.</p1>
<p1> </p1>



**<h2>Ejemplo de uso</h2>**
<p1> A continuación, se muestra un código de ejemplo sobre el uso de la función.</p1>

**<h3>Código :</h3>**
```Python
import pandas as pd
from data_science_helper import helper_dataframe as hd

train = pd.DataFrame(data = [ [1,'Juan',   12 , '4to' ],
                              [2,' Pedro',   11 , '5to' ],
                              [3,'  Alex',   13 , '4to' ],
                              [4,' Jose ',  None, '5to' ],
                              [5,'Manuel',   10 , '5to' ],
                              [6,  None  ,  None, '4to']], 
                  columns = ['ID', 'Nombre',  'Edad', 'Grado'])


test = pd.DataFrame(data = [ [1,'Juan', 'Rojas'    , 12 , '4to',    'JOD' ],
                             [2,' Pedro', None       , 11 , '5to' , 'JOD'],
                             [3,'  Alex', '  Sanchez', 13 , '4to' , 'JAE'],
                             [5,'Manuel', 'Julca'    , 10 , '5to' , 'JAE']],
                  columns = ['ID', 'Nombre', 'Apellido', 'Edad', 'Grado', 'Colegio'])

print('Dataframe TRAIN: ')

print(train.head(10))

print('Dataframe TEST: ')

print(test.head(10))

result = hd.igualar_columnas(train, test)

print('Dataframe RESULT: ')

print(result.head(10))
```


**<h3>Output :</h3>**

```Python
Dataframe TRAIN: 

   ID  Nombre  Edad Grado
0   1    Juan  12.0   4to
1   2   Pedro  11.0   5to
2   3    Alex  13.0   4to
3   4   Jose    NaN   5to
4   5  Manuel  10.0   5to
5   6    None   NaN   4to


Dataframe TEST: 

   ID  Nombre   Apellido  Edad Grado Colegio
0   1    Juan      Rojas    12   4to     JOD
1   2   Pedro       None    11   5to     JOD
2   3    Alex    Sanchez    13   4to     JAE
3   5  Manuel      Julca    10   5to     JAE


Dataframe RESULT: 

   ID  Nombre  Edad Grado
0   1    Juan    12   4to
1   2   Pedro    11   5to
2   3    Alex    13   4to
3   5  Manuel    10   5to
```

[Volver a índice](../../docsPrincipal.md ) $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ [Ir al siguiente](HELPER_DATAFRAME_reduce_mem_usage.md)
