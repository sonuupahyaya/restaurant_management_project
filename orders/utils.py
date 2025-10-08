import string
import secrets
from .models import Coupon  # Assuming you have a Coupon model with a 'code' field

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
                                                                                                