class Profile:
    # declaring attributes
    username: str
    bio: str
    followers: int
    following: int
    private: bool

    def __init__(self):
        self.username = "user482"
        self.bio = "hi"
        self.followers = 490
        self.following = 408
        self.private = False
