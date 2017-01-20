from django.contrib import admin

from .models import *

admin.site.register(BusinessType)
admin.site.register(District)
admin.site.register(MissionTypes)
admin.site.register(Person)
admin.site.register(PostTypes)
admin.site.register(RegionOfResponsibility)
admin.site.register(Tasks)
admin.site.register(PersonHasTasks)
