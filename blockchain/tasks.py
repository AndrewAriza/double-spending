from celery.decorators import task
from celery.utils.log import get_task_logger
from blockchain.models import Blockchain

logger = get_task_logger(__name__)

@task(name="processing")
def processing():
    transaction_list = Blockchain.objects.filter(processed=False).order_by('created_at')
    for transaction in transaction_list:
        last_transaction = Blockchain.objects.filter(processed=True).order_by('-created_at').first()
        print('Processing :::: Transaction {0}'.format(transaction.pk))
        Blockchain.objects.filter(pk=transaction.pk).update(
            total= (last_transaction.total if last_transaction else 0) + transaction.value,
            processed=True
        ) 