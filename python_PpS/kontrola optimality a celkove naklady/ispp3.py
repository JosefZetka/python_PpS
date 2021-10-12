from params_for_unit import params_for_unit
from pdg_from_veliciny import pdg_from_veliciny
from Kontrakty import kontrakt_SVR
import pandas as pd
import math
import pdb
import pulp
bilancni_skupina = 1
oh_ve_Veliciny = 1
# FROM'Veliciny.................xlsx'
veliciny_std = pdg_from_veliciny('Veliciny_std.xlsx', oh_ve_Veliciny)
# .......................................................................................................................................................................
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# FROM KOTEL PP.LST
##param = {'1st':'KOTEL_CostC', '2nd':'KOTEL_CostB', '3rd':'KOTEL_CostA', '4th':'KOTEL_Pdg', '5th': 'KOTEL_Pmaxtech', \
##         '6th': 'KOTEL_Pmintech', '7th': 'KOTEL_CmaxDO', '8th':'KOTEL_BsSE'}
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
pmin = []
pmax = []
costA=[]
costB=[]
costC=[]
pdg=[]
name = []
mer_nkl = []
bsse = []
for i in veliciny_std.index[:30] :   # Nacte vsechny indexy krome "b"
       
       #breakpoint()
       #print(i)
       try:
              #print(params_for_unit((i)))
       
              if params_for_unit((i))[7] == bilancni_skupina:
                     name.append(str(i))
                     costC.append(params_for_unit((i))[0])
                     costB.append(params_for_unit((i))[1])
                     costA.append(params_for_unit((i))[2])
                     pmin.append(params_for_unit((i))[5])
                     pmax.append(params_for_unit((i))[4])
                     bsse.append(params_for_unit((i))[7])
                     var_pdg = params_for_unit((i))[4]
                     #var_pdg = veliciny_std[i]
                     pdg.append(var_pdg)
                     mer_nkl.append(params_for_unit((i))[0] + params_for_unit((i))[1] * var_pdg + params_for_unit((i))[2] * var_pdg *var_pdg)
                     
       except:
              pass              
print(name)
print(pdg)
print(f" Celkove merne naklady bloků z bilancni skupiny {bilancni_skupina} jsou {round(sum(mer_nkl),0)} Kc")
NAME = name
Kontrakt_PR = kontrakt_SVR('Veliciny_std.xlsx',oh_ve_Veliciny,'PR')
#Kontrakt_PR = 0
Kontrakt_SRP = kontrakt_SVR('Veliciny_std.xlsx',oh_ve_Veliciny,'SR+')
#Kontrakt_SRP = 0
Kontrakt_SRM = kontrakt_SVR('Veliciny_std.xlsx',oh_ve_Veliciny,'SR-')
#Kontrakt_SRM = 0
Kontrakt_MZ15P = kontrakt_SVR('Veliciny_std.xlsx',oh_ve_Veliciny,'MZ15+')
#Kontrakt_MZ15P = 0
Kontrakt_MZ15M = kontrakt_SVR('Veliciny_std.xlsx',oh_ve_Veliciny,'MZ15-')
#Kontrakt_MZ15M = 0
LOCATIONS = [i for i in range(0,len(NAME))]

# Celkem vyrobit
Kontrakt_PDG = sum([el for el in pdg if not isinstance(el, str)]) -Kontrakt_PR-Kontrakt_SRP-Kontrakt_SRM-Kontrakt_MZ15P-Kontrakt_MZ15M
#Kontrakt_PDG = 4902

