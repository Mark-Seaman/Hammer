from models import Test
from bin.shell import shell_command
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
        else:
            self.stdout.write("usage: x script tst [ list | output | run ]")


def tst_run(self,args):
    self.stdout.write("running tests ...")
    for t in Test.objects.all():
        self.stdout.write("Test: %s" % t)
        t.output = tests[t.name] ()
        t.save()


def tst_list(self,args):
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


#------------------------------------------------------------------------------------
# Test Cases

def pip_test():
    return shell_command ('pip list')


def version_test():
    return shell_command('git status')


#------------------------------------------------------------------------------------
# Test Registry

tests = {
    'pip_test': pip_test,
    'version_test': version_test,
}

def register_tests():
    for t in tests:
        if not Test.objects.filter(name=t):
            Test.objects.create(name=t)
