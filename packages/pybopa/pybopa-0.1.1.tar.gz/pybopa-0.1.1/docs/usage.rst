===============
Cómo usarlo
===============

Para utilizar el paquete ``pybopa`` lo primero que debes hacer es importarlo::

    import pybopa

Con esto, ya tienes acceso a todas sus funcionalidades. Puedes acceder a la clase ``Boletin`` y a la clase ``Disposicion``.

Para obtener por ejemplo el boletín de hoy, podemos ejecutar el siguiente código. En la variable sumario se almacena un diccionario. También podemos escribir este en un archivo json.

```
from pybopa import Boletin
b = Boletin()
sumario = b.get_sumario()
b.crear_json()
```