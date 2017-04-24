# mypi.py
# Neftali Rodriguez, 04/19/17

def mypi(n):
    acc=0
    num= (12**(1/2))
    den= (2*n+1)*3**n
    for an in range(n):
        nextn= (num*((-1)**an))
        den= ((2*an+1) * 3**an)
        acc= acc + nextn/den
    return(acc)









# solution must be above this comment

# do not change any part of the code below
def main():
    num = int( input("enter number of terms: ") )
    print("estimate of pi is {0:.10f}".format(mypi(num)))

main()
