import pandas as pd
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import webbrowser as wb

# Fonction pour générer un DataFrame de mesures de capteurs
def generer_tableau_capteurs():
    data = {
        "Capteur": ["Capteur 1", "Capteur 2", "Capteur 1"],
        "Date": ["12/11/2025"]*3,
        "Heure": ["08:00", "08:05", "08:10"],
        "Tension (V)": [5.0, 4.8, 5.1],
        "Courant (A)": [0.2, 0.25, 0.22],
        "Puissance (W)": [1.0, 1.2, 1.12]
    }
    df = pd.DataFrame(data)
    return df

# Créer le DataFrame
df = generer_tableau_capteurs()

# Création du PDF
pdf_filename = 'tableau_capteurs.pdf'
pdf = SimpleDocTemplate(pdf_filename, pagesize=letter)

# Convertir le DataFrame en liste pour reportlab
data_list = [df.columns.tolist()] + df.values.tolist()

# Styles
styles = getSampleStyleSheet()
paragraph = Paragraph("Relevé automatique des capteurs\n\n", styles['Normal'])

# Création de la table
table = Table(data_list)
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
]))

# Construire le PDF
pdf.build([paragraph, table])

# Ouvrir le PDF automatiquement
wb.open(pdf_filename)
