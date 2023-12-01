"""
** El problema final **

Finalmente los hackers han conseguido acceder a la base de datos y la han dejado corrupta. Pero parece que han dejado un mensaje oculto en la base de datos. ¿Podrás encontrarlo?

Nuestra base de datos está en formato .csv. Las columnas son id, username, email, age, location.

Un usuario sólo es válido si:

    - id: existe y es alfanumérica
    - username: existe y es alfanumérico
    - email: existe y es válido (sigue el patrón user@dominio.com)
    - age: es opcional pero si aparece es un número
    - location: es opcional pero si aparece es una cadena de texto

Ejemplos:

    Entrada: 1a421fa,alex,alex9@gmail.com,18,Barcelona
    Resultado: ✅ Válido

    Entrada: 9412p_m,maria,mb@hotmail.com,22,CDMX
    Resultado: ❌ Inválido (id no es alfanumérica, sobra el _)

    Entrada: 494ee0,madeval,mdv@twitch.tv,,
    Resultado: ✅ Válido (age y location son opcionales)
    Entrada: 494ee0,madeval,twitch.tv,22,Montevideo
    Resultado: ❌ Inválido (email no es válido)

** Cómo resolverlo **

1. Analiza la lista de entradas de la baes de datos y detecta los inválidos: https://codember.dev/data/database_attacked.txt

2. Encuentra el primer caracter (número o letra) del username de cada usuario inválido. Júntalos por orden de aparición y descubre el mensaje oculto. Luego envíalo con submit. Por ejemplo:
submit att4ck
"""
import os

#* -- Lectura de archivos.
def read_file(file_name: str) -> str:
  file_path = f"{os.getcwd()}/challenges/CHALLENGE_05/{file_name}"

  File = open(file_path, "rt");

  data = []
  for lineas in File.readlines():
    data.append(lineas.strip())

  File.close();

  return data;

def identify_user(data: list[str]):
  valid_users = []
  invalid_users = []

  for row in data:
    user = row.split(",")
    id = user[0]
    username = user[1]
    email = user[2]

    valid_id: bool = id.isalnum()
    valid_username: bool = username.isalnum()
    valid_email: bool = email.count("@") == 1 and email.count(".") == 1

    if (valid_id and valid_username and valid_email):
      valid_users.append(row)
    else:
      invalid_users.append(row)

  return [valid_users, invalid_users];

#* -- Ejecución.
def challenge_05():
  # Lectura del archivo.
  data:str = read_file("CHALLENGE_05.txt");

  [valid_users, invalid_users] = identify_user(data);

  password = ""
  for user in invalid_users:
    username = user.split(",")[1]
    password += username[0]

  print("[🐎:Resultado] Secret message: ", password);
