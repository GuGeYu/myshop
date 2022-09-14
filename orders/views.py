from django.shortcuts import render
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.models import Cart
from .tasks import order_created
from django.core.mail import send_mail


def email_sent(order_id):
    order = Order.objects.get(id=order_id)
    subject = 'Номер заказа: {}'.format(order_id)
    message = 'Уважаемый {},\n\nВаш заказ успешно оформлен\
                    Номер вашего заказа {}.'.format(order.first_name,
                                                    order.id)
    mail_sent = send_mail(subject,
                          message,
                          'poltergeystgogy1@yandex.ru',
                          [order.email])
    return mail_sent



def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            # order_created.delay(order.id)
            email_sent(order.id)
            return render(request, 'orders/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/create.html', {'cart': cart, 'form': form})
