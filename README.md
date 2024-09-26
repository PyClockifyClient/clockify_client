# Clockify Client

# Simple API client for Clockify.
Python API client for Clockify. [Clockify API reference](https://clockify.me/developers-api)

- Base endpoints
  - Client
  - Project
  - Task  
  - Time Entry
  - User
  - Workspace
- Reports Endpoints
  - Reports
  - Shared reports


## 1. Installation

Add package to your project:

```
pip install clockify_client
```

## 2. Usage

```python
from clockify_client import Clockify


API_KEY = 'yourclockifyAPIkey'
API_URL = 'api.clockify.me/v1'

clockify = Clockify(API_KEY, API_URL)

workspaces = clockify.workspaces.get_workspaces()  # Returns list of workspaces.

```

## 3. More information
[Official Clockify API](https://docs.clockify.me/)