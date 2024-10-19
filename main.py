from fastapi import FastAPI
from fastapi.responses import FileResponse
from Algorthim import main

app = FastAPI()

@app.post("/process-video/")
async def process_video_endpoint(drive_link: str):
    main(drive_link)
    
    return FileResponse('Output_video/output_with_full_annotations.mp4', media_type="video/mp4", filename="output_video.mp4")

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
