from os import system
from time import sleep

from bin.shell import banner, differences
from bin.switches import TEST_PAGES, TEST_HOSTS
from log import log
from models import Page


def page_add(self, args):
    if not args:
        self.stdout.write('no page requested')
    else:
        url = args[0]
        try:
            Page.objects.create(url=url, expected_text='New page')
            self.stdout.write('added page %s' % url)
        except:
            self.stdout.write('page is already present %s' % url)
        #print('%s Pages found' % len(Page.objects.all()))


def page_command(self, options):
    log('page command %s' % options)

    if not options:
        page_help()
    else:
        cmd = options[0]
        args = options[1:]
        if cmd == 'add':
            page_add(self, args)
        elif cmd == 'delete':
            page_delete(self, args)
        elif cmd == 'diff':
            page_diff(self, args)
        elif cmd == 'expect':
            page_expect(self, args)
        elif cmd == 'get':
            page_get(self)
        elif cmd == 'html':
            page_html(self)
        elif cmd == 'like':
            page_like(self, args)
        elif cmd == 'list':
            page_list(self)
        elif cmd == 'reset':
            page_reset(self)
        elif cmd == 'text':
            page_text(self, args)
        else:
            page_help(self)


def page_delete(self, args):
    if args:
        if args[0] == 'all':
            self.stdout.write('delete all pages')
            Page.objects.all().delete()
        else:
            self.stdout.write('delete pages %s' % args[0])
            Page.objects.get(pk=args[0]).delete()
    else:
        self.stdout.write('no page given')


def page_diff(self, args):
    def show_diff(page):
        try:
            if page.text != page.expected_text:
                self.stdout.write(banner(page.url))
                self.stdout.write(differences(page.text, page.expected_text))
            #else:
                #self.stdout.write('%s: Expected results' % page.url)
        except:
            self.stdout.write('%s: Error in Expected results' % page.url)

    if args:
        page = page_lookup(args[0])
        show_diff(page)
    else:
        for page in Page.objects.all():
            show_diff(page)


def page_expect(self, args):
    page = page_lookup(args[0])
    self.stdout.write('Expected results: \n\n%s' % page.expected_text)


def page_get(self):

    # Fetch one web page from some web site
    def webpage_text(browser, page):
        try:
            browser.get('http://%s' % page.url)
            body = browser.find_element_by_tag_name('body')
            page.text = body.text.encode('ascii', 'ignore')
            if not page.text:
                page.text = 'No text'
            if not page.expected_text:
                page.expected_text = page.text
            sleep(2)
        except:
            page.text = 'Web page not found: ' + page.url
        page.save()

    # Login to the Support Center web site
    def login(browser,page):
        browser.get('http://%s' % page.url)
        username = 'TestSuperUser'
        password = 'wam'
        username_field = browser.find_element_by_name('username')
        username_field.send_keys(username)
        password_field = browser.find_element_by_name('password')
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
        page.text = 'Logging In'
        sleep(1)

    system('x app run')
    self.stdout.write('page get')
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys

    browser = webdriver.Firefox()
    for page in Page.objects.all():
        print('Get web page:  URL = %s' % page.url)
        if page.url.endswith('login'):
            login(browser,page)
            webpage_text(browser, page)
        else:
            webpage_text(browser, page)
    browser.quit()


def page_help(self):
    self.stdout.write('''

        script to manage pages on servers

        usage: x page command

        command

        Pages:
            list                - list the configured page
            add           page  - add a new page to the lineup
            delete        page  - remove this page

        Page Content:
            get                 - get all pages from the web or localhost servers
            text          page  - server page last text received
            html          page  - server page last html received

        Differences:
            expect        page  - server page text expected
            html-expected page  - server page html expected
            diff          page  - unexpected text received
            diff-html     page  - unexpected html received
            accept        page  - accept the text and html as correct

        ''')


def page_html(self):
    self.stdout.write('page html -- NOT IMPLEMENTED YET')


def page_like(self, args):
    def like_page(page):
        if page.expected_text != page.text:
            page.expected_text = page.text
            page.save()
            self.stdout.write('like %s' % page.url)

    if args:
        like_page(page_lookup(args[0]))
    else:
        for p in Page.objects.all():
            like_page(p)


def page_list(self):
    self.stdout.write('page list')
    for p in Page.objects.all():
        print('%s.  %s' % (p.pk, p.url))


def page_lookup(url):
    if Page.objects.filter(url=url):
        return Page.objects.get(url=url)


def page_reset(self):
    pages = open(TEST_PAGES).read().split('\n')
    for p in pages:
        p = p.strip()
        if p:
            page_add(self, [p])


def page_text(self, args):

    def show_output(page):            
        self.stdout.write(banner(page))
        p = page_lookup(page)
        if p:
            self.stdout.write(p.text)
        else:
            self.stdout.write('Page not found, %s' % page)

    if args:
        if args[0] == 'all':
            for p in Page.objects.all():
                show_output(p.url)
        else:
            show_output(args[0])
