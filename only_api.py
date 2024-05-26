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

def main():
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
        subprocess.run([
            "whisper", f, 
            "--model", "large-v2", 
            "--task", "transcribe", 
            "--output_dir", OL_Transcriptions, 
            "--output_format", "all"
        ])
        print(f"Original language transcript is ready: {OL_Transcriptions}")

        # Verschieben der fertig transkribierten Audiodatei in den Zielordner
        unique_destination_file = unique_path(transcribed_audio_folder, os.path.basename(f))
        shutil.move(f, unique_destination_file)
        print(f"Moved file to: {unique_destination_file}")

        # Zielordner festlegen für das Englische Transkript
        output_folder = unique_path(eng_transcript_base, file_name, is_directory=True)
        os.makedirs(output_folder, exist_ok=True)

        # Text aus der Transkription lesen
        transcript_file = os.path.join(OL_Transcriptions, f"{file_name}.txt")
        with open(transcript_file, 'r', encoding='utf-8') as file:
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
            print("API key not found. Skipping translation.")

if __name__ == "__main__":
    main()
