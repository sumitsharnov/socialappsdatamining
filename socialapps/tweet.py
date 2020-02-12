import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


class StdOutListener(StreamListener):
    def on_data(self, data):
        print(data)

    def on_error(self, status):
        print(status)


if __name__ == "__main__":
    listener = StdOutListener()
    auth = OAuthHandler("QOxdmel4EARpDA6fsPIYAHwLA", "EkasuWmyiAGMkWITMmV5VxQnWvZqjOaMZ3p0wz6X5J80Y6kt7v")
    auth.set_access_token("288147314-1y6bx7wCXjICJibYPKs99akCJH4RQdgLpVwUuuFg", "tiSf18RQnVLx0ZFv85VJrLbdToAoZM7LDaroBm2upjE8P")
    api = tweepy.API(auth)
    try:
        api.update_status("Hello tweepy")


    except:
        print("duplicate")
    new_tweets = api.user_timeline(count=200)
    print(new_tweets)
    stream = Stream(auth, listener)
    message = "I am sumit"

