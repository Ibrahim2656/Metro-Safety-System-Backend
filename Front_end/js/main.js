document.getElementById("videoForm").addEventListener("submit", async function (event) {
    event.preventDefault();

    const videoLink = document.getElementById("videoLink").value;

    // Send video link to the back-end
    const response = await fetch('http://20.83.24.19/process-video', {
        method: 'POST',
        body: JSON.stringify({ url: videoLink }),
        headers: {
            'Content-Type': 'application/json'
        }
    });

    const data = await response.json();
    const videoElement = document.getElementById("processedVideo");

    // Set the video source and display it
    videoElement.src = data.processedVideoUrl;
    videoElement.style.display = 'block';
});
