from .models import Gift
from celery import shared_task
from celery.utils.log import get_task_logger
import random
 
logger = get_task_logger(__name__)
 
@shared_task(bind=True)
def pick_winner(gift_id):
    gift = Gift.objects.get(id=gift_id)
    winner = random.choice(list(gift.interested_users.all()))
    gift.winner = winner
    gift.active = False
    gift.save()
    logger.info('winner picked')
    print(f'gift: {gift.id} winner: {winner}')
    return winner

@shared_task()
def print_expiration():
    logger.info('gift expired')
    print("gift expired")