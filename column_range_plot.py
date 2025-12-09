import numpy as np
import matplotlib.pyplot as plt

def column_range_plot(A, filename="column_ranges.pdf"):
   A=np.array(A)
   ranges = A.max(axis=0) - A.min(axis=0)
   
   plt.bar(range(len(ranges)),ranges)
   plt.xlabel("Column index")
   plt.ylabel("Range")
   plt.title("Column Ranges")
   
   plt.savefig(filename)
   plt.show()
   
   return ranges

