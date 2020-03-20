""" Virtual Assitant """
### wikipediaapi and wolframalpha combine
import wolframalpha
import wikipediaapi

while True:
    ip = input("Question: ")

    try:
        # wolframe
        app_id = 'api-token'
        client = wolframalpha.Client(app_id)
        result = client.query(ip)
        ans = next(result.results).text
        print(ans)
    except:
        # wikipediaapi
        wiki_wiki = wikipediaapi.Wikipedia('en')
        page_py = wiki_wiki.page(ip.title())
        if page_py.exists():
            print(page_py.summary)

