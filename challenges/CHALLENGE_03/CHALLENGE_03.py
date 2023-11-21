"""
** El Desafío del Cifrado Espía **

Un grupo de espías ha descubierto que su sistema de cifrado de mensajes está comprometido.

Han encontrado algunas contraseñas que no cumplen con laPolítica de Seguridad de Cifrado que tenían establecida cuando fueron creadas.

Para solucionar el problema, han creado una lista (tu entrada al desafío) de contraseñas (según la base de datos corrupta) y la política de seguridad cuando esa clave fue establecida.

Ejemplo de la lista:

    2-4 f: fgff
    4-6 z: zzzsg
    1-6 h: hhhhhh

Cada línea indica, separado por :, la política de la clave y la clave misma.

La política de la clave especifica el número mínimo y máximo de veces que un carácter dado debe aparecer para que la clave sea válida. Por ejemplo, 2-4 f significa que la clave debe contener f al menos 2 veces y como máximo 4 veces.

Sabiendo esto, en el ejemplo anterior, hay 2 claves válidas:

La segunda clave, zzzsg, no lo es; contiene 3 veces la letra z, pero necesita al menos 4. Las primeras y terceras claves son válidas: contienen la cantidad adecuada de f y h, respectivamente, según sus políticas.
** Tu desafío: **

Determina cuántas claves de cifrado son válidas según sus políticas.
** Cómo resolverlo **

1. Analiza la lista de políticas y claves de cifrado que encontrarás en este archivo: https://codember.dev/data/encryption_policies.txt

2. Crea un programa que devuelva la clave inválida número 42 (de todas las claves inválidas, la 42ª en orden de aparición). Por ejemplo:
submit bqamidgewtbuz
"""
import os

#* -- Lectura de archivos.
def read_file(file_name: str) -> str:
  file_path = f"{os.getcwd()}/challenges/CHALLENGE_03/{file_name}"

  File = open(file_path, "rt");
  data:str = File.read().strip();
  File.close();

  return data;

def comprobador_politicas(data:str):
  passAndPolicy = data.split("\n");

  invalidPasswords:str = [];
  # Ciclo para recorrer las políticas y contraseñas.
  for passpolicy in passAndPolicy:
    [policy, password] = passpolicy.split(":"); # [2-4 f, fgff]
    [policy, letter] = policy.split(" "); # [2-4, f]
    [min, max] = policy.split("-"); # [2, 4]

    # Identificando las contraseñas invalidas.
    if (password.count(letter) < int(min) or password.count(letter) > int(max)):
      invalidPasswords.append(password);

  return invalidPasswords[41];

#* -- Ejecución.
def challenge_03():
  # Lectura del archivo.
  data:str = read_file("CHALLENGE_03.txt");

  # Comprobación de políticas.
  resultado:str = comprobador_politicas(data);
  print("[🐎:Resultado] contraseña invalida n° 42: ", resultado);

