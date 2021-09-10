# import flask
import pyttsx3
# import bs4

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def my_form_post():
    if request.method == "POST":
        text = request.form['text']
        processed_text = text.upper()
        print(text)
        engine = pyttsx3.init()
        engine.say(text)
        engine.save_to_file(text,'message.mp3')
        engine.runAndWait()
        return render_template('my-form.html')
    return render_template('my-form.html')

if __name__ == '__main__':
    app.run()
