import pandas as pd
import json

df = pd.read_excel('BD.xlsx',header=None, sheet_name=None)

def normalize_key(s):
    """ Quita acentos, espacios y capitalizción de cadenas."""
    replacements = (("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"),
                    ("ú", "u"),("ñ", "n"), (".",""),(" ","_"))
    
    s = s.strip()
    for a, b in replacements:
        s = s.replace(a, b).replace(a.lower(), b.lower())
        s = s.lower()
    s = s.strip()
    return s


courses_list ={
    'al':'Aleman',
    'fr':'Frances',
    'po':'Portugues',
    'in':'Ingles',
    'ini':'Intensive Ingles',
    'it':'Italiano',
}

for sheet in df.keys():
    header = None
    try:
        header = df[sheet].iloc[0]
    except IndexError as i:
        print('La hoja ',sheet,' esta vacia')
        continue
    data = df[sheet].iloc[1:]
    data.columns  = header
    bd = []
    for row in data.iterrows():
        bd_data = {}
        row = row[1]
        for column in row.keys():
            bd_data[normalize_key(column)]= str(row[column])
        bd.append(bd_data)
    with open(normalize_key(sheet)+'.json','w') as f:
        json.dump(bd,f,indent=2)  

