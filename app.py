from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    audio_file = request.files['audio']
    # Ses dosyasını işleyerek istediğiniz işlemleri yapabilirsiniz.
    result = f"Ses dosyası alındı: {audio_file.filename}"
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
