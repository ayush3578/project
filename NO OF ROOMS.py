
import matplotlib.pyplot as plt
  
ROOMS = ['UNDER MAINTENANCE', 'EMPTY', 'OCCUPIED', ]
  
slices = [3, 50, 80]
  
colors = ['r', 'y', 'g']
  
plt.pie(slices, labels = ROOMS, colors=colors, 
        startangle=90, shadow = True, explode = (0, 0, 0.1),
        radius = 1.2, autopct = '%1.1f%%')
  
plt.legend()
  
plt.show()
