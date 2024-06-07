Función **ENCODER_CAT**
==============================
<p1>Esta función codifica todas las variables categóricas o de tipo Object de un Dataframe determinado usando la función LabelEncoder del paquete <a target="_blank" href="https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html">sklearn.preprocessing</a>.</p1>

**<h2>Parámetros</h2>**
<p> Esta función cuenta con dos parámetros principales</p>

```Python
helper_functions.encoder_cat( X=None, columns_cat=[] )
```

<p1><strong>X</strong> (Requerido): Dataframe sobre la cual se desea categorizar los campos, por defecto toma el valor de <strong>None</strong>.</p1>

<p1><strong>columns_cat</strong> (Requerido): lista de columnas que se desea categorizar, por defecto se encuentra con valor <strong>[ ]</strong> (Lista vacía)</p1>

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

hf.encoder_cat(df, ['Grado'] )

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

   ID  Nombre   Apellido  Edad  Grado
0   1   Juan       Rojas  12.0      0
1   2   Pedro       None  11.0      1
2   3    Alex    Sanchez  13.0      0
3   4   Jose     Romero    NaN      1
4   5  Manuel      Julca  10.0      1
5   6    None  Carrasco    NaN      0
```

[Volver a índice](../../docsPrincipal.md ) $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ [Ir al siguiente](HELPER_FUNCTIONS_pivot_columns.md)