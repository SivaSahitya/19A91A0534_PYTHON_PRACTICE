#tuple creation
bra=("CSE","IT","Mech","ECE","CSE")
#print
print(bra)
#Data type of bra
print(type(bra))
#size of tuple
print("Size of tuple is: {}" .format(len(bra)))#4
#Max element
max_ele=max(bra)
print("Max element is %s" %(max_ele))
#Min element
min_ele=min(bra)
print("Min element is %s" %(min_ele))
repetition=bra.count("IT")
print("IT is repeated %s times" %(repetition))




output:
('CSE', 'IT', 'Mech', 'ECE', 'CSE')
<type 'tuple'>
Size of tuple is: 5
Max element is Mech
Min element is CSE
IT is repeated 1 times