Pmin = pmin
Pmin =  [0 if i < 0 else i for i in pmin]
#Pmin = [125.0, 0.0, 125.0, 140.0, 100.0, 100.0, 100.0, 70.0, 330.0]
Pmax = pmax
#Pmax = [220, 220]
#odstavka =[1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0]
odstavka = [1 if i > 0 else int(i) for i in pmin]
PRmin = [3 for i in range(0,len(NAME))]
PRmax = [10 for i in range(0,len(NAME))]
SRPmin = [1 for i in range(0,len(NAME))]
SRPmax = [40 for i in range(0,len(NAME))]
SRMmin = [1 for i in range(0,len(NAME))]
SRMmax = [40 for i in range(0,len(NAME))]
MZ15Pmin = [1 for i in range(0,len(NAME))]
MZ15Pmax = [60 for i in range(0,len(NAME))]
MZ15Mmin = [1 for i in range(0,len(NAME))]
MZ15Mmax = [60 for i in range(0,len(NAME))]
# COSts
cc =  [0 if i < 0 else i for i in costC]
cb =  [0 if i < 0 else i for i in costB]



prob = pulp.LpProblem("PpS",pulp.LpMinimize)
pdg_vars = pulp.LpVariable.dicts("Pdg",LOCATIONS,0,max(pmax))
x_vars = pulp.LpVariable.dicts("uselocation",LOCATIONS,0, 1, pulp.LpBinary)
switch_pr_vars = pulp.LpVariable.dicts("pr",LOCATIONS,0,1,pulp.LpBinary)
switch_srp_vars = pulp.LpVariable.dicts("srp",LOCATIONS,0,1,pulp.LpBinary)
switch_srm_vars = pulp.LpVariable.dicts("srm",LOCATIONS,0,1,pulp.LpBinary)
switch_mz15p_vars = pulp.LpVariable.dicts("mz15p",LOCATIONS,0,1,pulp.LpBinary)
switch_mz15m_vars = pulp.LpVariable.dicts("mz15m",LOCATIONS,0,1,pulp.LpBinary)

srp_vars = pulp.LpVariable.dicts("SRP",LOCATIONS,0,40, pulp.LpInteger)
srm_vars = pulp.LpVariable.dicts("SRM",LOCATIONS,0,40, pulp.LpInteger)
pr_vars = pulp.LpVariable.dicts("PR",LOCATIONS,0,10, pulp.LpInteger)
mz15p_vars = pulp.LpVariable.dicts("MZ15P",LOCATIONS,0,60, pulp.LpInteger)
mz15m_vars = pulp.LpVariable.dicts("MZ15M",LOCATIONS,0,60, pulp.LpInteger)

prob +=pulp.lpSum(srp_vars[i]+srm_vars[i]+  pr_vars[i] + \
    mz15p_vars[i] + mz15m_vars[i]+ cc[i] + cb[i]*pdg_vars[i]   for i in LOCATIONS)

#+ cc[i] + cb[i]*pdg_vars[i]

for i in LOCATIONS:
    prob +=pdg_vars[i]-srm_vars[i]-mz15m_vars[i]-pr_vars[i] >= Pmin[i] * x_vars[i]
    prob +=pdg_vars[i] + srp_vars[i]+mz15p_vars[i]+pr_vars[i] <=Pmax[i] * x_vars[i]
    prob += x_vars[i]  == odstavka[i]
    prob += pdg_vars[i] >= Pmin[i] * x_vars[i]
    prob += pdg_vars[i] <= Pmax[i] * x_vars[i]
    prob +=pr_vars[i] >= PRmin[i] * switch_pr_vars[i]
    prob +=pr_vars[i] <= PRmax[i] * switch_pr_vars[i]
    prob +=srp_vars[i] >= SRPmin[i] * switch_srp_vars[i]
    prob +=srp_vars[i] <= SRPmax[i] * switch_srp_vars[i]
    prob +=srm_vars[i] >= SRMmin[i] * switch_srm_vars[i]
    prob +=srm_vars[i] <= SRMmax[i] * switch_srm_vars[i]
    prob +=mz15p_vars[i] >= MZ15Pmin[i] * switch_mz15p_vars[i]
    prob +=mz15p_vars[i] <= MZ15Pmax[i] * switch_mz15p_vars[i]
    prob +=mz15m_vars[i] >= MZ15Mmin[i] * switch_mz15m_vars[i]
    prob +=mz15m_vars[i] <= MZ15Mmax[i] * switch_mz15m_vars[i]

