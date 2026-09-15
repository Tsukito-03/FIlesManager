from Filemanager import Files_Organize as fm
from pathlib import Path
keyinp=input('Enter directory: ')
kkk = Path.home() / keyinp
fm(kkk)