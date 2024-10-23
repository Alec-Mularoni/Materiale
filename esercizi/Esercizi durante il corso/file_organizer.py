import shutil
import os

# Definizione delle estensioni dei file
IMG_EXTENSIONS = ["jpeg", "jfif", "tiff", "png", "ppm", "pgm", "pbm", "pnm", "heif", "webp", "exif", "img", "jpg", "ico"]
AUDIO_EXTENSIONS = ["3gp", "aa", "aac", "mp3", "m4p", "org", "raw", "ogg", "flac"]
VIDEO_EXTENSIONS = ["webm", "mkv", "flv", "vob", "ogv", "ogg", "drc", "gif", "mng", "avi", "mts", "ts", "m2ts", "mov", "wmv", "yuv", "rm", "rmvb", "viv", "mp4", "m4v"]
DOCS_EXTENSIONS = ["txt", "doc", "docx", "html", "htm", "xls", "xlsx", "ods", "ppt", "pptx", "pdf", "docm", "csv", "bmp"]
INSTALLER_EXTENSIONS = ["msi", "exe", "com", "bat", "vb", "vbs", "wsf", "pif", "app", "scpt", "applescript"]

# Definizione delle cartelle in cui saranno suddivisi i file
FOLDERS = {
    "IMAGE": IMG_EXTENSIONS,
    "AUDIO": AUDIO_EXTENSIONS,
    "VIDEO": VIDEO_EXTENSIONS,
    "DOCS": DOCS_EXTENSIONS,
    "INSTALLER": INSTALLER_EXTENSIONS
}

# Funzione per creare le cartelle se non esistono
def folder_creation(path):
    for folder in FOLDERS.keys():
        folder_path = os.path.join(path, folder)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
            print(f"Cartella '{folder}' creata in {folder_path}")
        else:
            print(f"Cartella '{folder}' già esistente in {folder_path}")

# Funzione per organizzare i file in base alla loro estensione
def file_organizer(path):
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        # Ignora se è una cartella
        if os.path.isdir(file_path):
            continue

        extension = filename.split(".")[-1].lower()  # Estensione in minuscolo per essere sicuri
        moved = False

        # Verifica a quale categoria appartiene l'estensione del file
        for folder, extensions in FOLDERS.items():
            if extension in extensions:
                dest_path = os.path.join(path, folder, filename)
                shutil.move(file_path, dest_path)
                print(f"File '{filename}' spostato in '{folder}' con successo!")
                moved = True
                break
        
        if not moved:
            print(f"Estensione sconosciuta per il file '{filename}', non spostato.")

# Funzione principale per l'input dell'utente
def main():
    # Richiede il percorso della cartella da organizzare
    path = input("Inserisci il percorso della cartella da organizzare: ")

    # Verifica che il percorso sia valido
    if not os.path.exists(path):
        print(f"Il percorso '{path}' non esiste. Assicurati che il percorso sia corretto.")
        return

    # Creazione delle cartelle e organizzazione dei file
    folder_creation(path)
    file_organizer(path)

if __name__ == "__main__":
    main()

