#Google Search Using Python
try:
	from googlesearch import search

except ImportError:
	print("No Module Found 'google'")

#Searching Query
query = "Python"

for i in search(query,tld="co.in",num=10,stop=10,pause=2):
	print(j)
