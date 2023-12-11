
from flask import Flask, render_template, request
import findnames
import mailatma
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_audio', methods=['POST'])
def process_audio():
    
    data = request.form.get('text')
    # Burada işlem yapabilirsiniz, örneğin metni başka bir sistemle işleyebilir veya depolayabilirsiniz.
    print("Received audio transcript:", data)
    result = " email atilamadi"
    check = False

    if "e-mail" in data or "E-mail" in data or "email" in data:
        check = findnames.bul(data)
    
    if check:
        #if "e-mail" in words or "E-mail" in words or "email" in words:
        result = "Atilan email adresleri: \n" 
        for email in mailatma.takvim.gonderilenler:
            result = result + "\n" + email
    return result

if __name__ == '__main__':
    app.run(debug=True)
