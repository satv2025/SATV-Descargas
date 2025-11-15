import ffmpeg
import os

# Ruta del archivo de entrada y salida
input_path = r"C:\Users\skbof\AppData\Roaming\Wondershare\Wondershare Filmora\Output\Mi video - copia.mp4"
output_path = r"C:\Users\skbof\OneDrive\Documentos\GitHub\SATV-Descargas\files\videondm2_comprimido.mp4"

# Verificar si el archivo de entrada existe
if not os.path.exists(input_path):
    print(f"El archivo {input_path} no existe.")
else:
    # Ejecutar FFmpeg para comprimir el video
    ffmpeg.input(input_path).output(output_path, vcodec='libx264', preset='slow', crf=23, acodec='aac', audio_bitrate='128k', movflags='+faststart').run()
    print(f"El video se ha comprimido y guardado en: {output_path}")