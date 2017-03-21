

def pos_neg(a, b, negative):
    """
    :type a: int
    :type b: int
    :type negative: str
    """
    if a<0 and b>0 and negative==False:
        pos_neg(a,b,negative)= True
    elif a>0 and b<0 and negative==True:
        pos_neg(a, b, negative)= False
    elif a+b>0 and negative==False:
        pos_neg(a,b,negative)=False
    else:
        pos_neg(a,b,negative)=True

    return pos_neg(a,b,negative)
# Expected outputs:

print(pos_neg(1, -1, False))
# True
print(pos_neg(-1, 1, False))
# True
print(pos_neg(-4, -5, True))
# True
print(pos_neg(-2, -5, False))
# False
print(pos_neg(1, 2, False))
# False
