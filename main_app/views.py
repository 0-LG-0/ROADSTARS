from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import User, Post, Event
from django.urls import reverse_lazy, reverse
from django.db import models



def home(request):
    posts = Post.objects.all()
    public_events = Event.objects.all().filter(public=True)
    earliest_event = Event.objects.all().order_by('event_date').first()
    public_earliest_event = public_events.order_by('event_date').first()
    most_attendees = Event.objects.all().order_by('attendees').last()
    public_most_attendees = public_events.order_by('attendees').last()
    most_participants = Event.objects.all().order_by('participants').last()
    public_most_participants = public_events.order_by('participants').last()
    return render(request, 'home.html', { 'posts': posts, 'earliest_event': earliest_event, 'most_attendees': most_attendees, 'public_earliest_event': public_earliest_event, 'public_most_attendees': public_most_attendees, 'most_participants': most_participants, 'public_most_participants': public_most_participants })
        
def post_index(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/index.html', {'posts': posts})
        
def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'posts/detail.html', { 'post': post })
    
class Login(LoginView):
    template_name= 'users/login.html'
  
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid Entry!'  
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'users/signup.html', context)

class PostCreate(CreateView):
    model = Post
    fields = ['image_URL', 'upload_image', 'post_text', 'public']
    template_name = 'posts/form.html'
    success_url = '/posts/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
def image(request):
    if request.method == 'POST':
        form = PostCreate(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PostCreate()
    return render(request, 'form.html', {'form': form})
    
def user_index(request):
    posts = Post.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'posts/user_index.html', { 'posts': posts })

def user_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'posts/user_detail.html', { 'post': post })

class PostUpdate(UpdateView):
    model = Post
    fields = ['image_URL', 'upload_image', 'post_text']
    template_name = 'posts/form.html'
    success_url = '/posts/user/'
    
class PostDelete(DeleteView):
    model = Post
    template_name = 'posts/post_confirm_delete.html'
    success_url = '/posts/user/'

def event_index(request):
    events = Event.objects.all().order_by('event_date')
    return render(request, 'events/index.html', { 'events': events })

def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'events/detail.html', { 'event': event })

def event_user_index(request):
    events = Event.objects.filter(user=request.user).order_by('event_date')
    return render(request, 'events/user_index.html', { 'events': events })

def event_user_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'events/user_detail.html', { 'event': event })

class EventCreate(CreateView):
    model = Event
    fields = ['public', 'event_date', 'image_URL', 'upload_image', 'title', 'description', 'instructions_and_rules', 'address_and_contact', 'participating_and_attending', 'attendees', 'participants']
    template_name = 'events/form.html'
    success_url = '/events/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class EventUpdate(UpdateView):
    model = Event
    fields = ['public', 'event_date', 'image_URL', 'upload_image', 'title', 'description', 'instructions_and_rules', 'address_and_contact', 'participating_and_attending', 'attendees', 'participants']
    template_name = 'events/form.html'
    success_url = '/events/user/'
    
class EventDelete(DeleteView):
    model = Event
    template_name = 'events/event_confirm_delete.html'
    success_url = '/events/user/'
    
class UserDelete(DeleteView):
    model = User
    template_name = 'users/user_confirm_delete.html'
    success_url = '/'
    
class UserUpdate(UpdateView):
    model=User
    fields = ['username']
    template_name = 'users/signup.html'
    success_url = '/user/profile'

def user_profile(request):
    user = request.user
    return render(request, 'users/profile.html', {'user': user })