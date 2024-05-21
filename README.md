# Numero_magico
Se desarrolló un juego de adivinanza donde el usuario intenta adivinar un número imaginado por la computadora. El programa proporciona pistas sobre si el número ingresado por el usuario es mayor o menor que el número ganador.

# Conceptos aplicados:
- Manejo de variables.
- Manejo de distintos tipos de datos (strings, ints, booleanos).
- Transformación de datos.
- Operadores lógicos y de comparación.
- Condicionales.
- Listas y el método append().
- Bucles (while).
  
#Pasos a seguir:
1. Importar el módulo random: Este módulo es esencial ya que nos permite generar el número ganador de forma aleatoria.
2. Configurar el número ganador: Utilizamos la función random.randint(numero_minimo, numero_maximo) para generar un número aleatorio dentro de un rango especificado, en este caso, entre 0 y 100.
3. Declarar las variables: Creamos variables para almacenar la información del juego, como los intentos del usuario (lista), la cantidad de intentos (entero) y si el usuario ya ha adivinado o no (booleano).
4. Solicitar el número al usuario: Utilizamos un bucle while para solicitar al usuario que ingrese un número entre 0 y 100. El número ingresado se convierte a tipo int para facilitar su comparación posteriormente. También se 5. registra el intento del usuario y se agrega el número a la lista de intentos. Es importante destacar que este proceso depende de si el string ingresado por el usuario puede convertirse a un número entero. En caso contrario, un bloque try-except permitirá al usuario ingresar un nuevo valor hasta que lo haga correctamente.
6. Condicionales: Dentro del bucle while, se utilizan condicionales para comparar el número ingresado por el usuario con el número ganador. Si el número es mayor o menor, se proporciona una pista al usuario. Si el usuario adivina el número ganador, se muestra un mensaje de felicitación, se cambia la variable de validación y el bucle while termina, finalizando el juego.
