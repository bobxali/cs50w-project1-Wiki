import random
from django.shortcuts import render
from markdown2 import Markdown


from . import util
def convert_mdtohtml(title):
    content = util.get_entry(title)
    markdowner = Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)
    markdowner.convert("*boo!*")
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    html_content = convert_mdtohtml(title)
    if html_content == None:
        return render(request,"encyclopedia/error.html", {
            "message": "This entry doesn't exist"
            
            })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
           "content": html_content
           
           })

def search(request):
    if request.method == "POST":
        entry_search = request.POST['q']
        html_content = convert_mdtohtml(entry_search)
        if html_content is not None:
            # If the search query matches the exact title of an entry, redirect to the entry page.
            return redirect('entry', title=entry_search)

        # If the search query doesn't match any exact entry, create a list of matching entries.
        entries = util.list_entries()
        recommendation = [entry for entry in entries if entry_search.lower() in entry.lower()]

        return render(request, "encyclopedia/search.html", {
            "recommendations": recommendation
        })

    # If it's not a POST request, you can handle it differently (e.g., display all entries).
    # For simplicity, let's assume it shows all entries here.
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })




def new_page(request):
    if request.method == "GET":
       return  render(request, "encyclopedia/new.html")
    else:
       title = request.POST['title']
       content = request.POST['content']
       titleExist = util.get_entry(title)
       if titleExist is not None:
           return render(request, "encyclopedia/error.html", {
             "message": "This entry page already exists"
               })
       else:
           util.save_entry(title, content)
           html_content = convert_mdtohtml(title)
           return render(request, "encyclopedia/entry.html", {
               "title": title,
               "content": html_content
               })

def edit_page(request):
    if request.method == "POST":
        title = request.POST['title']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": content
            })


def save_edit(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        html_content = convert_mdtohtml(title)
        return render(request, "encyclopedia/entry.html", {
               "title": title,
               "content": html_content
               })
def rand(request):
        entries = util.list_entries()
        rand_entry = random.choice(entries)
        html_content = convert_mdtohtml(rand_entry)
        return render(request, "encyclopedia/entry.html", {
            "title": rand_entry,
            "content": html_content
            })
