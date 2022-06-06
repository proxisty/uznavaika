from django.db import models


class Lesson(models.Model):
    title = models.CharField(max_length=50, verbose_name='Имя урока')
    description = models.CharField(max_length=500, null=True)
    big_description = models.TextField(verbose_name='Длинное описание уроков')
    teacher = models.ManyToManyField('Teacher', verbose_name='Преподаватель')
    image = models.ImageField(upload_to='lessons/', verbose_name='Изображение урока')
    slug = models.SlugField(unique=True)  # endpoint в нашем url к примеру /uznavaika/rastishka - последнее это slug

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Price(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название цены')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Цена урока')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'


class Teacher(models.Model):
    name = models.CharField(max_length=40, verbose_name='Имя преподавателя')
    image = models.ImageField(upload_to='teachers/', verbose_name='Изображение преподавателя')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class FeedBackHome(models.Model):
    """Форма обратной связи """
    name = models.CharField(verbose_name='Название модели', max_length=120)
    email = models.CharField(verbose_name='Email', max_length=120, blank=True, null=True)
    phone = models.CharField(verbose_name='Телефон', max_length=15)
    description = models.CharField(verbose_name='Описание', max_length=120, blank=True, null=True)
    call_time = models.CharField('Время для звонка', max_length=120, blank=True, null=True)
    create_at = models.DateTimeField('Время создания обращения', auto_now_add=True)

    def __str__(self):
        return f'Имя:{self.name}, номер:{self.phone}'

    class Meta:
        verbose_name = 'Форма обратной связи'
        verbose_name_plural = 'Формы обратной связи'
