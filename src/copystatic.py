""" copystatic """
import shutil
import os

def copy_static_to(folder):
    """ copy static files to specified folder """
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.mkdir(f'./{folder}')
    for root, _, files in os.walk('static'):
        rel_path = os.path.relpath(root, 'static')
        dest_path = os.path.join(folder, rel_path)
        os.makedirs(dest_path, exist_ok=True)

        for file in files:
            shutil.copy(os.path.join(root, file), os.path.join(dest_path, file))
