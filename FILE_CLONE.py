import os, sys
os.system('clear')
os.system('git pull')
try:
    __import__("JIHAD").menu()
except Exception as e:
    exit(str(e))
