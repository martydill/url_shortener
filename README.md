URL Shortener is a sample Python/Flask/Flask-RESTful/SQLAlchemy/React app. It's a fully functional URL shortener with a React.js frontend that calls a JSON-based API.

USAGE
----
*python backend/start.py*

*Creating shortened URLs*
```
curl -d "url=http://code-ninja.org" http://localhost:5000/urls
```
```
{
  "created_date": "Thu, 30 Jul 2015 04:20:51 GMT",
  "destination_url": "http://code-ninja.org",
  "id": 2,
  "short_url": "5Y6Sf"
}
```

*Retrieving URLs*
```
 curl http://localhost:5000/urls
```
```
{
  "page": 1,
  "total": 1234,
  "urls": [
    {
      "created_date": "Mon, 27 Jul 2015 23:30:45 GMT",
      "destination_url": "http://google.ca",
      "id": 1,
      "short_url": "asdfz"
    },
    ...
}
```

*Retrieving URL details*
```
 curl http://localhost:5000/urls/<url_id>
```

*Retrieving URL hits*
```
 curl http://localhost:5000/urls/<url_id>/hits
```
```
{
  "hits": [
    {
      "created_date": "Thu, 30 Jul 2015 04:02:56 GMT",
      "id": 12,
      "ip_address": "127.0.0.1",
      "referrer": null,
      "user_agent": "curl/7.37.1"
    }
    ...
  ],
  "page": 1,
  "total": 1234
}
```

*Retrieving URL stats*
```
 curl http://localhost:5000/urls/<url_id>/stats
```
```
{
  "destination_url": "http://google.ca",
  "hit_count": 12,
  "id": 1,
  "referrers": [
    {
      "": 12
    }
  ],
  "short_url": "asdfz",
  "user_agents": [
    {
      "IE": 2
    },
    {
      "Mozilla": 1
    },
    {
      "curl/7.37.1": 9
    }
  ]
}
```

TODO
----
* Switch to a real database!
* Add more features to the frontend!
