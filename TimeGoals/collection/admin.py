from django.contrib import admin

#import my models
from collection.models import Profile


#set up atuomated slug creation
class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ('name', 'description',)
    prepopulated_fields={'slug':('name',)}

#register model
admin.site.register(Profile, ProfileAdmin)
