# A simple Python3 program to find
# maximum score that
# maximizing player can get
import math

def maxmin(curDepth, nodeIndex, isMax, scores, targetDepth):
    # best care : targetDepth reached
    if curDepth == targetDepth:
        return scores[nodeIndex]

    if isMax:
        return max(maxmin(curDepth + 1, nodeIndex * 2, False, scores, targetDepth),
            maxmin(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth))
    else:
        return min(maxmin(curDepth + 1, nodeIndex * 2, True, scores, targetDepth),
            maxmin(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth))
    

# Driver code

scores = [3, 5, 2, 9, 12, 5, 23, 23]

treeDepth = math.log(len(scores), 2)

print("The optimal value is : ", end = "")
print(maxmin(0,0, True, scores, treeDepth))