# The purpose of this module is to query for the presidents of the United States from DuckDuckGo.

import requests


def president_search():
    url = 'https://duckduckgo.com/'
    query = "presidents of the united states"
    response = requests.get(url, params= {'q': query, "format": "json"})
    data = response.json()

    list_of_presidents = []
    for i in range(len(data["RelatedTopics"])):
        list_of_presidents.append(data["RelatedTopics"][i]["Text"])
    print(list_of_presidents)
    return list_of_presidents


president_search()
