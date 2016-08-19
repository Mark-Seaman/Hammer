from django.shortcuts import render, redirect
from os import listdir
from os.path import join, exists

from bin.doc import doc_redirect
from hammer.settings import BASE_DIR
from log import log
from tool.document import doc_text
from tool.domain import domain_directory


# ---------------------------
# General Views

def file_list():
    directory = join(BASE_DIR, 'doc')
    log('file_list', directory)
    if exists(directory):
        return listdir(directory)


def display_document(request, title, page):
    log('display_document (request: %s, title: %s, page: %s)' % (request.get_host() + request.path, title, page))
    r = doc_redirect(title)
    if r:
        log('doc_redirect', r)
        return redirect(r)
    data = {
        'settings': site_settings(page),
        'document': title,
        'card_text': doc_text(title),
    }
    return render(request, 'hammer_doc.html', data)


def create_menu(page, menu_data):
    def menu_active(page, menu_item):
        if page.startswith(menu_item):
            return 'class=active'

    def menu_entry(page, x):
        name, icon, label, url = x
        #log('menu_entry', page + ',' + name)
        return url, icon, label, menu_active(page, name)

    return [menu_entry(page, x) for x in menu_data]


def site_settings(title):
    page = 'sws'
    settings = {
        'sws': {
            'title': 'Hammer Technology',
            'subtitle': 'Application Showcase',
            'label': title,
            'color': 'orange',
            'css': None,
            'menu': showcase_menu(title),
            'footer': True,
        },
    }
    return settings.get(page)


def showcase_menu(page):
    menu_data = [
        ["tech", "zmdi-account", "Seaman Tech", 'http://seaman-tech.com'],
        ["Leverage", "zmdi-trending-up", "Leverage", 'http://world-class-software.com/Leverage/Index'],
        ["seamanslog", "zmdi-accounts-list", "Seaman's Log", 'http://seamanslog.com'],  #
        ["sws", "zmdi-image", "Shrinking World", 'http://shrinking-world.net'],
        ["brain", "zmdi-cloud-outline", "Brain", 'http://exteriorbrain.com'],
        ["collab", "zmdi-layers", "Collaborator", "http://seaman-tech.com/tech/collab"],
        ['client', "zmdi-calendar", 'Client Portal', 'http://seaman-tech.com/tech/client/BestPractice'],
        ["spiritual", "zmdi-account", "Spiritual Things", 'http://spiritual-things.org'],
    ]
    return create_menu(page, menu_data)


def tool_home(request):
    log('tool_home', request.get_host())
    return tool_doc(request, '')


def tool_test(request):
    title = "Test Page"
    files = file_list()
    return render(request, 'hammer_page.html', {'title': title, 'files': files})


def tool_doc(request, title, template='hammer_doc.html', content=None):
    log('tool_doc (host = %s, path = %s, title = %s)' % (request.get_host(), request.path, title))
    return display_document(request, title, title)


def tool_theme(request):
    title = "Test Page"
    files = file_list()
    data = {'title': title, 'files': files, 'theme': 'creative'}
    return render(request, 'tool_theme.html', data)
