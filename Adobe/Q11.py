def amendSentence(self, s):

    # code here
    ans, temp = "", ""
    ans += s[0].lower()
    for i in range(1,len(s)):
        if s[i].isupper():
            ans += temp
            ans += ' '
            temp = ""
            ch = s[i].lower()
            temp += ch
        else:
            temp += s[i]
    ans += temp
    return ans