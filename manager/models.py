from django.db import models


class Technology(models.Model):
    name = models.CharField(max_length=150, verbose_name='Texnalogiya')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Texnalogiya '
        verbose_name_plural = 'Texnalogiyalar'


class Portfolio(models.Model):
    title = models.CharField(max_length=250, verbose_name='Sarlavhasi')
    slug = models.SlugField(max_length=250, unique=True, verbose_name='Identifikatori')
    description = models.TextField(default="Ma'lumot qo'shilmadi.", verbose_name='Tavsifi')
    url = models.CharField(max_length=50, unique=True, verbose_name='Havolasi')
    image = models.ImageField(upload_to='images/', verbose_name='Surati')
    technologies = models.ManyToManyField(Technology, related_name='technologies', verbose_name='Texnalogiyalari')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Qo\'shilgan vaqti')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Loyiha '
        verbose_name_plural = 'Loyihalar'
        ordering = ['-created_at']


class Comment(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.lastname} - {self.portfolio}"

    class Meta:
        verbose_name = 'Izoh '
        verbose_name_plural = 'Izohlar'
        ordering = ['-created_at']
