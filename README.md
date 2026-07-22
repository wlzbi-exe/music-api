# music-api
🎵 A powerful FastAPI-based music API for searching, streaming, downloading, lyrics, playlists and more. Built with Python and designed for music bots, apps, and automation projects.

# 🎵 Music API

<p align="center">

<img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/FastAPI-API-green?style=for-the-badge&logo=fastapi">
<img src="https://img.shields.io/badge/SQLite-Database-orange?style=for-the-badge&logo=sqlite">
<img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge">

</p>

<p align="center">

<img src="https://img.shields.io/github/stars/wlzbi-exe/music-api?style=for-the-badge&logo=github">

</p>


## 🎧 About

A powerful, lightweight and developer-friendly Music API built with **FastAPI + Python**.

This API provides music search, streaming, playback, downloading, lyrics, playlists and more.

Designed for developers who want to integrate music features into:

- 🤖 Telegram Bots
- 🌐 Websites
- 📱 Applications
- ⚙️ Automation Tools


---

# ✨ Features

- 🎧 Music Search API
- 🔊 Audio Streaming
- ▶️ Music Playback System
- 📥 Download Support
- 🎤 Lyrics Fetching
- 📀 Playlist Management
- 🔐 Authentication System
- 📊 API Statistics
- ❤️ Health Monitoring
- ⚡ Cache System
- 📝 Logging System


---

# 🚀 Tech Stack

- Python 3.10+
- FastAPI
- Uvicorn
- SQLite Database
- Async API Architecture
- YouTube Music Extraction
- Custom Cache System


---

# 📂 Project Structure

```text
music-api/
│
├── app.py
├── config.py
├── requirements.txt
├── database.py
│
├── routes/
│   ├── __init__.py
│   ├── search.py
│   ├── stream.py
│   ├── play.py
│   ├── download.py
│   ├── lyrics.py
│   ├── playlist.py
│   ├── auth.py
│   ├── stats.py
│   └── health.py
│
├── services/
│   ├── __init__.py
│   ├── youtube.py
│   ├── extractor.py
│   ├── downloader.py
│   ├── lyrics.py
│   ├── cache.py
│   ├── auth.py
│   ├── logger.py
│   └── utils.py
│
├── cache/
├── downloads/
├── database/
├── logs/
│
└── README.md
```

---

# ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/wlzbi-exe/music-api.git
```

```bash
cd music-api
```

### Install Requirements

```bash
pip install -r requirements.txt
```


---

# ▶️ Run API

Start the server:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

API:

```
http://localhost:8000
```

Swagger Docs:

```
http://localhost:8000/docs
```


---

# 🔥 API Endpoints

## ❤️ Health Check

```
GET /health
```


## 🎵 Search Music

```
GET /search?q=query
```


## 🔊 Stream Music

```
GET /stream/{id}
```


## ▶️ Play Music

```
GET /play/{id}
```


---

# 🛣️ Roadmap

- ✅ Search API
- ✅ Streaming API
- ✅ Play API
- ⏳ Download API
- ⏳ Lyrics API
- ⏳ Playlist System
- ⏳ Authentication
- ⏳ User Statistics
- ⏳ Cloud Storage Support


---

# 🤝 Contributing

Contributions are welcome!

Steps:

1. Fork this repository
2. Create a new branch
3. Make your changes
4. Submit a Pull Request


---

# ⚠️ Disclaimer

This project is created for educational and development purposes.

Users are responsible for respecting copyright rules and external platform terms.


---

# 📜 License

Licensed under the MIT License.


---

# ⭐ Support

If you find this project useful, consider giving it a star ⭐ on GitHub.


---

# 👨‍💻 Developer

<p align="center">

<img src="https://img.shields.io/badge/DEV-WLZBI-black?style=for-the-badge&logo=github">

</p>


<p align="center">

<a href="https://github.com/wlzbi-exe">
<img src="https://img.shields.io/badge/GitHub-wlzbi--exe-181717?style=for-the-badge&logo=github">
</a>

<a href="https://t.me/rejerks">
<img src="https://img.shields.io/badge/Telegram-@rejerks-26A5E4?style=for-the-badge&logo=telegram">
</a>

</p>


<p align="center">
BY <b>WLZBI</b>
</p>
