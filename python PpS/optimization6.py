#from pulp import LpProblem,LpMaximize,LpVariable,LpBinary,lpSum, LpStatus, 
import pulp
#print(pulp.configSolvers())
NAME = ['EPC2','EPC3','EPC4','EPC5','EPC6']
Kontrakt_PR = 0
Kontrakt_SRP = 50
Kontrakt_SRM = 50
Kontrakt_MZ15P = 0
Kontrakt_MZ15M = 40
LOCATIONS = [0,1,2,3,4]
#LOCATION = [0]
Pmin = [120,160,120,140,120]
Pmax = [200,200,200,200,200]
odstavka = [1,0,0,1,0]
PRmin = [3,3,3,3,3]
PRmax = [10,10,10,10,10]
SRPmin = [10,10,10,10,10]
SRPmax = [30,30,30,30,30]
SRMmin = [10,10,10,10,10]
SRMmax = [30,30,30,30,30]
MZ15Pmin = [10,10,10,10,10]
MZ15Pmax = [45,30,30,30,45]
MZ15Mmin = [40,10,10,10,10]
MZ15Mmax = [40,45,30,30,45]

prob = pulp.LpProblem("PpS",pulp.LpMinimize)
pdg_vars = pulp.LpVariable.dicts("Pdg",LOCATIONS,0,200)
x_vars = pulp.LpVariable.dicts("uselocation",LOCATIONS,0, 1, pulp.LpBinary)
switch_pr_vars = pulp.LpVariable.dicts("pr",LOCATIONS,0,1,pulp.LpBinary)
switch_srp_vars = pulp.LpVariable.dicts("srp",LOCATIONS,0,1,pulp.LpBinary)
switch_srm_vars = pulp.LpVariable.dicts("srm",LOCATIONS,0,1,pulp.LpBinary)
switch_mz15p_vars = pulp.LpVariable.dicts("mz15p",LOCATIONS,0,1,pulp.LpBinary)
switch_mz15m_vars = pulp.LpVariable.dicts("mz15m",LOCATIONS,0,1,pulp.LpBinary)
#switch_vars = pulp.LpVariable.dicts("condition",LOCATIONS,0,1,pulp.LpBinary)
srp_vars = pulp.LpVariable.dicts("SRP",LOCATIONS,0,40)
srm_vars = pulp.LpVariable.dicts("SRM",LOCATIONS,0,40)
pr_vars = pulp.LpVariable.dicts("PR",LOCATIONS,0,10)
mz15p_vars = pulp.LpVariable.dicts("MZ15P",LOCATIONS,0,60)
mz15m_vars = pulp.LpVariable.dicts("MZ15M",LOCATIONS,0,60)
prob +=pulp.lpSum(4*srp_vars[i]+3*srm_vars[i]+ 0.5* pr_vars[i] + \
    2*mz15p_vars[i] + mz15m_vars[i] + 0.25*pdg_vars[i]  for i in LOCATIONS)
#prob +=pulp.lpSum(switch_mz15p_var[i] for i in LOCATION)
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
    #prob +=pdg_vars[i] >= Pmin[i] * x_vars[i]
    #prob +=pdg_vars[i] <=Pmax[i] * x_vars[i]
    #prob +=srp_vars[i] >=0
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
#prob += pulp.lpSum(mz15p_vars[i] for i in LOCATIONS) - Kontrakt_MZ15P >=pulp.lpSum(switch_mz15p_var[i] for i in LOCATION)* 100
#prob += Kontrakt_MZ15P - pulp.lpSum(mz15p_vars[i] for i in LOCATIONS) >=100*(1-pulp.lpSum(switch_mz15p_var[i] for i in LOCATION))
#prob += pulp.lpSum(x_vars[i] for i in LOCATIONS) >= 4
#prob += pulp.lpSum(x_vars[i] for i in LOCATIONS) <= 5

#prob += pulp.lpSum(pr_vars[i] for i in LOCATIONS) == 23
#prob += pulp.lpSum(mz15p_vars[i] for i in LOCATIONS) == 65
#prob += pulp.lpSum(mz15m_vars[i] for i in LOCATIONS) == 35
#prob += pulp.lpSum(pdg_vars[i] for i in LOCATIONS) >= 0
#prob += pulp.lpSum(pdg_vars[i] for i in LOCATIONS) <= 200
#prob += srp_vars[4]  == 49
#prob += srm_vars[4]  == 37
#prob += mz15p_vars[4]  == 20


#prob.solve(pulp.solvers.PULP_CBC_CMD(fracGap = 0.01, maxSeconds = 500000000, threads = None,mip = 1 ,msg = 1))
prob.solve()
print("Status:", pulp.LpStatus[prob.status])
TOL = 0.01
sumPR = sumSRP = sumSRM = sumMZ15P = sumMZ15M = 0

for i in LOCATIONS:
    print("TG{0} ma Pdg = {1}, PR = {7} , SRP = {2}, SRM = {3}, MZ15P = {5}, MZ15M = {6} a status {4}".format(i,pdg_vars[i].varValue,srp_vars[i].varValue,srm_vars[i].varValue,x_vars[i].varValue,mz15p_vars[i].varValue,mz15m_vars[i].varValue,pr_vars[i].varValue))
    sumPR += pr_vars[i].varValue
    sumSRP += srp_vars[i].varValue
    sumSRM += srm_vars[i].varValue
    sumMZ15P +=mz15p_vars[i].varValue
    sumMZ15M +=mz15m_vars[i].varValue
    
release = pulp.VERSION
print("Kontrakt: PR={0}, SRP={1}, SRM={2}, MZ15P={3}, MZ15M={4}.".format(sumPR,sumSRP,sumSRM,sumMZ15P,sumMZ15M))
# The short X.Y version.
print("version" + str(release))
print("----------------------------")
