 import webhoseio

    webhoseio.config(token="97029546-2c7f-4116-a16d-e88dd66f09c2")
    output = webhoseio.query("filterWebContent", {"q": search-terms " language:english"})
    print output['posts'][0]['text'] # Print the text of the first post
    print output['posts'][0]['published'] # Print the text of the first post publication date

    
# Get the next batch of posts

    output = webhoseio.get_next()

    
# Print the site of the first post

    print output['posts'][0]['thread']['site']
