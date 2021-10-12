import pandas as pd
##nazev_souboru_veliciny = 'Veliciny_cplex.xlsx'
##oh_ve_Veliciny = 3
def kontrakt_SVR(nazev_souboru_veliciny, oh, typ_SVR):
       
       veliciny = pd.read_excel(io = nazev_souboru_veliciny, sheet_name = typ_SVR,  skiprows = [0,1], \
                                      usecols = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25])
       veliciny.rename(columns={'Unnamed: 1':'unit_name'}, inplace=True)
       veliciny.rename(columns={'Obchodní hodina':'elna_name'}, inplace=True)

       for i in range (1, len(veliciny['elna_name'])):
              name = veliciny['elna_name'][i-1]
              if str(veliciny['elna_name'][i]) == 'nan':
                            veliciny['elna_name'][i]  = name
              if str(veliciny['unit_name'][i]) == 'nan' or str(veliciny['unit_name'][i]) == 'NaN':
                     veliciny['unit_name'][i] = 'n'
       veliciny.set_index(['elna_name', 'unit_name'], inplace = True)
       b = [(              'CEZ', 'n'), (              'EDE', 'n'),(             'EME1', 'n'),(           'Celkem',   'n')] # indexy ktere nechci ze souboru Veliciny nacitat
       #veliciny.index = list(filter(lambda el: el not in b, veliciny.index))
       [veliciny.drop(labels = i,  inplace=True) for i in b]
       res = veliciny.iloc[:,oh].to_list()
       res = sum([el for el in res if not isinstance(el, str)])
       return res

