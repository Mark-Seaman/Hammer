from os import environ, system, walk
from os.path import join
from platform import node
from selenium import webdriver
from subprocess import Popen,PIPE
from unittest import TestCase, main
from time import sleep


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
        self.open_browser()

    def tearDown(self):
        self.close_browser()
        

    # Helpers
    def open_browser(self):
        if RUN_WEB_BROWSER:
            run_server()
            self.browser = webdriver.Firefox()

    def close_browser(self):
        if RUN_WEB_BROWSER:
            self.browser.quit()
            pass

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

    def test_pages(self):
        pages = [ 'EngineeringLog', 'FunctionalTest', 'README', 'ToDo']
        urls = [ 'localhost:8000/%s.md'%p for p in pages ]
        for url in urls:
            webpage_text(self.browser,url)
            sleep(1)
    



if __name__ == '__main__': 
    main()
