from django.shortcuts import render, get_object_or_404, redirect
from .models import News
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, \
    DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm


# Create your views here.

# Обработка страницы контактов
def contacts(request):
    # Если есть POST данные, то обрабатываем их
    if request.method == "POST":
        # Получаем все данные
        form = ContactForm(request.POST)
        # Проверяем на правильность
        if form.is_valid():
            # Если все хорошо, то сохраняем данные в БД,
            form.save()

            # а также создаем отправку письма.
            # В качестве значений для письма берем данные из формы
            subject = form.cleaned_data.get('subject')
            plain_message = form.cleaned_data.get('text')
            from_email = f'From <{form.cleaned_data.get("email")}>'
            to = 'grebenev-81@mail.ru'

            # Отправляем письмо
            send_mail(subject, plain_message, from_email, [to])

            # Выводим успешное сообщение
            messages.success(request, 'Сообщение было успешно отправлено')
            # Делаем редирект
            return redirect('contacts')
    else:
        # Если пост данные не передаются, то просто
        # создаем объект на основе класса с формой.
        # И далее все эти данные выводим на странице шаблона
        form = ContactForm()
        return render(request, 'blog/contacts.html', {'title':'Контакты',
                                                      'form': form})

class ShowNewsView(ListView):
    model = News
    template_name = 'blog/home.html'
    context_object_name = 'news'
    ordering = ['-date']
    paginate_by = 2

    def get_context_data(self, **kwargs):
        ctx = super(ShowNewsView, self).get_context_data(**kwargs)

        ctx['title'] = 'Главная'
        return ctx

class UserAllNewsView(ListView):
    model = News
    template_name = 'blog/user_news.html'
    context_object_name = 'news'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return News.objects.filter(auther=user).order_by('-date')

    def get_context_data(self, **kwargs):
        ctx = super(UserAllNewsView, self).get_context_data(**kwargs)

        ctx['title'] = f"Статьи пользователя {self.kwargs.get('username')}"
        return ctx

class NewsDetailView(DetailView):
    model = News
    template_name = 'blog/news_detail.html'

    def get_context_data(self, **kwargs):
        ctx = super(NewsDetailView, self).get_context_data(**kwargs)

        ctx['title'] = News.objects.get(pk=self.kwargs['pk'])
        return ctx

class CreateNewsView(LoginRequiredMixin, CreateView):
    model = News
    template_name = 'blog/create_news.html'

    fields = ['title', 'text', ]

    def form_valid(self, form):
        form.instance.auther = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(CreateNewsView, self).get_context_data(**kwargs)

        ctx['title'] = 'Добавление статьи'
        ctx['btn_txt'] = 'Добавить статью'
        return ctx

class UpdateNewsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    template_name = 'blog/create_news.html'

    fields = ['title', 'text', ]

    def form_valid(self, form):
        form.instance.auther = self.request.user
        return super().form_valid(form)

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.auther:
            return True
        return False

    def get_context_data(self, **kwargs):
        ctx = super(UpdateNewsView, self).get_context_data(**kwargs)

        ctx['title'] = 'Обновление статьи'
        ctx['btn_txt'] = 'Обновить статью'
        return ctx

class DeleteNewsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    success_url = '/'
    template_name = 'blog/delete-news.html'

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.auther:
            return True
        return False

def services(request):
    data = {
        'title': 'Услуги',
    }
    return render(request, 'blog/servises.html', data)

# def contacts(request):
#     data = {
#         'title': 'Контакты',
#     }
#     return render(request, 'blog/contacts.html', data)
