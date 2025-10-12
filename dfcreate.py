
import pandas as pd
def tableau(objets):
    pu={"assiette":100,"banane":200,"stylo":300,"fourchette":500,"pomme":800}
    liste={}
    articles=list(set(objets))
    liste["ARTICLES"]=articles
    liste["QTE"]=[objets.count(i) for i in articles]
    liste["PRIX UNITAIRE"]=[pu[i] for i in articles]
    liste["MONTANT"]=[i*j for i,j in zip(liste["QTE"],liste["PRIX UNITAIRE"])]
    return pd.DataFrame(liste, columns=['QTE','ARTICLES','PRIX UNITAIRE',"MONTANT"])
tableau(["fourchette", "pomme", "fourchette", "fourchette"])
# Exemple de DataFrame
df=tableau(["fourchette", "pomme", "fourchette", "fourchette", "fourchette", "fourchette", "fourchette", "pomme","banane","assiette","stylo"])
df=df.set_index('ARTICLES')
print(df)