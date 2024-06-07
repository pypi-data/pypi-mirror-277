Función **DIFF**
==============================
<p1>Esta función retorna los valores excluyentes del cruce de dos listas, esto quiere decir que retorna los valores que no se encuentran en el conjunto de valores comunes de la primera y segunda lista.</p1>

**<h2>Parámetros</h2>**
<p> Esta función cuenta con dos parámetros principales</p>

```Python
helper_dataframe.Diff( li1, li2)
```

<p1><strong>li1</strong> (Requerido): Primera lista para el cruce con la segunda lista.</p1>

<p1><strong>li2</strong> (Requerido): Segunda lista para el cruce con la primera lista.</p1>

**<h2>Retornos</h2>**

<p1><strong>li_diff</strong> : Listado de valores excluyentes del cruce, es decir que no se encuentran en el conjunto de valores comunes.</p1>
<p1> </p1>



**<h2>Ejemplo de uso</h2>**
<p1> A continuación, se muestra un código de ejemplo sobre el uso de la función.</p1>

**<h3>Código :</h3>**
```Python
import pandas as pd
from data_science_helper import helper_dataframe as hd

lista1 = ['Sanchez', 'Julca', 'Juan', 'Alex', 'Jose', 'Manuel']
lista2 = ['Rojas', 'Sanchez', 'Julca', 'Juan', 'Jose', 'Juan', 'Carrasco']

list_diff = hd.Diff(lista1, lista2)

print('Lista 1: ',  lista1)
print('Lista 2: ',  lista2)
print('Result: ',  list_diff )
```


**<h3>Output :</h3>**

```Python
Lista 1:  ['Sanchez', 'Julca', 'Juan', 'Alex', 'Jose', 'Manuel']

Lista 2:  ['Rojas', 'Sanchez', 'Julca', 'Juan', 'Jose', 'Juan', 'Carrasco']

Result:  ['Alex', 'Manuel', 'Rojas', 'Carrasco']
```

[Volver a índice](../../docsPrincipal.md ) $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ [Ir al siguiente](HELPER_DATAFRAME_generate_dataset.md)