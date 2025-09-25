#info2 | Buzzfeed_Quiz.py

#Header Image
intro_pic = "Images/IntroPic.jpg"

Character_Options = ["Belly", "Conrad", "Jeremiah", "Steven", "Taylor", "Laurel"]

#Character Images (for Sidebar)
belly_pic = "Images/Belly.jpg"
conrad_pic = "Images/Conrad.jpg"
jeremiah_pic = "Images/Jeremiah.jpg"
steven_pic = "Images/Steven.jpg"
taylor_pic = "Images/Taylor.jpg"
laurel_pic = "Images/Laurel.jpg"

#Results
Results = {
    "Belly": {
        "name": "Belly 🐚",
        "image": "Images/Belly.jpg",
        "description": "Romantic, heart-first mindset, and currently growing into your own person.",
    },
    "Conrad": {
        "name": "Conrad 🩺",
        "image": "Images/Conrad.jpg",
        "description": "Reserved, deeply loyal, and actions over words.",
    },
    "Jeremiah": {
        "name": "Jeremiah 👩🏻‍🍳",
        "image": "Images/Jeremiah.jpg",
        "description": "Spontaneous, fun, and big‑hearted.",
    },
    "Steven": {
        "name": "Steven 🎮",
        "image": "Images/Steven.jpg",
        "description": "Sarcastic, competitive, but always there for your people.",
    },
    "Taylor": {
        "name": "Taylor 🌟",
        "image": "Images/Taylor.jpg",
        "description": "Trendy, loyal, and unafraid to speak your mind.",
    },
    "Laurel": {
        "name": "Laurel 📖",
        "image": "Images/Laurel.jpg",
        "description": "Grounded, wise, and quietly caring to those you love.",
    },
}

#Scoreing system
def add(points, scores):
    for k, v in points.items():
        scores[k] = scores.get(k, 0) + v

#Question 1
def score_q1(choice, scores):
    mapping = {
        "Quiet sunrise read on the sand": {"Conrad": 2, "Laurel": 2},
        "Competitive beach volleyball with friends": {"Steven": 2, "Jeremiah": 2},
        "Long solo swim—just thinking": {"Conrad": 2, "Belly": 1},
        "Boardwalk snacks + photos + shopping": {"Taylor": 2, "Jeremiah": 1},
        "Family cookout—everyone invited!": {"Laurel": 2, "Belly": 1, "Steven": 1},
    }
    add(mapping.get(choice, {}), scores)

#Question 2
def score_q2(choice, scores):
    mapping = {
        "Indie melancholic": {"Conrad": 2, "Belly": 1},
        "Upbeat pop": {"Jeremiah": 2, "Taylor": 2},
        "Classic rock": {"Steven": 2, "Laurel": 1},
        "R&B slow jams": {"Belly": 2, "Jeremiah": 1},
        "Acoustic coffeehouse": {"Laurel": 2, "Conrad": 1},
    }
    add(mapping.get(choice, {}), scores)

#Question 3
def score_q3(value, scores):
    if value <= 3:
        add({"Laurel": 2, "Conrad": 1}, scores)
    elif value <= 6:
        add({"Belly": 1, "Steven": 1}, scores)
    else:
        add({"Jeremiah": 2, "Taylor": 1}, scores)

#Question 4
def score_q4(choices, scores):
    for x in choices:
        if x == "Bonfire storytelling":
            add({"Laurel": 2, "Belly": 1}, scores)
        elif x == "Night swim":
            add({"Conrad": 1, "Belly": 1, "Jeremiah": 1}, scores)
        elif x == "Beach volleyball league":
            add({"Steven": 2, "Jeremiah": 1}, scores)
        elif x == "Photo walk for the aesthetic":
            add({"Taylor": 2, "Belly": 1}, scores)
        elif x == "Cooking for everyone":
            add({"Laurel": 2, "Steven": 1}, scores)
        elif x == "Solo journaling":
            add({"Conrad": 2, "Belly": 1}, scores)

#Question 5
def score_q5(value, scores):
    if value >= 8:
        add({"Laurel": 2, "Conrad": 1}, scores)
    elif value >= 5:
        add({"Belly": 1, "Steven": 1}, scores)
    else:
        add({"Jeremiah": 1, "Taylor": 1}, scores)

