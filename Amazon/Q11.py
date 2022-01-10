def serialize(root, A):
    #code here
   q=[]
   
   A.append(root)
   q.append(root)
   while(q):
       x=q.pop(0)
       if(x.left):
           A.append(x.left)
           q.append(x.left)
       else:
           A.append("N")
       if(x.right):
           A.append(x.right)
           q.append(x.right)
       else:
           A.append("N")
   return(A)

#Function to deserialize a list and construct the tree.   
def deSerialize(A):
    #code here
   q=[]
   d=A[0]
   root=d
   q.append(root)
   n=len(A)
   i=0
   for j in range(1,n,2):
       f=q.pop(0)
       if(A[j]!="N"):
           f.left=A[j]
           q.append(A[j])
       if(A[j+1]!="N"):
           f.right=A[j+1]
           q.append(A[j+1])
           
   return(root)