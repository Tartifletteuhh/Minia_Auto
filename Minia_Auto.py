from PIL import Image
import os

if not os.path.exists('sources'):
    os.makedirs('sources')

if not os.path.exists('output'):
    os.makedirs('output')

directory = r'.\sources'

q1 = input("redimensionner tout le dossier 'sources' ? y, n : ")
q2 = input("ajouter 'online' à toutes les images ? y, n : ")

if q1 == "y" and q2 == "n":

    for filename in os.listdir(directory):

        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".webp"):

            #source = input("nom du fichier (avec son extension) : ")
            background = Image.open("./sources/{}".format(filename))
            background_copy = background.copy()
            foreground = Image.open("online.png")
            foreground_copy = foreground.copy()

            background_copy = background_copy.resize((1024, 575))

            background_copy = background_copy.convert('RGB')

            filename = os.path.splitext(filename)[0]

            filename = filename.replace(" ", "-")

            filename = filename.replace("é", "e")
            filename = filename.replace("è", "e")
            filename = filename.replace("ê", "e")
            filename = filename.replace("ë", "e")

            filename = filename.replace("à", "a")
            filename = filename.replace("â", "a")

            filename = filename.replace("ù", "u")
            filename = filename.replace("ü", "u")
            filename = filename.replace("û", "u")
            filename = filename.replace("ũ", "u")
            filename = filename.replace("ú", "u")
            filename = filename.replace("ū", "u")

            filename = filename.replace("ç", "c")

            filename = filename.replace("ÿ", "y")

            filename = filename.replace("ô", "o")
            filename = filename.replace("ö", "o")
            filename = filename.replace("ó", "o")
            filename = filename.replace("ò", "o")
            filename = filename.replace("ō", "o")
            filename = filename.replace("õ", "o")

            background_copy.save(
                "./output/{}_ShibaGamesCrack.webp".format(filename), 'webp')


if q1 == "y" and q2 == "y":

    for filename in os.listdir(directory):

        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".webp"):

            #source = input("nom du fichier (avec son extension) : ")
            background = Image.open("./sources/{}".format(filename))
            background_copy = background.copy()
            foreground = Image.open("online.png")
            foreground_copy = foreground.copy()

            background_copy = background_copy.resize((1024, 575))

            foreground_copy.thumbnail((int(background_copy.width)/2, 10000))

            background_copy.paste(foreground_copy,
                                  (0, (int(background_copy.height) -
                                       int(foreground_copy.height))),
                                  foreground_copy
                                  )

            background_copy = background_copy.convert('RGB')

            filename = os.path.splitext(filename)[0]

            filename = filename.replace(" ", "-")

            filename = filename.replace("é", "e")
            filename = filename.replace("è", "e")
            filename = filename.replace("ê", "e")
            filename = filename.replace("ë", "e")

            filename = filename.replace("à", "a")
            filename = filename.replace("â", "a")

            filename = filename.replace("ù", "u")
            filename = filename.replace("ü", "u")
            filename = filename.replace("û", "u")
            filename = filename.replace("ũ", "u")
            filename = filename.replace("ú", "u")
            filename = filename.replace("ū", "u")

            filename = filename.replace("ç", "c")

            filename = filename.replace("ÿ", "y")

            filename = filename.replace("ô", "o")
            filename = filename.replace("ö", "o")
            filename = filename.replace("ó", "o")
            filename = filename.replace("ò", "o")
            filename = filename.replace("ō", "o")
            filename = filename.replace("õ", "o")

            background_copy.save(
                "./output/{}_ShibaGamesCrack.webp".format(filename), 'webp')
