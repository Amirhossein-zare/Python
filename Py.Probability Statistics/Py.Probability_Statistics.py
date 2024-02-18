import matplotlib.pyplot as plt 
partision = 'Riazy', 'Game', 'Varzesh'
sizes = [200, 400, 100]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=partision, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')
plt.show()
