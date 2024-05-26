import os

# Pfad zum Ordner mit den Audiodateien
input_folder = "C:/Users/Lukas/Documents/Uni/Würzburg/KI-Tutor/Whisper/Audiodateien/Testungen/Audioaufnahmen"
# Zielordner für fertig transkribierte Audiodateien
transcribed_audio_folder = "C:/Users/Lukas/Documents/Uni/Würzburg/KI-Tutor/Whisper/Audiodateien/Testungen/fertig transkribiert"
# Ordner für Transkripte in Originalsprache
original_language_folder = "C:/Users/Lukas/Documents/Uni/Würzburg/KI-Tutor/Whisper/Audiodateien/Testungen/Transkriptionen Deutsch"
# Ordner für die Englische Übersetzung
eng_transcript_base = "C:/Users/Lukas/Documents/Uni/Würzburg/KI-Tutor/Whisper/Audiodateien/Testungen/Transkriptionen Englisch"
# Dateipfad/Environment für den  Deepl-API-Schlüssel
api_key = os.getenv("Deepl_API-Key")
# Dateipfad/Environment für den  Deepl-API-Schlüssel
whisper_api_key = os.getenv("Whisper_API-Key")