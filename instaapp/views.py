from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, ImageUploadForm
from .models import Profile, Image
from cloudinary.forms import cl_init_js_callbacks

# Create your views here.
def index(request):
    images = Image.objects.all()
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully uploaded your pic!')
            return redirect('index')
    else:
        form = ImageUploadForm()



    # if request.method == "POST":
    #     form = ImageUploadForm(request.POST, request.FILES, instance=request.profile.image,)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, f'Successfully uploaded your pic!')
    #         return redirect('index')
    # else:
    #     form = ImageUploadForm(instance=request.profile.image)

    return render(request, 'index.html', {"images":images[::-1], "form": form })

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Successfully created account created for {username}! Please log in to continue')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
    images = Image.objects.all()

    # if request.method == "POST":   
    #     u_form = UserUpdateForm(request.POST, instance=request.user)
    #     p_form = ProfileUpdateForm(request.POST, request.FILES, 
    #     instance=request.user.profile)

    #     if u_form.is_valid() and p_form.is_valid():
    #         u_form.save()
    #         p_form.save()
    #         messages.success(request, f'Successfully updated your account!')
    #         return redirect('profile')

    
    # else:   
    #     u_form = UserUpdateForm(instance=request.user)
    #     p_form = ProfileUpdateForm(instance=request.user.profile)

    # context = {
    #     'u_form': u_form,
    #     'p_form': p_form
    # }   

    return render(request, 'users/profile.html', {"images":images[::-1]})



@login_required
def update(request):
    if request.method == "POST":   
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, 
        instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Successfully updated your account!')
            return redirect('profile')

    
    else:   
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/update.html', context)






