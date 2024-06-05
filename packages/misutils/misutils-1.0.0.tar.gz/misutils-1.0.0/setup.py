from setuptools import setup, find_packages

# Para crear la distribución, la carpeta dist con el zip, lanzamos el comando:
# sdist -> source distribution
# $ python setup.py sdist

setup(
  name='misutils',
  version='1.0.0',
  description='Paquete con utilidades básicas de operaciones, validaciones y traducciones',
  author='Charly Falco',
  author_email='c_falco@gmail.com',
  packages=find_packages()
)

# El find_packages, se supone que estaría encntrando nuestros paquetes, en este caso el "mis_utils_con_init"
print(f'l: {find_packages()}')