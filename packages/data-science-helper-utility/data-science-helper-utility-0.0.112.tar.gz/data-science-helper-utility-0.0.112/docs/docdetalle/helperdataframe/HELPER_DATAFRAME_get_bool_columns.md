Función **GET_BOOL_COLUMNS**
==============================
<p1>Esta función retorna las columnas que contienen datos booleanos, valores ceros y unos, el análisis se realiza sobre el Dataframe X ingresado como parámetro.</p1>

**<h2>Parámetros</h2>**
<p> Esta función cuenta con un parámetro principal</p>

```Python
helper_dataframe.get_bool_columns( X )
```

<p1><strong>X</strong> (Requerido): Dataframe a analizar las columnas booleanas.</p1>

**<h2>Retornos</h2>**

<p1><strong>bool_cols</strong> : Listado de columnas booleanas del Dataframe X.</p1>
<p1> </p1>



**<h2>Ejemplo de uso</h2>**
<p1> A continuación, se muestra un código de ejemplo sobre el uso de la función.</p1>

**<h3>Código :</h3>**
```Python
import pandas as pd
from data_science_helper import helper_dataframe as hd

# Genero : 1:Hombre, 0: Mujer
# Turno  : 1:Tarde, 0: Mañana

df = pd.DataFrame(data = [[1,'Juan'   ,'Rojas'    , 12 , '4to' ,1 , 1],
                          [2,'Pedro'  , None      , 11 , '5to' ,0 , 1],
                          [3,'Maria'   ,'Sanchez' , 13 , '4to' ,1 , 0],
                          [4,'Jose'   ,'Romero '  ,None, '5to' ,0 , 1],
                          [5,'Manuel' ,'Julca'    , 10 , '5to' ,1 , 1],
                          [6,'Fiorela', None      , 11 , '5to' ,1 , 0],
                          [7,'Pedro'  ,'Sanchez'  , 12 , '5to' ,0 , 1],
                          [8,'Ricardo','Paredes'  , 13 , '5to' ,1 , 1],
                          [9,'Carla'  , None      , 11 , '5to' ,1 , 0],
                         [10,'Ismael' , None      , 12 , '5to' ,0 , 1],
                         [11,'Jhon'   , None      , 11 , '5to' ,0 , 1],
                         [12,'Ana'    , None      , 10 , '5to' ,0 , 0],
                         [13,'Nicolas', 'Carrasco',None, '4to' ,1 , 1]], 
                  columns = ['ID', 'Nombre', 'Apellido', 'Edad', 'Grado', 'Turno', 'Genero'])

bool_columns = hd.get_bool_columns(df)

print(df.head(15))
 
print('LISTA DE COLUMNAS BOOLEANAS: ', bool_columns)
```


**<h3>Output :</h3>**

```Python
    ID   Nombre  Apellido  Edad Grado  Turno  Genero
0    1     Juan     Rojas  12.0   4to      1       1
1    2    Pedro      None  11.0   5to      0       1
2    3    Maria   Sanchez  13.0   4to      1       0
3    4     Jose   Romero    NaN   5to      0       1
4    5   Manuel     Julca  10.0   5to      1       1
5    6  Fiorela      None  11.0   5to      1       0
6    7    Pedro   Sanchez  12.0   5to      0       1
7    8  Ricardo   Paredes  13.0   5to      1       1
8    9    Carla      None  11.0   5to      1       0
9   10   Ismael      None  12.0   5to      0       1
10  11     Jhon      None  11.0   5to      0       1
11  12      Ana      None  10.0   5to      0       0
12  13  Nicolas  Carrasco   NaN   4to      1       1


LISTA DE COLUMNAS BOOLEANAS:  ['Turno', 'Genero']
```

[Volver a índice](../../docsPrincipal.md ) $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ [Ir al siguiente](HELPER_DATAFRAME_get_cat_columns_many_cats.md)