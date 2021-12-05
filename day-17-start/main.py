class User:
    def __init__(self,user_id,user_name):
        self.id=user_id
        self.user_name=user_name
        self.followers=0
        self.following=0

    def follow(self,user):
        self.following += 1
        user.followers += 1




user1=User(47,"Nandy")
user2=User(12,"Candy")

user1.follow(user2)

print(user1.followers)
print(user1.following)
print(user2.following)
print(user2.followers)