prob += pulp.lpSum(pr_vars[i] for i in LOCATIONS) >= Kontrakt_PR
prob += pulp.lpSum(pr_vars[i] for i in LOCATIONS) <= 100     
prob += pulp.lpSum(srp_vars[i] for i in LOCATIONS) >= Kontrakt_SRP
prob += pulp.lpSum(srp_vars[i] for i in LOCATIONS) <= 100
prob += pulp.lpSum(srm_vars[i] for i in LOCATIONS) >= Kontrakt_SRM
prob += pulp.lpSum(srm_vars[i] for i in LOCATIONS) <= 100
prob += pulp.lpSum(mz15p_vars[i] for i in LOCATIONS) >= Kontrakt_MZ15P
prob += pulp.lpSum(mz15p_vars[i] for i in LOCATIONS) <= 100
prob += pulp.lpSum(mz15m_vars[i] for i in LOCATIONS) >= Kontrakt_MZ15M
prob += pulp.lpSum(mz15m_vars[i] for i in LOCATIONS) <= 100
# Suma Pdg
prob += pulp.lpSum(pdg_vars[i] for i in LOCATIONS) >= Kontrakt_PDG-1
prob += pulp.lpSum(pdg_vars[i] for i in LOCATIONS) <= Kontrakt_PDG+1

#solver = pulp.getSolver('CPLEX_CMD', timeLimit=10)
#solver = pulp.getSolver('CPLEX_CMD', fracGap = 0.01, maxSeconds = 500000000, threads = None,mip = 1 ,msg = 1)
#prob.solve(pulp.CHOCO_CMD( mip = True ,msg = True, timeLimit = 100, keepFiles = True))
prob.solve(pulp.PULP_CBC_CMD(msg=True, warmStart=True))

#prob.solve()
print("Problem je:",prob)
print("Status:", pulp.LpStatus[prob.status])
TOL = 0.01
sumPR = sumSRP = sumSRM = sumMZ15P = sumMZ15M = sumPDG= 0
kodovnik = {  i : name[i] for i in range(0, len(name))}
for i in LOCATIONS:
    print("{0} ma Pdg = {1}, PR = {7} , SRP = {2}, SRM = {3}, MZ15P = {5}, MZ15M = {6} a status {4}".format(kodovnik[i],pdg_vars[i].varValue,srp_vars[i].varValue,srm_vars[i].varValue,x_vars[i].varValue,mz15p_vars[i].varValue,mz15m_vars[i].varValue,pr_vars[i].varValue))
    sumPR += pr_vars[i].varValue
    sumSRP += srp_vars[i].varValue
    #print(f" Elna {i} velikost SRP {srp_vars[i].varValue}, celkem {sumSRP}")
    sumSRM += srm_vars[i].varValue
    sumMZ15P +=mz15p_vars[i].varValue
    sumMZ15M +=mz15m_vars[i].varValue
    sumPDG += pdg_vars[i].varValue
    
release = pulp.VERSION
print("Kontrakt: PR={0}, SRP={1}, SRM={2}, MZ15P={3}, MZ15M={4}.".format(Kontrakt_PR,Kontrakt_SRP,Kontrakt_SRM,Kontrakt_MZ15P,Kontrakt_MZ15M))
print("Nasazeno: PR={0}, SRP={1}, SRM={2}, MZ15P={3}, MZ15M={4}.".format(sumPR,sumSRP,sumSRM,sumMZ15P,sumMZ15M))
print("Kontrakt PDG ={0}".format(Kontrakt_PDG))
print("PDG Celkem ={0}".format(sumPDG))
# The short X.Y version.
print("version" + str(release))
print("----------------------------")

