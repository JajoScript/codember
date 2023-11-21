"""
** Mini Compiler Challenge **

En el mundo del espionaje, se utiliza un lenguaje de codificación con símbolos que realizan operaciones matemáticas simples.

Tu tarea es crear un mini compilador que interprete y ejecute programas escritos en este lenguaje de símbolos.

Las operaciones del lenguaje son las siguientes:

    "#" Incrementa el valor numérico en 1.
    "@" Decrementa el valor numérico en 1.
    "*" Multiplica el valor numérico por sí mismo.
    "&" Imprime el valor numérico actual.

El valor numérico inicial es 0 y las operaciones deben aplicarse en elorden en que aparecen en la cadena de símbolos.
** Ejemplos de entrada: **

Entrada: "##*&"
Salida esperada: "4"
Explicación: Incrementa (1), incrementa (2), multiplica (4), imprime (4).

Entrada: "&##&*&@&"
Salida esperada: "0243"
Explicación: Imprime (0), incrementa (1), incrementa (2), imprime (2), multiplica (4), imprime (4), decrementa (3), imprime (3).
** Tu desafío: **

Desarrolla un mini compilador que tome una cadena de texto y devuelva otra cadena de texto con el resultado de ejecutar el programa.
** Cómo resolverlo **

1. Resuelve el mensaje que encontrarás en este archivo: https://codember.dev/data/message_02.txt

2. Crea un programa al que le pases como entrada el mensaje anterior. Envía la salida con el comando "submit" en la terminal, por ejemplo así:
submit 024899488
"""
import os;

#* -- Lectura de archivos.
def read_file(file_name: str) -> str:
  file_path = f"{os.getcwd()}/challenges/CHALLENGE_02/{file_name}"
  File = open(file_path, "rt");
  data:str = File.read().strip();
  File.close();

  return data;

def lector_caracteres(data:str) -> str:
  resultado = ""
  valor_actual = 0

  for caracter in data:
    # Identificar el tipo de operacion.
    if (caracter == "#"):
      valor_actual += 1
    elif (caracter == "@"):
      valor_actual -= 1
    elif (caracter == "*"):
      valor_actual *= valor_actual
    elif (caracter == "&"):
      resultado += str(valor_actual)
    else:
      print("[😡] No se reconoce el operador...")

  return resultado;

def challenge_02():
    # Lectura del archivo.
  data:str = read_file("CHALLENGE_02.txt");

  # Comprobación de políticas.
  resultado:str = lector_caracteres(data);
  print("[🐎:Resultado] Resultado del compilador:", resultado);
