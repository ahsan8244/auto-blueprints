from PIL import Image
from docx import Document
from docx.shared import Inches
import glob 

imageList = []

for filename in glob.glob('C:/Users/user/Documents/FCA/Blueprints/img/*'):
    imageList.append(filename)

#setup doc
document = Document()
tables = document.tables

while len(imageList) != 0:
    #create a 4x4 table
    table = document.add_table(rows=2, cols=2)
    #insert 4 pictures
    for col in table.columns:
        for cell in col.cells:
            paragraph = cell.paragraphs[0]
            run = paragraph.add_run()
            print('adding picture...')
            run.add_picture(imageList.pop(0), width=Inches(3))

#save the doc
document.save('C:/Users/user/Documents/FCA/Blueprints/L2_bp.docx')
print('done')
        

