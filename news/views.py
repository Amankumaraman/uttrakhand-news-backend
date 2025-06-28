import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def fetch_live_news(request):
    API_KEY = "80c5a3b849484cf29f8be1ad3ae70f80"
    url = (
        f"https://newsapi.org/v2/everything?"
        f"q=uttarakhand&"
        f"pageSize=10&"
        f"sortBy=publishedAt&"
        f"language=en&"
        f"apiKey={API_KEY}"
    )

    try:
        response = requests.get(url)
        data = response.json()
        articles = data.get("articles", [])

        # Optional: Format the news to only send required fields
        formatted_news = [
            {
                "title": article.get("title"),
                "short_description": article.get("description"),
                "full_description": article.get("content"),
                "source": article.get("source", {}).get("name"),
                "url": article.get("url"),
                "published_at": article.get("publishedAt"),
                'category': article.get("Category"),
            }
            for article in articles
        ]

        return Response(formatted_news)
    except Exception as e:
        return Response({"error": str(e)}, status=500)
