import urllib.request
import imageio

url = input("Please enter the URL of the GIF to download: ")
filename = "downloaded.gif"

with urllib.request.urlopen(url) as response:
    gif = response.read()
    with open(filename, 'wb') as f:
        f.write(gif)

print("Download complete. The GIF was saved as: ", filename)
