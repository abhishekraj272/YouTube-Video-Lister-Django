# YouTube Video Lister - Django

A python app which searchs predefined query on YouTube using YT Data API and saves it in MongoDB and lists it on dashboard.

It searches asynchronously in backgroud using Python asyncio and threading library.

Predefined search query: "cricket"

Time Interval for searching: 60sec


## Starting Server Locally
```bash
git clone https://github.com/abhishekraj272/youtube-video-lister-django.git

cd youtube-video-lister-django

pip3 install -r requirements.txt

# MacOS or Linux
python3 manage.py runserver


# Windows
python manage.py runserver
```

## API

```
1. GET /api/v1/video/data
2. GET /dashboard
2. GET /admin
```

## Features
1. Shuffles through the provided API Key set every time it searches.
2. The data fetched from YT are latest.

## Tools Used:
1. Django
2. Django Rest Framework