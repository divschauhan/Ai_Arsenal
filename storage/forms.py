from django import forms
from .models import AiModel, ReviewAiModel, ModelEditForm


class ModelUploadForm(forms.ModelForm):
    class Meta:
          model = AiModel
          fields = ('name','summary','category','model_file','model_image')


class ReviewUploadForm(forms.ModelForm):
    class Meta:
          model = ReviewAiModel
          fields = ('title','detail','rating')


class ModelEditForm(forms.ModelForm):
    class Meta:
          model = AiModel
          fields = ('name','summary','category','model_file','model_image')




