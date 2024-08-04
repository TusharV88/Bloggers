from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, PostForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import BlogPost
from mongoengine.errors import DoesNotExist, ConnectionError

def home_page(request):
    try:
        posts = BlogPost.objects.all()
        return render(request, 'blog/home.html', {'posts': posts})
    except DoesNotExist as e:
        print(str(e))
        return render(request, 'blog/home.html', {'posts': [], 'error': 'No blog posts found'})
    except ConnectionError as e:
        print(str(e))
        return render(request, 'blog/home.html', {'posts': [], 'error': 'Database connection error'})
    except Exception as e:
        print(str(e))
        return render(request, 'blog/home.html', {'posts': [], 'error': 'An error occurred'})

def about_page(request):
    return render(request, 'blog/about.html')

def contact_page(request):
    return render(request, 'blog/contact.html')

def dashboard_page(request):
    if request.user.is_authenticated:
        posts = BlogPost.objects.all()
        return render(request, 'blog/dashboard.html', {'posts': posts})
    else:
        return redirect('/login')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                nm = form.cleaned_data['username']
                pw = form.cleaned_data['password']
                user = authenticate(username=nm, password=pw)
                if user is not None:
                    messages.success(request, 'Logged in successfully.')
                    login(request, user)
                    return redirect('/dashboard/')
                else:
                    messages.error(request, 'Invalid credentials.')
                    return redirect('/login')
            else:
                messages.error(request, 'Invalid credentials.')
                return render(request, 'blog/login.html', {'form': form})
        else:
            form = LoginForm()
            return render(request, 'blog/login.html', {'form': form})
    else:
        return redirect('/dashboard')

def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['username']
            fn = form.cleaned_data['first_name']
            ln = form.cleaned_data['last_name']
            em = form.cleaned_data['email']
            pw1 = form.cleaned_data['password1']
            user = User.objects.create_user(username=nm, password=pw1, email=em, first_name=fn, last_name=ln)
            user.save()
            messages.success(request, 'Account has been created successfully. Now, you can process to login.')
            return redirect('/login')
        else:
            return render(request, 'blog/signup.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('/')

def create_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            title = request.POST['title']
            desc = request.POST['description']
            post = BlogPost(title=title, description=desc)
            post.save()
            messages.success(request, 'Post has been created successfully.')
            return redirect('/dashboard')
        else:
            fm = PostForm()
            return render(request, 'blog/createpost.html', {'form': fm})
    else:
        return redirect('/login')

def edit_post(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            post = BlogPost.objects.get(id=id)
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post.title = form.cleaned_data['title']
                post.description = form.cleaned_data['description']
                post.save()
                messages.success(request, 'Post has been updated successfully.')
                return redirect('/dashboard')
        else:
            post = BlogPost.objects.get(id=id)
            form = PostForm(initial={'title': post.title, 'description': post.description})
            return render(request, 'blog/editpost.html', {"form": form, "id": id})
    else:
        return redirect("/login")

def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            post = BlogPost.objects.get(id=id)
            post.delete()
            messages.success(request, "Post has been deleted successfully!!")
            return redirect("/dashboard")
    else:
        return redirect("/login")
