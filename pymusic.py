import tkinter as tk
from tkinter import filedialog, messagebox
import yt_dlp  # Certifique-se de instalar yt-dlp: pip install yt-dlp

def download_youtube_audio_yt_dlp(url, output_path):
    """
    Baixa o áudio de um vídeo do YouTube usando yt-dlp.

    Args:
        url (str): O URL do vídeo do YouTube.
        output_path (str): O caminho para salvar o arquivo MP3 baixado.
    """
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'extract_audio': True,
            'audio_format': 'mp3',
            'audio_quality': '0',  # Melhor qualidade
            'noplaylist': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            video_title = info_dict.get('title', None)
            messagebox.showinfo("Download Concluído", f"Download concluído com sucesso: {video_title}.mp3")

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

def browse_folder():
    """
    Abre a caixa de diálogo para selecionar o diretório de download.
    """
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        download_path_entry.delete(0, tk.END)
        download_path_entry.insert(0, folder_selected)

def start_download():
    """
    Inicia o download do áudio do vídeo do YouTube.
    """
    video_url = url_entry.get()
    download_path = download_path_entry.get()
    if video_url and download_path:
        download_youtube_audio_yt_dlp(video_url, download_path)
    else:
        messagebox.showerror("Erro", "Por favor, insira o URL do vídeo e o caminho de download.")

# Interface gráfica
window = tk.Tk()
window.title("YouTube to MP3 Downloader")

# Rótulos
url_label = tk.Label(window, text="URL do vídeo do YouTube:")
url_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

download_path_label = tk.Label(window, text="Salvar em:")
download_path_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

# Campos de entrada
url_entry = tk.Entry(window, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=5)

download_path_entry = tk.Entry(window, width=50)
download_path_entry.grid(row=1, column=1, padx=10, pady=5)
download_path_entry.insert(0, ".")  # Caminho padrão

# Botões
browse_button = tk.Button(window, text="Procurar", command=browse_folder)
browse_button.grid(row=1, column=2, padx=5, pady=5)

download_button = tk.Button(window, text="Baixar MP3", command=start_download)
download_button.grid(row=2, column=1, padx=10, pady=10)

# Iniciar o loop principal
window.mainloop()