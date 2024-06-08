from setuptools import setup, find_packages

setup(
    name='find-remove-blank-pdf',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/pradeeptomer4u/find-remove-blank-pdf',
    license='MIT',
    author='Pradeep',
    author_email='pradeeptomer4u@gmail.com',
    description='A Python package for PDF processing tasks like OCR, page manipulation, and PDF creation.',
    long_description='A Python SDK simplifies PDF processing in Python, offering functionalities such as Optical Character Recognition (OCR), page manipulation, and PDF creation.',
    python_requires='>=3.10',
    install_requires=[
        'Pillow',
        'pytesseract',
        'pdf2image',
        'reportlab',
        'PyPDF2',
        ],
)

