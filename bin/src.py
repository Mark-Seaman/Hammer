
from os import system, environ
from os.path import join, exists

from shell import file_tree_list, banner, shell
from log import log
from switches import PROJECT_BASE


def differences(f1,f2):
    return shell('diff %s %s' %(f1,f2))


def list_source_files(d):
    return [f for f in file_tree_list(d, '.py') if not '/migrations/' in f]


def show_differences(f1,f2):
    if not exists(f1):
        print('File does not exist, %s' % f1)
    elif not exists(f2):
        print('File does not exist, %s' % f2)
    elif differences(f1,f2):
        print(banner(f1.replace(src_dir()+'/', '')))
        print(shell('diff %s %s' %(f1,f2)))
    else:
        print('No differences in %s and %s' % (f1, f2))


def src_base():
    return PROJECT_BASE


def src_changed():
    for f1 in list_source_files(src_dir()):
        f2 = f1.replace(src_dir(), src_base())
        if exists(f2) and differences(f1,f2):
            print(f1.replace(src_dir()+'/', ''))


def src_common():
    for f1 in list_source_files(src_dir()):
        f2 = f1.replace(src_dir(), src_base())
        if exists(f2):
            print(f1.replace(src_dir()+'/', ''))


def src_command(options):
    log('src command %s' % options)

    cmd = options[0]
    args = options[1:]
    if cmd=='base':
        print(src_base())
    elif cmd=='changed':
        src_changed()
    elif cmd=='common':
        src_common()
    elif cmd=='diff':
        src_diff(args)
    elif cmd=='edit':
        src_edit(args)
    elif cmd=='list':
        src_list()
    elif cmd=='missing':
        src_missing()
    elif cmd=='pull':
        src_pull(args)
    elif cmd=='push':
        src_push(args)
    elif cmd=='same':
        src_same()
    elif cmd=='unique':
        src_unique()
    elif cmd=='update':
        src_update()
    else:
        src_help()


def src_diff(args):
    if args:
        f1 = join(src_dir(), args[0])
        f2 = join(src_base(), args[0])
        show_differences(f1, f2)
    else:
        for f1 in list_source_files(src_dir()):
            f2 = f1.replace(src_dir(), src_base())
            if exists(f1) and exists(f2):
                diff = differences(f1,f2)
                if diff:
                     print(banner(f1.replace(src_dir()+'/', '')))
                     print(shell('diff %s %s' %(f1,f2)))


def src_dir():
    return environ['p']


def src_edit(args):
    f1 = join(src_dir(), args[0])
    f2 = join(src_base(), args[0])
    system('e %s %s' % (f1,f2))


def src_help():
    print('''

        script to manage source code and keep multiple projects in sync


        usage: x src command

        command
            edit    - edit the source code for both files
            diff    - show the difference for one source file or all files
            update  - copy files from the base to the current project

            base    - project used for comparison
            list    - file list or source code

            common  - files shared with base project
            missing - files present only in the base project
            unique  - files that are not present in the base project
            changed - show common files that have changes
            same    - show common files that are unchanged

        ''')


def src_list():
    files = list_source_files(src_dir())
    for f in files:
        print(f)


def src_missing():
    for f1 in list_source_files(src_base()):
        f2 = f1.replace(src_base(), src_dir())
        if not exists(f2):
            print(f1)  #.replace(src_dir()+'/', ''))


def src_pull(args):
    f1 = join(src_base(),args[0])
    f2 = join(src_dir(),args[0])
    cmd = 'cp %s %s' % (f1,f2)
    print(cmd)
    system(cmd)


def src_push(args):
    f1 = join(src_dir(),args[0])
    f2 = join(src_base(),args[0])
    cmd = 'cp %s %s' % (f1,f2)
    print(cmd)
    system(cmd)


def src_same():
    for f1 in list_source_files(src_dir()):
        f2 = f1.replace(src_dir(), src_base())
        if exists(f2) and not differences(f1,f2):
            print(f1.replace(src_dir()+'/', ''))


def src_unique():
    for f1 in list_source_files(src_dir()):
        f2 = f1.replace(src_dir(), src_base())
        if not exists(f2):
            print(f1.replace(src_dir()+'/', ''))


def src_update():
    for f1 in list_source_files(src_dir()):
        f2 = f1.replace(src_dir(), src_base())
        if exists(f2) and differences(f1,f2):
            print('src pull %s' % f1.replace(src_dir()+'/', ''))

