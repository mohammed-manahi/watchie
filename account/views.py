from django.shortcuts import render, get_object_or_404
from account.forms import RegisterForm
from django.contrib.auth.decorators import login_required
from account.models import User, Profile, Favorite, Subscription


def index(request):
    """
    Create index view
    :param request:
    :return index template:
    """
    template = 'account/index.html'
    return render(request, template)


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
