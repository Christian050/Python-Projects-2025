import PyPDF2
import os

if(os.path.isdir('temp') == False):
    os.mkdir('temp')

txtpath = ''
pdfpath = ''

# Provide PDF path
pdfpath = input('Enter the name of your pdf file - please use backslash when typing in directory path: ')

# Provide output text file path
txtpath = input('Enter the name of your txt file - please use backslash when typing in directory path: ')

# Create sample base directory where all text files will be stored unless specified path
BASEDIR = os.path.realpath('temp')
print(BASEDIR)

if (len(txtpath) == 0):
    txtpath = os.path.join(BASEDIR, os.path.basename(os.path.normpath(pdfpath)).replace('.pdf', '') + '.txt')
    pdfobj = open(pdfpath, 'rb')
    pdfread = PyPDF2.PdfFileReader(pdfobj)
    x = pdfread.numPages
    for i in range(x):
        pageObj = pdfread.getPage(i)
        with open(txtpath, 'a+') as f:
            f.write(pageObj.extractText())
            # Provide the overview of the output, comment if unnecessary
            print(pageObj.extracttext())
            pdfobj.close()
