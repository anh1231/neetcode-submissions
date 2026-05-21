class Twitter:

    def __init__(self):
        self.followers = defaultdict(dict)
        self.feed = deque()

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.feed.append([userId, tweetId])
        if userId not in self.followers:
            self.followers[userId][userId] = 1

    def getNewsFeed(self, userId: int) -> List[int]:
        current_feed = self.feed.copy()
        res = []
        if not current_feed:
            return res
        count = 10
        while count and current_feed:
            user, tweet = current_feed.pop()
            if user in self.followers[userId]:
                if self.followers[userId][user] == 1:
                    res.append(tweet)
                    count -= 1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId][followeeId] = 1

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId and followeeId in self.followers[followerId]:
            self.followers[followerId].pop(followeeId)
