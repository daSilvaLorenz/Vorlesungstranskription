
#### transcribe_and_translate.py

import subprocess
import glob
import os
import shutil
import deepl

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

def create_folder(path):
    """Erstellt einen Ordner, falls er nicht existiert."""
    os.makedirs(path, exist_ok=True)

def main():
    # Überprüfen, ob Ziel-Ordner existieren
    create_folder(transcribed_audio_folder)
    create_folder(original_language_folder)

    # Erweiterung der Audiodateien, die verarbeitet werden sollen
    audio_extensions = ['*.mp3', '*.wav', '*.m4a', '*.flac', '*.ogg']

    # Suchen aller Audio Dateien im spezifizierten Ordner
    audio_files = []
    for extension in audio_extensions:
        audio_files.extend(glob.glob(os.path.join(input_folder, extension)))
    print(audio_files)

    for f in audio_files:
        try:
            # Sammelordner für die Transkripte
            file_name = os.path.splitext(os.path.basename(f))[0]

            OL_Transcriptions = unique_path(original_language_folder, file_name, is_directory=True)

            # Ordner erstellen, falls nicht vorhanden
            create_folder(OL_Transcriptions)

            # Ausführen des Whisper-Befehls für jede Datei, wobei der Output-Ordner spezifiziert wird
            subprocess.run(["whisper", f, "--model", "large-v2", "--task", "transcribe", "--output_dir", OL_Transcriptions])
            print(f"Original language transcript is ready: {OL_Transcriptions}")

            # Verschieben der fertig transkribierten Audiodatei in den Zielordner
            unique_destination_file = unique_path(transcribed_audio_folder, os.path.basename(f))
            shutil.move(f, unique_destination_file)
            print(f"Moved file to: {unique_destination_file}")

            # Übersetzung des Dokuments von Deutsch nach Englisch
            # Zielordner festlegen
            output_folder = unique_path(eng_transcript_base, file_name, is_directory=True)
            create_folder(output_folder)

            # Text aus der Transkription lesen
            with open(os.path.join(OL_Transcriptions, f"{file_name}.txt"), 'r', encoding='utf-8') as file:
                text_to_translate = file.read()

            if api_key:
                # Initialisiere den Übersetzer mit dem API-Schlüssel aus der Umgebungsvariable
                translator = deepl.Translator(api_key)

                # Führe die Übersetzung durch
                translated_text = translator.translate_text(text_to_translate, source_lang="DE", target_lang="EN-GB", split_sentences="nonewlines")

                # Übersetzten Text in Ausgabedatei schreiben
                output_file_name = file_name + "_Deepl.txt"
                output_file = os.path.join(output_folder, output_file_name)
                with open(output_file, 'w', encoding='utf-8') as file:
                    file.write(translated_text.text)
                print(f"Translated text saved to: {output_file}")
            else:
                print("API key not found. Please set the Deepl API key in your environment variables.")
        except Exception as e:
            print(f"An error occurred while processing the file {f}: {e}")

if __name__ == "__main__":
    main()
