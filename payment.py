from flask import Blueprint, jsonify, request
import stripe

class PaymentProcessor:
    def __init__(self, secret_key):
        self.stripe_api_key = secret_key
        stripe.api_key = self.stripe_api_key

    def process_payment(self, token, amount, currency='usd', description='Example charge'):
        try:
            charge = stripe.Charge.create(
                amount=amount,  # Amount in cents
                currency=currency,
                source=token,
                description=description
            )
            return {'status': 'success', 'message': 'Payment processed successfully'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}


payment_bp = Blueprint('payment', __name__)


payment_processor = PaymentProcessor(secret_key="your_stripe_secret_key")

@payment_bp.route('/process_payment', methods=['POST'])
def process_payment():
    data = request.json
    token = data.get('token')
    amount = data.get('amount', 1000)  # Default amount is 1000 cents if not provided
    response = payment_processor.process_payment(token, amount)
    return jsonify(response)
