from flask import Flask, render_template, request
import io
import wave
from flask_cors import CORS
from openai import OpenAI
from pydub import AudioSegment
from pydub.playback import play

from flask import Flask, request
from pydub import AudioSegment
from io import BytesIO
import time

app = Flask(__name__)
CORS(app)
client = OpenAI(api_key="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")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():



    import os

    def change_file_extension(file_path, new_extension):
        # Dosya adını ve uzantısını ayrıştır
        file_name, _ = os.path.splitext(file_path)

        # Yeni uzantıyı ekleyerek yeni dosya adını oluştur
        new_file_path = file_name + '.' + new_extension

        # Dosyayı yeniden adlandır
        os.rename(file_path, new_file_path)

    # Örnek kullanım
    file_path = "/home/tangel/recorded_audio.ogx"
    new_extension = "mp3"

    change_file_extension(file_path, new_extension)


    new_file = open("/home/tangel/recorded_audio.mp3", "rb")
    transcript = client.audio.translations.create(
    model="whisper-1", 
    file=new_file, 
    response_format="text"
)
    print(transcript)
    return 'Başarıyla alındı!'

if __name__ == '__main__':
    app.run(debug=True)