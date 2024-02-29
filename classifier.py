import numpy as np
import pandas as pd

inp = [0.0]*8 #insert parameters in this list  


diab_df = pd.read_csv("diabetes.csv")
true_filter = (diab_df["Outcome"] == 1)
diab_df.drop("Outcome",axis=1,inplace=True)

true_array = diab_df[true_filter].to_numpy()
false_array =  diab_df[~ true_filter].to_numpy()

true_prior= len(true_array)/len(diab_df)
'''means = true_array.mean(axis=0,keepdims=True)
variance = true_array.var(axis=0,keepdims=True)


means = np.concatenate((false_array.mean(axis=0,keepdims=True),means),axis=0)
variance = np.concatenate((false_array.var(axis=0,keepdims=True),variance),axis=0)
'''

means = np.array([[  3.298 ,     109.98,        68.184,       19.664,   68.792,   30.3042,       0.429734 ,   31.19      ],
 [  4.86567164, 141.25746269,  70.82462687,  22.1641791,  100.3358209,   35.14253731,   0.5505,      37.06716418]])


variance = np.array([[9.08519600e+00, 6.81995600e+02, 3.25622144e+02, 2.21267104e+02,  9.75479674e+03, 5.90156024e+01, 8.92731152e-02, 1.35861900e+02],
 [1.39446425e+01, 1.01633297e+03, 4.60174468e+02, 3.11405881e+02,1.91629021e+04, 5.25538622e+01, 1.38130519e-01, 1.19853698e+02]])

x = np.array([inp])
p_val = np.exp(-0.5*(x-means)**2/variance)/np.sqrt(2*np.pi*variance)


probs = (np.prod(p_val,axis=1))* np.array([1-true_prior,true_prior])

result = probs.argmax(axis=0) #0 if negative 1 if positive
print(result)
