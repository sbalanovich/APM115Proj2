#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "119164372-Sdkc00ZrCxaETE3bG4L1vkbfgkmmEnCqNMVRb3i0"
access_token_secret = "V9uWmSO8pZV9eF5opMXhBpj0ILK2XI3NHjIKlknoAbVUv"

consumer_key = "KBx5ff3Km0q8s7ESa7G6ZWWcE"
consumer_secret = "QPb59eocVqHorI6pVttmr6kzx6bgeBh1Hso1r3avZIrZJjiU6y"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print "Peppa"
        print data
        return True

    def on_error(self, status):
        print "Salt"
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    wyoming = [-111, 41, -104, 45]

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(locations=wyoming, track=['feelthebern', 'bernie', 'sanders', 'berniesanders', 'bernie2016', 'clinton', 'hillaryclinton', 'imwithher', 'hillary2016', ])