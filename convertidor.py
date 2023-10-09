from pydub import AudioSegment
import ffmpeg
import os

def convertir(primero, segundo, tercero):
    # Carga los archivos de audio que deseas unir
    audio1 = AudioSegment.from_file(primero)
    audio2 = AudioSegment.from_file(segundo)
    audio3 = AudioSegment.from_file(tercero)

    # Une los archivos de audio
    audio_unido = audio1 + audio2 + audio3

    # Guarda el archivo unido
    audio_unido.export('temp.mp4', format='mp4')

    input_file = "temp.mp4"  # Nombre de tu archivo de entrada en formato MP4

    nombre = os.path.splitext(os.path.basename(primero))[0]
    output_file = str(nombre) + ".3gp"  # Nombre del archivo de salida en formato 3GP

    ffmpeg.input(input_file).output(output_file, vf='scale=qcif', acodec='libopencore_amrnb', ar=8000, ac=1, vcodec='h263').run()