// const startButton = document.getElementById('startRecording');
// const stopButton = document.getElementById('stopRecording');
// const resultDiv = document.getElementById('resultDiv');

// let mediaRecorder;
// let chunks = [];

// startButton.addEventListener('click', () => {
//     navigator.mediaDevices.getUserMedia({ audio: true })
//         .then(stream => {
//             mediaRecorder = new MediaRecorder(stream);
//             mediaRecorder.ondataavailable = event => {
//                 if (event.data.size > 0) {
//                     chunks.push(event.data);
//                 }
//             };
//             mediaRecorder.onstop = () => {
//                 const blob = new Blob(chunks, { type: 'audio/wav' });

//                 const formData = new FormData();
//                 formData.append('audio', blob);

//                 // Sunucuya POST isteği gönder
//                 fetch('/upload', {
//                     method: 'POST',
//                     body: formData,
//                 })
//                     .then(response => response.text())
//                     .then(data => {
//                         console.log('Server response:', data);
//                         resultDiv.innerText = 'Server Response: ' + data;
//                     })
//                     .catch(error => {
//                         console.error('Error:', error);
//                         resultDiv.innerText = 'Error: ' + error.message;
//                     });
//             };

//             mediaRecorder.start();
//             startButton.disabled = true;
//             stopButton.disabled = false;
//         })
//         .catch(error => {
//             console.error('Hata:', error);
//         });
// });

// stopButton.addEventListener('click', () => {
//     mediaRecorder.stop();
//     startButton.disabled = false;
//     stopButton.disabled = true;
// });

// mediaRecorder.onstop = () => {
//     const blob = new Blob(chunks, { type: 'audio/wav' });
//     const audioUrl = URL.createObjectURL(blob);

//     // Ses dosyasını dinlemek için audioPlayer elementine ekleyin
//     const audioPlayer = document.getElementById('audioPlayer');
//     audioPlayer.src = audioUrl;
//     audioPlayer.play(); // Sesin otomatik olarak çalınmasını istiyorsanız
// };
