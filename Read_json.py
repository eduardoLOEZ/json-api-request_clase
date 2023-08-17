import json
import requests

#with open("Archivos_py/JSON/corredores.json", "r") as file:
  #  datos_decoded = json.load(file)
   # print(datos_decoded)


#LLAMAR A UN JSON DESDE UNA API
def guardar_json_file(datos: list, file_path: str) -> None:
    """Guarda los datos en un file_path JSON."""
    try:
        with open(file_path, "w") as file:
            json.dump(datos, file, indent=4)
        print("Se guardaron los datos correctamente.")
    except Exception as e:
        print("Error al guardar los datos:", e)



def get_json_data(url: str, file_path: str) -> None:
    """Obtiene datos JSON de una URL y los guarda en un file_path."""
    response=  requests.get(url)

    if response.status_code == 200:
        
        datos_json = response.json()
        guardar_json_file(datos_json, file_path)
        #print(guardar_json_file)
    else:
        print(f"error al traer el JSON {response.status_code}")

def main():
    api= "tu_api_aqui"
    json_path= "Archivos_py/JSON/Personajes-marvel.json"

    get_json_data(api, json_path)

if __name__ == "__main__":
    main()

