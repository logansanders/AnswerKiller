from answerkiller import app
from werkzeug import secure_filename
import os


ALLOWED_EXTENSIONS = app.config.get('ALLOWED_IMAGES', set([]))

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def save_file(uploaded_file, subfolder=None):
    if uploaded_file and allowed_file(uploaded_file.filename):
        filename = secure_filename(uploaded_file.filename)
        try:
            save_folder = os.path.join(app.config['UPLOAD_FOLDER'], subfolder)
            if not os.path.exists(save_folder):
                os.makedirs(save_folder)
        except:
            save_folder = os.path.join(app.config['UPLOAD_FOLDER'])

        if os.path.exists(os.path.join(save_folder, filename)):
            save_path = resolve_conflict(save_folder, filename)
        else:
            save_path = os.path.join(save_folder, filename)

        uploaded_file.save(save_path)
        return save_path


def resolve_conflict(folder, name):

    name, ext = name.split('.')
    save_path = os.join(folder, name)+'_{n}.{ext}'
    n = 1
    tmp = save_path.format(n=n, ext=ext)
    while os.path.exists(tmp):
        n += 1
        tmp = save_path.format(n=n, ext=ext)

    return tmp


def url_for_file(file_path):
    return file_path.split(app.config[UPLOAD_FOLDER])[-1]