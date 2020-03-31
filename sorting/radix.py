#Mistake: copied into the terminal
# Source: https://stackoverflow.com/questions/33901534/radix-sort-program-in-python

def RadixSort(A):
    RADIX = 10
    maxLength = False
    tmp , placement = -1, 1

    while not maxLength:
        maxLength = True
        buckets = [list() for _ in range(RADIX)]
        for  i in A:
            tmp = int(i / placement) # two mistakes: 1) should explicitly make int. 2) Should read the error in the terminal when debugging
            buckets[tmp % RADIX].append(i)
            if maxLength and tmp > 0:
                maxLength = False

        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                A[a] = i
                a += 1
        # move to next digit
        placement *= RADIX
    return A
A = []
n = input("Enter the numebr of elements you want to sort : ")
n = int(n)
print("Enter the numbers : \n")
for i in range(0, n):
    num = int(input())
    A.append(num)
print(RadixSort(A))
