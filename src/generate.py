""" generate titles and pages """

import re
from markdown_blocks import markdown_to_blocks, markdown_to_html_node

def extract_title(markdown):
    """ find title in markdown """
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if re.match(r'\A# .*', block):
            return block[2:]
    raise ValueError("Markdown does not have a title")

def generate_page(from_path, template_path, dest_path):
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

    with open(dest_path, mode="w", encoding="utf8") as file:
        file.write(template)
