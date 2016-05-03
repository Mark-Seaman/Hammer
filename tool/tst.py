from bin.shell import differences, banner
from log import log
from models import Test
from tool.test_cases import test_cases


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
        t.output = test_cases[t.name] ()
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
                if t.output != t.expected:
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


def tst_register(tests):
    for t in tests:
        if not Test.objects.filter(name=t):
            Test.objects.create(name=t)


