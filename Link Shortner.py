import pyshorteners

link = "https://github.com/TanmayProgrammer-13/Python-Projects-For-Begginers/blob/main/Link%20Shortner%20Python"

shortener = pyshorteners.Shortener()

x = shortener.tinyurl.short(link)

print(x)
