import uuid
from datetime import timedelta
from django.urls import reverse
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from account.models import User, Profile, Favorite, Subscription
from account.forms import RegistrationForm, ProfileForm, FavoriteForm, SubscriptionForm


def index(request):
    """
    Create index view
    :param request:
    :return index template:
    """
    template = 'account/index.html'
    return render(request, template)


# def register(request):
#     """
#     Create user registration view
#     :param request:
#     :return register template:
#     """
#     if request.method == 'POST':
#         register_form = RegisterForm(data=request.POST)
#         profile_form = ProfileForm(data=request.POST, files=request.FILES)
#         favorite_form = FavoriteForm(data=request.POST)
#         subscribe_form = SubscriptionForm(data=request.POST)
#
#         if register_form.is_valid() and profile_form.is_valid() and favorite_form.is_valid() and \
#                 subscribe_form.is_valid():
#             new_user = register_form.save(commit=False)
#             # Set password method handles password hashing
#             new_user.set_password(register_form.cleaned_data["password"])
#             new_user.save()
#
#             profile_form.user = Profile.objects.create(user=new_user)
#             profile_form.save()
#
#             # Save many-to-many relationship between user model and favorite model
#             Favorite.objects.create(user=new_user)
#             favorite_form.save()
#
#             # Set default subscription when new user performs registration
#             Subscription.objects.create(user=new_user, type='TR', valid_from=timezone.now(),
#                                         valid_to=timezone.now() + timedelta(days=14))
#             subscribe_form.save()
#             template = 'account/index.html'
#             return render(request, template)
#
#         user_form = RegisterForm()
#         profile_form = ProfileForm()
#         favorite_form = FavoriteForm()
#         subscribe_form = SubscriptionForm()
#         template = 'account/register.html'
#         context = {'user_form': user_form, 'profile_form': profile_form, 'favorite_form': favorite_form,
#                    'subscribe_form': subscribe_form}
#         return render(request, template, context)
#
#     else:
#         user_form = RegisterForm()
#         profile_form = ProfileForm()
#         favorite_form = FavoriteForm()
#         subscribe_form = SubscriptionForm()
#         template = 'account/register.html'
#         context = {'user_form': user_form, 'profile_form': profile_form, 'favorite_form': favorite_form,
#                    'subscribe_form': subscribe_form}
#         return render(request, template, context)


def register(request):
    """
    Create user registration view
    :param request:
    :return register template:
    """
    if request.method == 'POST':
        registration_form = RegistrationForm(data=request.POST)
        if registration_form.is_valid():
            new_user = registration_form.save(commit=False)
            # set password method handles password hashing
            new_user.set_password(registration_form.cleaned_data["password"])
            new_user.save()
            template = "account/index.html"
            context = {"new_user": new_user}
            return render(request, template, context)
    else:
        user_form = RegistrationForm()
        template = "account/register.html"
        context = {"user_form": user_form}
        return render(request, template, context)


@login_required
def dashboard(request, username, pk):
    """
    Create user dashboard view
    :param request:
    :return dashboard template:
    """
    user = get_object_or_404(User, username=username, pk=pk)
    subscription = Subscription.objects.select_related("user").get(user__pk=pk)
    profile = Profile.objects.select_related("user").get(user__pk=pk)
    favorites = user.user_favorites.all()
    template = 'account/dashboard.html'
    context = {'user': user, 'subscription': subscription, 'profile': profile, 'favorites': favorites}
    return render(request, template, context)
