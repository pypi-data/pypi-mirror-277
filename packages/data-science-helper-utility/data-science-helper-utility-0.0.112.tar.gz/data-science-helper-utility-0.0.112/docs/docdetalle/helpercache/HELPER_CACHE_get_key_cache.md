Función **GET_KEY_CACHE**
==============================
<p1>Esta función genera un Key para un listado de parámetros que sirve como parámetro durante el almacenamiento de un Dataframe dentro de la memoria temporal en la carpeta CACHE.</p1>

**<h2>Parámetros</h2>**
<p> Esta función cuenta con un parámetro principal</p>

```Python
helper_cache.get_key_cache( list_values )
```

<p1><strong>list_values</strong> (Requerido): Listado de combinaciones considerados para elaborar el KEY.</p1>

**<h2>Retornos</h2>**

<p1><strong>Key</strong> : Retorna una cadena de texto construida a partir de la lista LIST_VALUES, la cual se considera como un identificador.</p1>
<p1> </p1>



**<h2>Ejemplo de uso</h2>**
<p1> A continuación, se muestra un código de ejemplo sobre el uso de la función.</p1>


**<h3>Código :</h3>**
```Python
from data_science_helper import helper_cache as hc

key = hc.get_key_cache(['Colegio1','SeccionA','5toGrado'])

print('KEY: ', key)
```


**<h3>Output :</h3>**

```Python
KEY:  key_Colegio1_SeccionA_5toGrado
```

[Volver a índice](../../docsPrincipal.md) $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ [Ir al siguiente](HELPER_CACHE_save_cache.md)