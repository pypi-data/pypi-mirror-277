
# Webdriver

Geckodriver alpine install:

```sh
apk add --no-cache firefox # or firefox-esr
wget https://github.com/mozilla/geckodriver/releases/download/v0.34.0/geckodriver-v0.34.0-linux64.tar.gz -qO- | tar -zx -C /usr/bin
```

```
from shutil import which
if which('geckodriver') is None:
    cls.__log.warning("`geckodriver` not in path, installing...")
    what = 'geckodriver'
if which('firefox') is None:
    cls.__log.warning("`firefox` not in path, installing...")
    what = 'firefox'

try:
    import selenium
except ImportError:
    cls.__log.warning("Package `selenium` not installed. Installing with `pip`...")
    what = 'selenium'
    import subprocess
    from sys import executable
    subprocess.check_call([executable, '-m', 'pip', 'install', '--no-cache-dir', 'selenium'])
```

# Internet Archive as a Source / Pluggable Sources

https://archive.org/developers/tutorial-get-snapshot-wayback.html
