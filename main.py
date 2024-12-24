import tkinter as tkinter
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk 
import speedtest


#calcular velocidade
def calcular_speed():
    st=speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000  # Convertendo para Mbps
    upload_speed = st.upload() / 1_000_000
    return download_speed, upload_speed


def start_test():
    info_label.config(text="Testando...")
    download_speed, upload_speed =calcular_speed()
    
    speed_var["download"].set(f"{download_speed:.2f} Mbps")
    speed_var["upload"].set(f"{upload_speed:.2f} Mbps")
    
    
    if download_speed > 8:
        image_label.config(image=rapido_image)
    elif download_speed > 4:
        image_label.config(image=normal_image)
    else:
        image_label.config(image=lento_image)
        
    info_label.config(text="Teste concluído")

letras="#FFFFFF"
fundo="#233642"

janela = tk.Tk()
janela.title("Detectar velocidade da internet")
janela.geometry("450x300")
janela.resizable(False, False)
janela.configure(background=fundo)



style=ttk.Style()
style.configure("TFrame",background=fundo)
style.configure("TLabel",background=fundo,foreground=letras,font=("helvetica", 10))

frameCima=ttk.Frame(janela)
frameCima.pack(pady=(20,50))

logo_image=Image.open('globo.png')
logo_image=logo_image.resize((50,50))
logo_image=ImageTk.PhotoImage(logo_image)
logo_label=ttk.Label(frameCima,image=logo_image)
logo_label.pack(side="left",padx=(10,5))

nome_label=ttk.Label(frameCima,text="Detectar velocidade da internet",font=("helvetice",18,"bold"))
nome_label.pack(side="left")


frameConteudo=ttk.Frame(janela)
frameConteudo.pack(pady=(20,20))


info_label=ttk.Label(frameConteudo,text="Pressione o botão para testar a velocidade da internet")
info_label.grid(row=0,column=0,columnspan=3,pady=(0,10))

download_label=ttk.Label(frameConteudo,text="Velocidade de Download: ")
download_label.grid(row=1,column=0,sticky='w',pady=(0,5))

upload=ttk.Label(frameConteudo,text="Velocidade de Upload: ")
upload.grid(row=2,column=0,sticky='w',pady=(0,5))

speed_var={
    'download':tk.StringVar(),
    'upload':tk.StringVar(),
    }

download_speed_label = ttk.Label(frameConteudo, textvariable=speed_var['download'])
download_speed_label.grid(row=1, column=1, sticky='w')

upload_speed_label = ttk.Label(frameConteudo, textvariable=speed_var['upload'])
upload_speed_label.grid(row=2, column=1, sticky='w')


rapido_image_local='rápido.png'
lento_image_local='lento.png'
normal_image_local='normal.png'

rapido_image = ImageTk.PhotoImage(Image.open(rapido_image_local))
lento_image = ImageTk.PhotoImage(Image.open(lento_image_local))
normal_image = ImageTk.PhotoImage(Image.open(normal_image_local))

image_label=ttk.Label(frameConteudo)
image_label.grid(row=1,column=2,rowspan=2,padx=10)

iniciar_botao=ttk.Button(frameConteudo,text="Iniciar teste",command=start_test)
iniciar_botao.grid(row=3,column=0,columnspan=3,pady=(20,0))




janela.mainloop()