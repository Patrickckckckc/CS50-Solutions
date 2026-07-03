import random
import markdown2
from django.shortcuts import render, redirect
from django.urls import reverse

from . import util


def index(request):
    # Handle Search
    if request.method == "POST":
        # Get information from the Query
        query = request.POST.get("q")

        # If entry exis REDIRECT to entry
        if query and util.get_entry(query):
            return redirect(reverse("entry", kwargs={"title": query}))

        # If not exists SHOW all LIKE queries
        return render(request, "encyclopedia/search.html", {
            "entries": util.list_entries(),
            "query": query
        })


    # Render Homepage
    else:
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })

def entry(request, title):
    # Get information from the query
    entry_content = util.get_entry(title)

    # Check valid input
    if not entry_content:
        entry_content = "This page doesn´t exist 404"
        title = "ERROR"
    else:
        entry_content = markdown2.markdown(entry_content, extras=["fenced-code-blocks"])

    # Make the request
    return render(request, "encyclopedia/entry.html", {
        "entry" : entry_content,
        "title" : title
    })

def add(request):
    if request.method == "POST":
       # Get Input
        title = request.POST.get("title")
        content = request.POST.get("content")

       # Check Input is correct
        if not title or not content:
            message = "MISSING TITLE OR CONTENT"
            return render(request, "encyclopedia/error.html", {
                "message" : message
            })

        for entry in util.list_entries():
            if entry == title:
                # Display ERROR MESSAGE
                message = "THE PAGE ALREADY EXISTS"
                return render(request, "encyclopedia/error.html", {
                    "message" : message
                })
       # Add the new Entry
        util.save_entry(title, content)
        return redirect(reverse("entry", kwargs={"title": title}))


    else:
        return render(request, "encyclopedia/add.html")


def random_page(request):
    # Choose a random title
    title = random.choice(util.list_entries())

    # Redirect to it
    return redirect(reverse("entry", kwargs={"title": title}))

def edit_page(request, title):
    if request.method == "POST":
        # Save Content
        content = request.POST.get("content")
        util.save_entry(title, content)

        # Redirect to it
        return redirect(reverse("entry", kwargs={"title": title}))
    else:
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "entry": util.get_entry(title)

        })

