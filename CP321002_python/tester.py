from Filemanager import Files_Organize as fm
from pathlib import Path
keyinp=input('Enter directory: ')
display = Path.home() / keyinp
fm(display)
