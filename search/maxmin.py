# A simple Python3 program to find
# maximum score that
# maximizing player can get

from audioop import minmax
import math

def maxmin(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    # best care : targetDepth reached
    if curDepth == targetDepth:
        return scores[nodeIndex]

    if maxTurn:
        return max(minmax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth),
            minmax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth))
    else:
        return min(minmax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth),
            minmax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth))
    

# Driver code

scores = [3, 5, 2, 9, 12, 5, 23, 23]

treeDepth = math.log(len(scores), 2)

print("The optimal value is : ", end = "")
print(maxmin(0,0, True, scores, treeDepth))