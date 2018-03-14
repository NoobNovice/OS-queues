import matplotlib.pyplot as plt
import numpy as np

class Graph:

    def graph(page_fault, algorithm_name):
        plt.xlabel('number of frame')
        plt.ylabel('number of page fault')
        plt.title(algorithm_name)
        plt.grid(True)
        plt.ylim(10, 50)
        plt.xlim(3, 10)

        # line1
        y1 = page_fault[0]
        x1 = np.arange(0, len(page_fault[0]))
        plt.plot(x1, y1)
        # line2
        y2 = page_fault[1]
        x2 = np.arange(0, len(page_fault[1]))
        plt.plot(x2, y2)
        # line3
        y3 = page_fault[2]
        x3 = np.arange(0, len(page_fault[2]))
        plt.plot(x3, y3)

        plt.legend(['DataSet1', 'DataSet2', 'DataSet3'], loc='upper left')
        plt.savefig(algorithm_name)
        plt.show()
        print("\n")
        return

# def paintGraph(dataSet,pngName):
#     print(pngName)
#     plt.xlabel('process')
#     plt.ylabel('waiting time (milisec)')
#     plt.title('Average wait time')
#     plt.grid(True)
#
#     #FCFS drawing line
#     y1 = FCFS(dataSet)
#     x1 = np.arange(0, len(y1), 1)
#     plt.plot(x1,y1)
#     #SJF drawing line
#     y2 = SJF(dataSet)
#     x2 = np.arange(0, len(y2), 1)
#     plt.plot(x2, y2)
#     #RB drawing
#     y3 = RB(10,dataSet)
#     xB = np.arange(0,len(y3),1)#add this because number of process has unstable
#     plt.plot(xB,y3)
#     plt.legend(['FCFS', 'SJF', 'BR'], loc='upper left')
#     plt.savefig(pngName)
#     plt.show()
#     print("\n")
#     return