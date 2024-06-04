from   ..lib.PdfGenrator import PDFgenrator
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print(BASE_DIR)

# Sample data to be used in the PDF
sample_data = [
    ['7622100690917', 'IQOS ORIGINALS ONE MOBILITY KIT - SLATE', 1, '9.600', '12', '12', '9.600'],
    ['', 'أيقوص أوريجينالز وان موبايلتي كيت - arabic', '', '', '', '', ''],
    ['', 'AKXVA31C185P', '', '', '', '', ''],
    ['2222222222222', 'shipping cost', 1, '0.000', '12', '12', '0.000'],
    ['7622100690917', 'IQOS ORIGINALS ONE MOBILITY KIT - SLATE', 1, '9.600', '12', '12', '9.600'],
    ['7622100690917', 'IQOS ORIGINALS ONE MOBILITY KIT - SLATE', 1, '9.600', '12', '12', '9.600'],
    ['7622100690917', 'IQOS ORIGINALS ONE MOBILITY KIT - SLATE', 1, '9.600', '12', '12', '9.600'],
    ['7622100690917', 'IQOS ORIGINALS ONE MOBILITY KIT - SLATE', 1, '9.600', '12', '12', '9.600'],
    ['7622100690917', 'IQOS ORIGINALS ONE MOBILITY KIT - SLATE', 1, '9.600', '12', '12', '9.600'],
    ['7622100690917', 'IQOS ORIGINALS ONE MOBILITY KIT - SLATE', 1, '9.600', '12', '12', '9.600'],
    ['7622100690917', 'IQOS ORIGINALS ONE MOBILITY KIT - SLATE', 1, '9.600', '12', '12', '9.600'],
    ['7622100690917', 'IQOS ORIGINALS ONE MOBILITY KIT - SLATE', 1, '9.600', '12', '12', '9.600'],
    ['7622100690917', 'IQOS ORIGINALS ONE MOBILITY KIT - SLATE', 1, '9.600', '12', '12', '9.600'],
    ['7622100690917', 'IQOS ORIGINALS ONE MOBILITY KIT - SLATE', 1, '9.600', '12', '12', '9.600']
]

# Path to the logo image
image_path = f"file://{BASE_DIR}/ALAB_Logo.png"

# Configuration for PDF generation
pdf_config = PDFgenrator(
    html_template_file="template.html",
    data={
        "data": sample_data,
        "image_path": image_path,
        "customer_name": "رايق العتيبي",
        "invoice_number": 24,
        "invoice_date": "August 05, 2023",
        "invoice_time": "02:14 PM"
    },
    output_file="output_jinja_class.pdf"
)

# Generate the PDF
pdf_config.generate_pdf()