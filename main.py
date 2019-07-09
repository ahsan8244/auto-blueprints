from PIL import Image
from docx import Document
from docx.shared import Inches
import glob 

imageList = []

for filename in glob.glob('C:/Users/user/Documents/FCA/Blueprints/img/*'):
    imageList.append(filename)

document = Document()

for path in imageList:
    document.add_picture(path, width=Inches(2))

document.save('C:/Users/user/Documents/FCA/Blueprints/L2_bp.docx')
        

