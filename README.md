# Baidu Hot Search Service

A Python service that fetches and provides real-time trending topics from Baidu's hot search rankings.

## Features

- Fetches real-time trending topics from Baidu
- Returns top 10 hot search items
- Easy to integrate with other services

## Requirements

- Python 3.6+
- FastMCP
- Requests
- BeautifulSoup4

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Run the server:

```bash
python baidu_hotsearch_server.py
```

The service provides a tool that returns the current top 10 trending topics from Baidu's hot search rankings.

## Response Format

The service returns a list of dictionaries containing trending topics:

```python
[
    {"title": "First trending topic"},
    {"title": "Second trending topic"},
    # ...
]
```

In case of errors, it returns:

```python
[{"error": "Error message"}]
```

## License

MIT