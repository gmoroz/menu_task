from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название меню")
    url = models.CharField(max_length=200, verbose_name="url меню")
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, default=None, related_name="child"
    )

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"
