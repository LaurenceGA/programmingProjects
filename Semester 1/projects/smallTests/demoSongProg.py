songSize = 4.5 #each song is 4.5MB in size

name = input("What's your name?")
playerSize = input("What size is your music player (GB): ")

numOfSongs = float(playerSize) * 1024 // songSize
spaceLeft = float(playerSize) * 1024 % songSize

print("Hi %s" % name)
print("You could fit %d 4.5MB songs in your player." % numOfSongs)
print("You would have %.1f MB left." % spaceLeft)