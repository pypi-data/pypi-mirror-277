# fin_remove_blank_pdf/sdk.py
from PIL import Image
import pytesseract as tess 
from pdf2image import convert_from_path 
import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

import PyPDF2

def remove_pages_from_pdf(input_path, output_path, pages_to_remove):
    # Open the input PDF
    with open(input_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        writer = PyPDF2.PdfFileWriter()

        # Copy all pages except the ones to be removed
        for pageNum in range(reader.numPages):
            if pageNum not in pages_to_remove:
                writer.addPage(reader.getPage(pageNum))

        # Write the output PDF
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)

def find_blank_space(image_path, block_size):
    blank_count = 0
    img = Image.open(image_path)
    img_gray = img.convert('L')
    width, height = img_gray.size
    block_width, block_height = block_size
    for y in range(0, height, block_height):
        for x in range(0, width, block_width):
            block = img_gray.crop((x, y, x + block_width, y + block_height))

            if block.getextrema() == (255, 255):
                blank_count += 1
    return blank_count


def jpgs_to_pdf(input_paths, output_path):
    c = canvas.Canvas(output_path, pagesize=A4)

    for i, input_path in enumerate(input_paths):
        img = Image.open(input_path)
        width, height = img.size

        # Calculate aspect ratio
        aspect_ratio = height / width

        # Add the image to the PDF
        c.drawImage(input_path, 0, 0, width=A4[0], height=A4[0] * aspect_ratio)

        if i != len(input_paths) - 1:
            c.showPage()  # Add a new page for each image except the last one

    c.save()
    for i in input_paths:
        os.remove(i)

    
def read_pdf(file_name, output_path):   
    pages = []
    remove_pages = []

    try:
        images = convert_from_path(file_name)  

        for i, image in enumerate(images):
            filename = "page_" + str(i) + "_" + os.path.basename(file_name) + ".jpeg"  
            image.save(filename, "JPEG")  
            text = tess.image_to_string(Image.open(filename))
            if "End Of Report" in text or "Health Summary" in text or "Interpretation" in text:
                pass
            else:
                if find_blank_space(filename, (300,800)):
                    os.remove(filename)
                    remove_pages += [i]
                    continue
                    
            pages.append(filename)
        remove_pages_from_pdf(file_name, output_path, remove_pages)
    except Exception as e:
        print(str(e))
    return pages

def process_report(input_file_path, output_path):
    read_pdf(input_file_path, output_path)
