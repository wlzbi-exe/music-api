import re
import requests
from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse

app = FastAPI(title="Music API")

SEARCH_URL = "https://wlzbi-music-api.onrender.com/search"
DOWNLOAD_URL = "https://api.ytultra.com/ikool/youtube/download"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
    "Content-Type": "application/json",
    "Origin": "https://ytultra.com",
    "Referer": "https://ytultra.com/",
}


def search_top(query: str) -> dict | None:
    try:
        r = requests.get(SEARCH_URL, params={"q": query}, timeout=30)
    except requests.RequestException as e:
        raise HTTPException(502, f"search failed: {e}")

    if r.status_code != 200:
        raise HTTPException(502, f"search returned HTTP {r.status_code}")

    try:
        data = r.json()
    except ValueError:
        raise HTTPException(502, "search response not JSON")

    if isinstance(data, list):
        data = data[0] if data else {}
    results = data.get("results") or []
    if not results:
        return None
    return results[0]


def find_medias(obj):
    if isinstance(obj, dict):
        if "medias" in obj and isinstance(obj["medias"], list):
            return obj["medias"]
        for v in obj.values():
            r = find_medias(v)
            if r is not None:
                return r
    elif isinstance(obj, list):
        for item in obj:
            r = find_medias(item)
            if r is not None:
                return r
    return None


def mime_of(entry):
    m = re.search(r"[?&]mime=([^&]+)", entry.get("url", ""))
    return m.group(1).replace("%2F", "/").replace("%2f", "/") if m else ""


def get_audio_link(video_url: str):
    try:
        r = requests.post(
            DOWNLOAD_URL, headers=HEADERS, json={"url": video_url}, timeout=30
        )
    except requests.RequestException as e:
        raise HTTPException(502, f"download failed: {e}")

    if r.status_code != 200:
        raise HTTPException(502, f"download returned HTTP {r.status_code}")

    try:
        data = r.json()
    except ValueError:
        raise HTTPException(502, "download response not JSON")

    medias = find_medias(data)
    if not medias:
        return None, None

    for m in medias:
        if mime_of(m) == "audio/mp4":
            return m.get("url"), m.get("format")

    return None, None


@app.get("/music")
def music(q: str = Query(..., min_length=1)):
    top = search_top(q)
    if not top:
        raise HTTPException(404, "no results")

    video_url = top.get("url")
    if not video_url:
        raise HTTPException(502, "top result has no url")

    audio_url, label = get_audio_link(video_url)
    if not audio_url:
        raise HTTPException(404, "no audio stream found")

    return JSONResponse({
        "success": True,
        "credits": "WLZBI",
        "query": q,
        "title": top.get("title"),
        "channel": top.get("channel"),
        "thumbnail": top.get("thumbnail"),
        "video_url": video_url,
        "audio_url": audio_url,
        "format": label or "m4a",
    })