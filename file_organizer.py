import argparse
import sys
import os

zips = []
folders = []
executables = []
documents = []
videos = []
pictures = []
songs = []
misc = []

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--f', type=str, help="Directory to be organized.")
    args = parser.parse_args()
    sys.stdout.write(str(orga(args)))

def orga(args):
    fileName = args.f
    files_list = os.listdir(fileName)
    for i in files_list:
        if i[-3:] in ["zip","rar"]:
            zips.append(i)
        elif i[-3:] in ["mp3","wav","ogg"]:
            songs.append(i)
        elif i[-3:] in ["mp4","mkv","mov","vlc"]:
            videos.append(i)
        elif i[-4:] in ["pptx","docx","xlsx"] or i[-3:] in ["pdf","txt","doc","PDF"]:
            documents.append(i)
        elif i[-3:]=="exe":
            executables.append(i)
        elif i[-3:] in ["jpg","bmp","gif","png"] or i[-4:]=="jpeg":
            pictures.append(i)
        elif i[-3:] in ["ini","iso","srt"] or i[-7:]=="torrent" or i[-4:] in ["html","webp"]:
            misc.append(i)
        else:
            folders.append(i)

    if not os.path.exists(fileName + "folders\\"):
        os.makedirs(fileName + "folders\\")
    for i in folders:
        os.rename(fileName + i, fileName + "folders\\" + i)

    if not os.path.exists(fileName + "zips\\"):
        os.makedirs(fileName + "zips\\")
    for i in zips:
        os.rename(fileName + i, fileName + "zips\\" + i)

    if not os.path.exists(fileName + "executables\\"):
        os.makedirs(fileName + "executables\\")
    for i in executables:
        os.rename(fileName + i, fileName + "executables\\" + i)

    if not os.path.exists(fileName + "videos\\"):
        os.makedirs(fileName + "videos\\")
    for i in videos:
        os.rename(fileName + i, fileName + "videos\\" + i)

    if not os.path.exists(fileName + "documents\\"):
        os.makedirs(fileName + "documents\\")
    for i in documents:
        os.rename(fileName + i, fileName + "documents\\" + i)

    if not os.path.exists(fileName + "pictures\\"):
        os.makedirs(fileName + "pictures\\")
    for i in pictures:
        os.rename(fileName + i, fileName + "pictures\\" + i)

    if not os.path.exists(fileName + "songs\\"):
        os.makedirs(fileName + "songs\\")
    for i in songs:
        os.rename(fileName + i, fileName + "songs\\" + i)

    if not os.path.exists(fileName + "misc\\"):
        os.makedirs(fileName + "misc\\")
    for i in misc:
        os.rename(fileName + i, fileName + "misc\\" + i)

if __name__ == '__main__':
    main()
