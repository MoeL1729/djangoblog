from django.db import models

# Create your models here.

class Post(models.Model):
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True,null=True) # 1대N /지워지거나 기본값 NULL /값이없거나 null 이 괜찮다
    tags = models.ManyToManyField('Tag', blank=True) #N대N
    title = models.CharField('TITLE', max_length=50)
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple one-line text.')
    # charfield 는 null=true 를 안해주는게 좋다
    image = models.ImageField('IMAGE', upload_to='blog/%Y/%m/', blank=True, null=True)
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DT', auto_now_add=True)
    update_dt = models.DateTimeField('UPDATE DT', auto_now=True) #장고에서 자동으로 채워주기auto_now
    like = models.PositiveSmallIntegerField('LIKE',default=0)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(unique=True, max_length=50)
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple one-line text.')

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    #coment 테이블이 지워진경우cascade 하면 포스트도 같이 지워준다는 뜻
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DT', auto_now_add=True)
    update_dt = models.DateTimeField('UPDATE DT', auto_now=True)  # 장고에서 자동으로 채워주기auto_now


    @property
    def short_content(self):
        return self.content[:10]

    def __str__(self):
        return self.short_content
