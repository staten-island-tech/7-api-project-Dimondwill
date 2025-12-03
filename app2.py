import requests

def Munster():
    res = requests.get(f"https://www.dnd5eapi.co/api/2014/monsters")

    if res.status_code != 200:
        print("Error fetching data!")
        return None

    data = res.json()
    return {
        "name": data["name"],
        "index": data["index"],
        "url": data["url"]
    }
m = Munster("aboleth")
print(m)