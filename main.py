from flask import Flask, render_template, request, jsonify
from googletrans import Translator

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    # Check for the presence of required keys in the request data
    required_keys = ['source_lang', 'dest_lang', 'text']
    if not all(key in request.form for key in required_keys):
        return jsonify({'error': 'Missing required key(s)'})

    # Get source and target language codes and text from the request
    source_lang = request.form['source_lang']
    dest_lang = request.form['dest_lang']
    text = request.form['text']

    # Translate the text
    translator = Translator()
    translation = translator.translate(text, src=source_lang, dest=dest_lang)

    # Render the result template with the translation
    return render_template('result.html', translation=translation.text)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
