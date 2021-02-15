

class Switcher(object):
    import pandas as pd
    globals()['comercio'] = 0
    doc = pd.read_excel('chileMaestro.xlsx')
    
    def numbers_to_months(self, argument,data):
        
        """Dispatch method"""
        method_name = 'demo_' + str(argument)
        
        globals()['comercio'] = data
        print(method_name + ' - '+ str(comercio))
        # Get the method from 'self'. Default to a lambda.
        method = getattr(self, method_name, lambda: "Invalid month")
        # Call the method as we return it
        return method()
 
    def demo_amex(self):
        import pandas as pd
        doc = pd.read_excel('chileMaestro.xlsx')
        creditos = {}
        data = []
        ter = doc[doc['BRAND'] == 'Amex']
        filtro  = ter[ter['MERCHANT'] == comercio]
        for i in filtro.index:
            creditos ={
                    "min": int(filtro.QUANTITY_MIN[i]),
                    "max": int(filtro.QUANTITY_MAX[i]),
                    "active": True,
                    "region": filtro.BIN_REGION[i],
                    "subType": filtro.SALE_PLAN[i][0:2],
                    "salePlan": filtro.SUB_TYPE[i][0:2],
                    "cardType": filtro.BIN_TYPE[i],
                    "currency": filtro.MONEDA[i],
                    "infiltroest": 0
            }
            data.append(creditos)
        include = {"include":data}
        print(include)
        
    def demo_mastercard(self):
        import pandas as pd
        doc = pd.read_excel('chileMaestro.xlsx')
        creditos = {}
        data = []
        ter = doc[doc['BRAND'] == 'MasterCard']
        filtro  = ter[ter['MERCHANT'] == comercio]
        for i in filtro.index:
            creditos ={
                    "min": int(filtro.QUANTITY_MIN[i]),
                    "max": int(filtro.QUANTITY_MAX[i]),
                    "active": True,
                    "region": filtro.BIN_REGION[i],
                    "subType": filtro.SALE_PLAN[i][0:2],
                    "salePlan": filtro.SUB_TYPE[i][0:2],
                    "cardType": filtro.BIN_TYPE[i],
                    "currency": filtro.MONEDA[i],
                    "infiltroest": 0
            }
            data.append(creditos)
        include = {"include":data}
        print(include)

    def demo_maestro(self):
        import pandas as pd
        doc = pd.read_excel('chileMaestro.xlsx')
        creditos = {}
        data = []
        ter = doc[doc['BRAND'] == 'Maestro']
        filtro  = ter[ter['MERCHANT'] == comercio]
        for i in filtro.index:
            creditos ={
                    "min": int(filtro.QUANTITY_MIN[i]),
                    "max": int(filtro.QUANTITY_MAX[i]),
                    "active": True,
                    "region": filtro.BIN_REGION[i],
                    "subType": filtro.SALE_PLAN[i][0:2],
                    "salePlan": filtro.SUB_TYPE[i][0:2],
                    "cardType": filtro.BIN_TYPE[i],
                    "currency": filtro.MONEDA[i],
                    "infiltroest": 0
            }
            data.append(creditos)
        include = {"include":data}
        print(include)
        
    def demo_visa(self):
        import pandas as pd
        doc = pd.read_excel('chileMaestro.xlsx')
        creditos = {}
        data = []
        ter = doc[doc['BRAND'] == 'VISA']
        filtro  = ter[ter['MERCHANT'] == comercio]
        # print(filtro)
        for i in filtro.index:
            creditos ={
                    "min": int(filtro.QUANTITY_MIN[i]),
                    "max": int(filtro.QUANTITY_MAX[i]),
                    "active": True,
                    "region": filtro.BIN_REGION[i],
                    "subType": filtro.SALE_PLAN[i][0:2],
                    "salePlan": filtro.SUB_TYPE[i][0:2],
                    "cardType": filtro.BIN_TYPE[i],
                    "currency": filtro.MONEDA[i],
                    "interest": 0
            }
            data.append(creditos)
        include = {"include":data}
        print(include)
    
    def month_2(self):
        return "February"
 
    def month_3(self):
        return "March"
 
x = Switcher()
toma = x.numbers_to_months('visa',119)
# print()