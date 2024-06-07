Función **TWO_D**
==============================
<p1>Esta función convierte una lista o un vector de una dimensión a una matriz de dos dimensiones, considerando la lista como columna en el resultado.</p1>

**<h2>Parámetros</h2>**
<p> Esta función cuenta con un parámetro principal</p>

```Python
helper_dataframe.two_d( array )
```

<p1><strong>array</strong> (Requerido): Lista o vector que se desea convertir a un vector de dos dimensiones.</p1>

**<h2>Retornos</h2>**

<p1><strong>np_array</strong> : Vector en dos dimensiones.</p1>
<p1> </p1>



**<h2>Ejemplo de uso</h2>**
<p1> A continuación, se muestra un código de ejemplo sobre el uso de la función.</p1>

**<h3>Código :</h3>**
```Python
import pandas as pd
from data_science_helper import helper_dataframe as hd

edad = [13,12,13,14,12,11,13]

print('Dimension Inicial: ', len(edad) )
print( edad)

edad_two_d = hd.two_d(edad)

print('Dimension Final: ', edad_two_d.shape )
print( edad_two_d)
```


**<h3>Output :</h3>**

```Python
Dimension Inicial:  7

[13, 12, 13, 14, 12, 11, 13]


Dimension Final:  (7, 1)

[[13]
 [12]
 [13]
 [14]
 [12]
 [11]
 [13]]
```

[Volver a índice](../../docsPrincipal.md ) $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ [Ir al siguiente](../helperfunctions/HELPER_FUNCTIONS_clean_df.md)