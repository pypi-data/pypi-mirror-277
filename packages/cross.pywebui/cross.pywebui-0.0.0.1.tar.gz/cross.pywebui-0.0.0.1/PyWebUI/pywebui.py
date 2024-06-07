import shutil
import os
from PyWebUI._template import \
    main_script as template_main

from PyWebUI.utilities import \
    util4files as u4f, \
    util4string as u4s
import argparse
import os
import shutil

def copy_directory_contents(src_dir, dst_dir):
    """
    Copy the contents of src_dir to dst_dir, excluding the root folder itself.
    
    Args:
        src_dir (str): Source directory.
        dst_dir (str): Destination directory.
    """
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    for item in os.listdir(src_dir):
        src_path = os.path.join(src_dir, item)
        dst_path = os.path.join(dst_dir, item)
        
        try:
            if os.path.isdir(src_path):
                if os.path.basename(src_path) != '__pycache__':
                    shutil.copytree(src_path, dst_path)
            else:
                if not u4f.check_path_exists(dst_path):
                    shutil.copy2(src_path, dst_path)
                else:
                    raise FileExistsError(f'Cannot create a file when that file already exists: \'{dst_path}\'')
        except Exception as e:
            print(u4s.get_asciiface(f'Cannot create {os.path.basename(src_path)}: {e}', [255,0,0]))


def get_module_path(module_name):
    try:
        # Import the module dynamically using __import__
        module = __import__(module_name)
        # Return the file path of the module
        return os.path.abspath(module.__file__)
    except ImportError:
        return f"Module '{module_name}' not found."
    
class New:
    def create():
        path_main = u4f.get_dirpath(template_main.__file__)
        copy_directory_contents(src_dir=path_main,
                                dst_dir=u4f.get_dirpath(__file__))
def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description='')

    # Add sub-parser for the 'new' command
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    new_parser = subparsers.add_parser('new', help='Create a new file')

    # Parse the command line arguments
    args = parser.parse_args()

    # Check the command
    if args.command == 'new':
        # Call a function to handle the 'new' command
        New.create()
        
if __name__ == "__main__":
    main()