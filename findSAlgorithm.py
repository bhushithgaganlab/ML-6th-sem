#Find S Algorithm

#Training function to implement find-s algorithm
def train(c,t):
    for i, val in enumerate(t):
        if val == "Yes":
            specific_hypothesis = c[i].copy()
            break
             
    for i, val in enumerate(c):
        if t[i] == "Yes":
            for x in range(len(specific_hypothesis)):
                if val[x] != specific_hypothesis[x]:
                    specific_hypothesis[x] = '?'
                else:
                    pass
                 
    return specific_hypothesis
    
    #Input tuples
d = [['Sunny', 'Hot', 'Dry', ' Afternoon'],
     ['Rainy', 'Cold', 'Humid', ' Evening'], 
     ['Overcast', 'Hot', 'Dry', 'Morning'], 
     ['Sunny', 'Hot', 'Humid', ' Afternoon']]

target = ['Yes', 'No', 'Yes', 'No']

#Obtaining the final hypothesis
print("The final hypothesis is:",train(d,target))
