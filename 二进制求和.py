def addBinary(a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        rev=0
        res=""
        zero="0"
        one="1"
        i=len(a)-1
        j=len(b)-1
        while i>=0 or j>=0:
            if i<0:
                num1="0"
            else:
                num1=a[i]
            if j<0:
                num2="0"
            else:
                num2=b[j]
            if num1==one and num2==one and rev:
                rev=1
                res=one+res
            elif rev:
                if num1==zero and num2==zero:
                    rev=0
                    res=one+res
                else:
                    rev=1
                    res=zero+res
            else:
                if num1==one and num2==one:
                    rev=1
                    res=zero+res
                elif num1==zero and num2==zero:
                    rev=0
                    res=zero+res
                else:
                    rev=0
                    res=one+res
            i-=1
            j-=1
        if rev:
            res=one+res
        return res

a=addBinary('1111','1001')
print(a)