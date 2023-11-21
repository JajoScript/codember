"""
** El reto **

Un espía está enviando mensajes encriptados.

Tu misión es crear un programa que nos ayude a buscar patrones...

Los mensajes son palabras separadas por espacios como este:
gato perro perro coche Gato peRRo sol

Necesitamos que el programa nos devuelva el número de veces que aparece cada palabra en el mensaje, independientemente de si está en mayúsculas o minúsculas.

El resultado será una cadena de texto con la palabra y el número de veces que aparece en el mensaje, con este formato:
gato2perro3coche1sol1

¡Las palabras son ordenadas por su primera aparición en el mensaje!
** Más ejemplos: **

llaveS casa CASA casa llaves -> llaves2casa3
taza ta za taza -> taza2ta1za1
casas casa casasas -> casas1casa1casasas1
"""
import os;

#* -- Lectura de archivos.
def read_file(file_name: str) -> str:
  file_path = f"{os.getcwd()}/challenges/CHALLENGE_01/{file_name}"

  File = open(file_path, "rt");
  data:str = File.read().strip();
  File.close();

  return data;

#* -- Solución
def solve_challenge(data:str) -> None:
  result = [];
  animals_viewed = []
  animals = data.lower().split(" ")

  for animal in animals:
    if (not(animal in animals_viewed)):
      animals_viewed.append(animal);
      result.append(animal + str(animals.count(animal)));

  return "".join(result);

def challenge_01():
  data:str = read_file("CHALLENGE_01.txt");

  # Challenge 01.
  resultado:str = solve_challenge(data);
  print("[🐎:Resultado] Mensaje desencriptado:", resultado);
