from .models import Gift
from celery import shared_task
from celery.utils.log import get_task_logger
import random
 
logger = get_task_logger(__name__)
 
@shared_task(bind=True)
def pick_winner(self, gift_id):
    gift = Gift.objects.get(id=gift_id)
    if gift.interested_users.length > 0:
        winner = random.choice(list(gift.interested_users.all()))
        gift.winner = winner
    gift.active = False
    gift.save()


@shared_task()
def print_expiration():
    logger.info('gift expired')
    print("gift expired")