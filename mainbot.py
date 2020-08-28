import tweepy
import os #operating system library
def create_api():
    CONSUMER_KEY = os.getenv('CONSUMER_KEY')    #API key
    CONSUMER_SECRET = os.getenv('CONSUMER_SECRET ')  #API Secret
    ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')  #Generate Access Token
    ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET') #Access Token Secret

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        print('Error creating API', exc_info=True)
        raise e
    print('API created')
    return api
  
 #checked 
import time
def follower_count(user):
    emoji_numbers = {0: "0️⃣", 1: "1️⃣", 2: "2️⃣", 3: "3️⃣",
                     4: "4️⃣", 5: "5️⃣", 6: "6️⃣", 7: "7️⃣", 8: "8️⃣", 9: "9️⃣"}
    uf_split = [int(i) for i in str(user.followers_count)]

    follower_count_list = [int(i) for i in str(user.followers_count)]

    emoji_followers = ''.join([emoji_numbers[j]
                               for j in follower_count_list if j in emoji_numbers.keys()])

    return emoji_followers      # FOLLOWERS IN SMILEYS

api = create_api()

while True:
   # change to your own twitter_handle
    user = api.get_user('Remya__R') #Twitter Username

    api.update_profile(name=f'Remya R|{follower_count(user)} Followers')
    print(f'Updating twitter name: Remya R|{follower_count(user)} Followers')
    print("Waiting to refresh..")
    time.sleep(60)
    
    
                 
              
