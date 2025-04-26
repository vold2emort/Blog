from django.shortcuts import render
from datetime import date
# Create your views here.

all_posts = [
    {
        "slug": "average-day-nepal",
        "image": "mountains.jpg",
        "author": "Pramish",
        "date": date(2025, 4, 15),
        "title": "Nepal, Mountain and Me",
        "excerpt": """Living in Nepal: Where Mountains Are Just Background Noise 🌄 | Yeti is My Homeboy 🐾
You think hiking is tough? Buddy, I live surrounded by mountains — they're basically my backyard. 🏡⛰️ The Yeti and I are on a first-name basis (he still owes me lunch, by the way).Climbing Mount Everest? Pfft. Took me 5 minutes last weekend — would've been 4 if I hadn’t stopped for selfies📸.""",
        "content": """Living in Nepal is basically like living in a giant outdoor gym, except the equipment is mountains and the personal trainers are Yetis. 🏔️ No big deal — the Himalayas are just my front yard. The Yeti? Absolute bro. We trade life advice over cups of butter tea. Honestly, climbing Mount Everest is just part of my morning warm-up routine. Takes about five minutes, seven if I’m feeling lazy. People make a big deal out of it, but really, it's just a mildly inconvenient staircase at this point.

One time, while casually playing football, I kicked the ball so hard it launched itself into orbit and crash-landed somewhere near the summit of Everest. Naturally, I had to jog up there, grab the ball, and still made it back before my friends noticed. They were too busy arguing about who should be goalie. It’s a hard life, being this legendary — but somebody’s gotta do it. 😂

Sometimes, when my little brother and I get bored, we spice things up by jumping from one mountain to another. 🏔️🦘 It's our version of "long jump," but with, you know, a little more altitude. Pretty sure NASA wants to study us, but we're busy setting unofficial world records in our backyard. No biggie.

When I feel like swimming, I don't bother with pools — that's for amateurs. I just grab my goggles, hike up Everest, and use the summit as a diving board. 🏊‍♂️ People in the West are bragging about "cold showers" for mental toughness, meanwhile kids here are sprinting barefoot in underwear around glaciers for fun. ❄️ David Goggins would be like a regular two-year-old in these mountains — cute effort, Dave. Try harder.

Oh, and about that time I raced The Flash? 🏃‍♂️⚡Yeah, he thought he could outrun me until he slipped on some snow halfway through. I casually jogged past him, waved, and still finished a mile ahead. Poor guy never stood a chance — hope he's recovering well. 😌

But hey, all jokes aside — life in Nepal is absolutely amazing. 🌄 The mountains, the people, the culture — it's not about crazy stunts or superhero races (usually). It's about waking up every day surrounded by the most breathtaking views on Earth, sharing laughter with friends, and feeling at home where the sky kisses the land. ❤️"""
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Pramish K.C",
        "date": date(2025, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": """You say coding builds character — mostly because I spend 90% of my time arguing with a semicolon. 👨‍💻 Every "easy" bug turns into a three-hour emotional journey. Applying logic? Bro, sometimes even my if statements have trust issues. 🤡 I don’t always fix bugs, but when I do, it's by accident. Still waiting for my code to run perfectly on purpose someday.""",
        "content": """Every time I open my code editor, it's like stepping into a different dimension where I have no idea what's happening, but somehow I’m still the main character. 💻✨ I type things, magic happens (or errors happen — mostly errors), and I just vibe with it. They say you should "understand" your code... I'm more into "trusting the process" and hoping for the best.

Debugging is a spiritual experience. 🔍 One second I'm fixing a missing bracket, the next second my entire program collapses like a Jenga tower made of spaghetti. Half the time, I’m not even sure if I’m coding or just aggressively typing random characters and summoning gremlins. Either way, 10/10, would recommend.

Applying logic while coding sounds cute until you realize your brain has decided to go on a coffee break without you. ☕ "If true, then false" — that’s basically my entire logic flow. Honestly, I’m not even writing programs anymore, I’m composing avant-garde art pieces for future historians to cry over.

Sometimes my code runs on the first try, and I immediately get suspicious. 👀 Like... who helped you? What deal with the devil did I accidentally make? I don't trust it. Good code should at least involve three emotional breakdowns and a mild existential crisis, otherwise, it's suspiciously fake.

At the end of the day, I have absolutely no idea what I’m doing — and I love every chaotic, nonsensical, bug-infested second of it. 💥 Because that’s what coding is all about: living in a beautiful, confusing mess and pretending you’re in control. And honestly? It’s kind of perfect."""
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Pramish",
        "date": date(2024, 12, 5),
        "title": "Nepal Ko Jungle",
        "excerpt": """Living in Nepal’s wild woods is basically a Disney movie... if Disney movies had bears as wrestling partners and tigers as tea buddies. 🐻☕ Inspired by Khabib, I wrestle bears for cardio, and when I need fresh air, I just whistle — instantly covered in birds like some kind of forest superhero. 🕊️✨ It's wild, it's beautiful, and honestly, it's the best kind of madness you could ever live in. 🌲""",
        "content": """Out here in Nepal’s woods, dangerous wild animals aren’t something you fear — they’re just your weird group of tea buddies. 🦁🐻 Every morning, I sip on a cup of chai while a leopard complains about his hunting schedule and a rhino talks about early retirement. It’s a whole social club, and I’m the unofficial president.

The bears? Oh, they’re my little cutie-patuties. 🧸 Inspired by Khabib, I wrestle them every other weekend — it's cheaper than a gym membership and ten times more fun. You haven’t lived until you’ve been body-slammed into a pile of leaves by a 600-pound ball of fluff who's just happy to see you.

When I feel like getting some fresh air (and by fresh, I mean pure mountain magic), I just give a casual whistle. 🎶 Instantly, birds from all corners of the woods come flying, latch onto me like a feathery jacket, and we take off soaring above the trees. It’s basically Uber... but better and run by nature.

Flying over Nepal's endless forests with a bunch of chirping birds attached to you is a whole vibe. 🌲✨ You see the rivers twisting like silver threads, the mountains sitting grand like ancient gods, and sunsets that look like the sky is blushing. Honestly, Instagram filters cry themselves to sleep trying to match it.

So yeah, life here is completely insane... but in the best way. Between wrestling bears, hosting tea parties with tigers, and joyriding with birds, every day feels like stepping into a fairy tale where nature isn’t scary — it’s family. 🏞️❤️"""
    }
]

def get_date(post):
    return post['date']

def index_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {'posts': latest_posts})


def posts(request):
    return render(request, 'blog/all-post.html', {'all_posts': all_posts})


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug) # basic python
    return render(request, "blog/post-detail.html", {'post': identified_post})
