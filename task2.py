""" Task 2 ---- Write a Python function to create a new configuration file that 
replaces all (sub-)interface IP addresses that start with '172.' and '192." to "10." 
and also change the security-level to "10" . """

def ipaddress_effect(file_name):
	file=open(file_name)
	lst=[]
	lst2=[]	#this list using for ip address
	elementlst3=[]	#elements in ip address
	updatedlst4=[]	#updated ip address  
	for line in file:
		line=line.strip()
		for word in line.split():
			lst.append(word)
	for i in range(len(lst)):
		if lst[i-1]!='no' and lst[i]=='ip' and lst[i+1]=='address':
			lst2.append(lst[i+2])	#add all ip add in lst2
	for i in lst2:
		elementlst3.append(i.split('.'))	#list of elements in ip
	for i in elementlst3:		#remove '172' or '192' and update with '10'
		del i[0]	#del first element
		i.insert(0,'10')	#insert '10' at first location
		updatedlst4.append('.'.join(i))	#add upated ip add in list
	return updatedlst4

print(ipaddress_effect('running-config.txt'))

