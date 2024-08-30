from flask import Flask, request, render_template
from PIL import Image
import io
import pytesseract

pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'



app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    text = ""
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part"
        file = request.files['file']
        if file.filename == '':
            return "No selected file"
        if file:
            image = Image.open(io.BytesIO(file.read()))
            text = pytesseract.image_to_string(image)
    return render_template('index.html', extracted_text=text)
