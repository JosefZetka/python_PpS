import pandas as pd
#from zaznam import Zaznam
from decimal import Decimal

kotel = pd.read_csv('KOTEL PP.LST',engine='python', delimiter=r"\t",   header =[0],skiprows=None, index_col = [0,1])
#cols = kotel.columns
#inxs = kotel.index
index = ( '12.3.2021 1:00',  '12.3.2021 2:00')

def import_par_from_KOTELPP(inx, kotel, **par):
       """
       returns a dictionary where keys are str(doh19[i]['RTISZDef.Prefix']) + str(doh19[i]['RTISZDef.Suffix']), i.e. 'ETU24' and values
       are lists containing items that corrensponds with **par parameters. The dictionary contains all units.
       
       inx ... index, tzn. index = ('25.2.2021 18:00', '25.2.2021 19:00')
       kotel ... kotel, tzn. kotel = pd.read_csv('KOTEL PP.LST',engine='python', delimiter=r"\t",   header =[0],skiprows=None, \
       index_col = [0,1])
       **par = {'1st':'KOTEL_CostCnt', '2nd':'KOTEL_CostBnt', '3rd':'KOTEL_CostAnt', '4th':'KOTEL_Pdgnt'}
       1st ... KOTEL_CostCnt
       2nd ... KOTEL_CostBnt
       3rd ... KOTEL_CostAnt
       4th ... KOTEL_Pdgnt
       """       
       skotel=kotel.sort_index() #sorted
       oh19 = skotel.loc[inx[0],inx[1]].fillna(0) #
       doh19 = oh19.to_dict('records')
       vysledek = {}
       number_of_useful_rows = len(doh19)-2 # kvuli nekolika tabulkam v KOTEL_PP.LST  je nutne eliminovat zaznam obshaujjici 'true'
       for i in range(0 ,number_of_useful_rows):
              key = str(doh19[i]['RTISZDef.Prefix']) + str(doh19[i]['RTISZDef.Suffix'])
              value = []
              for k,v in par.items():
                     value.append(float(doh19[i][v]))
              vysledek.update({key: value})
                               
       return(vysledek)
par = {'1st':'KOTEL_CostCnt', '2nd':'KOTEL_CostBnt', '3rd':'KOTEL_CostAnt', '4th':'KOTEL_Pdgnt'}
par2 = {'1st':'KOTEL_CostCnt'}
vys = import_par_from_KOTELPP(index,kotel, **par2)

    
