function startRecording() {
    let videoElement = document.createElement('video');
    videoElement.setAttribute('id', 'videoElement');
    videoElement.setAttribute('width', '320');
    videoElement.setAttribute('height', '240');
    videoElement.setAttribute('autoplay', '');
    document.body.appendChild(videoElement);

    let constraints = { video: true, audio: true };
    let recordedChunks = [];
    let stream = navigator.mediaDevices.getUserMedia(constraints).then((stream) => {
        videoElement.srcObject = stream;
        let mediaRecorder = new MediaRecorder(stream);
        mediaRecorder.ondataavailable = (e) => {
            if (e.data.size > 0) {
                recordedChunks.push(e.data);
            }
        };
        mediaRecorder.onstop = () => {
            let blob = new Blob(recordedChunks, { type: 'video/webm' });
            let url = URL.createObjectURL(blob);
            let a = document.createElement('a');
            a.style.display = 'none';
            a.href = url;
            a.download = 'recorded_video.webm';
            document.body.appendChild(a);
            a.click();
            URL.revokeObjectURL(url);
            stream.getTracks().forEach((track) => track.stop());
            document.body.removeChild(videoElement);
        };
        mediaRecorder.start();
        setTimeout(() => {
            mediaRecorder.stop();
        }, 5000); // Record for 5 seconds
    });
}
