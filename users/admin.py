from django.contrib import admin
from .models import Profile
# from django.utils.html import format_html
# from django.urls import reverse
# from django.shortcuts import redirect
# Register your models here.


admin.site.register(Profile)

# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'image', 'delete_image')

#     def delete_image(self, obj):
#         return format_html('<a class="button" href="{}">Delete Image</a>&nbsp;', 
#             reverse('admin:delete_profile_image', args=[obj.pk]))

#     delete_image.short_description = 'Image Actions'
#     delete_image.allow_tags = True

#     def get_urls(self):
#         from django.urls import path
#         urls = super().get_urls()
#         custom_urls = [
#             path('delete_image/<int:profile_id>/', self.admin_site.admin_view(self.process_delete_image), name='delete_profile_image'),
#         ]
#         return custom_urls + urls

#     def process_delete_image(self, request, profile_id, *args, **kwargs):
#         profile = Profile.objects.get(pk=profile_id)
#         if profile.image.name != 'default.png':
#             profile.image.delete(save=True)
#             profile.image = 'default.png'
#             profile.save()
#         return redirect(reverse('admin:blogApp'))