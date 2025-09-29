""" copystatic """
import shutil
import os

def copy_static_to_public():
    """ copy static files to public folder """
    if os.path.exists('public'):
        shutil.rmtree('public')
    os.mkdir('./public')
    for root, _, files in os.walk('static'):
        rel_path = os.path.relpath(root, 'static')
        dest_path = os.path.join('public', rel_path)
        os.makedirs(dest_path, exist_ok=True)

        for file in files:
            shutil.copy(os.path.join(root, file), os.path.join(dest_path, file))
