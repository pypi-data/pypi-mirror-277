Función **SHOW_NA**
==============================
<p1>Esta función analiza los valores nulos, retornando estadísticos respecto a su cantidad, además de retornar como valor el listado de columnas con al menos un valor nulo.</p1>

**<h2>Parámetros</h2>**
<p> Esta función cuenta con un parámetro principal</p>

```Python
helper_dataframe.show_na( df )
```

<p1><strong>df</strong> (Requerido): Dataframe a analizar, contiene valores nulos en sus columnas.</p1>

**<h2>Retornos</h2>**

<p1><strong>lista_nan_column</strong> : Listado de columnas que contienen al menos un valor nulo.</p1>
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


lista_nan_cols = hd.show_na(df)

print('COLUMNAS CON VALORES NAN: ', lista_nan_cols)
```


**<h3>Output :</h3>**

```Python
Nombre : 1, frac: 1/7 , per: 0.14285714285714285
Apellido : 2, frac: 2/7 , per: 0.2857142857142857
Edad : 2, frac: 2/7 , per: 0.2857142857142857
Turno : 6, frac: 6/7 , per: 0.8571428571428571


COLUMNAS CON VALORES NAN:  ['Nombre', 'Apellido', 'Edad', 'Turno']
```

[Volver a índice](../../docsPrincipal.md ) $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ [Ir al siguiente](HELPER_DATAFRAME_two_d.md)