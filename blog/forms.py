from django import forms
from .models import Message

# Создаем контактную форму
class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwards):
        super(ContactForm, self).__init__(*args, **kwards)
        # Прописываем новые названия для полей
        self.fields['subject'].label = "Тема письма"
        self.fields['email'].label = "Ваша почта"
        self.fields['text'].label = "Текст сообщения"

    class Meta:
        # Указываем модель
        model = Message
        # Выводим поля в форме, которые нам нужны
        fields = ['subject', 'email', 'text']
