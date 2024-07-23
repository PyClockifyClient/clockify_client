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
from clockify_client import ClockifyClient


API_KEY = 'yourclockifyAPIkey'
API_URL = 'api.clockify.me/v1'

client = ClockifyClient(API_KEY, API_URL)

workspaces = client.workspaces.get_workspaces()  # Returns list of workspaces.

```
