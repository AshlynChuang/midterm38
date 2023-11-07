from django.db import models
class Post(models.Model):
    STATUS = (
        ('Loaned', '已借出'),
        ('On shelf', '在架上'),
    )
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    synopsis = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-pub_date',)
        
    def __str__(self):
        return self.title