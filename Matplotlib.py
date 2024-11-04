import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [85,87,83,86,85]
plt.plot(x,y)
plt.title("Performance report")
plt.xlabel("Semester number")
plt.ylabel("percentage of marks")
plt.show()

import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [25,87,53,36,95]
plt.bar(x,y)
plt.title("Performance report")
plt.xlabel("Semester number")
plt.ylabel("percentage of marks")
plt.show()

import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [85,87,83,86,85]
plt.scatter(x,y)
plt.title("Performance report")
plt.xlabel("Semester number")
plt.ylabel("percentage of marks")
plt.show()

import matplotlib.pyplot as plt
x = [1,2,4,5,2,5]
plt.hist(x, bins = [1,2,3,4,5,6])
plt.title("Histogram")
plt.legend("bar")
plt.show()

import matplotlib.pyplot as plt
x = [1,2,3,4]
e = (0,0,0.1,0)
plt.pie(x, explode = e)
plt.title("pie chart")
plt.show()

import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [10,2,50,200,80]
z = [1,2,5,9,3]
fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.plot3D(z,y,x)
