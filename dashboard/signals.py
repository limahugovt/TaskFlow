from django.db.models.signals import post_save
from django.dispatch import receiver
from authentication.models import Board, List

@receiver(post_save, sender=Board)
def create_related_models(sender, instance, created, **kwargs):
    if created:
        List.objects.create(board=instance, name='Pendentes')
        List.objects.create(board=instance, name='Em Andamento')
        List.objects.create(board=instance, name='Em Teste')
        List.objects.create(board=instance, name='Concluidas')
