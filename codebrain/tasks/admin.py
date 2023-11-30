from django.contrib import admin
from .models import Tag, Task, Solutiuon, Complexity, ProgLang, Comment


admin.site.register(Tag)
admin.site.register(Task)
admin.site.register(Solutiuon)
admin.site.register(Complexity)
admin.site.register(ProgLang)
admin.site.register(Comment)
