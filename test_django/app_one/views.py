from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from app_one import forms
from app_one import models
from app_one.models import FriendModel
from django.contrib.auth.models import User

class HomeView(TemplateView):
    template_name = 'app_one/home.html'

    def get(self, request):
        form = forms.HomeForm()
        # posts = models.PostModel.objects.all()
        posts = models.PostModel.objects.order_by('-created')
        users = User.objects.exclude(id=request.user.id)

        friend, created = FriendModel.objects.get_or_create(current_user=request.user)
        friends = friend.users.all()
        args = {'form':form,'posts':posts,'users':users,'friends':friends}

        return render(request, self.template_name, args)

    def post(self, request):
        form = forms.HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            text = form.cleaned_data['post']
            form = forms.HomeForm()
            return redirect('app_one:home')
        args = {'form':form, 'text':text}
        return render(request, self.template_name, args)

def change_friends(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        models.FriendModel.make_friend(request.user, friend)
    elif operation == 'remove':
        models.FriendModel.lose_friend(request.user, friend)
    return redirect('app_one:home')
