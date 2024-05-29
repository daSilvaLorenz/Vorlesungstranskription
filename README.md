# Projekt: Audio Transkription und Übersetzung mit Whisper und DeepL

## Übersicht

Dieses Projekt automatisiert den Prozess der Transkription von Audiodateien und deren anschließender Übersetzung. Es verwendet OpenAI's Whisper-Modell zur Transkription und die DeepL-API zur Übersetzung. Die Zielgruppe dieses Projekts sind Lehrende an der Universität, die regelmäßig Audiodateien transkribieren und übersetzen müssen.

## Inhaltsverzeichnis

1. [Erklärung](#erklärung)
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
Über Google Colaboratory kann man Skripte ausführen lassen und externe GPU Rechenleistung benutzen. Das bietet sich für Whisper an, weil es für die Transkription sehr viel Rechenleistung benötigt. Abhängig von dem PC kann es dann mehrere Stunden dauern, bis eine Vorlesung transkribiert wurde. Wenn man über Google Colab eine GPU benutzt dauert das mit dem large_v2 Modell ca. 40 Minuten. Der Nachteil ist, dass man nur für eine begrenzte Zeit auf diese GPU Leistung zugreifen kann und die Laufzeitverbindung unterbrochen wird, wenn man über eine längere Zeit nicht aktiv damit arbeitet. Deswegen eignet sich dieses System vor allem dafür, wenn man die Funktionalität erst einmal testen, oder nur wenige Veranstaltungen transkribieren will.

Wenn Sie dieses System benutzen wollen öffnen Sie bitte zuerst dieses [Colab-Notebook](https://colab.research.google.com/drive/17QYYbLTORudIGh7v2WcN56NydUuEpYMA?usp=sharing) und melden sich mit ihrem Google Account an.

Drücke Sie oben rechts auf den Pfeil neben "Verbinden".
![image](https://github.com/daSilvaLorenz/Transkription/assets/160653026/9e4586ac-1e1e-42ad-92fa-e1a8c4b2db29)

Dann auf Laufzeittyyp ändern.
![image](https://github.com/daSilvaLorenz/Transkription/assets/160653026/39137ef1-0c19-462a-a123-c46be681dec8)

Und dann auf T4 GPU und Speichern.
![image](https://github.com/daSilvaLorenz/Transkription/assets/160653026/a31caaf4-2382-444d-b601-08953e482977)

Als nächstes drücken Sie auf das Ordner Symbol.
![image](https://github.com/daSilvaLorenz/Transkription/assets/160653026/2208b97c-6a4a-405e-91aa-b143056bd82c)

Verbinden sich mit ihrem Google Drive Account.
![image](https://github.com/daSilvaLorenz/Transkription/assets/160653026/6c918628-135f-4bb3-b572-660f2031d10d)

Öffnen den Google Drive Ordner und navigieren zu den Ordner, wo sie ihre Dateien aufbewahren wollen.
![image](https://github.com/daSilvaLorenz/Transkription/assets/160653026/d762f677-6ce3-458b-9e37-3d3a61778f37)

Rechtsklick auf den entsprechenden Ordner/die entsprechende Datei und auf Pfad kopieren drücken.
![image](https://github.com/daSilvaLorenz/Transkription/assets/160653026/f6ccbb64-360a-4c31-a798-94e2549cf395)

Den jeweiligen Pfad in die entprechende Zeile einfügen.
![image](https://github.com/daSilvaLorenz/Transkription/assets/160653026/bddc1d05-e61b-4faf-905b-47b9a5784df5)

Wenn Sie alle nötigen Pfade festgelegt haben drücken Sie auf das Play Symbol, um das Programm zu starten.
![image](https://github.com/daSilvaLorenz/Transkription/assets/160653026/6d7ecdfc-01b9-402f-b60f-f754f78733ec)

### Lokale Transkription und Übersetzung mit Whisper 
Whsiper ist auch dazu in der Lage eine Englische Übersetzung der Transkription zu machen. Diese Variante ist hilfreich, wenn sie die Übersetzung gleich im passenden Untertitelformat erhalten wollen, oder wenn es Ihnen wichtig ist das gesamte Programm lokal auf dem Rechner laufen zu lassen. Nachteile sind, dass dieser Prozess vergleichsweise langsam ist, nur ins Englische übersetzt werden kann und die Übersetzung meistens nicht mit DeepL mithalten kann. Sollten Sie sich für diese Option entscheiden können Sie sich gleich aauf [Whisper GitHub-Seite](https://github.com/openai/whisper) genauer darüber informieren. Sie können auch, wenn Sie den Schritten unter [Installation](#installation) gefolgt sind dem folgenden Befehl eine Deutsche und Englische Transkription über Whisper starten.
    ```bash
    python transcribe_and_translate_whisper.py
    ```
### Lokale Transkription und Übersetzung mit DeepL
Bei dieser Option wird mit Hilfe von Whisper zunächst lokal ein Transkript in Originalsprache verfasst und dann mit der DeepL API übersetzt. Vorteile sind, dass die DeepL API eine komplette Vorlesung in wenigen Minuten übersetzen kann, die Übersetzung in 32 Sprachen möglich ist und dass die Übersetzung meistens besser ist als die von Whisper. Nachteil ist, dass wenn man im Monat mehr als 500.000 Zeichen übersetzen will (ca. 5 Vorlesungen), für die API zahlen muss. Wenn Sie mit der [Installation](#installation) ferrtig sind können Sie dieses Programm mit folgendem Befehl starten.
    ```bash
    python local_whisper_deepL_api.py
    ``` 
### Transkription und Übersetzung nur mit API's
Hier benutzen wir sowohl für die Transkription als auch für die Übersetzung API's. Vorteile sind, dass die Transkription und Übersetzung dadurch viel schneller geht und lokal keine hohe Rechenkapazität benötigt wird. Nachteile sind, die Kosten für die API und dass man maximal 100 MB große Dateien auf einmal transkribieren lassen kann. Das sollte aber für die meisten Veranstaltungen, die 1,5 h dauern kein Problem sein, wenn man ein reines Audioformat benutzt. Diese Option bietet sich am besten für Personen an, die mehrere Vorlesungen transkribieren wollen. Starten können Sie dieses Programm nach der [Installation](#installation) mit.
    ```bash
    python only_api.py
    ```
## Installation

1. **Python Installieren:** Stellen Sie sicher, dass [Python](https://www.python.org/downloads/) 3.7 oder höher installiert ist.
2. **ffmpeg installieren:** Folgen Sie den Anwesisungen auf der [ffmpeg Seite](https://ffmpeg.org/download.html) zur Installation dieses Audioverarbeitungsprogramms.
3. Wenn Sie Whsiper lokal benutzen wollen folgen Sie den Anweisungen auf der [Whisper GitHub-Seite](https://github.com/openai/whisper).
   Wenn Sie die Whisper API benutzen wollen erstellen Sie sich bitte auf https://whisperapi.com/ einen API- Schlüssel und speichern diesen in einer Umgebungsvariablen namens `Whisper_API-Key`.
4. Wenn Sie mit Hilfe von DeepL übersetzen wollen, erstellen Sie einen API-Key für die DeepL-API und speichern Sie diesen in einer Umgebungsvariable `Deepl_API-Key`. Bitte installieren Sie auch noch die nötigen Python-Pakete mit folgendem Befehl in der Kommandozeile
    ```bash
    pip install deepl
    ```
    Weitere Informationen finden sie in der [Deepl API Dokumentation](https://developers.deepl.com/docs/v/de).
5. Ordnen Sie die entsprechenden Ordner in der config.py Datei zu, damit das Programm  weiß wo die Audiodatei finden und die Transkriptionen zu speichern sind. 

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
