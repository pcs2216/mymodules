#!/usr/bin/env python
import csv


# Leer el archivo 'datos.csv' con reader() y
# mostrar todos los registros, uno a uno:
"""with open('res.partner.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        # row is a list of strings
        # use string.join to put them together
        print ', '.join(row)"""
"""        
changes = [
    ['1 dozen', '12'],
    ['1 ,banana, puebla,puebla ', '13'],
    ['1 dollar', 'elephant', 'heffalump'],
]

with open('res.partner.csv', 'ab') as f:
    writer = csv.writer(f)
    writer.writerows(changes)"""

reader = csv.reader(open('res.partner.csv', 'rb'))

#for x in reader
campo=[]
partner_template={}
band=1
for row in reader:
    if band == 1:
        campo=row
        band=2
    else:
        cont=0  
        for col in campo:                 
            print cont            
            partner_template.update({campo[cont]: row[cont]})
            cont=cont+1            
print partner_template
