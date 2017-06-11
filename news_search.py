import webhose

def news_search(keyword):
	webhose.config(token="97029546-2c7f-4116-a16d-e88dd66f09c2")
	r = webhose.search(keyword)
	print(r.total)
	for i in range(10):
		print(r.posts[i].title)
