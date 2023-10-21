from PyPDF2 import PdfReader
import tkinter as tk
from tkinter import filedialog

def extract_information_from_pdf(pdf_path):
    try:
        pdf = PdfReader(pdf_path)
        extracted_text = ""
        for page in pdf.pages:
            extracted_text += page.extract_text()
        return extracted_text
    except Exception as e:
        return str(e)

def select_pdf_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])

    if file_path:
        extracted_text = extract_information_from_pdf(file_path)
        if extracted_text:
            print("Extracted Information:")
            print(extracted_text)
        else:
            print("Text extraction failed.")
    else:
        print("No PDF file selected.")

if __name__ == "__main__":
    select_pdf_file()
