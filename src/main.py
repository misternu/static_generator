""" main """
import sys
from copystatic import copy_static_to
from generate import generate_page_recursive

def main():
    """ static site generator """
    if len(sys.argv) == 1:
        basepath = '/'
    else:
        basepath = sys.argv[1]
    print("overwriting docs file from static folder...")
    copy_static_to('docs')
    print("generating index page")
    generate_page_recursive('content', 'docs', basepath)

if __name__ == "__main__":
    main()
