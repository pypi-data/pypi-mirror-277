Función **AGREGAR_NA_CLS**
==============================
<p1>Esta función adiciona columnas en las que se identifica los valores nulos asignándoles un valor de 1 y 0 en el caso contrario, esto se realiza en cada una de las columnas listadas en el parámetro CL_LIST.</p1>

**<h2>Parámetros</h2>**
<p> Esta función cuenta con dos parámetros principales</p>

```Python
helper_clear.agregar_na_cls(df, cl_list)
```

<p1><strong>df</strong> (Requerido): Dataframe sobre el cual se desea agregar las columnas identificando los valores nulos.</p1>

<p1><strong>cl_list</strong> (Requerido):  Listado de columnas del DATAFRAME sobre las cuales se requiere realizar el análisis de los valores nulos.</p1>


**<h2>Retornos</h2>**

<p1><strong>df_result</strong> : Dataframe Resultado del análisis de valores nulos, esta contiene nuevas columnas identificando que registro contiene un valor nulo, la cantidad de columnas adicionadas es la cantidad de columnas listadas en la variable CL_LIST.</p1>
<p1> </p1>



**<h2>Ejemplo de uso</h2>**
<p1> A continuación, se muestra un código de ejemplo sobre el uso de la función.</p1>


**<h3>Código :</h3>**
```Python
import pandas as pd
from data_science_helper import helper_clean as hcl

# Dataset Estudiantes
df = pd.DataFrame(data = [[1,' Juan ', 'Rojas'    , 12 , '4to' ],
                          [2,' Pedro', None       , 11 , '5to' ],
                          [3,'  Alex', '  Sanchez', 13 , '4to' ],
                          [4,' Jose ', '  Romero ',None, '5to' ],
                          [5,'Manuel', 'Julca'    , 10 , '5to' ],
                          [6,  None  , 'Carrasco ',None, '4to']], 
                  columns = ['ID', 'Nombre', 'Apellido', 'Edad', 'Grado'])

# Agregando Columnas 
df_cl = hcl.agregar_na_cls(df, ['Nombre', 'Apellido', 'Edad'])

print(df_cl.head(10))
```


**<h3>Output :</h3>**

```Python
NEW : NA_Nombre
NEW : NA_Apellido
NEW : NA_Edad

   ID  Nombre   Apellido  Edad Grado  NA_Nombre  NA_Apellido  NA_Edad
0   1   Juan       Rojas  12.0   4to          0            0        0
1   2   Pedro       None  11.0   5to          0            1        0
2   3    Alex    Sanchez  13.0   4to          0            0        0
3   4   Jose     Romero    NaN   5to          0            0        1
4   5  Manuel      Julca  10.0   5to          0            0        0
5   6    None  Carrasco    NaN   4to          1            0        1
```
[Volver a índice](../../docsPrincipal.md ) $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ [Ir al siguiente](HELPER_CLEAN_fill_nan_with_mean_in_cl.md)
