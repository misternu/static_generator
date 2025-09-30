""" generate titles and pages """

import os
import shutil
import re
from markdown_blocks import markdown_to_blocks, markdown_to_html_node

def extract_title(markdown):
    """ find title in markdown """
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if re.match(r'\A# .*', block):
            return block[2:]
    raise ValueError("Markdown does not have a title")

def generate_page(from_path, dest_path, basepath, template_path):
    """ generate page from content """
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, mode="r", encoding="utf-8") as from_file:
        content = from_file.read()

    with open(template_path, mode="r", encoding="utf-8") as template_file:
        template = template_file.read()

    html = markdown_to_html_node(content).to_html()
    title = extract_title(content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')

    with open(dest_path, mode="w", encoding="utf8") as file:
        file.write(template)

def generate_page_recursive(dir_path_content, dest_dir_path, basepath, template_path="template.html"):
    """ recursively generate pages from content """
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = dest_path.replace("md", "html")
            generate_page(from_path, dest_path, basepath, template_path)
        else:
            generate_page_recursive(from_path, dest_path, basepath, template_path)


# import shutil
# import os

# def copy_static_to_public():
#     """ copy static files to public folder """
#     if os.path.exists('public'):
#         shutil.rmtree('public')
#     os.mkdir('./public')
#     for root, _, files in os.walk('static'):
#         rel_path = os.path.relpath(root, 'static')
#         dest_path = os.path.join('public', rel_path)
#         os.makedirs(dest_path, exist_ok=True)

#         for file in files:
#             shutil.copy(os.path.join(root, file), os.path.join(dest_path, file))
