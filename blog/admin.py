from django.contrib import admin
from blog.models import Blog, Category, Comment, Contact


class CommentInline(admin.StackedInline):
    model = Comment


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'category', 'posted')
    list_filter = ("status",)
    search_fields = ['title', 'content', 'category']
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [CommentInline]


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Contact)
