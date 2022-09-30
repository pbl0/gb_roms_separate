# gb roms separate

Script that separates `.gb` and `.gbc` ROM files from a single directory. Requires [python](https://www.python.org/).

## Usage

The ROMS must be placed in the `input/` directory and each has to be in their own `.zip` file.

Run script from terminal/cmd/powershell:
```
python main.py
```

The ROMS will then get copied over to `GB/` and `GBC/` directories.

> You can customize the default folders in the `config.ini` file.
