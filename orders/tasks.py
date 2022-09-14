from django.core.mail import send_mail
from .models import Order
from myshop.celery import app


@app.task
def order_created(order_id):
    """
    Задача для отправки уведомления по электронной почте при успешном создании заказа.
    """
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