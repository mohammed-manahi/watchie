import stripe
from decimal import Decimal

from django.contrib import messages
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from account.models import User, Subscription

# Load stripe api configuration
stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION


@login_required
def subscribe(request):
    """
    Create subscribe view
    :param request:
    :return:
    """
    user_id = request.user.id
    current_plan = Subscription.objects.get(user_id=user_id)
    template = 'payment/subscribe.html'
    context = {'current_plan': current_plan}
    return render(request, template, context)


@login_required
def standard_subscription(request):
    """
    Create standard subscription payment view
    :param request:
    :return:
    """
    user_id = request.user.id
    subscription_plan = Subscription(type=Subscription.STANDARD)
    if request.method == 'POST':
        success_url = request.build_absolute_uri(reverse('payment:completed'))
        cancel_url = request.build_absolute_uri(reverse('payment:canceled'))
        session_data = {
            'mode': 'payment',
            'success_url': success_url,
            'cancel_url': cancel_url,
            'line_items': []
        }
        session_data['line_items'].append({
            'price_data': {
                'unit_amount': int(19 * Decimal('100')),
                'currency': 'usd',
                'product_data': {
                    'name': subscription_plan.get_type_display()+ ' ' + 'Subscription',
                },
            },
            'quantity': 1,
        })
        session = stripe.checkout.Session.create(**session_data)
        return redirect(session.url, code=303)
    else:
        return render(request, 'payment/standard_subscription.html', locals())


@login_required
def premium_subscription(request):
    """
    Create premium subscription payment view
    :param request:
    :return:
    """
    user_id = request.user.id
    subscription_plan = Subscription(type=Subscription.PREMIUM)
    if request.method == 'POST':
        success_url = request.build_absolute_uri(reverse('payment:completed'))
        cancel_url = request.build_absolute_uri(reverse('payment:canceled'))
        session_data = {
            'mode': 'payment',
            'success_url': success_url,
            'cancel_url': cancel_url,
            'line_items': []
        }
        session_data['line_items'].append({
            'price_data': {
                'unit_amount': int(39 * Decimal('100')),
                'currency': 'usd',
                'product_data': {
                    'name': subscription_plan.get_type_display() + ' ' + 'Subscription',
                },
            },
            'quantity': 1,
        })
        session = stripe.checkout.Session.create(**session_data)
        return redirect(session.url, code=303)
    else:
        return render(request, 'payment/standard_subscription.html', locals())


def payment_completed(request):
    """
    Create successful payment view
    :param request:
    :return:
    """
    return render(request, 'payment/completed.html')


def payment_canceled(request):
    """
    Create canceled payment view
    :param request:
    :return:
    """
    return render(request, 'payment/canceled.html')
