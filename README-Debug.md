# Debugging Django in VS Code

This guide will help you set up debugging for a Django application in Visual Studio Code (VS Code). It also covers how to install and use the Django Debug Toolbar.

## Prerequisites

- Visual Studio Code installed
- Python and Django installed
- A Django project

## Step-by-Step Guide

### 1. Install VS Code Python Extension

Ensure you have the Python extension for VS Code installed. You can find it in the VS Code marketplace.

### 2. Open Your Django Project in VS Code

Open your Django project folder in VS Code.

### 3. Create a Debug Configuration

1. Click on the Run and Debug icon on the left sidebar menu in VS Code.
2. Click on `create a launch.json file` link.
3. Select `Python` from the options.

Add the following configuration to your `launch.json` file:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Django",
      "type": "python",
      "request": "launch",
      "program": "${workspaceFolder}/manage.py",
      "args": ["runserver", "0.0.0.0:8000"],
      "django": true,
      "justMyCode": true
    }
  ]
}
```

### 4. Start Debugging

Set breakpoints in your Django project by clicking in the gutter next to the line numbers in your Python files.
Start the debugger by selecting the Django configuration from the dropdown in the Run and Debug view and clicking the green play button.

### 5. Install Django Debug Toolbar

The Django Debug Toolbar provides a configurable set of panels that display various debug information about the current request/response.

### Installation

Install the toolbar using pip:
`pip install django-debug-toolbar`

### 5. Configuration

1. Add `debug_toolbar` to your `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'debug_toolbar',
]
```

2. Add the middleware to `settings.py`:

```python
MIDDLEWARE = [
    ...
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    ...
]

```

3. Add the following to your `settings.py` to configure the toolbar:

```python
INTERNAL_IPS = [
    '127.0.0.1',
]

if DEBUG:
    import mimetypes
    mimetypes.add_type("application/javascript", ".js", True)

import socket
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS += [ip[:-1] + "1" for ip in ips]

```

4. Include the debug toolbar `URLconf `in your u`rls.py`:

```python
from django.conf import settings
from django.conf.urls import include

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        ...
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

```

### Resources

- [Debug Django in VSCode Article](https://medium.com/django-unleashed/debug-django-in-vscode-cd9759e82618)
- [Django Debug Toolbar Documentation](https://django-debug-toolbar.readthedocs.io/en/latest/)

By following these steps, you should be able to effectively debug your Django application using VS Code and the Django Debug Toolbar.
