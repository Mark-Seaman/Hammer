from os import environ, system, walk
from os.path import join
from platform import node
from selenium import webdriver
from subprocess import Popen,PIPE
from unittest import TestCase, main

#from functional_tests.tests import  FunctionalTestCase

RUN_WEB_BROWSER = True

def run_server():
    system('''
            cd $p;
            rbg python manage.py runserver;
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

class PagesTest(TestCase):

    # Setup & teardown

    def setUp(self):
        if RUN_WEB_BROWSER:
            self.browser = webdriver.Firefox()

    def tearDown(self):
        if RUN_WEB_BROWSER:
            self.browser.quit()

    # Helpers

    def assertBetween(self, num, min, max):
        self.assertGreaterEqual(num, min)
        self.assertLessEqual(num, max)

    def assertLineCount(self, text, min=1, max=10):
        self.assertBetween(len(text.split('\n')), min, max)

    #---------------------------------------------------------------------------
    # Tests

    # def test_visit_google(self):
    #     if RUN_WEB_BROWSER:
    #         self.browser.get('http://google.com')
    #         assert 'Google' in self.browser.title

    def test_simple_page(self):
        run_server()
        url = 'localhost:8000'
        #self.browser.get(url)
        #print(self.browser.text)
        webpage_text(self.browser,url)



if __name__ == '__main__': 
    main()
