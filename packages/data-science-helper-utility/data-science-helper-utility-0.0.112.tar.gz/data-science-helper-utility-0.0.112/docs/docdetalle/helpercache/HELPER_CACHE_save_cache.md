Función **SAVE_CACHE**
==============================
<p1>Guarda un DATAFRAME en memoria CACHE en el archivo de nombre FILENAME, requiere como entrada el KEY_CACHE para su posterior identificación.</p1>

**<h2>Parámetros</h2>**
<p> Esta función cuenta con tres parámetros principales</p>

```Python
helper_cache.save_cache(df, filename, key)
```

<p1><strong>df</strong> (Requerido): Dataframe que se requiere guardar en el archivo FILENAME.</p1>

<p1><strong>filename</strong> (Requerido):  Nombre del archivo sobre el cual se guardará la información en CACHE.</p1>

<p1><strong>key</strong> (Requerido): Identificador con la cual se guardará la información en CACHE, esta es una cadena de texto.</p1>

**<h2>Retornos</h2>**

<p1><strong>None</strong> :  No retorna ningún valor.</p1>
<p1> </p1>



**<h2>Ejemplo de uso</h2>**
<p1> A continuación, se muestra un código de ejemplo sobre el uso de la función.</p1>


**<h3>Código :</h3>**
```Python
import pandas as pd
from data_science_helper import helper_cache as hc

# Data Estudiantes
df = pd.DataFrame(data = [[1, 'Juan' ],
                          [2, 'Pedro'],
                          [3, 'Alex' ]], 
                  columns = ['ID', 'Nombre'])

key = hc.get_key_cache(['Colegio1','SeccionA','5toGrado'])

print('KEY: ', key)

filename = 'estudiantes'

hc.save_cache(df, filename, key)
```


**<h3>Output :</h3>**

```Python
KEY:  key_Colegio1_SeccionA_5toGrado
```

[Volver a índice](../../docsPrincipal.md ) $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ [Ir al siguiente](../helperclean/HELPER_CLEAN_agregar_na_cls.md)
