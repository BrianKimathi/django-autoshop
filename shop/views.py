from django.shortcuts import render, redirect
from .models import Product, Category, Comment, Slide, Vehicle, Contacts
from django.db.models import Q
from random import sample
from django.shortcuts import render, get_object_or_404




# Create your views here.
def index(request):
    # Get all products from the database
    all_products = Product.objects.all()
    # Randomly sample six products
    random_products = sample(list(all_products), min(6, len(all_products)))
    slides = Slide.objects.all()
    categories = Category.objects.filter(parent_id=None)
    vehicles = Vehicle.objects.all()
    comments = Comment.objects.all()

    context = {
        'random_products': random_products,
        'slides': slides,
        'categories': categories,
        'vehicles': vehicles,
        'comments': comments,
    }
    return render(request, 'index.html', context)

def submit_comment(request):
    if request.method == 'POST':
        commenter = request.POST.get('name')
        comment_text = request.POST.get('comment_text')
        # Create a new Comment object and save it to the database
        Comment.objects.create(name=commenter, comment_text=comment_text)
        # Redirect the user back to the index page after submitting the comment
        return redirect('index')
    else:
        # If the request method is not POST, redirect to a different page or handle it as needed
        return redirect('index') 

def products(request):
    category_id = request.GET.get('category_id')
    subcategory_id = request.GET.get('subcategory_id')

    print(f"Sub Category id is: {subcategory_id}")
    
    main_categories = Category.objects.filter(parent_id=None)
    selected_category = None
    selected_subcategory = None  # Add this line
    subcategories = None
    products = Product.objects.all()

    print(f"Category id is: {category_id}")
    
    if category_id and category_id != 'all':
        selected_category = get_object_or_404(Category, id=category_id)
        products = products.filter(category=selected_category)
        if selected_category:
            subcategories = Category.objects.filter(parent_id=category_id)
    
    if subcategory_id:
        selected_subcategory = get_object_or_404(Category, id=subcategory_id)  # Get the subcategory object
        products = products.filter(category=selected_subcategory)  # Filter products by the subcategory object

    # print(f"Selected category is: {selected_category.title}")
    print(f"Sub categories are: {selected_subcategory}")

    context = {
        'main_categories': main_categories,
        'selected_category': selected_category,
        'subcategories': subcategories,
        'products': products,
        'selected_subcategory_id': subcategory_id,
        'selected_subcategory': selected_subcategory  # Pass selected subcategory object to context
    }
    return render(request, 'products.html', context)




def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Validate form data
        if name and email and message:
            # Save data to the database
            contact = Contacts.objects.create(name=name, email=email, message=message)
            # Optionally, you can do additional processing here
            
            # Redirect to a success page or render a success message
            return redirect('thank_you')  # Replace 'thank_you' with your actual success URL
        else:
            # Handle form validation errors
            # For simplicity, you can just render the form again with an error message
            error_message = "Please fill in all fields."
            return render(request, 'contacts.html', {'error_message': error_message})
    else:
        return render(request, 'contacts.html')

def about(request):
    return render(request, 'about.html')

def product_detail(request, product_id):
    # Retrieve the product from the database based on the product ID
    product = get_object_or_404(Product, pk=product_id)
    
    print(f"Product is: {product.description}")
    # Pass the product to the template context
    context = {'product': product}
    
    # Render the product detail template with the product data
    return render(request, 'product_detail.html', context)

def search(request):
    query = request.GET.get('q')
    category_id = request.GET.get('category_id')

    categories = Category.objects.filter(parent_id=None)

    products = Product.objects.all()

    if query:
        products = products.filter(
            title__icontains=query
        ) | products.filter(
            description__icontains=query
        ) | products.filter(
            vehicle__title__icontains=query
        )




    if category_id and category_id != 'all':
        print(f"Category id is: {category_id}, And query is: {query}")
        category = get_object_or_404(Category, id=category_id)
        products = products.filter(category=category)

    context = {
        'categories': categories,
        'products': products,
        'query': query
    }
    return render(request, 'search.html', context)