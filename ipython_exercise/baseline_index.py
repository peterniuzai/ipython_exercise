import numpy as np
#antan_No = 4 
#'''
#to_bl = antan_No*2*(antan_No*2 + 1) / 2
#ro_bl = np.zeros((to_bl,2),np.int)# create a total_baseline * 2 matrix to put the baseline information. 
#print ro_bl.shape
#b=0
#for i in range(antan_No*2): 
#    print i
#    for j in range(i, antan_No*2,1):
#      print j 
#      ro_bl[b] = [i,j]
#      print ro_bl[b] 
#      b += 1   

#print ro_bl

#def bl_index():
#    '''create a baseline index from [0,0] to [n,n] '''
antan_No = 16 
to_chan  = antan_No * 2
to_bl = to_chan*(to_chan + 1) / 2
ro_bl = np.zeros((to_bl,2),np.int)# create a total_baseline * 2 matrix to put the baseline information. 
b=0
for i in range(to_chan):    
      for j in range(i, antan_No*2,1):
         ro_bl[b] = [i,j]
         b += 1  
print ro_bl
