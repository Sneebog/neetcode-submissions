class Twitter:

    def __init__(self):
        #hashmap for user id to queue of tweets
        self.user_map = {}
        self.recent_tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_map[userId] = self.user_map.get(userId, set())
        self.recent_tweets.append((userId,tweetId))
        print(self.recent_tweets)

    def getNewsFeed(self, userId: int) -> List[int]:
        i = len(self.recent_tweets) - 1
        user_follows = self.user_map[userId]
        print(user_follows)
        tweets = []
        while i >= 0 and len(tweets) < 10:
            if self.recent_tweets[i][0] in user_follows or self.recent_tweets[i][0] == userId :
                tweets.append(self.recent_tweets[i][1])
            i -= 1
        return tweets



    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_map[followerId] = self.user_map.get(followerId, set())
        self.user_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_map[followerId] = self.user_map.get(followerId, set())
        if self.user_map[followerId] and followeeId in self.user_map[followerId]:
            self.user_map[followerId].remove(followeeId)
