import csv
file=open("acc.csv")
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
	if(c>=1):
		if(int(i[9])<20):
			i[9]="YOUNG"
		elif(int(i[9])>=20 and int(i[9])<45):
			i[9]="MIDDLE-AGED"
		elif(int (i[9])>=45):
			i[9]="SENIOR CITIZEN"
		
		st=i[1]
		res_st=st[3:6]
		i[1]=res_st
	c=c+1

for i in l:
	line_res=[]
	for h in range(len(i)):
		line_res.append(i[h])
	res.append(line_res)


with open("acc1.csv", "w") as f:
    w=csv.writer(f)
    for row in res:
        w.writerow(row)


