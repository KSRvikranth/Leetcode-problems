class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        t=0
        for j in range(0,len(tickets)):
            if(j<=k):
                if(tickets[j]>tickets[k]):
                    t+=tickets[k]
                else:
                    t+=tickets[j]
            else:
                if(tickets[j]>=tickets[k]):
                    t+=tickets[k]-1
                else:
                    t+=tickets[j]
        return t