from os import environ, system, walk
from os.path import join
from platform import node
from selenium import webdriver
from subprocess import Popen,PIPE
from unittest import TestCase, main
from time import sleep

from doc import list_documents, doc_list

RUN_WEB_BROWSER = True

LOCAL_HOST = 'localhost:8000'
REMOTE_HOST = 'mybookonline.org' #environ['DJANGO_IP']

TEST_PAGES = '''
tech/Index
spiritual/Index
spiritual/teaching
spiritual/prayers
spiritual/bible
spiritual/reflect
'''


def run_server():
    system('''
            cd $p;
            rbg python bin/manage.py runserver;
            sleep 2
           ''')

# Get page text
def webpage_text(browser,url):
    #print_banner ('%s...' % url)
    try:
        browser.get('http://%s' % url)
        body = browser.find_element_by_tag_name('body')
        text = body.text.decode('ascii','ignore')
    except:
        text = 'Web page not found: '+url
    print ('\nTitle: %s\n\n%s\n\n' % (browser.title,text))
    return text

    

#---------------------------------------------------------------------------
# Test local pages
#
# class PagesTest(TestCase):
#
#     def setUp(self):
#         if RUN_WEB_BROWSER:
#             run_server()
#             self.browser = webdriver.Firefox()
#
#     def tearDown(self):
#         if RUN_WEB_BROWSER:
#             self.browser.quit()
#
#
#     def assertBetween(self, num, min, max):
#         self.assertGreaterEqual(num, min)
#         self.assertLessEqual(num, max)
#
#     def assertLineCount(self, text, min=1, max=10):
#         self.assertBetween(len(text.split('\n')), min, max)
#
#
#     def test_pages(self):
#         pages = TEST_PAGES.split('\n')[1:-1]
#         urls = [ join(LOCAL_HOST,p) for p in pages ]
#         for url in urls:
#             webpage_text(self.browser,url)
#             sleep(1)
    
#---------------------------------------------------------------------------
# Test remote pages

class RemoteTest(TestCase):

    def setUp(self):
        if RUN_WEB_BROWSER:
            self.browser = webdriver.Firefox()

    def tearDown(self):
        if RUN_WEB_BROWSER:
            self.browser.quit()
    
    def test_pages(self):
        #pages = TEST_PAGES.split('\n')[1:-1]
        pages = list_documents()
        for p in pages:
            if not p.startswith('app/'):
                p = p.replace('.md','')
            url =  join(REMOTE_HOST,p)
            webpage_text(self.browser,url)
            sleep(1)


#---------------------------------------------------------------------------
# Test remote pages

# class RemoteTest(TestCase):
    # def test_visit_google(self):
    #     if RUN_WEB_BROWSER:
    #         self.browser.get('http://google.com')
    #         assert 'Google' in self.browser.title



if __name__ == '__main__': 
    main()
