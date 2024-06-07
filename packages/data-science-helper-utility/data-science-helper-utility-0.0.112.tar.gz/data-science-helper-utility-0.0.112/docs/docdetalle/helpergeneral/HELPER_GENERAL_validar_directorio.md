Función **validar_directorio**
==============================
<p1>Permite obtener la ruta raiz de un proyecto de ciencia de datos que emplea la plantilla  [data-science-project-template](https://github.com/ecandela/data-science-project-template).</p1>


```Python
helper_general.validar_directorio()
```


**<h2>Retornos</h2>**

<p1><strong>Boolean</strong> : Devuelve [True] si existe la carpeta. Si no existe la carpeta, devolvera [False] y creara la ruta ingresada </p1>
<p1> </p1>


**<h2>Ejemplo de uso</h2>**
<p1> A continuación, se muestra un código de ejemplo sobre el uso de la función.</p1>

**<h3>Código :</h3>**
```Python

import data_science_helper.helper_general as hg

path = "C:\\Users\\admin\\Temp" #No existe

if hg.validar_directorio(path):

    print("Directorio creado")


**<h3>Output :</h3>**

Directorio creado

```Python

```
[Volver a índice](../../docsPrincipal.md ) $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ [Ir al siguiente](HELPER_FUNCTIONS_encoder_cat.md)



