from django.contrib import admin
from .models import Farm, Field, Crop, Project, Task

# Registering the models to the admin panel
admin.site.register(Farm)
admin.site.register(Field)
admin.site.register(Crop)
admin.site.register(Project)
admin.site.register(Task)
