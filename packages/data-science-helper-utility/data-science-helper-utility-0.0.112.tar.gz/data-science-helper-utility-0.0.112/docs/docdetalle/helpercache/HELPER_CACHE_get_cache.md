Función **GET_CACHE**
==============================
<p1>Obtiene un Dataframe identificado con el KEY solicitado, el parámetro KEY es un identificador del Dataframe almacenado en CACHE.</p1>

**<h2>Parámetros</h2>**
<p> Esta función cuenta con dos parámetros principales</p>

```Python
helper_cache.get_cache(filename , key)
```

<p1><strong>filename</strong> (Requerido): Nombre del archivo sobre el cual se guardó la información en CACHE.</p1>

<p1><strong>key</strong> (Requerido): Identificador con la cual se guardó la información en CACHE, esta es una cadena de texto.</p1>

**<h2>Retornos</h2>**

<p1><strong>df_</strong> : Retorna el DATAFRAME al cual hace referencia el identificador KEY en el archivo FILENAME.</p1>
<p1> </p1>



**<h2>Ejemplo de uso</h2>**
<p1> A continuación, se muestra un código de ejemplo sobre el uso de la función.</p1>


**<h3>Código :</h3>**
```Python
import pandas as pd
from data_science_helper import helper_cache as hc

key = hc.get_key_cache(['Colegio1','SeccionA','5toGrado'])
print('KEY: ', key)

filename = 'estudiantes'

df_cache = hc.get_cache(filename,key)
print( df_cache.head() )

```


**<h3>Output :</h3>**

```Python
KEY:  key_Colegio1_SeccionA_5toGrado

   ID Nombre
0   1   Juan
1   2  Pedro
2   3   Alex
```

[Volver a índice](../../docsPrincipal.md ) $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ [Ir al siguiente](HELPER_CACHE_get_key_cache.md)