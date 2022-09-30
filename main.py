import os
from zipfile import ZipFile
from shutil import copyfile
import configparser

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
    # Read config
    CONFIG = get_config('config.ini')
    inputd = CONFIG['input'] # 'input/'
    gb_outputd = CONFIG['gb_output'] # 'GB/'
    gbc_outputd = CONFIG['gbc_output'] # 'GBC/'
    # Iterate over files in input directory
    for filename in os.listdir(inputd):
        f = os.path.join(inputd, filename)
        print(filename)
        # Checking if it's a zip file
        if os.path.isfile(f) and '.zip' in f:
            # Read zipfile
            with ZipFile(f, 'r') as z:
                contents = z.namelist()[0]
                if gbc_ext in contents:
                    # Gameboy color ROM found
                    copyfile(f, gbc_outputd + filename)
                    gbc_count += 1
                elif gb_ext in contents:
                    # Gameboy ROM found
                    copyfile(f, gb_outputd + filename)
                    gb_count += 1
    print('========================')
    print('GameBoy: ' + str(gb_count))
    print('GameBoy Color: ' + str(gbc_count))
    print('========================')
    print('Script made by pablo. || https://github.com/pbl0')

