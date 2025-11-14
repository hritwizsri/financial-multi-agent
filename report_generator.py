from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from datetime import datetime

class ReportGenerator:
    """Generate PDF financial reports"""
    
    def __init__(self):
        self.styles = getSampleStyleSheet()
    
    def generate_pdf(self, content, output_file="financial_report.pdf"):
        """Create PDF report"""
        doc = SimpleDocTemplate(output_file, pagesize=letter)
        story = []
        
        # Title
        title = Paragraph("Financial Analysis Report", self.styles['Title'])
        story.append(title)
        story.append(Spacer(1, 0.3*inch))
        
        # Date
        date_text = f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
        story.append(Paragraph(date_text, self.styles['Normal']))
        story.append(Spacer(1, 0.2*inch))
        
        # Content
        for line in content.split('\n'):
            if line.strip():
                para = Paragraph(line, self.styles['Normal'])
                story.append(para)
                story.append(Spacer(1, 0.1*inch))
        
        # Build PDF
        doc.build(story)
        print(f"Report saved: {output_file}")
