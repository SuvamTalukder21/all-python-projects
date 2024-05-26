import requests

API_KEY = "6QChxgDE1EXsGG8zpjfQqj5D"

response = requests.post(
    "https://api.remove.bg/v1.0/removebg",
    # data={
    #     "image_url": "https://static.showit.co/800/JdptfznbTtebQfqskj-l9Q/123597/portraits-10.jpg",
    #     "size": "auto"
    # },
    files={"image_file": open("nameLogo.png", "rb")},
    data={"size": "auto"},

    headers={"X-Api-Key": API_KEY},
)
if response.status_code == requests.codes.ok:
    with open("no-bg.png", "wb") as out:
        out.write(response.content)
else:
    print("Error:", response.status_code, response.text)
