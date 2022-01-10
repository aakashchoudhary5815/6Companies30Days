def colName (self, n):
    # your code here
    ans = ""
    while n>0:
        r = n%26
        if r == 0:
            ans += 'Z'
            n = (n//26)-1
        else:
            ans += chr((r-1)+ord('A'))
            n = n//26
    return ans[::-1]