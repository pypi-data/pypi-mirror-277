Función **GET_CAT_COLUMNS_MANY_CATS**
==============================
<p1>Esta función retorna las columnas categóricas que contienen como mínimo N número de categorías, esto se logra configurando el parámetro MIN_UNIQUE al valor que se desea.</p1>

**<h2>Parámetros</h2>**
<p> Esta función cuenta con dos parámetros principales</p>

```Python
helper_dataframe.get_cat_columns_many_cats( X, min_unique = 15 )
```

<p1><strong>X</strong> (Requerido): Dataframe a analizar las columnas categóricas.</p1>

<p1><strong>min_unique</strong> : Mínimo número de categorías para ser considerado a una columna como variable categórica, por defecto toma el valor de 15.</p1>

**<h2>Retornos</h2>**

<p1><strong>list_cl_many_cat</strong> : Listado de columnas categóricas.</p1>
<p1> </p1>



**<h2>Ejemplo de uso</h2>**
<p1> A continuación, se muestra un código de ejemplo sobre el uso de la función.</p1>

**<h3>Código :</h3>**
```Python
import pandas as pd
from data_science_helper import helper_dataframe as hd

df = pd.DataFrame(data = [[1,'Juan'   ,'Rojas'    , 12 , '4to' ,'Mañana'],
                          [2,'Pedro'  , None      , 11 , '5to' , None   ],
                          [3,'Alex'   ,'Sanchez'  , 13 , '4to' ,'Tarde' ],
                          [4,'Jose'   ,'Romero '  ,None, '5to' , None   ],
                          [5,'Manuel' ,'Julca'    , 10 , '5to' ,'Mañana'],
                          [6,'Jose'   , None      , 11 , '5to' , None   ],
                          [7,'Pedro'  ,'Sanchez'  , 12 , '5to' ,'Tarde' ],
                          [8,'Ricardo','Paredes'  , 13 , '5to' ,'Tarde' ],
                          [9,'Gustavo', None      , 11 , '5to' , None   ],
                         [10,'Ismael' , None      , 12 , '5to' ,'Tarde' ],
                         [11,'Jhon'   , None      , 11 , '5to' , None   ],
                         [12,'Ana'    , None      , 10 , '5to' ,'Mañana'],
                         [13,'Nicolas', 'Carrasco',None, '4to' ,'Mañana']], 
                  columns = ['ID', 'Nombre', 'Apellido', 'Edad', 'Grado', 'Turno'])

cat_columns = hd.get_cat_columns_many_cats(df, min_nunique=2)

print(df.head(15))
 
print('LISTA DE COLUMNAS CATEGORICAS: ', cat_columns)
```


**<h3>Output :</h3>**

```Python
    ID   Nombre  Apellido  Edad Grado   Turno
0    1     Juan     Rojas  12.0   4to  Mañana
1    2    Pedro      None  11.0   5to    None
2    3     Alex   Sanchez  13.0   4to   Tarde
3    4     Jose   Romero    NaN   5to    None
4    5   Manuel     Julca  10.0   5to  Mañana
5    6     Jose      None  11.0   5to    None
6    7    Pedro   Sanchez  12.0   5to   Tarde
7    8  Ricardo   Paredes  13.0   5to   Tarde
8    9  Gustavo      None  11.0   5to    None
9   10   Ismael      None  12.0   5to   Tarde
10  11     Jhon      None  11.0   5to    None
11  12      Ana      None  10.0   5to  Mañana
12  13  Nicolas  Carrasco   NaN   4to  Mañana


LISTA DE COLUMNAS CATEGORICAS:  ['Nombre', 'Apellido']
```

[Volver a índice](../../docsPrincipal.md ) $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ [Ir al siguiente](HELPER_DATAFRAME_get_cat_columns.md)