while (True):
    try:
        h=int(input("Height: "))
        
    except ValueError:
        print("Enter integer only.")

    if h>8 or h<1:
        print("Enter integer between 0 to 8")
        continue

    def patten(h):
        i =h-1
        k=h
        n=0
        while i>=n:
            print(i*" ",end='')
            while k>i:
                print((k-i)*"#")
                break
            i-=1
        return 0

    patten(h)
