class MedianFinder:

    def __init__(self):
        #two heaps for each half 
        #max heap
        self.first_half = []
        #min heap
        self.second_half = []

    def addNum(self, num: int) -> None:
        #append to first_half if smaller then max of lower half
        
        if self.first_half: 
            if num < -(self.first_half[0]):
                #negative because of max heap
                heapq.heappush(self.first_half, -num)
                self.heap_size_adjust()
            else:
                #positve because of min heap
                heapq.heappush(self.second_half, num)
                self.heap_size_adjust()
        else:
            heapq.heappush(self.first_half, -num)
        

    def heap_size_adjust(self) -> None:
        #adjust half sizes using heap pushes
        l1 = len(self.first_half)
        l2 = len(self.second_half)
        if l1 > l2 + 1:
            num = -(heapq.heappop(self.first_half))
            heapq.heappush(self.second_half, num)
        elif l2 > l1 + 1:
            num = -(heapq.heappop(self.second_half))
            heapq.heappush(self.first_half, num)

    def findMedian(self) -> float:
        l1 = len(self.first_half)
        l2 = len(self.second_half)
        print(l1, l2)
        #even array
        if (l1 + l2) % 2 == 0:
            #return the middle division
            return ((-(self.first_half[0]) + self.second_half[0]) / 2)
        else:
            if l1 > l2:
                return -(self.first_half[0]) 
            else:
                return self.second_half[0]
        