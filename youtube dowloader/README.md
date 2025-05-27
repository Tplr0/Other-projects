# YouTube Downloader with FFmpeg Support

**Audio and Video Downloader using Python**
This Python project allows you to download YouTube videos or extract audio using open-source tools. Built on top of `pytube` and integrated with `ffmpeg`, the downloader provides a lightweight way to save content from YouTube for offline viewing.

---

## **Features**

* Download YouTube videos in various resolutions
* Extract and convert audio using FFmpeg
* Option to select video/audio quality
* Uses `pytube` for fetching content
* Terminal/CLI-based interface

---

## **Prerequisites**

To run this project, you’ll need:

* Python 3.6 or newer
* [pytube](https://pytube.io/) library
* [FFmpeg](https://ffmpeg.org/) installed and available in system PATH

Install dependencies:

```bash
pip install pytube
```

Ensure FFmpeg is installed:

* [Download FFmpeg](https://ffmpeg.org/download.html) and add it to your system path

---

## **Getting Started**

*Clone the Repository:*

```
git clone https://github.com/yourusername/youtube-downloader.git
cd youtube-downloader
```

*Run the Script:*

```
python downloader.py
```

---

## **Usage**

* Input the YouTube URL when prompted
* Choose download type (video or audio)
* The script handles download and conversion

---

## **Troubleshooting**

* `ModuleNotFoundError`: Use `pip install` to install missing packages like `pytube`
* `FFmpeg not found`: Ensure it’s installed and added to PATH
* YouTube URL errors: Double-check the link format and availability

---

## **Acknowledgments**

This project uses the open-source [pytube](https://github.com/pytube/pytube) library and [FFmpeg](https://ffmpeg.org/). These tools are created and maintained by their respective contributors. This project is for personal and educational use only—respect copyright and terms of service when downloading online content.
