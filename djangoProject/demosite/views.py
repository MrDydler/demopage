from django.shortcuts import render
from demosite.models import RegistrationForm
from demosite.models import Product


def demo_page(request):
    print("demo view вызвался")
    # Отображаем продукты на главной странице
    products = Product.objects.all()
    success = False
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        registration_form = RegistrationForm(name=name, phone=phone, email=email, message=message)
        registration_form.save()
        
        success = True
        
    context = {
        'products': products,
        'success': success
    }
    
    return render(request, 'demo.html', context)
