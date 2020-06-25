def is_palindrome(x):
    y=x.split()
    z="".join(y)
    z=z.lower()
    print(z)
    if(z==z[::-1]):
        return True
    else:
        return False

#print(is_palindrome("a car a man a maraca"))
