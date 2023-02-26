import os, sys
try:
    __import__("JIHAD").mex()
except Exception as e:
    exit(str(e))
