# AQUÍ INDICAMOS QUE SE VA A EXPORTAR CON EL mis_utils_con_init

from .operaciones import multiplica, resta
from .traducciones import *
# from .validaciones import *

# Al no estar importando .validaciones y suma y divide, entonces estos métodos tendremos que usarlos proporcionando toda la ruta
# mis_utils_con_init.validaciones.es_email('email')
# mis_utils_con_init.operaciones.suma(1, 1)