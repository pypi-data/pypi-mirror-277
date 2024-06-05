
traducciones = {
  'es': {
    'hola': 'hola',
    'adios': 'adios'
  },
  'en': {
    'hola': 'hello',
    'adios': 'bye'
  }
}

def traducir(texto, lang='en'):
  if lang in traducciones:
    if texto in traducciones[lang]:
      return traducciones[lang][texto]
    else:
      return 'No tenemos la traducción que buscas :('
  else:
    return 'No tenemos el lenguaje al que buscas traducir :('



if __name__ == '__main__':

  print(traducir('hola'))
  print(traducir('hola', 'es'))
  print(traducir('hola', 'it'))

  print(traducir('mundo'))
  print(traducir('mundo', 'es'))
  print(traducir('mundo', 'it'))