def checkString(s):
    # write your code here
    s=s.lower()
    vowels=['a','e','i','o','u']
    vov=[]
    const=[]
    for i in s:
        if i in vowels:
            vov.append(i)
        elif i.isalpha():
            const.append(i)
    a=len(vov)
    b=len(const)
    if a < b:
        print("No")
    elif a>b:
        print("Yes")
    else:
        print("Same")