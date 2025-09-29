""" main """
from copystatic import copy_static_to_public

def main():
    """ static site generator """
    print("overwriting public file from static folder...")
    copy_static_to_public()

if __name__ == "__main__":
    main()
