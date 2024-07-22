```python
# Instalar dependencias necesarias
# Ejecuta estas líneas en tu terminal o desde el entorno de PyCharm si aún no las has instalado
# pip install pydub SpeechRecognition

import speech_recognition as sr
from pydub import AudioSegment
import os

# Ruta completa al archivo de audio
audio_file_path = "C:/ruta/al/archivo/audio.ogg"  # Cambia esta ruta a la ubicación de tu archivo de audio

# Convertir el archivo de audio a formato WAV si es necesario
audio = AudioSegment.from_file(audio_file_path)
wav_file = "C:/ruta/al/archivo/converted_audio.wav"  # Cambia esta ruta a la ubicación deseada para el archivo WAV
audio.export(wav_file, format="wav")

# Transcribir el audio a texto usando SpeechRecognition
recognizer = sr.Recognizer()
audio_file = sr.AudioFile(wav_file)

with audio_file as source:
    audio_data = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio_data, language="es-ES")
    print("Transcripción: ", text)
except sr.UnknownValueError:
    print("El reconocimiento de voz de Google no pudo entender el audio")
except sr.RequestError as e:
    print(f"No se pudieron solicitar los resultados del servicio de reconocimiento de voz de Google; {e}")
