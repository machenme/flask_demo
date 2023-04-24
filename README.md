# Creating Single Flask executable file with Pyinstaller
pyinstaller command
```bash
pyinstaller app.py -F --add-data "./templates/*;templates" --add-data "./static/*;static"
```

## difference 
app.py
```bash
import sys
import os

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


app = Flask(__name__, static_url_path="", static_folder=resource_path(
    'static'), template_folder=resource_path("templates"))

```
index.html
```bash
<link rel="stylesheet" type="text/css" href={{ url_for('static', filename='style.css') }}>
```
