from flask import Flask , render_template, request, redirect, flash, url_for, send_from_directory
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = ""
app.config['SECRET_KEY'] = ''

txt = ""


@app.route("/")
def index():
    my_files = os.listdir(app.config["UPLOAD_FOLDER"])
    print(my_files)
    return render_template("index.html",my_files=my_files,txt=txt)

@app.route("/upload", methods=["POST"])
def upload():
    my_file = request.files.get("my_file")
    dst_file = my_file.filename
    flash("File uploaded")
    my_file.save(os.path.join(app.config["UPLOAD_FOLDER"], dst_file))
    return redirect(url_for("index"))


@app.route("/clipboard", methods=["POST"])
def clipboard():
    global txt
    txt = request.form.get("copy")
    print(txt)
    return redirect(url_for("index"))    

@app.route("/download")
def download():
    download_file = request.args.get("my_file")
    return send_from_directory(app.config['UPLOAD_FOLDER'], download_file, as_attachment=True)


if __name__ == "__main__":
    #Here ip and port
    app.run(debug=False, host="public IP", port=5000)
    #app.run(debug=False)

