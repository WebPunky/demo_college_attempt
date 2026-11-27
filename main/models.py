from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator


class Services(models.Model):
    title = models.CharField(blank=True, max_length=30)
    desc = models.TextField(blank=True)
    image = models.ImageField(
        upload_to="services/%Y/%m/",
        blank=True,
        null=True
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.title

class Orders(models.Model):
    class Status(models.TextChoices):
        NEW = "new", "новый"
        IN_PROGRESS = "in_progress", "в работе"
        DONE = "done", "выполнен"
        CANCELL = "cancell", "отменен"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="orders"
    )
    service = models.ForeignKey(
        Services,
        on_delete=models.PROTECT,
        related_name="prders"
    )
    status = models.CharField(max_length=20, choices=Status, default=Status.NEW)
    cancel_reason = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    scheduled_at = models.DateTimeField()

    def __str__(self):
        return f"Заявка {self.pk} ({self.get_status_display()})"

    def clean(self) -> None:
        if self.status == self.Status.CANCELL and not self.cancel_reason:
            raise ValidationError({"cancell reason": "укажите причину отмены"})

    def cancel(self) -> None:
        if self.status != self.Status.NEW:
            raise ValueError("Отменить можно только новую заявку")
        self.status = self.Status.CANCELL
        self.cancel_reason = "Отменено клиентом"
        self.save(update_fields=["status", "cancel_reason"])

class Review(models.Model):
    order = models.OneToOneField(
        Orders,
        on_delete=models.CASCADE,
        related_name="review"   
    )
    rating = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Отзыв на {self.order}: {self.rating}"
