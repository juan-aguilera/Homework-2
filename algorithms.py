#Time complexity O(a*b), a is text len and b is target len.
def sliding_window(Text, Target):

    def matching(Pos, len_target):
        for i in range(0,len_target):
            if Text[Pos + i] != Target[i]:
                return False
        return True
    a = len(Text)
    b = len(Target)
    result = []
    for i in range(0,a-b+1):
        if matching(i,b):
            result.append(i)
    if len(result) > 0: return result
    else: return "target not found" 

def Hashing(): 
#same strings must have same hash value
# same hash values means strings may be same 
#its possible that 2 differente strings have same hash. When that happens, it is know as colission. 




    return    