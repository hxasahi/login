import msvcrt, sys, os
print('password: ', end='', flush=True)

li = []

while 1:
    ch = msvcrt.getch()
    #�س�
    if ch == b'\r':
        msvcrt.putch(b'\n')
        print('����������ǣ�%s' % b''.join(li).decode())
        break
    #�˸�
    elif ch == b'\x08':
        if li:
            li.pop()
            msvcrt.putch(b'\b')
            msvcrt.putch(b' ')
            msvcrt.putch(b'\b')
    #Esc
    elif ch == b'\x1b':
        break
    else:
        li.append(ch)
        msvcrt.putch(b'*')

os.system('pause')
