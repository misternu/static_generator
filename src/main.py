""" main """
from copystatic import copy_static_to_public
from generate import generate_page

def main():
    """ static site generator """
    print("overwriting public file from static folder...")
    copy_static_to_public()
    print("generating index page")
    generate_page('content/index.md', 'template.html', 'public/index.html')

if __name__ == "__main__":
    main()
