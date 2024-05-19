**Project: Python Flask Server for Uploading and Processing Files with Azure Blob Storage**

This project provides a Flask-based server that allows users to upload files and optionally process them before storing them in Azure Blob Storage.

**Features:**

- client file uploader using Flask's `request` object and saving to a designated upload folder on the server part.
- Error handling with appropriate status codes:
    - 200: Success
    - 7: Upload processing error (non-specific)
    - 8: General error during upload
- Optional file processing using a placeholder comment section.
- Azure Blob Storage integration for secure and scalable storage.

**Requirements:**

- Flask
- Azure Storage SDK for Python (`azure-storage-blob`)
- The `secrets` module (Python 3.6+)

**Installation:**

1. Clone this repository.
2. Install the required dependencies:

   ```bash
   pip install Flask
   pip install azure-storage-blob
   ```

   OR
   
   ```bash
   pip install -r requirements.txt
   ```
**Configuration:**

- Edit the file named `temp.txt` in the project directory. This file should contain a valid Shared Access Signature (SAS) URI for accessing your Azure Blob Storage container.

**Optional File Processing:**

- The code includes a placeholder comment section (`#YOU CAN ADD YOUR OWN MODIFICATION OF THE FILE HERE`) where you can implement custom logic to modify uploaded files before storing them in Azure Blob Storage.

**Running the Server:**

```bash
python server.py
```

This will start the server on the default IP address and port 5000. You can access the upload endpoint at the client part `s=requests.post("http:// ------  PUT THE PUBLIC IP HERE ------ :5000/upload", files = myFile, timeout = 2.5)`.


**Azure Blob Storage Setup:**

- Create an Azure Storage account if you haven't already.
- Create a container within your storage account where you want to store uploaded files.
- Generate a Shared Access Signature (SAS) URI that grants write access to the container. Paste this SAS URI into the `temp.txt` file.

**Security Considerations:**

- This is a basic example and should not be deployed in production environments without additional security measures.
- Be cautious when storing sensitive data in uploaded files.
- Validate and sanitize user input to prevent potential security vulnerabilities.