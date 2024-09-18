from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from .serializers import ContactMessageSerializer
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import base64
import requests
from django.core.mail import EmailMessage


@api_view(['GET'])
def product_list(request):
    """
    List all products or create a new product.
    """
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def product_commanded(request, pk):
    """
    Retrieve a single product by ID.
    """
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

@api_view(['POST'])
def contact_message(request):
    if request.method == 'POST':
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            contact_message = serializer.save()

            # Send email to admin
            send_mail(
                subject=f"New contact message from {contact_message.name}",
                message=f"Message:\n{contact_message.message}\n\nReply to: {contact_message.email}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],  # Admin email
            )

            # Send confirmation email to the user
            send_mail(
                subject="Thank you for contacting us",
                message="Thank you for reaching out to us. We have received your message and will get back to you shortly.",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[contact_message.email],  # User email
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




def get_image_base64(image_url):
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            return base64.b64encode(response.content).decode('utf-8')
        else:
            return None
    except Exception as e:
        return None

@csrf_exempt
def order(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            phone_number = data.get('phoneNumber')
            street_address = data.get('streetAddress')
            wilaya = data.get('wilaya')
            cart_items = data.get('cartItems')
            delivery_price = data.get('deliveryPrice')
            cart_total = data.get('cartTotal')
            total_price = data.get('totalPrice')

            # Email content with HTML formatting
            email_content = f"""
            <html>
            <body>
            <h1>New Order Received</h1>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Phone Number:</strong> {phone_number}</p>
            <p><strong>Street Address:</strong> {street_address}</p>
            <p><strong>Wilaya:</strong> {wilaya}</p>
            <h2>Cart Items:</h2>
            <ul>
            """

            for item in cart_items:
                image_base64 = get_image_base64(f"http://localhost:8000{item.get('image_url')}")
                img_tag = f'<img src="data:image/jpeg;base64,{image_base64}" width="100" height="100"/>' if image_base64 else ''
                email_content += f"""
                <li>
                    <strong>Product:</strong> {item.get('name')}<br>
                    <strong>Description:</strong> {item.get('description')}<br>
                    <strong>Size:</strong> {item.get('selectedSize')}<br>
                    <strong>Price:</strong> {item.get('price')} DA<br>
                    {img_tag}
                </li>
                """

            email_content += f"""
            </ul>
            <p><strong>Cart Total:</strong> {cart_total} DA</p>
            <p><strong>Delivery Price:</strong> {delivery_price} DA</p>
            <p><strong>Total Price:</strong> {total_price} DA</p>
            </body>
            </html>
            """

            subject = 'New Order Received'
            from_email = 'your-email@example.com'
            recipient_list = ['recipient@example.com']

            email = EmailMessage(
                subject,
                email_content,
                from_email,
                recipient_list,
            )
            email.content_subtype = 'html'  # Important to set the email type to HTML
            email.send()

            return JsonResponse({'message': 'Order received'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'message': 'Invalid request'}, status=400)
