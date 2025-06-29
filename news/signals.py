import json
import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_celery_beat.models import ClockedSchedule, PeriodicTask
from django.utils import timezone
from news.models import News

logger = logging.getLogger(__name__)

@receiver(post_save, sender=News)
def schedule_news_publish(sender, instance, created, **kwargs):
    """
    При создании News заполненным scheduled_time создаём одноразовый PeriodicTask.
    """
    logger.info("Singnal post_save for News triggered.")
    if created and instance.scheduled_time:
        logger.info("if statement for (created and scheduled_time) passed.")
        publish_time = instance.scheduled_time
        # Создаём или получаем ClockedSchedule на заданное время
        schedule, _ = ClockedSchedule.objects.get_or_create(
            clocked_time=publish_time,
        )
        task_name = f"publish_news_{instance.id}"
        # Создаём одноразовую задачу
        PeriodicTask.objects.get_or_create(
            name=task_name,
            task="news.tasks.publish_news",
            clocked=schedule,
            args=json.dumps([instance.id]),
            one_off=True,
            start_time=publish_time,
        )
        logger.debug(f"Scheduled publish_news for {instance.id} at {publish_time}")