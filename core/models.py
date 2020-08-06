from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import uuid
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    content = RichTextField()
    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,max_length=30)
    writer = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    activation_key = models.SlugField(default="",editable=True,max_length=15,unique=True)

    def get_slug(self):
        uuid_value = str(uuid.uuid4())
        unique_slug = slugify(uuid_value[0:12])
        return unique_slug

    def __str__(self):
        return f'{self.user.username}'

    def save(self, *args, **kwargs):
        self.activation_key = self.get_slug()
        super().save(*args, **kwargs)

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import signals

@receiver(post_save,sender=User)
def save_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()

def delete_user(sender, instance=None, **kwargs):
    try:
        instance.user
    except User.DoesNotExist:
        pass
    else:
        instance.user.delete()
signals.post_delete.connect(delete_user, sender=Profile)
