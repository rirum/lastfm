import requests
import os
from dotenv import load_dotenv


load_dotenv()

user = os.getenv("USER")
api_key = os.getenv("API_KEY")

url = "https://ws.audioscrobbler.com/2.0/"


params = {
    "method": "user.gettoptracks",
    "user": user,
    "api_key": api_key,
    "format": "json",
    "page": 1  
}


lista_de_musicas = []

while True:
    
    response = requests.get(url, params=params)
    
   
    if response.status_code == 200:
        
        data = response.json()
       
        
        if "toptracks" in data and "track" in data["toptracks"]:
          
            for track in data["toptracks"]["track"]:
               
                lista_de_musicas.append(track["name"])
        print("passou toptrack")
       
        if "toptracks" in data and "@attr" in data["toptracks"] and "page" in data["toptracks"]["@attr"]:
            current_page = int(data["toptracks"]["@attr"]["page"])
            total_pages = int(data["toptracks"]["@attr"]["totalPages"])
            
            if current_page < total_pages:
                params["page"] = current_page + 1  
            else:
                break  
        else:
            break 
    else:
        
        print("Erro ao obter os dados da API:", response.status_code)
        break

caminho_arquivo = "lista_de_musicas.txt"


with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
   
    for musica in lista_de_musicas:
        arquivo.write(f"{musica}\n")

print("Lista de músicas gravada em", caminho_arquivo)