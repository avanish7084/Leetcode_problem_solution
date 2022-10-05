class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        s=sum(distance)
        if start<destination:
            d1=sum(distance[start:destination ])
        else:
            d1=sum(distance[destination:start])
        d2=abs(s-d1)
        if d1>d2:
            return d2
        return d1