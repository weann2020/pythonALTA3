import requests
import wget


def api_pull():
    choice= input("What Pokemon would you like a picture of? ")
    url = "https://pokeapi.co/api/v2/pokemon/" + choice;
    return url

def json_conv(poke_api):
    try:
       obj= requests.get(poke_api).json()
       return obj
    except:
       print("Error") 


def api_slice(json2python):

    poke_pic = json2python["sprites"]["front_default"]
   
    return poke_pic


def wget_pic (imagelink):
#    destination = os.path.join(home/student/mycode, f.PNG)
    
    pokemon = wget.download(imagelink, out ='/home/student/mycode/')


#print(api_slice(json_conv(api_pull())))
wget_pic(api_slice(json_conv(api_pull())))
#wget_pic("https://media0.giphy.com/media/KpLPyE3D6HJPa/giphy.gif?cid=96d546206drs9lc9e6vxt7mv5x9m4q4y3rtmtou74ch3qq04&rid=giphy.gif")
#wget_pic("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/132.png")
