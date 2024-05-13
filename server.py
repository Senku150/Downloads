from flask import Flask ,request,flash
import os
import socket
import secrets



app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "storage"
app.config['SECRET_KEY'] = secrets.token_bytes(32).hex()



@app.route("/upload", methods=["POST"])

def upload():
  try:
    my_file = request.files.get("my_file")
    dst_file = my_file.filename
    flash("File uploaded")
    my_file.save(os.path.join(app.config["UPLOAD_FOLDER"], dst_file))
    path=os.path.join(app.config["UPLOAD_FOLDER"], dst_file)
  except Exception as error:
    print(error)
    return "8"
  try:
    #TODO the azure blob here
    os.remove(path)
  except:
    os.remove(path)
    return "7"
  finally:
    return "1"



if __name__ == "__main__":
    #Here ip and port
    ip= socket.gethostbyname(socket.gethostname())
    app.run(debug=False, host=ip, port=5000)
