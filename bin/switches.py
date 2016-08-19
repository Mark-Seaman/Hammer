from os import environ
from os.path import join


PROJECT_BASE = join(environ['HOME'],'Projects','MyBook')

IMPORT_RECORDS = True

EXPORT_RECORDS = True

SHOW_WEB_PAGE = False

ON_INTERNET = True

TEST_DOC = join(environ['p'], 'Documents', 'Index.md')

TODO_DIR  = join(environ['HOME'], 'Projects', 'MyBook', 'Documents', 'tech', 'collab', 'Client')

TODO_FILES = [
    join(TODO_DIR, 'Hammer-ToDo'),
    join(TODO_DIR, 'Hammer-Done'),
    join(TODO_DIR, 'Today.md'),
    join(TODO_DIR, '2016-08.md'),
]

APP_PORT = '8003'

APP_DIRS = ['hammer', 'tool']

APP_DIR = 'tool'

TEST_DOC_ENCODING = False

TEST_DATA = False

TEST_SELENIUM = True

TEST_PAGES = join(environ['p'], 'Documents', 'test-pages')

TEST_HOSTS = ['localhost:8003', environ['DROPLET_IP']]

