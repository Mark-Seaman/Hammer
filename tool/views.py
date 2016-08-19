from django.shortcuts import render, redirect
from os import listdir
from os.path import join, exists

from bin.doc import doc_redirect, doc_random_select
from hammer.settings import BASE_DIR
from log import log
from tasks.models import Task
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


def domain_redirect(request, title):
    dom = domain_directory(request.get_host())
    log('domain directory', dom)
    if dom and not title.startswith(dom):
        if title:
            url = '/' + dom + '/' + title
        else:
            url = '/' + dom
        log('domain_redirect --> ', url)
        return url


def page_redirect(request, title):
    r = domain_redirect(request, title)
    if r:
        return r
    return doc_redirect(title)


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
    if title.startswith('tech/collab'):
        page = 'collab'
    elif title.startswith('tech/client'):
        page = 'client'
    elif title.startswith('spiritual'):
        page = 'spiritual'
    else:
        page = 'sws'
    settings = {
        'sws': {
            'title': 'Hammer Technology',
            'subtitle': 'Application Showcase',
            'label': title,
            'color': 'teal',
            'css': None,
            'menu': showcase_menu(title),
            'footer': True,
        },
        'client': {
            'title': 'Client Portal',
            'subtitle': 'Producing exceptional value for clients',
            'label': title,
            'color': 'green',
            'css': None,
            'menu': client_menu(title),
            'footer': True,
        },
        'collab': {
            'title': 'Application Collaborator',
            'subtitle': 'Application Development Planner',
            'label': title,
            'color': 'blue',
            'css': None,
            'menu': collab_menu(title),
            'footer': True,
        },
        'spiritual': {
            'title': 'Spiritual Things',
            'subtitle': 'Worthy Meditations',
            'label': title,
            'color': 'red-400',
            'css': 'spiritual',
            'menu': spiritual_menu(title),
            'footer': False,
        },
    }
    return settings.get(page)


# ---------------------------
# Application Views

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


# 'home': ('Hammer Showcase', 'Showcase for technology and business demos'),
# '4-thot': ('4 - Thot', 'Information organizer'),
# 'mybook': ('My Book Online', 'Personal publisher'),
# 'task': ('Task Master', 'Task organizer'),
# 'page': ('Page Master', 'Web page tester'),
# 'app': ('App Master', 'Predictable web app development'),
# 'brain': ('Brain demo', 'Exterior brain for info management'),
# 'test': ('Test demo', 'Automated test manager'),
# "Home",      "zmdi-home",           "Hammer Showcase",  "http://exteriorbrain.com/Home")),
# "4-thot", "zmdi-accounts-list",  "4 thot",     'http://exteriorbrain.com/4-thot')),
# "page",   "zmdi-layers",  "Page Master",     'http://exteriorbrain.com/page')),
# "test",   "zmdi-layers",  "Test Master",     'http://exteriorbrain.com/test')),
# "task",   "zmdi-layers",  "Task Master",     'http://exteriorbrain.com/task')),


def spiritual_menu(page):
    menu_data = [
        ["prayers", "zmdi-comment-outline", "Prayer", '/spiritual/prayers'],
        ["bible", "zmdi-local-library", "Meditate", '/spiritual/bible'],
        ["reflect", "zmdi-key", "Reflect", '/spiritual/reflect'],
        ["teaching", "zmdi-face", "Learn", '/spiritual/teaching'],
    ]
    return create_menu(page, menu_data)


def collab_menu(page):
    menu_data = [
        ["Project", "zmdi-key", "Project", '/tech/collab/Project'],
        ["UX", "zmdi-account", "User Experience", '/tech/collab/UX'],
        ["Front-end", "zmdi-cloud", "Front-end", '/tech/collab/Front-end'],
        ["Back-end", "zmdi-face", "Back-end", '/tech/collab/Back-end'],
        ["Hosting", "zmdi-local-library", "Hosting", '/tech/collab/Hosting'],
        ["Automation", "zmdi-trending-up", "Automation", '/tech/collab/Automation'],
        ["Test", "zmdi-comment-outline", "Test", '/tech/collab/Test'],
        #["tech", "zmdi-account", "Seaman Tech", 'http://seaman-tech.com'],
    ]
    return create_menu(page, menu_data)


def client_menu(page):
    menu_data = [
        ['Login', "zmdi-account", "login", '/login'],
        ['BestPractice', "zmdi-comment-outline", 'How We Work', '/tech/client/BestPractice']
        #["tech", "zmdi-account", "Seaman Tech", 'http://seaman-tech.com'],
    ]
    return create_menu(page, menu_data)

# ---------------------------
# Application Views

# def collab_doc(request, title=None):
#     return display_document(request, 'collab'+title, title)


def tool_home(request):
    log('tool_home', request.get_host())
    return tool_doc(request, '')
    # title = "Directory"
    # files = file_list()
    # return render(request, 'tool_dir.html', {'title': title, 'files': files})


def tool_test(request):
    title = "Test Page"
    files = file_list()
    return render(request, 'hammer_page.html', {'title': title, 'files': files})


def tool_task(request, id=None):
    content = Task.objects.all()
    data = {'list': content}
    if id:
        data['task'] = Task.objects.get(pk=id)
    return tool_doc(request, 'task', 'tool_task.html', data)


def spiritual_doc(request, title=''):
    log('spirit_doc', title)
    if title.endswith('/'):
        title = title[:-1]
    if not title:
        log('spirit_doc -- random_select', 'spiritual')
        return redirect(doc_random_select('spiritual'))
    if '/' not in title:
        log('spirit_doc -- random_select', 'spiritual/%s' % title)
        return redirect(doc_random_select('spiritual/%s' % title))

    # log('spirit_doc -- 2', title)

    page = title
    settings = {
        'title': 'Spiritual Things',
        'subtitle': 'Worthy Meditations',
        'color': 'red-400',
        'css': 'spiritual',
        'menu': spiritual_menu(title),
    }
    data = {
        'settings': settings,
        'document': page if page else 'Home',
        'card_action': page,
        'card_text': doc_text('spiritual/' + page),
    }
    return render(request, 'hammer_doc.html', data)


def tool_seamanslog(request):
    log('seamanslog')
    return redirect(doc_random_select('seamanslog'))


# def client_doc(request, title=None):
#     log('client', title)
#     if title:
#         title = 'client/' + title
#         return display_document(request, title, 'client')
#     else:
#         return redirect('/client/Index')


def tool_doc(request, title, template='hammer_doc.html', content=None):
    log('tool_doc (host = %s, path = %s, title = %s)' % (request.get_host(), request.path, title))
    r = domain_redirect(request, title)
    if r:
        return redirect(r)
    return display_document(request, title, title)


def tool_theme(request):
    title = "Test Page"
    files = file_list()
    data = {'title': title, 'files': files, 'theme': 'creative'}
    return render(request, 'tool_theme.html', data)
