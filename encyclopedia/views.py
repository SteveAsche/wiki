from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
    "entries": util.list_entries()   
    })

def contents(request, title):
    f = util.get_entry(title)
    if f != None:
        print(f)
        return render(request, "encyclopedia/contents.html", {
        "content": f,
        "title": title  })
    else:
        return render(request, "encyclopedia/nofile.html", {
            "title": title    
        })
