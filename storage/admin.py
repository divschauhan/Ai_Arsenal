from django.contrib import admin
from  .models import AiModel,ReviewAiModel,ModelEditForm

# Register your models here.

admin.site.register(AiModel)
admin.site.register(ReviewAiModel)
admin.site.register(ModelEditForm)


