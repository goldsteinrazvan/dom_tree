from django.shortcuts import render
from django.http import HttpResponse
from .models import Element
# Create your views here.

def index(request):
    return HttpResponse("Hello World. You are at the tree index.")

def fetch(request):
    dom_tree = Element.objects.all()
    html = create_dom(dom_tree)
    return HttpResponse(html)

def create_dom(dom_tree):
    html = '<!doctype html>'
    dom_tree_iterator = dom_tree.iterator()
    next(dom_tree_iterator)
    elements = []
    for element in dom_tree:
        lft = element.lft
        rgt = element.rgt
        try:
            next_element = next(dom_tree_iterator)
        except StopIteration:
            pass
        else:
            next_lft = next_element.lft
            element_html = None
            if (lft <= next_lft <= rgt):
                #element_html += "<" + next_element.tag + ">"
                print("Element tag: " + element.tag + " " + str(element.lft) + " --- " + str(element.rgt) + " /// Next element: " + next_element.tag + " - " + str(next_lft))
            else:
                element_html = "<" + element.tag + ">"
                element_html += "</" + element.tag + ">"
            elements.append(element_html)
    print(elements)
    return html