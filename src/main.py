""" main """
from copystatic import copy_static_to_public
from generate import generate_page_recursive

def main():
    """ static site generator """
    print("overwriting public file from static folder...")
    copy_static_to_public()
    print("generating index page")
    generate_page_recursive('content', 'public', 'template.html')

if __name__ == "__main__":
    main()
