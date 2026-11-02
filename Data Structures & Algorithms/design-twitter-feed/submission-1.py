
class Twitter:

    def __init__(self):
        # tweets | userID: [(timestamp, tweetID)]
        # following | userID: {followeeIDs}
        self.tweets = {}
        self.following = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []

        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Max heap: (-timestamp, tweetID)
        maxHeap = []

        # Include the user and everyone they follow
        users = {userId}

        for followingId in self.following.get(userId, set()):
            users.add(followingId)

        # Add all their tweets to the heap
        for user in users:
            for timestamp, tweetId in self.tweets.get(user, []):
                heapq.heappush(maxHeap, (-timestamp, tweetId))

        # Retrieve the 10 most recent tweets
        res = []

        for i in range(10):
            if not maxHeap:
                break

            timestamp, tweetId = heapq.heappop(maxHeap)
            res.append(tweetId)

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)
