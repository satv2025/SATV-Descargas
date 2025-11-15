import ffmpeg
import shutil
import os

# Ruta del archivo original (que no se debe tocar)
original_file = r"C:\Users\skbof\AppData\Roaming\Wondershare\Wondershare Filmora\Output\Mi video.mp4"
# Ruta del archivo comprimido (donde se guardará el archivo comprimido)
compressed_file = r"C:\Users\skbof\OneDrive\Documentos\GitHub\SATV-Descargas\files\videondm.mp4"  # Este es el archivo comprimido de salida

# Comprimir el video (usar el mismo formato de compresión que ya usamos)
ffmpeg.input(original_file).output(compressed_file, vcodec='libx264', crf=23, preset='fast', acodec='aac', audio_bitrate='128k').run()

print("El archivo original ha sido comprimido y guardado como:", compressed_file)