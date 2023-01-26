import uuid
from datetime import timedelta
from django.urls import reverse
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.models import User, Profile, Subscription
from account.forms import RegistrationForm, ProfileForm, SubscriptionForm, UserEditForm
from account.helpers import is_subscription_active
from activity.helpers import create_activity
from activity.models import Activity


def index(request):
    """
    Create index view
    :param request:
    :return index template:
    """
    template = 'account/index.html'
    return render(request, template)


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
            new_user.set_password(registration_form.cleaned_data['password'])
            new_user.save()
            if request.user.id == new_user.id:
                create_activity(new_user, 'You registered you account successfully')
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
    subscription = Subscription.objects.select_related('user').get(user__pk=pk)
    profile = Profile.objects.select_related("user").get(user__pk=pk)
    subscription_status = is_subscription_active(pk)
    last_day = timezone.now() - timedelta(hours=24)
    activities = Activity.objects.filter(user__pk=pk, created_at__gte=last_day)[:5]
    template = 'account/dashboard.html'
    context = {'user': user, 'subscription': subscription, 'profile': profile,
               'subscription_status': subscription_status, 'activities': activities}
    return render(request, template, context)


@login_required
def edit(request, pk):
    """
    Create user edit view
    :param request:
    :param pk:
    :return edit template:
    """
    user = get_object_or_404(User, pk=pk, is_active=True)
    if user:
        if request.method == 'POST':
            user_form = UserEditForm(data=request.POST, instance=request.user)
            profile_form = ProfileForm(data=request.POST, instance=request.user.profile, files=request.FILES)
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                create_activity(request.user, 'You have updated your account successfully')
                messages.success(request, "Your profile has been updated successfully")
            else:
                messages.error(request, "An Error occurred while updating your profile")
        else:
            user_form = UserEditForm(instance=request.user)
            profile_form = ProfileForm(instance=request.user.profile)

        template = "account/edit.html"
        context = {'user_form': user_form, 'profile_form': profile_form}
        return render(request, template, context)
    return HttpResponse('Not Found')
