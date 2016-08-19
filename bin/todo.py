from os import  system

from switches import TODO_FILES


def todo_command(options):
    path = TODO_FILES[0]

    if options:    
        cmd = options[0]
        if cmd=='send-todo':
            system('x send doc tech/collab/Client/Today me')
            system('x send dispatch')
        elif cmd=='send-done':
            system('x send doc tech/collab/Client/2016-08 me')
            system('x send dispatch')
        elif cmd=='show':
            print(open(path).read())
        else:
            item = ' '.join(options)
            open(path, 'a').write('* '+item+'\n')
    else:   
        for x in TODO_FILES:
            system('e %s' % x)

