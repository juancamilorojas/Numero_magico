import random 

def juego_adivinanza():
  def imprimir_datos(intentos_usuario, lista_intentos, intento):
      impreso_intentos=f'¡Van {intentos_usuario} intentos!'
      impreso_lista_intentos=f'Tus intentos fueron: {lista_intentos}'

      return impreso_intentos, impreso_lista_intentos

  numero_ganador=random.randint(0,100)
  intentos_usuario=0
  validacion= False
  lista_intentos=[]
    
  print('BIENVENIDO A MI PRIMER VIDEO JUEGO')
  print('EL JUEGO DE LAS ADIVINANZAS EMPEZARÁ')
  print('')
  print('Tengo aquí anotado un número entre 0 y 100 ¿Podrás adivinar?')
  print('')
  while not validacion:
    try:
      intento_digitado=input('A ver...Un número del 0 al 100: ')
      intento=int(intento_digitado)
      intentos_usuario += 1
      lista_intentos.append(intento)
      impreso_intentos, impreso_lista_intentos = imprimir_datos(intentos_usuario, lista_intentos, intento)
    except ValueError as e:
      print(f'Debes insertar un número entero. "{intento_digitado}" no cumple este requisito.') 
      continue
  
    if intento == numero_ganador:
      print(f'GANASTE, ¡Necesitaste de {intentos_usuario} intentos!')
      print(impreso_lista_intentos)
      validacion=True
    elif intento > numero_ganador:   
      print(f'Uff, te pasaste: el numero es menor {impreso_intentos}')
      print(impreso_lista_intentos)
    elif intento < numero_ganador:
      print(f'Uff, muy bajito: el numero es mayor {impreso_intentos}')
      print(impreso_lista_intentos)

  juego_adivinanza()