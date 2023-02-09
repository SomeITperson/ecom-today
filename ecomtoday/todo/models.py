from django.db import models
import uuid
from django.core.exceptions import ValidationError

"""
Валидация на наличие uuid в базе
"""
def validate_id_exists(value):
    incident = Todo.objects.filter(uuid=value).exists()
    if incident:
        raise ValidationError('Значение uuid уже есть в базе')

"""
Генерация uuid длинной в 8 символов
"""
def generate_uuid():
    default_uuid = str(uuid.uuid4())
    uuid_short = default_uuid.split("-")[0]
    return uuid_short

class UUIDModel(models.Model):
    #uuid = models.UUIDField(editable=False, default=generate_uuid, validators=[validate_id_exists], unique=True)
    uuid = models.CharField(max_length=8, editable=False, default=generate_uuid, validators=[validate_id_exists], unique=True)
    
class Todo(UUIDModel):
    created = models.DateTimeField(verbose_name="Creation time", auto_now_add=True)
    body = models.TextField(verbose_name="Текст")
    active = models.BooleanField(verbose_name="Активно", default=True)

    class Meta:
        verbose_name = "Todo"
        verbose_name_plural = "Todos"

    def __str__(self):
        return str(self.uuid)