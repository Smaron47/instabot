import time
import instagrapi 
from random import choice
user='A_fielex'
pas='Arielfielex'
client = instagrapi.Client()



hashtags = open("hashtags.txt", "r")
hashtags=(hashtags.read().replace("#","")).split("\n")
comments=open("comments.txt", "r")
comments=(comments.read().replace("-","")).split("\n")
accounts=open("accounts.txt", "r")
accounts=accounts.read().split("\n")
print(len(accounts))
duration = int(input("Enter the duration runtime of program (in minutes do not enter more than 120 min ) : "))
end_time = time.time() + duration * 60


im=0
while time.time() < end_time:
    try:
        ch=choice(accounts)
        ch=eval(ch)
        hashtag=choice(hashtags)
        comment=choice(comments)
        time.sleep(13)
        client.login(ch[0],ch[1])
        r=[24,20,28,31,33,37,67,54]
        top_posts = client.hashtag_medias_recent_v1(hashtag, amount=100)

        # Sort all the posts by date
        all_posts = sorted(top_posts, key=lambda post: post.taken_at, reverse=True)

        print(all_posts[0])
        for i,media in enumerate(all_posts):
            if i==4:
                break
            client.media_like(media.id)
            print(f"Liked {media.code}")
            time.sleep(4)
            client.media_comment(media.id,comment)
            print(f"Liked post number: {i+1} of {media.code}, Comment: {comment} , Hashtags: {hashtag}")
            time.sleep(choice(r))
            print("Time Stoped For FeW moment")
        client.logout()
        print("logged out")
        time.sleep(choice(r))
    except:
        print(f"Please remove or add new account {ch[0]} {ch[1]} Or Change password")
        try:
            client.logout()
        except:
            pass
        time.sleep(5)
        pass

#print(hashtags, comments)


print("Program has completed the specified duration and will now exit.")


"""
import time

# get the duration in minutes from the user

# calculate the end time
print(end_time)
# run the program for the specified duration
while time.time() < end_time:
    print(time.time())
    time.sleep(1)
    pass
"""

"""
from instapy import InstaPy
from instapy.util import smart_run

# Create a new instance of InstaPy
session = InstaPy(username='A_fielex', password='ArielFielex')

# Login to your Instagram account
with smart_run(session):
    session.login()

    # Set the hashtag to search for
    hashtags = ["vancouverevents"]

    # Like and comment on posts with the specified hashtags
    session.like_by_tags(hashtags, amount=3)
    session.set_do_comment(True, percentage=50)
    session.set_comments(['Nice one!', 'Love it!', 'Great post!'])
    session.set_comment_emoji(['❤️', '👍', '😊'])
    session.join_pods()
    
    # Logout of your Instagram account
    session.end()
"""

"""from instabot import Bot
import random,time

# create a new bot instance
bot = Bot()

# login to Instagram
bot.login(username='A_fielex', password='Fiverr')


# set the hashtag you want to interact with
hashtag = "travel"

# get the posts using the hashtag
posts = bot.get_hashtag_medias(hashtag)

i=0


# loop through the posts and like/comment on each one
for post in posts:
    # like the post
    print(post)
    r=[24,20,28,31,33,37,67,54]
    bot.like(post)
    time.sleep(9)


    # generate a random comment from a list of comments
    comments = ["Great post!", "Love it!", "Amazing!", "Awesome!"]
    comment = random.choice(comments)

    # comment on the post
    bot.comment(post, comment)
    if i==5:
        break
    i=i+1
    time.sleep(random.choice(r))
# logout of Instagram
bot.logout()"""
