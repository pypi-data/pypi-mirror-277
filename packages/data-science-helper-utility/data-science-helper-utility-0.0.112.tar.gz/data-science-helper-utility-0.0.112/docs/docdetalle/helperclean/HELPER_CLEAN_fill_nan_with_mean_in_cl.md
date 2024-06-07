Función **FILL_NAN_WITH_MEAN_IN_CL**
==============================
<p1>Esta función completa los valores nulos en las variables numéricas asignando el valor de la media (MEAN) para los valores nulos en la columna CL_NAME considerando la columna CLS_GROUP la columna de agrupamiento para el cálculo de la media.</p1>

**<h2>Parámetros</h2>**
<p> Esta función cuenta con tres parámetros principales</p>

```Python
helper_clear.fill_nan_with_mean_in_cl(df, cl_name, cls_group)
```

<p1><strong>df</strong> (Requerido): Dataframe sobre el cual se desea realizar la operación de la función, esta contiene las columnas listadas en la variable CL_NAME que contienen valores nulos.</p1>

<p1><strong>cl_name</strong> (Requerido):  Columna sobre la cual se requiere completar los valores nulos con la media del grupo CLS_GROUPS.</p1>

<p1><strong>cls_group</strong> (Requerido):  Columnas de agrupamiento para el cálculo de la media.</p1>

**<h2>Retornos</h2>**

<p1><strong>df_result</strong> : Dataframe resultado con los valores completados con la media.</p1>
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

df_mean = hcl.fill_nan_with_mean_in_cl(df,'Edad','Grado')

print(df_mean.head(10))
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

   ID  Nombre   Apellido  Edad Grado
0   1   Juan       Rojas  12.0   4to
1   2   Pedro       None  11.0   5to
2   3    Alex    Sanchez  13.0   4to
3   4   Jose     Romero   10.5   5to
4   5  Manuel      Julca  10.0   5to
5   6    None  Carrasco   12.5   4to
```
[Volver a índice](../../docsPrincipal.md ) $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ [Ir al siguiente](HELPER_CLEAN_fill_nan_with_nan_category_in_cls.md)