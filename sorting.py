debug = False #will print out the splitting and recombing of the sorted subarrays if true

def merge_sort(A):
    if len(A) <= 1: 
        if debug: print "Returning single: ", A
        return A
    else:
        middle = len(A)/2
        left  = merge_sort(A[:middle])
        if debug: print 'Found a left : ', left
        right = merge_sort(A[middle:])
        if debug: print 'Found a right: ', right
        return merge_with_no_sent(left, right)
         
#################################################
def merge(A,B): 
    length = len(A) + len(B)
    A.append(1000000000)
    B.append(1000000000)
    i, j = 0, 0
    C = [0]*length
    for k in range(length):
        if (A[i] <= B[j]):
            C[k] = A[i]
            i += 1
        else:
            C[k] = B[j]
            j += 1
    if debug: print 'C: ',C
    return C      
    
    
        
###################################################
def merge_with_no_sent(A,B): 
    length = len(A) + len(B)
    i, j = 0, 0
    C = [0]*length
    for k in range(length):
        #first two control statements check to see if subarrays are 'empty'
        if(i == len(A)):
            C[k:] = B[j:]
            return C
        if(j == len(B)):
            C[k:] = A[i:]
            return C  
        if (A[i] <= B[j]):
            C[k] = A[i]
            i += 1
        else:
            C[k] = B[j]
            j += 1
    if debug: print 'C: ',C
    return C      
    
    
        
###################################################

def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i+1] = key
    return A    
##################################################
def check(A):
    #checks to see that list is in ascending order
    for i in range(len(A)-1):
        if A[i] > A[i + 1]:
            return False
    return True

##################################################
if __name__ == '__main__':
    
    #testing insertion sort
    print 'Testing INSERTION SORT...'
    x = [5,2,4,6,1,3]
    print 'Before: ' , x , '\nSorting...'
    insertion_sort(x)
    print 'Sorted: ', x
    print '---' * 20
    #testing merge
    print 'Testing MERGE SORT...'
    y = [1,6,3,8,5,3,64,8,7,5436,32,542,6,2345,6,2,346,3234]
    print 'Before: ', y, '\nMerging'
    print 'Sorted: ' ,merge_sort(y)
  
    
 
        
