import pandas as pd
import PyPDF2
from docx import Document
import pdfplumber

class DataProcessor:
    """Simple data processor for multiple formats"""
    
    def process_csv(self, file_path):
        """Read CSV file"""
        df = pd.read_csv(file_path)
        return df.to_string()
    
    def process_excel(self, file_path):
        """Read Excel file"""
        df = pd.read_excel(file_path)
        return df.to_string()
    
    def process_pdf(self, file_path):
        """Extract text from PDF"""
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text()
        return text
    
    def process_docx(self, file_path):
        """Extract text from DOCX"""
        doc = Document(file_path)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text
