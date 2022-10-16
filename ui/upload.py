import pandas as pd
import sqlite3
import sys

df = pd.read_csv(sys.argv[1])
db = sqlite3.connect("data.db")
cu = db.cursor()

show = {
	"id": 35760,
	"name": "Shingeki no Kyojin Season 3",
	"img": "https://cdn.myanimelist.net/images/anime/1173/92110.jpg",
	"desc": """Still threatened by the "Titans" that rob them of their freedom, mankind remains caged inside the two remaining walls. Efforts to eradicate these monsters continue; however, threats arise not only from the Titans beyond the walls, but from the humans within them as well.

After being rescued from the Colossal and Armored Titans, Eren Yaeger devotes himself to improving his Titan form. Krista Lenz struggles to accept the loss of her friend, Captain Levi chooses Eren and his friends to form his new personal squad, and Commander Erwin Smith recovers from his injuries. All seems well for the soldiers, until the government suddenly demands custody of Eren and Krista. The Survey Corps' recent successes have drawn attention, and a familiar face from Levi's past is sent to collect the wanted soldiers. Sought after by the government, Levi and his new squad must evade their adversaries in hopes of keeping Eren and Krista safe.

In Shingeki no Kyojin Season 3, Eren and his fellow soldiers are not only fighting for their survival against the terrifying Titans, but also against the terror of a far more conniving foe: humans.
""",
	"members": 3001460,
    "ranked": 76,
    "rating": 7.8,
}


cu.execute("INSERT INTO shows (id, name, desc, img, members, ranked, rating) VALUES (?, ?, ?, ?, ?, ?, ?)", (show["id"], show["name"], show["desc"], show["img"], show["members"], show["ranked"], show["rating"]))
for idx, row in df.iterrows():
    cu.execute("INSERT INTO reviews (show_id, review, author, rating, old) VALUES (?, ?, ?, ?, ?)", (row.anime_id, row.review_text, row.author_username, row.classified, row.review_rating))

db.commit()
