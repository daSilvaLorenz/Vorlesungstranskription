# Projekt: Audio Transkription und Übersetzung mit Whisper und DeepL

## Übersicht

Dieses Projekt automatisiert den Prozess der Transkription von Audiodateien und deren anschließender Übersetzung. Es verwendet OpenAI's Whisper-Modell zur Transkription und die DeepL-API zur Übersetzung. Die Zielgruppe dieses Projekts sind Lehrende an der Universität, die regelmäßig Audiodateien transkribieren und übersetzen müssen.

## Inhaltsverzeichnis

1. [Installation](#installation)
2. [Ordnerstruktur](#ordnerstruktur)
3. [Verwendung](#verwendung)
4. [Funktionsweise](#funktionsweise)
5. [Konfiguration](#konfiguration)
6. [Beitragen](#beitragen)
7. [Lizenz](#lizenz)

## Installation

1. **Python Installieren:** Stellen Sie sicher, dass [Python](https://www.python.org/downloads/) 3.7 oder höher installiert ist.
2. **Abhängigkeiten Installieren:** Installieren Sie die erforderlichen Python-Pakete mit folgendem Befehl in der Kommandozeile:
    ```bash
    pip install deepl
    ```
3. **Whisper Installieren:** Folgen Sie den Anweisungen auf der [Whisper GitHub-Seite](https://github.com/openai/whisper) zur Installation des Whisper-Tools.
4. **DeepL API-Key:** Erstellen Sie einen API-Key für die DeepL-API und speichern Sie diesen in einer Umgebungsvariable `Deepl_API-Key`. Weitere Informationen [Deepl API Dokumentation](https://developers.deepl.com/docs/v/de)
5. **ffmpeg installieren:** Folgen Sie den Anwesisungen auf der [ffmpeg Seite](https://ffmpeg.org/download.html) zur Installation dieses Audioverarbeitungsprogramms.

## Ordnerstruktur
Hier wird festgelegt, wo sich die zu transkribierenden Audiodateien befinden und wo die Transkripte gespeichert werden sollen.
Diese Ordner müssen in den Zeilen 8 - 15 im Code festgelegt werden. 

- `input_folder`: Eingabeordner für die Audiodateien.
- `transcribed_audio_folder`: Ordner für fertig transkribierte Audiodateien.
- `Deutsches Transkript`: Ordner für Transkripte in der Originalsprache.
- `Englisches Transkript`: Ordner für die englische Übersetzung der Transkripte.

## Verwendung 
1. **Audiodateien Hinzufügen:** Legen Sie die zu transkribierenden Audiodateien im Ordner `input_folder` ab.
2. **Skript Ausführen:** Führen Sie das Skript aus:
    ```bash
    python transcribe_and_translate.py
    ```

## Funktionsweise

1. **Dateien suchen:** Das Skript durchsucht den Eingabeordner nach Audiodateien mit den folgenden Erweiterungen: `.mp3`, `.wav`, `.m4a`, `.flac`, `.ogg`.
2. **Transkription:** Jede Audiodatei wird mithilfe von Whisper transkribiert und die Transkripte werden im Ordner `Deutsches Transkript` gespeichert.
3. **Verschieben der Audiodateien:** Die transkribierten Audiodateien werden in den Ordner `fertige Audio` verschoben.
4. **Übersetzung:** Die deutschen Transkripte werden mit der DeepL-API ins Englische übersetzt und im Ordner `Englisches Transkript` gespeichert.

## Konfiguration

- **API-Schlüssel:** Der API-Schlüssel für DeepL muss als Umgebungsvariable `Deepl_API-Key` gesetzt sein.
- **Ordnerpfade:** Die Pfade zu den Eingabe- und Ausgabeordnern können im Skript angepasst werden.

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Weitere Informationen finden Sie in der `LICENSE` Datei.

---

Wenn Sie Fragen oder Probleme haben, öffnen Sie bitte ein Issue auf GitHub.
