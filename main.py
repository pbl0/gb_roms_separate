from xml.etree.ElementInclude import include
from zipfile import ZipFile
import os
from shutil import move
import configparser

# dont touch values below
gbc_ext = '.gbc'
gb_ext = '.gb'
gb_count = 0
gbc_count = 0

def get_config(rel_path):
    script_dir = os.path.dirname(__file__)
    config_file = rel_path
    abs_file_path = os.path.join(script_dir, config_file)
    config = configparser.ConfigParser()
    config.read(abs_file_path)
    return config['DEFAULT']

if __name__ == "__main__":
    CONFIG = get_config('config.ini')

    print(CONFIG)

    inputd = CONFIG['input'] # 'input/'
    gb_outputd = CONFIG['gb_output'] # 'GB/'
    gbc_outputd = CONFIG['gbc_output'] # 'GBC/'
    # iterate over files in
    # input directory
    for filename in os.listdir(inputd):
        f = os.path.join(inputd, filename)
        # checking if it is a file
        if os.path.isfile(f) and '.zip' in f:
            # Read zipfile
            with ZipFile(f, 'r') as z:
                contents = z.namelist()[0]
                if gbc_ext in contents:
                    print(gbc_ext)
                    move(f, gbc_outputd)
                    gbc_count += 1
                elif gb_ext in contents:
                    print(gb_ext)
                    move(f, gb_outputd)
                    gb_count += 1
    print('GameBoy: ' + str(gb_count))
    print('GameBoy Color: ' + str(gbc_count))

