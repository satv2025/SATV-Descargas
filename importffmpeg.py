import ffmpeg
import shutil
import os

# Ruta del archivo original (que no se debe tocar)
original_file = r"C:\Users\skbof\AppData\Roaming\Wondershare\Wondershare Filmora\Output\Mi video.mp4"
# Ruta del archivo comprimido (el que será reemplazado)
compressed_file = r"C:\Users\skbof\OneDrive\Documentos\GitHub\SATV-Descargas\files\videondm.mp4"  # Este es el archivo comprimido ya tocado

# Ruta temporal para el archivo comprimido de salida
temp_output_file = r"C:\Users\skbof\OneDrive\Documentos\GitHub\SATV-Descargas\files\temp_compressed_video.mp4"

# Comprimir el video (usar el mismo formato de compresión que ya usamos)
ffmpeg.input(compressed_file).output(temp_output_file, vcodec='libx264', crf=23, preset='fast', acodec='aac', audio_bitrate='128k').run()

# Reemplazar el archivo comprimido con el nuevo comprimido procesado
shutil.move(temp_output_file, compressed_file)

print("El archivo comprimido ha sido reemplazado exitosamente.")