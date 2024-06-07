Función **PRINT_ITEMS**
==============================
<p1>Esta función imprime los valores de una lista de datos excluyendo la lista declarada en el parámetro EXCEPTO agregando un prefijo al momento de imprimir.</p1>

**<h2>Parámetros</h2>**
<p> Esta función cuenta con tres parámetros principales</p>

```Python
helper_output.print_items( list_, prefix="NEW", excepto = ["ID_PERSONA"] )
```

<p1><strong>list_</strong> (Requerido): Listado de parámetros a imprimir.</p1>

<p1><strong>prefix</strong> : Prefijo que se adiciona al imprimir el listado, por defecto toma el valor de "NEW".</p1>

<p1><strong>excepto</strong> : Listado de valores a excluir, por defecto toma el valor de ["ID_PERSONA"].</p1>

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


ho.print_items(df.Nombre, prefix="Estudents:", excepto=["Manuel", "Fiorela", "Ricardo"])
```


**<h3>Output :</h3>**

```Python
Estudents: : Juan
Estudents: : Pedro
Estudents: : Maria
Estudents: : Jose
Estudents: : Pedro
Estudents: : Carla
Estudents: : Ismael
Estudents: : Jhon
Estudents: : Ana
Estudents: : Nicolas
```

[Volver a índice](../../docsPrincipal.md ) $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ [Ir al siguiente](HELPER_OUTPUT_print_message_green.md)