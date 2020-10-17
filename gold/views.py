from django.shortcuts import render, redirect
import random


def index(request):
    if "gold" not in request.session:
        request.session["gold"] = 0

    if "locations" not in request.session:
        request.session["locations"] = [
            {"name": "farm", "min": 10, "max": 20},
            {"name": "cave", "min": 5, "max": 10},
            {"name": "house", "min": 2, "max": 5},
            {"name": "casino", "min": -50, "max": 50},
        ]

    if "activities" not in request.session:
        request.session["activities"] = []

    return render(request, "index.html")


def process(request):
    if request.method != "POST":
        pass
    else:

        for ix in request.session["locations"]:
            if ix["name"] in request.POST:
                earnings = round(random.random() * (ix["max"] - ix["min"]) + ix["min"])
                request.session["gold"] += earnings
                if earnings >= 0:
                    request.session["activities"].append(
                        f'Earned {earnings} golds from the {ix["name"]}!'
                    )
                else:
                    request.session["activities"].append(
                        f"Entered a {ix['name']} and lost {abs(earnings)} golds... Ouch."
                    )
                break
    return redirect("/")
