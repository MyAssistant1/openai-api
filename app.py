
from flask import Flask, render_template, request,jsonify,redirect,url_for
import findnames
import mailatma
import event
import json
import os
app = Flask(__name__)

@app.route('/')
def index():
    if os.path.exists('files/user.json'):
        return render_template('index.html')
    return render_template('login_page.html')

@app.route('/login', methods=['GET'])
def login():
    return render_template('login_page.html')

@app.route('/email', methods=['GET'])
def email():
    return render_template('index.html')

@app.route('/process_audio', methods=['POST'])
def process_audio():
    #MEHMET ACAR NASILSIN

    #bir fonksyion e-mail or start an event()
    #event e eklenicek kisiler
    # Manuel olarak da mail adresi girebilmeli
    #
    data = request.form.get('text')
    _list = data.split("%%")
    print(_list[0])
    print(_list[1])
    print(_list[2])
    print(_list[3])
    # Burada işlem yapabilirsiniz, örneğin metni başka bir sistemle işleyebilir veya depolayabilirsiniz.
    #print("Received audio transcript:", data)
    result = " email atilamadi"
    check = False

    if "e-mail" in _list[0] or "E-mail" in _list[0] or "email" in _list[0]:
        
        ## 3 sefer 
        check = findnames.bul(_list[0],_list[1],_list[2])
    elif "Event" in _list[0] or "event" in _list[0]:
        #front ende event baslatiliyor yazicaz.
        event.addEvent(_list[1],_list[2],_list[3])
        #_list[3] bizim saatimiz olucak.


    if check:
        #if "e-mail" in words or "E-mail" in words or "email" in words:
        result = "Atilan email adresleri: \n" 
        for email in mailatma.takvim.gonderilenler:
            result = result + "\n" + email
    return result



@app.route('/login_page', methods=['POST'])
def login_page():
    
    data = request.form.get('text')
    print(data)
    _list = data.split("%%")
    username=_list[0]
    password=_list[1] 
    print("username: ",username," password: ",password)

 
    # Data to be written
    dictionary = {
        "email": username,
        "password": password,
    }
    
    # Serializing json
    json_object = json.dumps(dictionary, indent=4)
    
    # Writing to sample.json
    with open("files/user.json", "w") as outfile:
        outfile.write(json_object)

    return "ok"

    

if __name__ == '__main__':
    app.run(debug=True)
