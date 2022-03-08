import os
import pytesseract
from shutil import rmtree

from pdf2image import convert_from_path
from PIL import Image
from typing import List


root_folder = 'pdf_tempo/'

pytesseract.pytesseract.tesseract_cmd='.venv/bin/pytesseract'

def convert(files: List):
    if os.path.exists(root_folder):
        rmtree(root_folder)
    os.mkdir(root_folder)
    for f in files:
        filename = f.split('/')[-1].split('.')[0]
        fullpath = root_folder + filename
        os.mkdir(fullpath)
        pages = convert_from_path(f)
        for p, page in enumerate(pages):
            pagename = f'{fullpath}/page{p}.png'
            page.save(pagename, 'PNG')
    

files = []
files.append(os.getcwd()+'/teste0.pdf')
files.append(os.getcwd()+'/teste1.pdf')

convert(files)