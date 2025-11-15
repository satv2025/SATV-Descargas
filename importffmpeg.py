import subprocess

input_file = r"C:\Users\skbof\AppData\Roaming\Wondershare\Wondershare Filmora\Output\Mi video - copia.mp4"
output_file = r"C:\Users\skbof\AppData\Roaming\Wondershare\Wondershare Filmora\Output\Mi_video.wav"

# Comando FFmpeg: extraer audio a WAV (44.1 kHz, 16-bit, mono o estéreo según necesites)
command = [
    "ffmpeg",
    "-i", input_file,
    "-acodec", "pcm_s16le",  # WAV sin compresión
    "-ar", "44100",          # Frecuencia de muestreo
    output_file
]

subprocess.run(command, check=True)

print("Conversión completada:", output_file)
