from django.shortcuts import render
from django import forms
from . import util
from  markdown2 import markdown
from django.urls import reverse
from django.http import HttpResponseRedirect
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
# функція з пошуку статей
def wiki(request, title):
    article_md = util.get_entry(title)
    if article_md == None:
        return render(request, "encyclopedia/not_found.html", {
            "title": title
        })
    
    return render(request, "encyclopedia/wiki.html", {
        "article": markdown(article_md),
        "title": title
    })