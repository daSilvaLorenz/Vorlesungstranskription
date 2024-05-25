# Importieren nur einmal erforderlich
import subprocess
import glob
import os
import shutil
import deepl

# Pfad zum Ordner mit den Audiodateien
input_folder = "path/to/your/audio/files",
# Zielordner für fertig transkribierte Audiodateien
transcribed_audio_folder = "path/to/your/transcribed/audio",
# Ordner für Transkripte in Originalsprache
original_language_folder = "path/to/your/original/language/transcripts",
# Ordner für die Englische Übersetzung
eng_transcript_base = "path/to/your/english/transcripts"
# Environment für den API-Schlüssel
api_key = os.getenv("Deepl_API-Key")

 

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
    file_name = os.path.splitext(os.path.basename(f))[0]

    OL_Transcriptions = unique_path(original_language_folder, file_name, is_directory=True)

    # Ordner erstellen, falls nicht vorhanden
    os.makedirs(OL_Transcriptions, exist_ok=True)

    # Ausführen des Whisper-Befehls für jede Datei, wobei der Output-Ordner spezifiziert wird
    subprocess.run(["whisper", f, "--model", "large-v2", "--task", "transcribe", "--output_dir", OL_Transcriptions])
    print(f"Original language transcript is ready: {OL_Transcriptions}")

    # Verschieben der fertig transkribierten Audiodatei in den Zielordner
    unique_destination_file = unique_path(transcribed_audio_folder, os.path.basename(f))
    shutil.move(f, unique_destination_file)
    print(f"Moved file to: {unique_destination_file}")

    # Übersetzung des Dokuments von Deutsch nach Englisch
    #Zielordner festlegen
    output_folder = unique_path(eng_transcript_base, file_name, is_directory=True)
    os.makedirs(output_folder, exist_ok=True)

    # Text aus der Transkription lesen
    with open(os.path.join(OL_Transcriptions, f"{file_name}.txt"), 'r', encoding='utf-8') as file:
        text_to_translate = file.read()

if api_key:
    # Initialisiere den Übersetzer mit dem API-Schlüssel aus der Umgebungsvariable
    translator = deepl.Translator(api_key)
        
    # Führe die Übersetzung durch
    translated_text = translator.translate_text(text_to_translate, source_lang="DE", target_lang="EN-GB",split_sentences="nonewlines")

    # Übersetzten Text in Ausgabedatei schreiben
    output_file_name = file_name + "_Deepl.txt"
    output_file = os.path.join(output_folder, output_file_name)
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(translated_text.text)
    print(f"Translated text saved to: {output_file}")
else:
    print("API key file not found.")
