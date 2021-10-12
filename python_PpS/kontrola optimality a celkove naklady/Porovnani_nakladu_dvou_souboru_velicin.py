from params_for_unit import params_for_unit
from pdg_from_veliciny import pdg_from_veliciny

import pandas as pd
import math
import pdb

bilancni_skupina = 1
oh_ve_Veliciny = 5

# FROM'Veliciny.................xlsx'
veliciny_cplex = pdg_from_veliciny('Veliciny_cplex.xlsx', oh_ve_Veliciny)
veliciny_std = pdg_from_veliciny('Veliciny_std.xlsx', oh_ve_Veliciny)
# .......................................................................................................................................................................
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# FROM KOTEL PP.LST
##param = {'1st':'KOTEL_CostC', '2nd':'KOTEL_CostB', '3rd':'KOTEL_CostA', '4th':'KOTEL_Pdg', '5th': 'KOTEL_Pmaxtech', \
##         '6th': 'KOTEL_Pmintech', '7th': 'KOTEL_CmaxDO', '8th':'KOTEL_BsSE'}
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


costA=[]
costB=[]
costC=[]
pdg=[]
name = []
mer_nkl = []
bsse = []
for i in veliciny_cplex.index :   # Nacte vsechny indexy krome "b"
       #breakpoint()
       #print(i)
       try:
              #print(params_for_unit((i)))
       
              if params_for_unit((i))[7] == bilancni_skupina:
                     name.append(str(i))
                     costC.append(params_for_unit((i))[0])
                     costB.append(params_for_unit((i))[1])
                     costA.append(params_for_unit((i))[2])
                     bsse.append(params_for_unit((i))[7])
                     #var_pdg = params_for_unit((i))[4]
                     var_pdg = veliciny_cplex[i]
                     pdg.append(var_pdg)
                     mer_nkl.append(params_for_unit((i))[0] + params_for_unit((i))[1] * var_pdg + params_for_unit((i))[2] * var_pdg *var_pdg)
                     
       except:
              pass              
print(name)
print(pdg)
print(f" Celkove merne naklady bloků z bilancni skupiny {bilancni_skupina} jsou {round(sum(mer_nkl),0)} Kc")

costA=[]
costB=[]
costC=[]
pdg=[]
name = []
mer_nkl = []
bsse = []
for i in veliciny_std.index :   # Nacte vsechny indexy krome "b"
       #breakpoint()
       #print(i)
       try:
              #print(params_for_unit((i)))
       
              if params_for_unit((i))[7] == bilancni_skupina:
                     name.append(str(i))
                     costC.append(params_for_unit((i))[0])
                     costB.append(params_for_unit((i))[1])
                     costA.append(params_for_unit((i))[2])
                     bsse.append(params_for_unit((i))[7])
                     #var_pdg = params_for_unit((i))[4]
                     var_pdg = veliciny_std[i]
                     pdg.append(var_pdg)
                     mer_nkl.append(params_for_unit((i))[0] + params_for_unit((i))[1] * var_pdg + params_for_unit((i))[2] * var_pdg *var_pdg)
                     
       except:
              pass              
print(name)
print(pdg)
print(f" Celkove merne naklady bloků z bilancni skupiny {bilancni_skupina} jsou {round(sum(mer_nkl),0)} Kc")
