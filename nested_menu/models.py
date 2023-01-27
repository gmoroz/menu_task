from django.db import models
from django.urls import reverse_lazy


class Menu(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название меню")
    url = models.CharField(max_length=200, verbose_name="url меню")
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, default=None, related_name="child"
    )

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"

    def __str__(self):
        return self.title

    def save(self):
        url = "-".join(self.get_parents()) + self.title
        self.url = reverse_lazy("index", kwargs={"url": url})
        super(Menu, self).save()

    def get_parents(self):
        if self.parent:
            return self.parent.get_parents() + [self.parent.title]
        return []

    def get_children(self):
        return self.child.all()
