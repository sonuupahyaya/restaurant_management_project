import string
import secrets
from .models import Coupon  # Assuming you have a Coupon model with a 'code' field
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
import logging

# Configure logging
logger = logging.getLogger(__name__)

def send_order_confirmation_email(order_id, customer_email, customer_name, total_price, items_list):
    """
        Sends an order confirmation email to the customer.

            Args:
                    order_id (int): ID of the order.
                            customer_email (str): Customer's email address.
                                    customer_name (str): Name of the customer.
                                            total_price (float): Total price of the order.
                                                    items_list (list): List of ordered items (strings).

                                                        Returns:
                                                                dict: Status message indicating success or failure.
                                                                    """

                                                                        subject = f"Order Confirmation - Order #{order_id}"
                                                                            message = (
                                                                                    f"Dear {customer_name},\n\n"
                                                                                            f"Thank you for your order!\n\n"
                                                                                                    f"Order ID: {order_id}\n"
                                                                                                            f"Items:\n  - " + "\n  - ".join(items_list) + "\n\n"
                                                                                                                    f"Total Price: ₹{total_price}\n\n"
                                                                                                                            f"We’re preparing your order and will notify you once it's ready for delivery.\n\n"
                                                                                                                                    f"Best regards,\n"
                                                                                                                                            f"The Restaurant Team"
                                                                                                                                                )
                                                                                                                                                    from_email = settings.DEFAULT_FROM_EMAIL
                                                                                                                                                        recipient_list = [customer_email]

                                                                                                                                                            try:
                                                                                                                                                                    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
                                                                                                                                                                            logger.info(f"Order confirmation email sent successfully to {customer_email} for Order #{order_id}.")
                                                                                                                                                                                    return {"success": True, "message": "Email sent successfully."}

                                                                                                                                                                                        except BadHeaderError:
                                                                                                                                                                                                logger.error(f"Invalid header found while sending email to {customer_email} for Order #{order_id}.")
                                                                                                                                                                                                        return {"success": False, "message": "Invalid header found."}

                                                                                                                                                                                                            except Exception as e:
                                                                                                                                                                                                                    logger.error(f"Error sending email to {customer_email} for Order #{order_id}: {e
                                                                                                                                                                                                                    
def generate_coupon_code(length=10):
    """
        Generate a unique alphanumeric coupon code.
            
                Args:
                        length (int): Length of the generated code (default: 10)
                            
                                Returns:
                                        str: Unique coupon code
                                            """
                                                characters = string.ascii_uppercase + string.digits  # A-Z + 0-9

                                                    while True:
                                                            # Generate random code
                                                                    code = ''.join(secrets.choice(characters) for _ in range(length))

                                                                            # Check if the code already exists in the database
                                                                                    if not Coupon.objects.filter(code=code).exists():
                                                                                                return code


def get_daily_sales_total(date):
    """
        Calculate total sales for a specific date.

            Args:
                    date (datetime.date): The date for which to calculate sales.

                        Returns:
                                Decimal or float: The total sales amount for the given date.
                                    """
                                        result = Order.objects.filter(created_at__date=date).aggregate(
                                                total_sum=Sum('total_price')
                                                    )['total_sum']

                                                        return result or 0
