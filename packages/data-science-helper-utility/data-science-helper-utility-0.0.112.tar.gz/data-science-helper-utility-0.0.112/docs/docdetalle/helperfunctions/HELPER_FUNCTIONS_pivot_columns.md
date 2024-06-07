Función **PIVOT_COLUMNS**
==============================
<p1>Esta función toma los dos niveles del nombre de la columna para concatenarlas y establecer una única columna, combinando los valores en ambos niveles.</p1>

**<h2>Parámetros</h2>**
<p> Esta función cuenta con dos parámetros principales</p>

```Python
helper_functions.pivot_columns( df_prod_bco_pivot )
```

<p1><strong>df_prod_bco_pivot</strong> (Requerido): Dataframe que contiene columnas con dos niveles.</p1>

**<h2>Retornos</h2>**

<p1><strong>None</strong> : No retorna ningún valor.</p1>
<p1> </p1>



**<h2>Ejemplo de uso</h2>**
<p1> A continuación, se muestra un código de ejemplo sobre el uso de la función.</p1>

**<h3>Código :</h3>**
```Python
import pandas as pd
from data_science_helper import helper_functions as hf

# Dataset Estudiantes
cols = pd.MultiIndex.from_tuples([("4to", "Matematica"), 
                                  ("4to", "Lenguaje"), 
                                  ("5to", "Matematica"),
                                  ("5to", "Lenguaje")])

data=[[11, 12,  5, 12],
      [20, 15, 13, 16],
      [12, 18, 11, 19],
      [13, 10,  6, 11],
      [14, 15, 12,  9],
      [12, 19,  8,  1]]

df = pd.DataFrame(data, columns=cols)

print(df.head(10))

hf.pivot_columns(df)

print(df.head(10))
```


**<h3>Output :</h3>**

```Python
         4to                 5to         
  Matematica Lenguaje Matematica Lenguaje
0         11       12          5       12
1         20       15         13       16
2         12       18         11       19
3         13       10          6       11
4         14       15         12        9
5         12       19          8        1

   index  4to_Matematica  4to_Lenguaje  5to_Matematica  5to_Lenguaje
0      0              11            12               5            12
1      1              20            15              13            16
2      2              12            18              11            19
3      3              13            10               6            11
4      4              14            15              12             9
5      5              12            19               8             1
```

[Volver a índice](../../docsPrincipal.md ) $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ [Ir al siguiente](HELPER_FUNCTIONS_plot_boundaries_iris_dataset.md)