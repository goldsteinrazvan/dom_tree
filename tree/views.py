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
    elements = Element.objects.all()
    html = create_dom(elements)
    return HttpResponse(html)

def create_dom(elements):
    # construct list of parent nodes
    parents = defaultdict(list)

    for element in elements:
        element_list = [element, element.id]
        parents[element.parent].append(tuple(element_list))
    
    elements_tree = build_tree(parents)
    dom = create_html_from_tree(elements_tree, [])
    
    html = '<!doctype html>' + ''.join(dom)
   
    return html

def build_tree(parents, t=None, parent_eid=0):
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
        build_tree(parents, report, eid)
    return t

def create_html_from_tree(tree, element_list):
    element_list.append(create_html_element(tree['element']))
    for child in tree['children']:
        if 'children' in child:
            create_html_from_tree(child, element_list)
        else:
            element_list.append(create_html_element(child['element']))
            if not(child['name'] == 'meta' or child['name'] == 'link'):
                element_list.append("</" + child['name'] + ">")
    element_list.append("</" +tree['name'] + ">")
    return element_list

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