import numpy as np
import matplotlib.pyplot as plt
import json
from numpy import empty
# Load rainfall data from a JSON file
with open('rainfall_data.json', 'r') as json_file:
    data = json.load(json_file)    
    rainfall = data['rainfall']
    runoff = data['runoff']
    Time = empty(len(rainfall))

#define the lengh of unithydrograph
for i in range(len(rainfall)-1 , -1, -1):
    if rainfall[i] != 0:
        last_non_zero = rainfall[i]        
        break
#unit_hydrograph = empty(len(runoff)-i)

smallrainfall = rainfall[:i+1]
# Create a unit hydrograph by dividing the runoff by the peak runoff value
#Amatrix 


aMatreix = np.empty((len(rainfall),len(rainfall)))
bMatreix = np.array(runoff)



for i in range (0,len(rainfall),1):
    for j in range (0,len(smallrainfall)-1,1):        
        if i+j>len(rainfall)-1 and i>0 and j>0:
            continue
        else:
            aMatreix[i,i+j]=smallrainfall[j+1]
            

    
   
aMatreix = aMatreix.T      
bMatreix = bMatreix.T
inverse_matrix_A = np.linalg.inv(aMatreix)




#unit_hydrograph = 
solution = np.linalg.solve(aMatreix, bMatreix)
np.set_printoptions(precision=2, suppress=True)
print(solution)
#print(len(runoff)-i)



# Plot the unit hydrograph
'''
plt.plot(unit_hydrograph)
plt.xlabel('Time (hours)')
plt.ylabel('Unit Hydrograph')
plt.title('Unit Hydrograph')
plt.grid(True)
plt.show()
'''