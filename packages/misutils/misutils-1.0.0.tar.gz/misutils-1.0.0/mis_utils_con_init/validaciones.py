import re

def es_email(texto):
  patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
  return re.match(patron, texto) is not None


def solo_numeros(texto):
  return texto.isdigit()


def solo_mayusculas(texto):
  return texto.isupper()


def longitud_dada(texto, longitud):
  return len(texto) == longitud


if __name__ == '__main__':

  texto_email = "ejemplo@dominio.com"
  print(f"'{texto_email}' es un email: {es_email(texto_email)}")

  texto_email = "ejemplodominio.com"
  print(f"'{texto_email}' es un email: {es_email(texto_email)}")

  texto_numeros = "123456"
  print(f"'{texto_numeros}' solo contiene números: {solo_numeros(texto_numeros)}")

  texto_numeros = "123A56"
  print(f"'{texto_numeros}' solo contiene números: {solo_numeros(texto_numeros)}")

  texto_mayusculas = "TEXTOENMAYUSCULAS"
  print(f"'{texto_mayusculas}' solo contiene mayúsculas: {solo_mayusculas(texto_mayusculas)}")

  texto_mayusculas = "TEXToenmayuSCULAS"
  print(f"'{texto_mayusculas}' solo contiene mayúsculas: {solo_mayusculas(texto_mayusculas)}")

  texto_longitud = "Python"
  longitud = 6
  print(f"'{texto_longitud}' tiene una longitud de {longitud}: {longitud_dada(texto_longitud, longitud)}")

  texto_longitud = "Bla bla bla"
  longitud = 6
  print(f"'{texto_longitud}' tiene una longitud de {longitud}: {longitud_dada(texto_longitud, longitud)}")
