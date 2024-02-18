import urllib.request
import imageio

url = input("Veuillez saisir l'URL du GIF à télécharger : ")
filename = "downloaded.gif"

with urllib.request.urlopen(url) as response:
    gif = response.read()
    with open(filename, 'wb') as f:
        f.write(gif)

print("Téléchargement terminé. Le GIF a été enregistré sous le nom : ", filename)
