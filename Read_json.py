import json
import requests

#with open("Archivos_py/JSON/corredores.json", "r") as file:
  #  datos_decoded = json.load(file)
   # print(datos_decoded)


#LLAMAR A UN JSON DESDE UNA API
def guardar_json_file(datos: list) -> None:

    with open("Archivos_py/JSON/Personajes-marvel.json", "w") as file:
        try:
            json.dump(datos, file, indent=4)
            print("se guardaron los datos!!")
        except Exception as e:
            print("no se guardaron los datos", e)

def get_json_data(url: str) -> json:
    response=  requests.get(url)

    if response.status_code == 200:
        
        datos_json = response.json()
        guardar_json_file(datos_json)
    else:
        print(f"error al traer el JSON {response.status_code}")


get_json_data("tu_api_aqui")