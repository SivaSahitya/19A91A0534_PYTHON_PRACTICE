class Faculty:
   def __init__(self,n,s):
     self.name=n;
     self.sub=s;
   def print_details(self):
     print("name=",self.name)
     print("subject=",self.sub)
ob=Faculty("Devipriya","python")
ob.print_details()

"""
output:
name= Devipriya
subject= python
"""
