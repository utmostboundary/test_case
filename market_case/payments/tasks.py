from django.core.mail import send_mail

from cart.models import Cart
from celery_app import app
from payments.utils import check_item_quantity, get_payment_link, clear_cart


@app.task()
def send_order_mail_task(cart_id: int, email) -> str:
    print(email)
    cart = Cart.objects.get(id=cart_id)
    check = check_item_quantity(cart)
    if check:
        return f'Продукта {check} нет в таком количестве'
    if cart.items.exists():
        response = get_payment_link(cart, email)
        subject = "Оплата"
        message = f"Ссылка: {response['url']}, номер заказа: {response['orderId']}"
        recipient_list = [email]
        try:
            send_mail(subject=subject,
                      message=message,
                      from_email=None,
                      recipient_list=recipient_list,
                      fail_silently=False)
            clear_cart(cart)
            return 'Письмо успешно отправлено'
        except Exception as e:
            return f'Ошибка с отправкой письма: {str(e)}'
    return 'Пустая корзина'
