#!c:\ezlifter\envezlifter\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'ipdb==0.11','console_scripts','ipdb3'
__requires__ = 'ipdb==0.11'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('ipdb==0.11', 'console_scripts', 'ipdb3')()
    )
