class Twitter:

    def __init__(self):
        #recency counter
        self.count = 0
        #user and follower map - set for set of following
        self.follow_map = defaultdict(set)
        #user and tweet map - list for list of tweets
        self.tweet_map = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append((self.count, tweetId))
        #negative for max heap
        self.count -= 1 

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        max_heap = []
        self.follow_map[userId].add(userId)
        for followee in self.follow_map[userId]:
            if self.tweet_map[followee]:
                index = len(self.tweet_map[followee]) - 1
                count, tweetid = self.tweet_map[followee][index]
                max_heap.append([count, tweetid, followee, index])
        heapq.heapify(max_heap)
        while max_heap and len(res) < 10:
            count, tweetid, followee, index = heapq.heappop(max_heap)
            res.append(tweetid)
            index -= 1
            if index >= 0:
                count, tweetid = self.tweet_map[followee][index]
                heapq.heappush(max_heap, [count, tweetid, followee, index])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
