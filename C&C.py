import instabot
bot = Bot()
bot.login(username="nottheoffice.co", password="Armyscout1317")

my_followers = bot.followers()

print(my_followers)

image = "cat.com"

bot.upload_photo(image, caption = "yayayay")
#this lets you upload a photo with a caption and image is a url of a photo

getAllPosts = bot.get_your_medias()

for post in getAllPosts:
    print (bot.get_your_medias(post))
