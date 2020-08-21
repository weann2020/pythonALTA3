import requests
import wget


def api_pull():
    choice= input("What Pokemon would you like a picture of? ")
    url = "https://pokeapi.co/api/v2/pokemon/" + choice;
    return url

def json_conv(poke_api):
    if poke_api is not None:
        return requests.get(poke_api).json()
    else:
        return None


def api_slice(json2python):

    poke_pic = json2python["sprites"]["front_default"]
   
    return poke_pic


def wget_pic (imagelink):
#    destination = os.path.join(home/student/mycode, f.PNG)
    wget.download(imagelink, out= 'home/student/mycode/')


print(api_slice(json_conv(api_pull())))
wget_pic(api_slice(json_conv(api_pull())))
