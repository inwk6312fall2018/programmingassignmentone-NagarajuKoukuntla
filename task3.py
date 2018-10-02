"""Task3 --- function to create a list of "access-list" for "global_access" and "fw-management_access_in"""

def access_lst(detailfile):
	file=open(detailfile) #file accessing though detailfile parameter
	lst=[]
	for line in file:
	  line=line.strip()
	  for i in line.split():	#if line contains global-access or fw-management appends to list
		if i=='global_access' or i=='fw-management_access_in':
			lst.append(line)
	return lst
print(access_lst('running-config.cfg')		



