class Twitter:

    def __init__(self):
        self.time_stamp = 0  
        self.posts = {} # adj list of posts
        self.follower = {} # adj list of set with int


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time_stamp += 1
        post = (tweetId, self.time_stamp)
        if userId not in self.posts:
            self.posts[userId] = [post]
        else:
            self.posts[userId].append(post)

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId in self.follower:
            other_users_to_display = self.follower[userId]
            posts = []
            if userId in self.posts:
                posts = [x for x in self.posts[userId][-10:]]
            for other_user in other_users_to_display:
                if other_user in self.posts:
                    for post in self.posts[other_user][-10:]:
                        posts.append(post)
            posts = sorted(posts, key = lambda x:x[-1])[-10:][::-1]
            return [x[0] for x in posts]
        else:
            if userId in self.posts:
                return [x[0] for x in self.posts[userId][-10:]][::-1]
            else:
                return []



    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follower:
            self.follower[followerId] = set()
            self.follower[followerId].add(followeeId)
        else:
            self.follower[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follower:
            return
        else:
            if followeeId in self.follower[followerId]:
                self.follower[followerId].remove(followeeId)