def binary(n):
    bin = []
    while n > 0:
        r = n%2;
        n = n/2
        if(n == 2):
            bin.append(1)
        else:
            bin.append(r)
    return bin

n = int(input())
bin = binary(n)
for i in bin:
    print(i)
