#MP1-Python
import matplotlib.pyplot as plt
n = 0
val = []
while n <=99:
    xn = n
    if xn >= 10:
        while xn >= 10:
            z = xn - 10
            xn = z
            if xn < 0: 
               xn = 0
        val.append(xn)
    if xn <= 9:
        y = xn**2 - 7
        val.append(y)
    n = n + 1
plt.xlim(None,100)
plt.stem(val,use_line_collection=True)
plt.xlabel('n')
plt.ylabel('f(n)')
plt.show()

#   The pieace-wise function is a periodic function beacause any number
# greater than 9 will always be reduced by 10 until it satisfies the upper
# condition of being less than or equal to 9.
