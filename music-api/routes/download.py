from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import FileResponse

from services.downloader import downloader

router = APIRouter(
    prefix="/download",
    tags=["Download"]
)


@router.get("")
async def download(
    id: str = Query(..., description="YouTube Video ID")
):
    try:

        data = await downloader.download(id)

        return FileResponse(
            path=data["filename"],
            filename=f"{data['title']}.mp3",
            media_type="audio/mpeg"
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )