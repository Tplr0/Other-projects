from yt_dlp import YoutubeDL
import os
import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import re

def fetch_links(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        links = []
        for a_tag in soup.find_all('a', href=True):
            link = a_tag['href']
            if re.match(r'http[s]?://', link):
                links.append(link)
        return links
    except Exception as e:
        showinfo("Error", f"Failed to fetch links: {e}")
        return []

def download_video(url, output_path):
    try:
        options = {
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
        }
        with YoutubeDL(options) as ydl:
            ydl.download([url])
        showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        showinfo("Error", f"Failed to download video: {e}")

def download_audio(url, output_path):
    try:
        options = {
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with YoutubeDL(options) as ydl:
            ydl.download([url])
        showinfo("Success", "Audio downloaded successfully!")
    except Exception as e:
        showinfo("Error", f"Failed to download audio: {e}")

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

def start_download():
    url = url_var.get().strip()
    output_path = path_var.get().strip()
    if not output_path:
        output_path = os.getcwd()

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    if choice_var.get() == "1":
        download_video(url, output_path)
    elif choice_var.get() == "2":
        download_audio(url, output_path)
    else:
        showinfo("Error", "Please select a valid download option.")

def fetch_and_display_links():
    url = url_var.get().strip()
    links = fetch_links(url)
    link_list.delete(0, tk.END)
    for link in links:
        link_list.insert(tk.END, link)

def use_selected_link():
    selected = link_list.curselection()
    if selected:
        url_var.set(link_list.get(selected[0]))

def main():
    global url_var, path_var, choice_var, link_list

    root = tk.Tk()
    root.title("Video Downloader")
    center_window(root, 700, 500)

    frame_top = tk.Frame(root, pady=10)
    frame_top.pack(fill="x")

    tk.Label(frame_top, text="Enter URL:", anchor="w", width=15).grid(row=0, column=0, padx=10, pady=5)
    url_var = tk.StringVar()
    tk.Entry(frame_top, textvariable=url_var, width=50).grid(row=0, column=1, padx=10, pady=5, sticky="w")

    tk.Label(frame_top, text="Output Directory:", anchor="w", width=15).grid(row=1, column=0, padx=10, pady=5)
    path_var = tk.StringVar()
    tk.Entry(frame_top, textvariable=path_var, width=50).grid(row=1, column=1, padx=10, pady=5, sticky="w")

    frame_middle = tk.Frame(root, pady=10)
    frame_middle.pack(fill="x")

    tk.Label(frame_middle, text="Select Option:", anchor="w", width=15).grid(row=0, column=0, padx=10, pady=5)
    choice_var = tk.StringVar(value="1")
    tk.Radiobutton(frame_middle, text="Download Video (MP4)", variable=choice_var, value="1").grid(row=0, column=1, sticky="w")
    tk.Radiobutton(frame_middle, text="Download Audio (MP3)", variable=choice_var, value="2").grid(row=1, column=1, sticky="w")

    frame_buttons = tk.Frame(root, pady=10)
    frame_buttons.pack(fill="x")

    tk.Button(frame_buttons, text="Fetch Links", command=fetch_and_display_links).pack(side="left", padx=10)
    tk.Button(frame_buttons, text="Start Download", command=start_download).pack(side="right", padx=10)

    frame_links = tk.Frame(root, pady=10)
    frame_links.pack(fill="both", expand=True)

    tk.Label(frame_links, text="Available Links:", anchor="w").pack(anchor="w", padx=10)
    link_list = tk.Listbox(frame_links, width=80, height=15)
    link_list.pack(fill="both", expand=True, padx=10, pady=5)

    tk.Button(frame_links, text="Use Selected Link", command=use_selected_link).pack(side="bottom", pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
