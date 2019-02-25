import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,100)
y = x*2
z = x**2

fig = plt.figure()
axis1 = fig.add_axes([0.1,0.1,0.8,0.8])
axis1.plot(x,y)
axis1.set_title('title')
axis1.set_ylabel('y')
axis1.set_xlabel('x')


fig2 = plt.figure()
axis2 = fig2.add_axes([0.1,0.1,0.8,0.8])
axis3 = fig2.add_axes([0.2,0.5,.2,.2])
axis2.plot(x,y)
axis3.plot(x,y)
axis2.set_ylabel('y')
axis2.set_xlabel('x')
axis3.set_ylabel('y')
axis3.set_xlabel('x')

fig3 = plt.figure()
axis5 = fig3.add_axes([0.1,0.1,0.8,0.8])
axis4 = fig3.add_axes([0.2,0.5,.3,.3])
axis4.plot(x,y)
axis5.plot(x,z)
axis4.set_ylim([30,50])
axis4.set_xlim([20,22])
axis5.set_ylim([0,10000])
axis5.set_xlim([0,100])
axis4.set_title('zoom')
axis4.set_ylabel('y')
axis4.set_xlabel('x')
axis5.set_ylabel('z')
axis5.set_xlabel('x')


fig4, ax = plt.subplots(nrows=1,ncols=2)
ax[0].plot(x,y, color='blue', ls='--', lw=3)
ax[1].plot(x,z, color='red',lw=3)


fig5, axis = plt.subplots(nrows=1,ncols=2,figsize=(12,2))
axis[0].plot(x,y, color='blue', ls='--', lw=3)
axis[1].plot(x,z, color='red',lw=3)

plt.tight_layout()

plt.show()



# fig, ax = plt.subplots(figsize=(12, 6))
#
# ax.plot(x, x +
# ax.plot(x, x + 6, color="green", lw=3, ls='-.')
# ax.plot(x, x + 7, color="green", lw=3, ls=':')
#
# # custom dash
# line, = ax.plot(x, x + 8, color="black", lw=1.50)
# line.set_dashes([5, 10, 15, 10])  # format: line length, space length, ...
#
# # possible marker symbols: marker = '+', 'o', '*', 's', ',', '.', '1', '2', '3', '4', ...
# ax.plot(x, x + 9, color="blue", lw=3, ls='-', marker='+')
# ax.plot(x, x + 10, color="blue", lw=3, ls='--', marker='o')
# ax.plot(x, x + 11, color="blue", lw=3, ls='-', marker='s')
# ax.plot(x, x + 12, color="blue", lw=3, ls='--', marker='1')
#  1, color="red", linewidth=0.25)
# ax.plot(x, x + 2, color="red", linewidth=0.50)
# ax.plot(x, x + 3, color="red", linewidth=1.00)
# ax.plot(x, x + 4, color="red", linewidth=2.00)
#
# # possible linestype options ‘-‘, ‘–’, ‘-.’, ‘:’, ‘steps’
# ax.plot(x, x + 5, color="green", lw=3, linestyle='-')
# # marker size and color
# ax.plot(x, x + 13, color="purple", lw=1, ls='-', marker='o', markersize=2)
# ax.plot(x, x + 14, color="purple", lw=1, ls='-', marker='o', markersize=4)
# ax.plot(x, x + 15, color="purple", lw=1, ls='-', marker='o', markersize=8, markerfacecolor="red")
# ax.plot(x, x + 16, color="purple", lw=1, ls='-', marker='s', markersize=8,
#         markerfacecolor="yellow", markeredgewidth=3, markeredgecolor="green")
plt.show()
