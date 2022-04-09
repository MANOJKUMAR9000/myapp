from django.contrib import admin
from webapp.models import Books
# Register your models here.
class BooksAdmin(admin.ModelAdmin):
    list_display = ['Eunit','Elesson','Epoem','Eobj']

admin.site.register(Books,BooksAdmin)