from django.db import models
from django.urls import reverse_lazy


class Menu(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название меню", unique=True)
    url = models.CharField(
        max_length=200, verbose_name="url меню", null=True, blank=True
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
        related_name="child",
        verbose_name="Родительское меню",
    )

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"

    def __str__(self):
        return self.title

    def save(self):
        parents = [parent.title.lower() for parent in self.get_parents()]
        url = "-".join(parents + [self.title.lower()])
        self.url = reverse_lazy("menu", kwargs={"url": url})
        super(Menu, self).save()

    def get_parents(self):
        if self.parent:
            return self.parent.get_parents() + [self.parent]
        return []

    def get_children(self):
        return self.child.all()
