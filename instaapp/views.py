from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, ImageUploadForm
from .models import Profile, Image, User, Subscribers, Follow, Comment, Like
from cloudinary.forms import cl_init_js_callbacks
from django.core.exceptions import ObjectDoesNotExist
from .email import send_welcome_email



# Create your views here.
@login_required

def index(request):
    images = Image.objects.all()
    users = User.objects.exclude(id=request.user.id)
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit = False)
            image.user = request.user.profile
            image.save()
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

    return render(request, 'index.html', {"images":images[::-1], "form": form, "users": users })

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data['email']


            recipient = Subscribers(name = username,email =email)
            recipient.save()
            send_welcome_email(username,email)


            messages.success(request, f'Successfully created account created for {username}! Please log in to continue')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
    # images = Image.objects.all()
    # images = request.user.profile.images.all()
    # images = request.user.images.all()


    images = request.user.profile.images.all()

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



def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"image.html", {"image":image})



@login_required
def search_profile(request):
    if 'profile' in request.GET and request.GET['profile']:
        search_term = request.GET.get("profile")
        searched_profiles = Profile.search_profile(search_term)
        # print('searched_profiles')

        message = f"{search_term}"
        
        return render(request, 'search.html', {"message":message,"searched_profiles": searched_profiles})

    else:
        message = "You haven't searched for any profile"

    return render(request, 'search.html', {'message': message})



def like_post(request):
    user = request.user
    if request.method == 'POST':
        image_id = request.POST.get('image_id')
        img_obj = Image.objects.get(id = image_id)

        if user in img_obj.liked.all():
            img_obj.liked.remove(user)
        else:
            img_obj.liked.add(user)

        like, created = Like.objects.get_or_create(user = user, image_id = image_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'

            else:
                like.value = 'Like'

        like.save()


    
    return redirect(request, 'index.html')