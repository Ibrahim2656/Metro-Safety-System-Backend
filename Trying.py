import streamlit as st
import requests
import os

# FastAPI backend URL
backend_url = "http://20.83.24.19/process-video"

def process_video(video_link):
    # Send the video link to the backend for processing
    try:
        response = requests.post(backend_url, json={"video_link": video_link})
        if response.status_code == 200:
            # Download the processed video from the response
            video_filename = "output_with_full_annotations.mp4"
            with open(video_filename, 'wb') as f:
                f.write(response.content)
            return video_filename
        else:
            st.error(f"Error: Backend returned status code {response.status_code}")
            return None
    except Exception as e:
        st.error(f"Error: {e}")
        return None

# Streamlit UI
st.title("Video Processing App")

# Input for the video link
video_link = st.text_input("Enter the video link:")

if st.button("Process Video"):
    if video_link:
        with st.spinner('Processing the video...'):
            processed_video_path = process_video(video_link)
            if processed_video_path:
                st.success("Video processed successfully!")
                
                # Display the processed video
                video_file = open(processed_video_path, 'rb')
                video_bytes = video_file.read()
                st.video(video_bytes)
            else:
                st.error("Failed to process the video.")
    else:
        st.warning("Please provide a video link.")
