from django.shortcuts import render
from django.http import HttpResponse
from .models import Element
import json
from collections import defaultdict
from pprint import pprint
# Create your views here.

def index(request):
    return HttpResponse("Hello World. You are at the tree index.")

def fetch(request):
    dom_tree = Element.objects.all()
    html = create_dom(dom_tree)
    return HttpResponse(html)

def create_dom(dom_tree):
    html = '<!doctype html>'

    # contstruct list of parents
    parents = defaultdict(list)

    for element in dom_tree:
        element_list = [element, element.id]
        parents[element.parent].append(tuple(element_list))
   
    data = buildtree(parents)
    print_tree(data)
    return html

def buildtree(parents, t=None, parent_eid=0):
    parent = parents.get(parent_eid, None)
    if parent is None:
        return t
    for element, eid in parent:
        report = {'id': element.id, 'name': element.tag, 'element': element}
        if t is None:
            t = report
        else:
            reports = t.setdefault('children', [])
            reports.append(report)
        buildtree(parents, report, eid)
    return t

def print_tree(tree, html=''):
    # print("<" + tree['name'] + " " + str(tree['element']._class) + ">")
    print(create_html_element(tree['element']))
    for child in tree['children']:
        if 'children' in child:
            print_tree(child, html)
        else:
            # print("<" + child['name'] + " class=" + str(child['element']._class) + "></" + child['name'] + ">")
            print(create_html_element(child['element']))
            if not(child['name'] == 'meta' or child['name'] == 'link'):
                print("</" + child['name'] + ">")

    print("</" +tree['name'] + ">")

def create_html_element(element):
    html = "<" + element.tag
    if(element._id):
        html += " id=\"" + element._id + "\""
    if(element._class):
        html += " class=\"" + element._class + "\""
    if(element.style):
        html += " style=\"" + element.style + "\""
    if(element.attributes):
        attributes = json.loads(element.attributes)
        for (index, attribute) in attributes.items():
            html += " " + index + "=\"" + attribute + "\""
    html += ">"
    
    if (element.content):
        html += element.content

    return html