Función **PRINT_MESSAGE_GREEN**
==============================
<p1>Imprime texto en color azul por defeco, utiliza la clase PRETTY_OUTPUT internamente para dicho objetivo.</p1>

**<h2>Parámetros</h2>**
<p> Esta función cuenta con un parámetro principal</p>

```Python
helper_output.print_message_green(text)
```

<p1><strong>text</strong> (Requerido): Texto que se requiere imprimir.</p1>

**<h2>Retornos</h2>**

<p1><strong>None</strong> : No retorna ningún valor.</p1>
<p1> </p1>



**<h2>Ejemplo de uso</h2>**
<p1> A continuación, se muestra un código de ejemplo sobre el uso de la función.</p1>

**<h3>Código :</h3>**
```Python
import pandas as pd
from data_science_helper import helper_output as ho


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

ho.print_underscore('Texto de Prueba')

for value in df.Nombre:
    ho.print_underscore(value)
```


**<h3>Output :</h3>**

<pre style="color: #0000FF; font-family: consolas; text-decoration: underline;">

Texto de Prueba
Juan
Pedro
Maria
Jose
Manuel
Fiorela
Pedro
Ricardo
Carla
Ismael
Jhon
Ana
Nicolas

</pre>

[Volver a índice](../../docsPrincipal.md ) $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ 