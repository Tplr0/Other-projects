from yt_dlp import YoutubeDL
import os

def download_video(url, output_path):
    try:
        print("Downloading video with audio...")
        options = {
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'format': 'bestvideo+bestaudio/best',  # Combine video and audio
            'merge_output_format': 'mp4',          # Ensure output is MP4
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',           # Final output format
            }],
        }
        with YoutubeDL(options) as ydl:
            ydl.download([url])
        print("Video downloaded successfully with audio.")
    except Exception as e:
        print(f"Error downloading video: {e}")


def download_audio(url, output_path):
    try:
        print("Downloading audio...")
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
        print("Audio downloaded successfully.")
    except Exception as e:
        print(f"Error downloading audio: {e}")

def main():
    print("YouTube Downloader")
    url = input("Enter the YouTube URL: ")
    output_path = input("Enter the output directory (leave blank for current directory): ")

    if not output_path:
        output_path = os.getcwd()

    if not os.path.exists(output_path):
        print("Output directory does not exist. Creating it...")
        os.makedirs(output_path)

    print("Choose an option:")
    print("1. Download as MP4 (video)")
    print("2. Download as MP3 (audio)")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        download_video(url, output_path)
    elif choice == "2":
        download_audio(url, output_path)
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
