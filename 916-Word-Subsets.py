class Solution(object):
    def wordSubsets(self, words1, words2):
        result = []
        c = Counter()
        for i in words2:
            c |= Counter(i)
        for i in words1:
            if not (c-Counter(i)):
                result.append(i)
        return result
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       # result = []
        #for i in words1:
         #   for j in words2:
          #      count = 0
           #     for k in j:
            #        if k in i:
            #            count += 1
            #    if count == len(j):
            #        equals = True
            #if equals == True:
            #    result.append(i)
        #return result















       # result = words1
        #for i in words2:                
           # for k in i:
            #    for j in result:
              #      if len(i) >= len (j) or k not in j:
                    #    result.remove(j)
        #return result