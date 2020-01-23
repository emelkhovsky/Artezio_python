def processing(S):
    new_s = S[0]
    for i in range(1, len(S)):
        if S[i-1] == ' ':
            new_s += S[i].upper()
        else:
            new_s += S[i].lower()
    return new_s

S = 'Asd 11fAAf fD df'
new_s = processing(S)
print(new_s) #Asd 11faaf Fd Df

