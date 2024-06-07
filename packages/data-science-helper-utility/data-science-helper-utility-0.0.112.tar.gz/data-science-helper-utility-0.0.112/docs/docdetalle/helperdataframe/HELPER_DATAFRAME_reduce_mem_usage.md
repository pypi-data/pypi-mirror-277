Función **REDUCE_MEM_USAGE**
==============================
<p1>Esta función reduce el tamaño de la memoria que se usa para almacenar los Dataframes, esto se logra iterando a través de todas las columnas del Dataframe y modifica el tipo de datos para reducir el uso de la memoria.</p1>

**<h2>Parámetros</h2>**
<p> Esta función cuenta con tres parámetros principales</p>

```Python
helper_dataframe.reduce_mem_usage(df, category=False, verbose=False)
```

<p1><strong>df</strong> (Requerido): Dataframe sobre el cual se desea realizar la operación de la función de optimización de memoria.</p1>

<p1><strong>category</strong> : Flag que indica si contiene variables categóricas, por defecto toma el valor de FALSE.</p1>

<p1><strong>verbose</strong> : Flag que indica si se requiere imprimir el avance de la optimización en todas las iteraciones que esta toma, por defecto toma el valor de FALSE.</p1>

**<h2>Retornos</h2>**

<p1><strong>None</strong> : No retorna ningún valor.</p1>
<p1> </p1>



**<h2>Ejemplo de uso</h2>**
<p1> A continuación, se muestra un código de ejemplo sobre el uso de la función.</p1>

**<h3>Código :</h3>**

```Python
import pandas as pd
from data_science_helper import helper_dataframe as hd

df = pd.DataFrame(data = [[1,' Juan ', 'Rojas'    , 12 , '4to' ],
                          [2,' Pedro', None       , 11 , '5to' ],
                          [3,'  Alex', '  Sanchez', 13 , '4to' ],
                          [4,' Jose ', '  Romero ',None, '5to' ],
                          [5,'Manuel', 'Julca'    , 10 , '5to' ],
                          [6,  None  , 'Carrasco ',None, '4to']], 
                  columns = ['ID', 'Nombre', 'Apellido', 'Edad', 'Grado'])

print('Tamaño de la memria usada: ', df.memory_usage().sum())
print(df.head(10))

hd.reduce_mem_usage(df = df, verbose=True)

print('Tamaño de la memria usada: ', df.memory_usage().sum())
print(df.head(10))
```


**<h3>Output :</h3>**

```Python
Tamaño de la memria usada:  368


   ID  Nombre   Apellido  Edad Grado
0   1   Juan       Rojas  12.0   4to
1   2   Pedro       None  11.0   5to
2   3    Alex    Sanchez  13.0   4to
3   4   Jose     Romero    NaN   5to
4   5  Manuel      Julca  10.0   5to
5   6    None  Carrasco    NaN   4to


Memory usage of dataframe is 0.00 MB
Memory usage after optimization is: 0.00 MB
Decreased by 21.2%


Tamaño de la memria usada:  290


   ID  Nombre   Apellido  Edad Grado
0   1   Juan       Rojas  12.0   4to
1   2   Pedro       None  11.0   5to
2   3    Alex    Sanchez  13.0   4to
3   4   Jose     Romero    NaN   5to
4   5  Manuel      Julca  10.0   5to
5   6    None  Carrasco    NaN   4to
```

[Volver a índice](../../docsPrincipal.md ) $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ [Ir al siguiente](HELPER_DATAFRAME_show_na.md)
