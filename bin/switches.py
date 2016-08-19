from os import environ
from os.path import join


PROJECT_BASE = join(environ['HOME'],'Projects','w2w')

IMPORT_RECORDS = True
EXPORT_RECORDS = True
SHOW_WEB_PAGE = False
ON_INTERNET = True



TEST_DOC = join(environ['p'],'Documents','tech', 'Index.md')

TODO_DIR  = join(environ['p'], 'Documents', 'tech', 'collab', 'Client')
#TASK_DIR  = join(environ['HOME'], 'Documents', 'MyBook', 'notes', 'Task')
TODO_FILES = [
    join(TODO_DIR, 'Hammer-ToDo'),
    join(TODO_DIR, 'Hammer-Done'),
    join(TODO_DIR, 'Today.md'),
    join(TODO_DIR, '2016-08.md'),
]

APP_PORT = '8001'
APP_DIRS = ['hammer', 'tool', 'spiritual']
APP_DIR = 'tool'


#if environ.has_key('p'):
#     BASE_DIR = environ['p']
# else:
#     from hammer.settings import BASE_DIR

TEST_DOC_ENCODING = False
TEST_DATA = False

TEST_SELENIUM = True
TEST_PAGES = join(environ['p'], 'Documents', 'tech', 'test', 'pages')

TEST_HOSTS = ['localhost:8001', environ['DROPLET_IP']]

