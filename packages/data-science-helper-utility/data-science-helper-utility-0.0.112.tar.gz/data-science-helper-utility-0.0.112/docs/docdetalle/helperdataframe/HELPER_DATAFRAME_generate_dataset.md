Función **GENERATE_DATASET**
==============================
<p1>Esta función genera un Dataset a base de valores aleatorios, esto se logra configurando los parámetros de entrada, en los que se puede definir el numero de columnas, el número de categorías como target, parámetros de aleatoriedad, etc.</p1>

**<h2>Parámetros</h2>**
<p> Esta función cuenta con cinco parámetros principales</p>

```Python
helper_dataframe.generate_dataset(n_samples=10000, n_features=100, n_classes=2, random_state=42,df=True)
```

<p1><strong>n_samples</strong> : Numero de registros o muestras a generar para el Dataset, por defecto toma el valor de 10000.</p1>

<p1><strong>n_features</strong> : Numero de columnas a generar para el Dataset, por defecto toma el valor de 100.</p1>

<p1><strong>n_classes</strong> : Numero de categorías (target) a generar para el Dataset, por defecto toma el valor de 2.</p1>

<p1><strong>random_state</strong> : Parámetro de aleatoriedad, por defecto toma el valor de 42</p1>

<p1><strong>df</strong> : Flag con el que se puede retornar X como matriz o Dataframe.</p1>

**<h2>Retornos</h2>**

<p1><strong>X</strong> : Dataset generado con los parámetros de configuración de los parámetros N_SAMPLES, N_FEATURES.</p1>

<p1><strong>y</strong> : Target generado en base a la variable N_CLASES.</p1>

<p1> </p1>



**<h2>Ejemplo de uso</h2>**
<p1> A continuación, se muestra un código de ejemplo sobre el uso de la función.</p1>

**<h3>Código :</h3>**
```Python

import pandas as pd
from data_science_helper import helper_dataframe as hd

n_samples = 10000 # Numero de registros o muestras
n_features = 50   # Numero de columnas
n_classes = 3     # Numero de categorias (target)
random_state = 45 # Parametro de aletoriedad
X, y = hd.generate_dataset(n_samples,n_features,n_classes,random_state)

print('Dataframe X: ')
print(X)
 
print('Categorias (Target) y: ')
print(set( y) )
```


**<h3>Output :</h3>**

```Python
Dataframe X: 

            f0        f1        f2  ...       f47       f48       f49
0    -1.746721 -0.414185  4.756175  ... -1.635925  1.506576 -0.993736
1    -0.643824  0.114782  6.068709  ... -4.136979  0.335104  0.065663
2    -2.976752 -1.122490 -0.390859  ... -1.135879  0.845657  0.946421
3     2.721607 -0.700768  0.980411  ... -0.223885  1.243848 -1.030504
4    -0.166226 -0.738451  4.411621  ...  1.689626 -0.402227 -0.313005
       ...       ...       ...  ...       ...       ...       ...
9995 -1.661925 -0.271851  1.171140  ...  0.228019  1.949247 -1.282330
9996  6.187681  0.418983 -2.270754  ... -4.532742 -0.850101  0.356151
9997  0.162233 -0.351216  2.151894  ... -1.774133 -0.548380  0.160462
9998 -4.313908 -0.785536 -0.985411  ... -0.617708  0.793155  1.271230
9999 -0.953687 -0.466571 -1.353690  ... -3.909181 -0.556400  0.355606

[10000 rows x 50 columns]


Categorias (Target) y: 

{0, 1, 2}
```

[Volver a índice](../../docsPrincipal.md ) $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ [Ir al siguiente](HELPER_DATAFRAME_get_bool_columns.md)