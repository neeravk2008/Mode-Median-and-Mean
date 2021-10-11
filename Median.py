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
#print(n)

new_data.sort()

if n%2==0:
    median1=float(new_data[n//2])
    median2=float(new_data[n//2+1])
    median=(median1+median2)/2
else:
    median=new_data[n//2]

print("median is = "+str(median))