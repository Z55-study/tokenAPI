from django.db import models


class TokenT(models.Model):
    # id - primary key по дефолту создается колонка
    unique_hash = models.CharField(max_length=400, null=True)  # unique_hash - уникальный хэш
    tx_hash = models.CharField(max_length=400, null=True)  # tx_hash - хэш транзакции создания токена
    media_url = models.URLField(null=True)  # media_url - урл с произвольным изображением
    owner = models.CharField(max_length=400, null=True)  # owner - адрес пользователя в сети Ethereum

    class Meta:
        ordering = ['id']

    def __str_(self):
        return "Token for {}".format(self.name)
