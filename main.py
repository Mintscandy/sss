import os
import generate2
from flask import Flask, request, url_for, send_from_directory, render_template

ALLOWED_EXTENSIONS = set(['xlsx'])

app = Flask(__name__, template_folder="./templates")
app.config['UPLOAD_FOLDER'] = os.getcwd()
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

html = '''
    <!DOCTYPE html>
    <title>Upload File</title>
    <h1>文件上传</h1>
    <form method=post enctype=multipart/form-data>
         <input type=file name=file>
         <input type=submit value=上传>
    </form>
    '''


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route("/overall")
@app.route("/createPage/<filename>")
def page(filename):
    data = generate2.getinfo(filename)
    return render_template('temp.html',
                           data=data, student={'score': 600, 'rankings': 6000, 'subjects': ["物理", '化学', '生物']})


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file_url = url_for('uploaded_file', filename=filename)
            return html + '<p>文件上传成功！</p>'
    return html


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080")
