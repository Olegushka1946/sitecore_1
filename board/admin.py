from django.contrib import admin
from . import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from board.models import Post, Category, Reply

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Reply)


# Register your models here.

class PostAdminForm(forms.ModelForm):
    context = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm