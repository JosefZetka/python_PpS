import pandas as pd
from import_par_from_KOTELPP import import_par_from_KOTELPP
import pdb
param = {'1st':'KOTEL_CostC', '2nd':'KOTEL_CostB', '3rd':'KOTEL_CostA', '4th':'KOTEL_Pdg', '5th': 'KOTEL_Pmaxtech', \
         '6th': 'KOTEL_Pmintech', '7th': 'KOTEL_CmaxDO', '8th':'KOTEL_BsSE'}
index = ( '12.3.2021 1:00',  '12.3.2021 2:00')
kotel = pd.read_csv('KOTEL PP.LST',engine='python', delimiter=r"\t",   header =[0],skiprows=None, index_col = [0,1])
kotelpplst = import_par_from_KOTELPP(index, kotel, **param)
def zkratka(index_veliciny):
        switcher={
               ('Mělník 3', 'B11'):'EME11',
               ('Prunéřov 2', 'B23'):'EPR223',
               (       'Prunéřov 2', 'B24'):'EPR224',
              (       'Prunéřov 2', 'B25'):'EPR225',
              (       'Tušimice 2', 'B21'):'ETU21',
              (       'Tušimice 2', 'B22'):'ETU22',
              (       'Tušimice 2', 'B23'):'ETU23',
              (       'Tušimice 2', 'B24'):'ETU24',
              (      'Dětmarovice',  'B2'):'EDE2',
              (      'Dětmarovice',  'B3'):'EDE3',
              (      'Dětmarovice',  'B4'):'EDE4',
              (         'Mělník 2',  'B9'):'EME9',
              (         'Mělník 2', 'B10'):'EME10',
              (        'Ledvice 3',  'B4'):'ELE4',
              (        'Ledvice 4',  'B6'):'ELE6',
              (         'Mělník 1', 'FBA'):'EME1fa',
              (         'Mělník 1', 'FBB'):'EME1fb',
              ('Teplárna Trmice 1', 'FBA'):'TTRfa',
              ('Teplárna Trmice 1', 'FBB'):'TTRfb',
              (         'Poříčí 2', 'FBA'):'EPOf1',
              (         'Poříčí 2', 'FBB'):'EPOf2',
              (          'Hodonín',   'nan'):'EHOf',
              (     'Dvůr Králové',   'nan'):'TDKf',
              (          'Temelín',  'B1'):'ETE1',
              (          'Temelín',  'B2'):'ETE2',
              (         'Dukovany',  'B1'):'EDUb1',
              (         'Dukovany',  'B2'):'EDUb2',
              (         'Dukovany',  'B3'):'EDUb3',
              (         'Dukovany',  'B4'):'EDUb4',
              (       'Počerady 2', 'B21'):'EPC2f',
              (           'Vltava', 'FBA'):'EVDfa',
              (           'Vltava', 'FBB'):'EVDfb',
              (     'Štěchovice 2', 'TG3'):'EST2fs',
              (         'Dalešice', 'TG1'):'EDAfs',
              (         'Dalešice', 'TG2'):'EDAfs',
              (         'Dalešice', 'TG3'):'EDAfs',
              (         'Dalešice', 'TG4'):'EDAfs',
              (  'Dlouhé stráně 1', 'TG1'):'EDSfs',
              (  'Dlouhé stráně 1', 'TG2'):'EDSfs'

               }
        return switcher.get(index_veliciny)
def params_for_unit(index_veliciny):
       #print(f'kotelpplst = {kotelpplst }')
       return kotelpplst[zkratka(index_veliciny)]
