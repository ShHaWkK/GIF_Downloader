import gif_handler
from urllib.request import urlopen
from tqdm import tqdm
import validators

def download_gif(url, filename):
    if validators.url(url):
        response = urlopen(url)
        with open(filename, 'wb') as f:
            pbar = tqdm(unit="B", unit_scale=True, unit_divisor=1024)
            while True:
                buffer = response.read(8192)
                if not buffer:
                    break
                f.write(buffer)
                pbar.update(len(buffer))
            pbar.close()
        print("Téléchargement terminé. Le GIF a été enregistré sous le nom : ", filename)
    else:
        print("L'URL n'est pas valide.")

if __name__ == "__main__":
    url = input("Veuillez saisir l'URL du GIF à télécharger : ")
    filename = "downloads/downloaded.gif"
    download_gif(url, filename)
