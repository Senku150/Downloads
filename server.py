from flask import Flask ,request,flash
import os
import socket
import secrets
from azure.storage.blob import BlobClient
from urllib.parse import urlparse


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "storage"
app.config['SECRET_KEY'] = secrets.token_bytes(32).hex()


@app.route("/", methods=["GET"])
def index():
        return "200"

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
    send_to_blob(path)
    os.remove(path)
  except:
    os.remove(path)
    return "7"
  finally:
    return "1"

def send_to_blob(path):

    def read_first_line(file_path):
        with open(file_path, 'r') as file:
            first_line = file.readline().strip()
        return first_line
    
    sas = read_first_line("temp.txt")
    container = 'storage'
    sasUrlParts = urlparse(sas)
    accountEndpoint = sasUrlParts.scheme + '://' + sasUrlParts.netloc
    sasToken = sasUrlParts.query
    blobName = "VM_ZONE_1/"+os.path.basename(path) 
    blobSasUrl = accountEndpoint + '/' + container + '/' + blobName + '?' + sasToken
    blobClient = BlobClient.from_blob_url(blobSasUrl)
    with open(path, 'rb') as f:
        blobClient.upload_blob(f) 


if __name__ == "__main__":
    #Here ip and port
    ip= socket.gethostbyname(socket.gethostname())
    app.run(debug=False, host=ip, port=5000)
