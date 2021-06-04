#tuple creation
branch=("CSE","IT","Mech","ECE","CSE","AGRI","PT")
#print
print(branch)

#slicing
print(branch[1])#IT
#Fetch the elements from index 2 to index 4(end-1)
print(branch[2:5])#Mech,ECE,CSE
#Zero index to endindex-1(4)
print(branch[:5])#("CSE","IT","Mech","ECE","CSE")
#Starting 3 index to end+1
print(branch[3:])#("ECE","CSE","AGRI","PT")
#start to end+1
print(branch[:])#Default is 0 and endindex+1,prints entire tuple
#from start to end with step count is 2
print(branch[::2])#('CSE', 'Mech', 'CSE', 'PT')from start to end with step count is 2
#from start to end with step count is 3
print(branch[::3])#('CSE', 'ECE', 'PT')
#Negative step count-Reverse order
print(branch[::-2])#PT CSE MECH CSE
print(branch[::-3])#PT ECE CSE
print(branch[::1])#All elements are printed from left to right
print(branch[::-1])#Right to left(Reverse of tuple)
#Left to right fetching with -ve index
print(branch[-5:-2])#MECH,ECE,CSE

#Methods-tuple
#1.Count
#2.index
#Returns the first index of search element
result=branch.index("Mech")
print(result)#2


Output:
('CSE', 'IT', 'Mech', 'ECE', 'CSE', 'AGRI', 'PT')
IT
('Mech', 'ECE', 'CSE')
('CSE', 'IT', 'Mech', 'ECE', 'CSE')
('ECE', 'CSE', 'AGRI', 'PT')
('CSE', 'IT', 'Mech', 'ECE', 'CSE', 'AGRI', 'PT')
('CSE', 'Mech', 'CSE', 'PT')
('CSE', 'ECE', 'PT')
('PT', 'CSE', 'Mech', 'CSE')
('PT', 'ECE', 'CSE')
('CSE', 'IT', 'Mech', 'ECE', 'CSE', 'AGRI', 'PT')
('PT', 'AGRI', 'CSE', 'ECE', 'Mech', 'IT', 'CSE')
('Mech', 'ECE', 'CSE')
2
