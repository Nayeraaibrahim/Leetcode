class Solution(object):
    def minOperations(self, boxes):
        result = []
        for i in range(len(boxes)):
                counter = 0
                for j in range(len(boxes)):
                    if boxes[j] == '1':
                        distance = abs(j-i)
                        counter += distance
                result.append(counter)
        return result


        