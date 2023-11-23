// script.js

const startButton = document.getElementById('startRecording');
const stopButton = document.getElementById('stopRecording');

let mediaRecorder;
let chunks = [];

startButton.addEventListener('click', () => {
    navigator.mediaDevices.getUserMedia({ audio: true })
        .then(stream => {
            mediaRecorder = new MediaRecorder(stream);
            mediaRecorder.ondataavailable = event => {
                if (event.data.size > 0) {
                    chunks.push(event.data);
                }
            };
            mediaRecorder.onstop = () => {
                const blob = new Blob(chunks, { type: 'audio/wav' });
                const audioUrl = URL.createObjectURL(blob);
                // Şimdi bu audioUrl'yi sunucuya gönderebilir veya işleyebilirsiniz.
            };
            mediaRecorder.start();
        })
        .catch(error => {
            console.error('Hata:', error);
        });
});

stopButton.addEventListener('click', () => {
    mediaRecorder.stop();
});

mediaRecorder.onstop = () => {
    const blob = new Blob(chunks, { type: 'audio/wav' });
    const audioUrl = URL.createObjectURL(blob);

    // Ses dosyasını dinlemek için audioPlayer elementine ekleyin
    const audioPlayer = document.getElementById('audioPlayer');
    audioPlayer.src = audioUrl;
    audioPlayer.play(); // Sesin otomatik olarak çalınmasını istiyorsanız
};
