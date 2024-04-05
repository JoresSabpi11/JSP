import os,platform
os.system('git pull')
os.system("clear")
print('\033[92;1m Join Whatsapp Group')
os.system('xdg-open https://chat.whatsapp.com/FZDjbC8Fgev9CQld7Pt4h4')
jsp=platform.architecture()[0]
if jsp=="32bit":
    __import__("p32")
elif jsp=="64bit":
    __import__("p64")