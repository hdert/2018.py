import numpy as np
import matplotlib.pyplot as plt

ay = [1993,1994,1995,1996,1997,1998,
     1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013]
average_year = np.array(ay)

at = [11.84,12.33,12.59,12.45,12.27,13.41,13.35,12.79,12.9,12.67,12.62,12.17,
     13.11,12.4,12.67,12.86,12.29,13.07,12.83,12.45,13.33]
average_temp = np.array(at)

sy = [1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,
      2007,2008,2009,2010,2011,2012,2013]
sea_year = np.array(sy)

st = [22.9843,22.1622,21.9661,21.8135,21.1279,22.1117,20.8799,21.2933,22.6084,
      21.4905,21.3952,23.1089,21.6462,24.1099,22.1351,21.7013,21.989,20.9917,
      23.1961,23.3739,21.491]
sea_temp = np.array(st)

plt.plot(average_year, average_temp, color = "darkblue")

plt.plot(sea_year, sea_temp, color = "red")

plt.title("Average Temperature Nz (Blue) and Average Sea Temperature Nz (Red)")
plt.xlabel("Year")
plt.ylabel("Temperature")
plt.show()
