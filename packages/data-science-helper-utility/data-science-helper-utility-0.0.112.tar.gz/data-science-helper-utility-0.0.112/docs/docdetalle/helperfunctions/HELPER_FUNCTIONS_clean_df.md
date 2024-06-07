Función **CLEAN_DF**
==============================
<p1>Esta función realiza la limpieza de los espacios en blanco y convierte las los datos de columnas definidas en mayúsculas.</p1>

**<h2>Parámetros</h2>**
<p1> Esta función cuenta con dos parámetros principales</p1>

```Python
helper_functions.clean_df(df, columns)
```

<p1><strong>df</strong> (Requerido): Dataframe que contiene las columnas que requiere convertir a Texto y aplicar la limpieza.</p1>

<p1><strong>columns </strong> (Requerido): Listado de columnas sobre los cuales se aplicara la función.</p1>

**<h2>Retornos</h2>**

<p1><strong>None</strong> : No retorna ningún valor.</p1>
<p1> </p1>


**<h2>Ejemplo de uso</h2>**
<p1> A continuación, se muestra un código de ejemplo sobre el uso de la función.</p1>

**<h3>Código :</h3>**
```Python
import pandas as pd
from data_science_helper import helper_functions as hf

# Dataset Estudiantes
df = pd.DataFrame(data = [[1,' Juan ', 'Rojas'    , 12 , '4to' ],
                          [2,' Pedro', None       , 11 , '5to' ],
                          [3,'  Alex', '  Sanchez', 13 , '4to' ],
                          [4,' Jose ', '  Romero ',None, '5to' ],
                          [5,'Manuel', 'Julca'    , 10 , '5to' ],
                          [6,  None  , 'Carrasco ',None, '4to']], 
                  columns = ['ID', 'Nombre', 'Apellido', 'Edad', 'Grado'])

print(df.head(10))

hf.clean_df(df, ['Nombre', 'Apellido'] )

print(df.head(10))
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

   ID  Nombre  Apellido  Edad Grado
0   1    JUAN     ROJAS  12.0   4to
1   2   PEDRO       NAN  11.0   5to
2   3    ALEX   SANCHEZ  13.0   4to
3   4    JOSE    ROMERO   NaN   5to
4   5  MANUEL     JULCA  10.0   5to
5   6     NAN  CARRASCO   NaN   4to
```
[Volver a índice](../../docsPrincipal.md ) $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ [Ir al siguiente](HELPER_FUNCTIONS_encoder_cat.md)



