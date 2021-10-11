import csv
with open('Height Weight.csv',newline ='') as f:
    reader=csv.reader(f)
    file_data=list(reader)
#print(file_data)

file_data.pop(0)
new_data=[]

for i in range(len(file_data)):
    num=file_data[i][1]
    new_data.append(float(num))
#print(new_data)

n=len(new_data)
total=0

for x in new_data:
    total+=x

mean=total/n
print("mean is = "+str(mean))