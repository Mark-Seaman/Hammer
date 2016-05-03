from os import environ

from models import Test
from bin.shell import shell_command, file_tree_list, differences, banner
from log import log

#------------------------------------------------------------------------------------
# Test Commands

def tst_command(self,args):
    if args:
        log('tst %s' % args)
        cmd = args[0]
        args = args[1:]
        if cmd=='list':
            tst_list(self,args)
        elif cmd=='output':
            tst_output(self,args)
        elif cmd=='run':
            tst_run(self,args)
            tst_results(self,args)
        elif cmd=='like':
            tst_like(self,args)
        elif cmd=='results':
            tst_results(self,args)
        else:
            self.stdout.write("usage: x script tst [ like | list | output | results | run ]")


def tst_run(self,args):
    self.stdout.write("running tests ...")
    for t in Test.objects.all():
        self.stdout.write("    %s" % t.name)
        t.output = tests[t.name] ()
        t.save()


def tst_list(self,args):
    register_tests()
    tests = Test.objects.all()
    if tests:
        for t in tests:
            self.stdout.write(t.name)
    else:
        self.stdout.write('no tests found')


def tst_output(self,args):
    tests = Test.objects.all()
    if tests:
        for t in tests:
            self.stdout.write(t.output)
    else:
        self.stdout.write('no tests found')


def tst_like(self,args):
    if args:
        t = Test.objects.get(name=args[0])
        t.expected = t.output
        t.save()
        self.stdout.write("Like: "+t.name)
    else:
        tests = Test.objects.all()
        if tests:
            for t in tests:
                t.expected = t.output
                t.save()
                self.stdout.write("Like: "+t.name)
        else:
            self.stdout.write('no tests found')


def tst_results(self,args):
    tests = Test.objects.all()
    if tests:
        for t in tests:
            if t.output != t.expected:
                self.stdout.write(banner(t.name))
                diffs = differences(t.output, t.expected)
                self.stdout.write(diffs)
    else:
        self.stdout.write('no tests found')


#------------------------------------------------------------------------------------
# Test Cases

def pip_test():
    return shell_command ('pip list')


def version_test():
    return shell_command('git status')


def files_test():
    return '\n'.join(file_tree_list(environ['p']))


#------------------------------------------------------------------------------------
# Test Registry

tests = {
    'pip_test': pip_test,
    'version_test': version_test,
    'files_test': files_test,
}

def register_tests():
    for t in tests:
        if not Test.objects.filter(name=t):
            Test.objects.create(name=t)
