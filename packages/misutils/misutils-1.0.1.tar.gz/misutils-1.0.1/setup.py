from setuptools import setup, find_packages


# 1. Vamos a crear el archivo pyproject.toml en la raíz del proyecto
# Ahí vamos a añadir la información de que herramientas se van a usar para construir el proyecto
# ----
# [build-system]
# requires = ["setuptools", "wheel"]
# build-backend = "setuptools.build_meta"
# ----

# 2. Instalar las dependencias de setuptools y wheel en caso de no tenerlas
# $ pip install setuptools wheel

# 3. Configuramos este archivo de setup.py como vemos a continuación

setup(
  name='misutils',
  version='1.0.1',
  description='Paquete con utilidades básicas de operaciones, validaciones y traducciones',
  long_description='## Paquete con utilidades básicas de operaciones, validaciones y traducciones',
  long_description_content_type='text/markdown',
  author='Charly Falco',
  author_email='c_falco@gmail.com',
  packages=find_packages()
)


# Para construir la distribución, la carpeta dist con el zip, lanzamos el comando:
# sdist -> source distribution
# $ python -m build

# El find_packages, se supone que estaría encntrando nuestros paquetes, en este caso el "mis_utils_con_init"
# print(f'l: {find_packages()}')

# Para distribuir luego el paquete desde pypi, hay que seguir estos pasos:
# $ pip install twine
# $ twine upload dist/*

# Para que ese comando funcione, tenemos que hacer otros pasos previos:

# Crear un archivo .pypirc en la raíz (donde estan los .bashrc y demas)
# ------
# [distutils]
# index-servers =
#         pypi

# [pypi]
# username = __token__
# password = pypi-bkdjasdbjkasbdjkbasjkbdajkbsdasjbdajkbskdjbakjs
# ------
#
# El valor de password del archivo es un token que tienes que generar.
#
# Crea una cuenta en https://pypi.org/
# En Configuración de la cuenta buscas Fichas de API, creas una y obtienes el token que pegas en password

# Una vez que tenemos esto, ahora si debería de funcionar el comando:
# $ twine upload dist/*