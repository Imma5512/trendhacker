from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_pdf_report(keyword, trends, etsy_data):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, f"Report Trend: {keyword}")

    c.setFont("Helvetica", 12)
    c.drawString(50, height - 80, "Google Trends:")
    y = height - 100
    for date, value in trends:
        c.drawString(60, y, f"{date}: {value}")
        y -= 15

    c.drawString(50, y - 20, "Etsy Prodotti Trovati:")
    y -= 40
    for item in etsy_data:
        c.drawString(60, y, f"- {item['Titolo']} | {item['Vendite stimate']} vendite | {item['Prezzo (€)']} €")
        y -= 15
        if y < 100:
            c.showPage()
            y = height - 50

    c.save()
    buffer.seek(0)
    return buffer
