import webbrowser
import json
from urllib.request import urlopen


print("hello")
site = input("url: ")
era = input("date like 20150613: ")
url = f"http://archive.org/wayback/available?url={site}&timestamp={era}"

try:
    response = urlopen(url)
    contents = response.read()
    text = contents.decode("utf-8")
    data = json.loads(text)

    old_site = data["archived_snapshots"]["closest"]["url"]
    print("Found: ", old_site)
    print("Appear!")
    webbrowser.open(old_site)
except json.JSONDecodeError as e:
    print("JSON", e)
except KeyError:
    print("No archived")
except Exception as e:
    print("An erroe")


#https://www.youtube.com/

