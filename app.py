
from flask import Flask, render_template, request
import findnames
import mailatma
import event
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_audio', methods=['POST'])
def process_audio():
    

    #bir fonksyion e-mail or start an event()
    #event e eklenicek kisiler
    # Manuel olarak da mail adresi girebilmeli
    #
    data = request.form.get('text')
    _list = data.split("%%")
    print(_list[0])
    print(_list[1])
    print(_list[2])
    # Burada işlem yapabilirsiniz, örneğin metni başka bir sistemle işleyebilir veya depolayabilirsiniz.
    #print("Received audio transcript:", data)
    result = " email atilamadi"
    check = False

    if "e-mail" in _list[0] or "E-mail" in _list[0] or "email" in _list[0]:
        
        ## 3 sefer 
        check = findnames.bul(_list[0],_list[1],_list[2])
    elif "Etkinlik" in _list[0] or "etkinlik" in _list[0]:
        #front ende event baslatiliyor yazicaz.
        event.addEvent()
    
    if check:
        #if "e-mail" in words or "E-mail" in words or "email" in words:
        result = "Atilan email adresleri: \n" 
        for email in mailatma.takvim.gonderilenler:
            result = result + "\n" + email
    return result

if __name__ == '__main__':
    app.run(debug=True)

