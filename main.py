from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from Algorithm import main

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust as necessary for your application
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/process-video/")
async def process_video_endpoint(drive_link: str = Form(...)):  # Accept the string directly from the form
    main(drive_link)
    
    return FileResponse('Output_video/output_with_full_annotations.mp4', media_type="video/mp4", filename="output_video.mp4")

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
