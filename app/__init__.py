from flask import Flask
from .kenzie import make_directory
from .kenzie.image import download, download_zip, list_by_type, list_files, upload_item
import os

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1*1000*1000

make_directory()


@app.post('/upload')
def upload():
    return upload_item()


@app.get('/files')
def files():
    return list_files()


@app.get('/files/<ext>')
def list_files_by_extension(ext):
    return list_by_type(ext)


@app.get('/download/<file_name>')
def download_file_name(file_name):
    return download(file_name)


@app.get('/download-zip')
def download_dir_as_zip():
    return download_zip()
