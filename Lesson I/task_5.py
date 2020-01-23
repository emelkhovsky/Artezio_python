def processing(s1,s2,s3):
    if len(set.intersection(s1, s3)) == len(s3) and len(set.intersection(s2, s3)) == len(s3):
        return True
    return False

s1 = {1,2}
s2 = {2,3}
s3 = {2}
result = processing(s1,s2,s3)
print(result) #True
s4 = {5}
result = processing(s1,s2,s4)
print(result) #False