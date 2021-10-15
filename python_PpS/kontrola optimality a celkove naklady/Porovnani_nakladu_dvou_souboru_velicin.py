from params_for_unit import params_for_unit
from pdg_from_veliciny import pdg_from_veliciny
from unit import Unit
import pandas as pd
import math
import pdb

bilancni_skupina = 1
oh_ve_Veliciny = 23 # uved cele cislo napr pro 6.oh odpovida 5:00, proto zadam 5

# FROM'Veliciny.................xlsx'
veliciny_cplex = pdg_from_veliciny('Veliciny_std.xlsx', oh_ve_Veliciny)
veliciny_std = pdg_from_veliciny('Veliciny_std2.xlsx', oh_ve_Veliciny)
# .......................................................................................................................................................................
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# FROM KOTEL PP.LST
##param = {'1st':'KOTEL_CostC', '2nd':'KOTEL_CostB', '3rd':'KOTEL_CostA', '4th':'KOTEL_Pdg', '5th': 'KOTEL_Pmaxtech', \
##         '6th': 'KOTEL_Pmintech', '7th': 'KOTEL_CmaxDO', '8th':'KOTEL_BsSE'}
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
units_cplex = []
print(f' ******* CPLEX **********')
print(f' name      , costC        , pdg       , nkl ')
for i in veliciny_cplex.index :   # Nacte vsechny indexy krome "b"
       try:
              if params_for_unit((i))[7] == bilancni_skupina:

                  #breakpoint()
                  u_cplex = Unit()
                  u_cplex.name = str(i)
                  u_cplex.costC = params_for_unit((i))[0]
                  u_cplex.costB = params_for_unit((i))[1]
                  u_cplex.costA = params_for_unit((i))[2]
                  u_cplex.bsse = params_for_unit((i))[7]
                  u_cplex.pdg = veliciny_cplex[i]
                  u_cplex.vypocet_mer_nkl
                  units_cplex.append(u_cplex)
                  #print(f' name      , costC        , pdg       , nkl ')
                  print(f'{u_cplex.name} {u_cplex.costC} {u_cplex.pdg} {u_cplex.mer_nkl}')
       except:
              pass

units_std = []
print(f' ******* STD **********')
print(f' name      , costC        , pdg       , nkl ')
for i in veliciny_std.index :   # Nacte vsechny indexy krome "b"
       try:
              if params_for_unit((i))[7] == bilancni_skupina:
                  u_std = Unit()
                  u_std.name = str(i)
                  u_std.costC = params_for_unit((i))[0]
                  u_std.costB = params_for_unit((i))[1]
                  u_std.costA = params_for_unit((i))[2]
                  u_std.bsse = params_for_unit((i))[7]
                  u_std.pdg = veliciny_std[i]
                  u_std.vypocet_mer_nkl
                  units_std.append(u_std)
                  print(f'{u_std.name} {u_std.costC} {u_std.pdg} {u_std.mer_nkl}')

                  #print(f' name = {u_std.name}, costC= {u_std.costC}, pdg = {u_std.pdg}, nkl = {u_std.mer_nkl}')
       except:
              pass

suma_nakladu_cplex = 0 
for i in units_cplex:
    suma_nakladu_cplex += i.mer_nkl
print(f'suma_nakladu_cplex = {suma_nakladu_cplex}')
    
suma_nakladu_std = 0 
for i in units_std:
    suma_nakladu_std += i.mer_nkl
print(f'suma_nakladu_std = {suma_nakladu_std}')
