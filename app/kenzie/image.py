from flask import Flask, request, send_from_directory, jsonify
from werkzeug.utils import secure_filename
import os

allowed_ext = os.getenv('ALLOWED_EXTENSIONS')
max_size = os.getenv('MAX_CONTENT_LENGTH')
files_directory = os.getenv('FILES_DIRECTORY')


def upload_item():
    up_file = request.files['file']
    file_name = secure_filename(up_file.filename)
    file_ext = file_name.split(".")

    if file_ext[1] not in allowed_ext:
        return {"message": "Formato não suportado"}, 415
    if file_name in os.listdir(f'{files_directory}/{file_ext[1]}'):
        return {"message": "Arquivo já existe"}, 409
    else:
        up_file.save(os.path.join(f'{files_directory}/{file_ext[1]}', file_name))
        return {"message": f"Upload de '{file_name}' concluído"}, 201


def list_files():
    files_png = os.listdir(f'{files_directory}/png')
    files_jpg = os.listdir(f'{files_directory}/jpg')
    files_gif = os.listdir(f'{files_directory}/gif')
    response = jsonify(files_png, files_jpg, files_gif)
    return response, 200


def list_by_type(ext):
    files = os.listdir(f'{files_directory}/{ext}')
    return jsonify(files)


def download(file_name):
    ext = file_name[-3:]
    if ext not in allowed_ext or file_name not in os.listdir(path=f'{files_directory}/{ext}'):
        return {"msg": "O arquivo não existe neste diretório"}, 404
    else:
        return send_from_directory(directory=f".{files_directory}/{ext}", path=file_name, as_attachment=True), 200


def download_zip():
    ext = str(request.args.get('file_extension'))
    ratio = int(request.args.get('compression_ratio'))
    main_list = os.listdir(path=f'{files_directory}/{ext}')
    if len(main_list)== 0:
        return {"msg": "Diretório está vazio"}, 404
    else:
        os.system(f'zip -r /tmp/{ext}-zip {files_directory}/{ext} -{ratio}')
    return send_from_directory(directory=f'/tmp', path=f'{ext}-zip.zip', as_attachment=True), 200
