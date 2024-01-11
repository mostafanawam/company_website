from django.contrib import admin

from .models import *

class CompanyAdmin(admin.ModelAdmin):  
    list_display = (
        "id",
        "email",
        "phone"    
    )
admin.site.register(Company,CompanyAdmin)

class SocialLinksAdmin(admin.ModelAdmin):  
    list_display = (
        "id",
        "name",
        "icon",
        "url"  
    )
admin.site.register(SocialLinks,SocialLinksAdmin)




class ContactUsAdmin(admin.ModelAdmin):  
    list_display = (
        "id",
        "full_name",
        "email",
        "subject",
        "created_at"
    )
admin.site.register(ContactUs,ContactUsAdmin)



