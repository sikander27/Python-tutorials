import requests

data = [
    {
        "city": "Mumbai",
        "products": [
            {
                "name": "Watch",
                "price": "20"
            },
            {
                "name": "Belt",
                "price": "540"
            },
            {
                "name": "wallet",
                "price": "15"
            }
        ]
    }
]
def score(url=None):
    response = requests.get(url)
    data = response.json()
    top_3_posts = {}
    for i in data:
        top_posts = sorted(i["products"], key=lambda x: x["price"], reverse=True)
        top_3_posts[i["city"]] = [(i["name"], i["price"]) for i in top_posts[:3]]

    return top_3_posts


print(score())