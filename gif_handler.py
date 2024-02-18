import os

def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Le fichier {filename} a été supprimé avec succès.")
    else:
        print(f"Le fichier {filename} n'existe pas.")
