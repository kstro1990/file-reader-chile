# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 13:11:26 2021

@author: luis.castro
"""

import pandas as pd
import json as js

doc = pd.read_excel('chileMaestro.xlsx')


# data = []
# creditos = {}


# =============================================================================
# for i in doc:
#     print(i)
# =============================================================================
    

# =============================================================================
# creditos ={ "min": int(doc.QUANTITY_MIN[0]),
#             "max": int(doc.QUANTITY_MAX[0]),
#             "active": True,
#             "region": doc.BIN_REGION[0],
#             "subType": doc.SALE_PLAN[0][0:2],
#             "salePlan": doc.SUB_TYPE[0][0:2],
#             "cardType": doc.BIN_TYPE[0],
#             "currency": doc.MONEDA[0],
#             "interest": 0
# }
# =============================================================================


# =============================================================================
# contador = 0 
# for i in doc.QUANTITY_MIN:
#         if ( 1 != i and  2 != i):
#             i
#         else:
#             creditos ={ "min": int(doc.QUANTITY_MIN[contador]),
#                 "max": int(doc.QUANTITY_MAX[contador]),
#                 "active": True,
#                 "region": doc.BIN_REGION[contador],
#                 "subType": doc.SALE_PLAN[contador][0:2],
#                 "salePlan": doc.SUB_TYPE[contador][0:2],
#                 "cardType": doc.BIN_TYPE[contador],
#                 "currency": doc.MONEDA[contador],
#                 "interest": 0
#             }
#             contador = 1 + contador
#             data.append(creditos)
#             
# 
# include = {"include":data}
# =============================================================================


# =============================================================================
# print(include)
# =============================================================================
    

def amex_demo():
    contador = 0
    creditos = {}
    data = []
    ter = doc[doc['BRAND'] == 'Amex']
    for i in ter.index:
        creditos ={
            "band": ter.BRAND[i],
                "min": int(ter.QUANTITY_MIN[i]),
                "max": int(ter.QUANTITY_MAX[i]),
                "active": True,
                "region": ter.BIN_REGION[i],
                "subType": ter.SALE_PLAN[i][0:2],
                "salePlan": ter.SUB_TYPE[i][0:2],
                "cardType": ter.BIN_TYPE[i],
                "currency": ter.MONEDA[i],
                "interest": 0
        }
        data.append(creditos)
    include = {"include":data}
    print(include)

        
        

def switch_demo(argument):
    switcher = {
        "Amex":
            amex_demo(),
        "Maestro": "February",
        "MasterCard": "March",
        "VISA": "April"
    }
    print (switcher.get(argument, "Invalid month"))

switch_demo("Amex")

# =============================================================================
# df = pd.DataFrame(doc.BRAND,index=doc,columns=doc.keys())
# df.filter(items=['BRAND'])
# tomas = df.filter(like='Amex', axis=0)
# =============================================================================

# ter = doc[doc['BRAND'] == 'VISA']
# print(ter)