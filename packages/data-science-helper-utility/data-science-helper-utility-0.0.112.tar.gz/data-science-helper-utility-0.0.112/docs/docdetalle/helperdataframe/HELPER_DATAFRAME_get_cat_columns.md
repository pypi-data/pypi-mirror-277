Función **GET_CAT_COLUMNS**
==============================
<p1>Esta función retorna las posibles columnas que podrían tratarse como variables categóricas.</p1>

**<h2>Parámetros</h2>**
<p> Esta función cuenta con un parámetro principal</p>

```Python
helper_dataframe.get_cat_columns( X )
```

<p1><strong>X</strong> (Requerido): Dataframe a analizar las columnas categóricas.</p1>

**<h2>Retornos</h2>**

<p1><strong>_categorical_columns_name</strong> : Listado de columnas que podrían tratarse como valores categóricos.</p1>
<p1> </p1>



**<h2>Ejemplo de uso</h2>**
<p1> A continuación, se muestra un código de ejemplo sobre el uso de la función.</p1>

**<h3>Código :</h3>**
```Python
import pandas as pd
from data_science_helper import helper_dataframe as hd

df = pd.DataFrame(data = [[1,' Juan ', 'Rojas'    , 12 , '4to' , None ],
                          [2,' Pedro', None       , 11 , '5to' , None ],
                          [3,'  Alex', '  Sanchez', 13 , '4to' , None ],
                          [4,' Jose ', '  Romero ',None, '5to' , None ],
                          [5,'Manuel', 'Julca'    , 10 , '5to' , None ],
                          [6,'Juan'  ,  None      , 11 , '5to' , None ],
                          [7,  None  , 'Carrasco ',None, '4to' , 'Mañana' ]], 
                  columns = ['ID', 'Nombre', 'Apellido', 'Edad', 'Grado', 'Turno'])

cat_columns = hd.get_cat_columns(df)

print(df.head(10))
 
print('LISTA DE COLUMNAS CATEGORICAS: ', cat_columns)
```


**<h3>Output :</h3>**

```Python
   ID  Nombre   Apellido  Edad Grado   Turno
0   1   Juan       Rojas  12.0   4to    None
1   2   Pedro       None  11.0   5to    None
2   3    Alex    Sanchez  13.0   4to    None
3   4   Jose     Romero    NaN   5to    None
4   5  Manuel      Julca  10.0   5to    None
5   6    Juan       None  11.0   5to    None
6   7    None  Carrasco    NaN   4to  Mañana


LISTA DE COLUMNAS CATEGORICAS:  ['Nombre', 'Apellido', 'Grado', 'Turno']
```

[Volver a índice](../../docsPrincipal.md ) $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ [Ir al siguiente](HELPER_DATAFRAME_heatmap_nan.md)