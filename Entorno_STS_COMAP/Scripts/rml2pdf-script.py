#!c:\django\sts_comap\entorno_sts_comap\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'rlextra==3.5.17','console_scripts','rml2pdf'
__requires__ = 'rlextra==3.5.17'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('rlextra==3.5.17', 'console_scripts', 'rml2pdf')()
    )
