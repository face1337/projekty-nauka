import re

re.compile(r'''(\d\d\d) | # pierwsze trzy cyfry
(\(\d\d\d) ) # -or- 
\d\d\d # kolejne 3 cyfry
- # pauza
\d\d\d # ostatnie 3 cyfry
\sx\d{2,4} #rozszerzenie jakieś
''', re.VERBOSE)
