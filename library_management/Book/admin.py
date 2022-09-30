from django.contrib import admin

from .models import Book,student

class BookAdmin(admin.ModelAdmin):
    pass
admin.site.register(Book, BookAdmin)

class StudentAdmin(admin.ModelAdmin):
    pass
admin.site.register(student, StudentAdmin)

