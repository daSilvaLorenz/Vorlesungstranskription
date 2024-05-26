# Projekt: Audio Transkription und Übersetzung mit Whisper und DeepL

## Übersicht

Dieses Projekt automatisiert den Prozess der Transkription von Audiodateien und deren anschließender Übersetzung. Es verwendet OpenAI's Whisper-Modell zur Transkription und die DeepL-API zur Übersetzung. Die Zielgruppe dieses Projekts sind Lehrende an der Universität, die regelmäßig Audiodateien transkribieren und übersetzen müssen.

## Inhaltsverzeichnis

1. [Erklärung](#Erklärung)
2. [Installation](#installation)
3. [Ordnerstruktur](#ordnerstruktur)
4. [Verwendung](#verwendung)
5. [Funktionsweise](#funktionsweise)
6. [Konfiguration](#konfiguration)
7. [Beitragen](#beitragen)
8. [Lizenz](#lizenz)

## Erklärung
Es gibt verschiedene Möglichkeiten mit hilfe von Whisper Vorlesungen zu transkribieren. Welche am sinvollsten ist hängt von verschiedenen Faktoren ab. Hier sollen einige Möglichkeiten vorgestellt werden, damit Sie eine Methode finden, die auf ihre Situation passt.

### Google Colab
Über Google Colaboratory kann man Skripte ausführen lassen und externe GPU Rechenleistung benutzen. Das bietet sich für Whisper an, weil es für die Transkription sehr viel Rechenleistung benötigt. Abhängig von dem PC kann es dann mehrere Stunden dauern, bis eine Vorlesung transkribiert wurde. Wenn man über Google Colab eiin GPU benutzt dauert das ca. 30 Minuten. Der Nachteil ist, dass man nur für eine begrenzte Zeit auf diese GPU Leistung zugreifen kann und die Laufzeitverbindung abgebrochen wird, wenn man über eine längere Zeit nicht aktiv damit arbeitet. Deswegen eignet sich dieses System vor allem dafür, wenn man die Funktionalität für sich erst einmal testen will oder man nur wenige Veranstaltungen transkribieren will.

![image](https://github.com/daSilvaLorenz/Transkription/assets/160653026/9b641d71-da88-4fe2-b676-e7a5f22592ce)



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
