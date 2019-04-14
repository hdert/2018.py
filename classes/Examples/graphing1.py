import matplotlib.pyplot as plt

year = [1950, 1970, 1990, 2010, 2020, 2030, 2040, 2050, 2060, 2070, 2080, 2090, 2100]
pop = [2.519, 3.692, 5.263, 6.972, 7.123, 7.456, 8.342, 9.123,
       10.326, 10.556, 10.881, 11.204, 11.442]

#plt.plot(year, pop)
#plt.show()

plt.scatter(year, pop)
#plt.show()

#plt.bar(year, pop)
plt.show()
