from StringIO import StringIO
from flask import Flask, send_file, request, render_template

app = Flask(__name__)

@app.route('/')
def upload_main():
    return render_template('upload.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    file = request.files['file']
    s = StringIO()
    file.save(s)
    s.seek(0)
    return send_file(s, mimetype=file.mimetype)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)