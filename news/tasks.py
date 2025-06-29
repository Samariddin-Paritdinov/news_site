from celery import shared_task
from django.utils import timezone
from news.models import News

@shared_task
def publish_news(news_id: int):
    """
    Publishes a scheduled News item by setting is_active=True and updating publish_date.
    """
    try:
        news = News.objects.get(id=news_id)
    except News.DoesNotExist:
        return f"News with id {news_id} does not exist."

    # Activate and set publish_date to now
    news.is_active = True
    news.save()
