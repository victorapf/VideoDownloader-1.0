from pytube import YouTube
from pytube.cli import on_progress

def download():
    yt = input('Ingresa la url del video a descargar: ')
    video=YouTube(yt, on_progress_callback=on_progress)
    for i in video.streams: 
        print('Itag: {} | Formato: {} | Resolucion: {} '.format(i.itag,i.mime_type,i.resolution))
    itag=input('Ingrese el itag del video a descargar: ')
    print(video.title, 'descargando, por favor espere...')
    video.streams.get_by_itag(itag).download()
    #video.streams.download()  
    print('\nDescargado satisfactoriamente')

download()