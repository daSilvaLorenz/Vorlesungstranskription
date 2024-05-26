import subprocess
import glob
import os
import shutil
import subprocess

# Konfigurationsdatei importieren
from config import input_folder, transcribed_audio_folder, original_language_folder, eng_transcript_base, api_key


def unique_path(base_path, name, is_directory=False):
    """Generiert einen einzigartigen Pfad, indem eine Nummer hinzugefügt wird, falls der Pfad bereits existiert."""
    counter = 1
    if is_directory:
        new_path = os.path.join(base_path, name)
        while os.path.exists(new_path):
            new_path = os.path.join(base_path, f"{name} ({counter})")
            counter += 1
    else:
        base_name, extension = os.path.splitext(name)
        new_path = os.path.join(base_path, name)
        while os.path.exists(new_path):
            new_path = os.path.join(base_path, f"{base_name} ({counter}){extension}")
            counter += 1
    return new_path


# Überprüfen, ob Ziel-Ordner existieren
os.makedirs(transcribed_audio_folder, exist_ok=True)
os.makedirs(eng_transcript_base, exist_ok=True)
os.makedirs(original_language_folder, exist_ok=True)



# Erweiterung der Audiodateien, die verarbeitet werden sollen
audio_extensions = ['*.mp3', '*.wav', '*.m4a', '*.flac', '*.ogg']

# Suchen aller Audio Dateien im spezifizierten Ordner
audio_files = []
for extension in audio_extensions:
    audio_files.extend(glob.glob(os.path.join(input_folder, extension)))
print(audio_files)

for f in audio_files:
    # Sammelordner für die Transkripte
    file_name= os.path.splitext(os.path.basename(f))[0]

    OL_Transcriptions = unique_path(original_language_folder, file_name, is_directory=True)
    Eng_Transcriptions = unique_path(eng_transcript_base, file_name, is_directory=True)

    # Ordner erstellen, falls nicht vorhanden
    os.makedirs(OL_Transcriptions, exist_ok=True)
    os.makedirs(Eng_Transcriptions, exist_ok=True)

    # Ausführen des Whisper-Befehls für jede Datei, wobei der Output-Ordner spezifiziert wird
    # Englische Übersetzung
    subprocess.run(["whisper", f, "--model", "large-v2", "--task", "translate", "--output_dir", Eng_Transcriptions])
    print(f"Translation is ready: {Eng_Transcriptions}")
    # Originalsprache
    subprocess.run(["whisper", f, "--model", "large-v2", "--task", "transcribe", "--output_dir", OL_Transcriptions])
    print(f"Original language transcript is ready: {OL_Transcriptions}")

# Verschieben der fertig transkribierten Audiodatei in den Zielordner
    unique_destination_file = unique_path(transcribed_audio_folder, os.path.basename(f))
    shutil.move(f, unique_destination_file)
    print(f"Moved file to: {unique_destination_file}")