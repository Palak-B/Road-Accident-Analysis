import csv
file=open("accident.csv")
l=[]
k=[]
res=[]
line_res=[]
count=0
t=file.readlines()
age=0
c=0
for i in t :
	k=i.strip().split(",")
	l.append(k)
	count=count+1
for i in l:
	if(i[13]!="" and c>1):
		age=age+int(i[13])
	c=c+1;
avg=age/count
print (avg)
for i in l:
	if (i[13]==""):
		i[13]=avg


for i in l:
	line_res=[]
	for h in range(3,len(i)):
		if(h!=6):
			line_res.append(i[h])
	res.append(line_res)


with open("acc.csv", "w") as f:
    w=csv.writer(f)
    for row in res:
        w.writerow(row)


	


