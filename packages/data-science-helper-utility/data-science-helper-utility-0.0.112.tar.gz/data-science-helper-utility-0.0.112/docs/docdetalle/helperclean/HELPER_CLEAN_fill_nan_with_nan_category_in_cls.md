Función **FILL_NAN_WITH_NAN_CATEGORY_IN_CLS**
==============================
<p1>Esta función completa los valores nulos en las variables categóricas asignando el valor de NAN_CATEGORY para los valores nulos en todas las columnas categóricas listadas en el parámetro CL_LIST.</p1>

**<h2>Parámetros</h2>**
<p> Esta función cuenta con dos parámetros principales</p>

```Python
helper_clear.fill_nan_with_nan_category_in_cls(df, cl_list)
```

<p1><strong>df</strong> (Requerido): Dataframe sobre el cual se desea realizar la operación de la función, esta contiene las columnas listadas en la variable CL_LIST que contienen valores nulos.</p1>

<p1><strong>cl_list</strong> (Requerido): Listado de columnas categóricas del DATAFRAME sobre las cuales se requiere realizar la operación..</p1>


**<h2>Retornos</h2>**

<p1><strong>df_result</strong> : Dataframe Resultado de la operación al asignar una nueva categoría a los valores nulos de las columnas listadas en el parámetro CL_LIST.</p1>
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

print(df.head(10))

df_nan = hcl.fill_nan_with_nan_category_in_cls(df, ['Nombre']) 

print(df_nan.head(10))
```


**<h3>Output :</h3>**

```Python
   ID  Nombre   Apellido  Edad Grado
0   1   Juan       Rojas  12.0   4to
1   2   Pedro       None  11.0   5to
2   3    Alex    Sanchez  13.0   4to
3   4   Jose     Romero    NaN   5to
4   5  Manuel      Julca  10.0   5to
5   6    None  Carrasco    NaN   4to

NEW nan_category:  Nombre
   ID        Nombre   Apellido  Edad Grado
0   1         Juan       Rojas  12.0   4to
1   2         Pedro       None  11.0   5to
2   3          Alex    Sanchez  13.0   4to
3   4         Jose     Romero    NaN   5to
4   5        Manuel      Julca  10.0   5to
5   6  NAN_CATEGORY  Carrasco    NaN   4to
```
[Volver a índice](../../docsPrincipal.md ) $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ [Ir al siguiente](HELPER_CLEAN_trim_category_cls.md)