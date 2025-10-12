#Packages
import pandas as pd
import pandas as pd
from reportlab.lib import colors #pour gérer les couleurs
from reportlab.lib.pagesizes import letter # pour le format de la page
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle,Image,Paragraph
from reportlab.lib.styles import getSampleStyleSheet #pour le text
from reportlab.lib.units import inch # pour la taille de l'image
import webbrowser as wb # pour l'afichage du pdf
from reportlab.pdfgen import canvas
#Compter le nombre de produits
def tableau(objets):
    pu={"assiette":100,"banane":200,"stylo":300,"fourchette":500,"pomme":800}
    liste={}
    articles=list(set(objets))
    liste["articles"]=articles
    liste["Qte"]=[objets.count(i) for i in articles]
    liste["prix unitaire"]=[pu[i] for i in articles]
    liste["Montant"]=[i*j for i,j in zip(liste["Qte"],liste["prix unitaire"])]
    return pd.DataFrame(liste, columns=['Qte','articles','prix unitaire',"Montant"])
tableau(["fourchette", "pomme", "fourchette", "fourchette"])
# Exemple de DataFrame
df=tableau(["fourchette", "pomme", "fourchette", "fourchette"])
# Création du PDF
pdf_filename = 'tableau_utilisateur.pdf'
pdf=SimpleDocTemplate(pdf_filename)

# Convertir le DataFrame en liste
data_list = [df.columns.tolist()]+ df.values.tolist()

print(data_list)
# Créer un objet Image pour le logo
l="E:\logo.jpg"
logo = Image(l)
logo.drawHeight = 0.5 * inch  # Ajuster la hauteur du logo
logo.drawWidth = 0.5 * inch  
#Styles de texte
styles = getSampleStyleSheet()
style_normal = styles['Normal']
# Créer un paragraphe de texte
texte = "No de Facture\n\n"
paragraph = Paragraph(texte, style_normal)
# Création de la table
table = Table(data_list)
table.wrapOn(canvas, 0, 0)
table.draw(canvas, (1, 5))
# Style de la table
style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),])
table.setStyle(style)
# Construire le PDF
elements = [logo,paragraph,table]
pdf.build(elements)
wb.open(pdf_filename)
