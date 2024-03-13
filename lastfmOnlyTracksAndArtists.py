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


music_list = []

while True:
    
    response = requests.get(url, params=params)
    
   
    if response.status_code == 200:
        
        data = response.json()
       
        
        if "toptracks" in data and "track" in data["toptracks"]:
          
            for track in data["toptracks"]["track"]:
               
                music_name = track["name"]
                artist_name = track["artist"]["name"]
                
                

                music_list.append(f'{music_name} - {artist_name}')
      
       
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
        
        print("Error obtaining API data:", response.status_code)
        break

file_path = "lastfm_toptracksArtists.txt"


with open(file_path, "w", encoding="utf-8") as file:
   
    for music in music_list:
        file.write(f"{music}\n")

print("File saved in:", file_path)