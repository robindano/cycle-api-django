from .models import Gift
from celery import shared_task
from celery.utils.log import get_task_logger
import random
 
logger = get_task_logger(__name__)
 
@shared_task(bind=True)
def pick_winner(self, gift_id):
    gift = Gift.objects.get(id=gift_id)
    interested_list = list(gift.interested_users.all())
    if interested_list.length > 0:
        winner = random.choice(interested_list)
        gift.winner = winner
    gift.active = False
    gift.save()


@shared_task()
def print_expiration():
    logger.info('gift expired')
    print("gift expired")