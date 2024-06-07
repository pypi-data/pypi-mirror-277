Función **UPPER_CATEGORY_CLS**
==============================
<p1>Esta función convierte a mayúscula el valor de cada registro de las columnas listadas en el parámetro CL_LIST, ignora los valores nulos u los deja como nulos.</p1>

**<h2>Parámetros</h2>**
<p1> Esta función cuenta con dos parámetros principales</p1>

```Python
helper_clear.upper_category_cls(df, cl_list)
```

<p1><strong>df</strong> (Requerido): Dataframe sobre el cual se desea realizar la operación de la función, esta contiene las columnas listadas en la variable CL_LIST.</p1>

<p1><strong>cl_list</strong> (Requerido): Listado de columnas del DATAFRAME sobre las cuales se requiere realizar la operación de pasar el texto a mayúscula.</p1>


**<h2>Retornos</h2>**

<p1><strong>df_result</strong> : Dataframe Resultado de la operación convertir a mayúscula, realizando la operación sobre las columnas listadas en el parámetro CL_LIST.</p1>
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

df_up = hcl.upper_category_cls(df, ['Nombre']) 

print(df_up.head(10))
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
0   1   JUAN       Rojas  12.0   4to
1   2   PEDRO       None  11.0   5to
2   3    ALEX    Sanchez  13.0   4to
3   4   JOSE     Romero    NaN   5to
4   5  MANUEL      Julca  10.0   5to
5   6    None  Carrasco    NaN   4to
```

[Volver a índice](../../docsPrincipal.md ) $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ [Ir al siguiente](../helperdataframe/HELPER_DATAFRAME_Diff.md)