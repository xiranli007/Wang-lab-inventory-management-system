from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Inventory, Order, Request, Culture
from django.urls import reverse
from .forms import InventoryForm, OrderForm, RequestForm, CultureCollectionForm
from django.db.models import Q # complex query

@login_required(login_url='user-login')
def index(request):
    
    orders_count = Order.objects.all().count()
    requests_count  = Request.objects.all().count()
    items_count = Inventory.objects.all().count()
    # handle the search logic
    if 'q' in request.GET:
        q = request.GET['q']
        multi_query = Q(Q(organism__icontains = q) | Q(idNumber__icontains = q) | 
                        Q(description__icontains = q) | Q(isolationSource__icontains = q))
        collections = Culture.objects.filter(multi_query)
    else:
        collections = Culture.objects.all()
    # handle the add new culture logic
    if request.method =='POST':
        form = CultureCollectionForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('dashboard-index')
    else:
        form = CultureCollectionForm()
    context ={
        'requests_count':requests_count, 
        'orders_count' : orders_count,
        'items_count': items_count,
        'collections':collections,
        'form' : form
    }
    return render(request, 'dashboard/index.html', context)

@login_required(login_url='user-login')
def culture_delete(request, pk):
    culture = Culture.objects.get(id = pk)
    if request.method == 'POST':
        culture.delete()
    return redirect('dashboard-index')

@login_required(login_url='user-login')
def culture_edit(request, pk):
    culture = Culture.objects.get(id = pk)
    if request.method == 'POST':
        form = CultureCollectionForm(request.POST, instance = culture)
        if form.is_valid():
            form.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm(instance = culture)
    context ={
        'form' : form
    }
    return render(request, 'dashboard/culture_edit.html', context)

@login_required(login_url='user-login')
def users(request):
    return render(request, 'dashboard/users.html')

@login_required(login_url='user-login')
def inventory(request):
    items = Inventory.objects.all() # grab all the items from the database
    orders_count = Order.objects.all().count()
    requests_count  = Request.objects.all().count()
    items_count = items.count()
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-inventory')
    else:
        form = InventoryForm()
    context ={
        'items': items,
        'form': form,
        'requests_count':requests_count, 
        'orders_count' : orders_count,
        'items_count': items_count, 
    }
    return render(request, 'dashboard/inventory.html', context) # pass in the context so the html file can access to the item variable

@login_required(login_url='user-login')
def product_delete(request, pk):
    item = Inventory.objects.get(id = pk)
    if request.method == 'POST':
        item.delete()
    return redirect('dashboard-inventory')

@login_required(login_url='user-login')
def product_detail(request,pk):
    item = Inventory.objects.get(id = pk)
    context = {
        'item' : item
    }
    return render(request,'dashboard/product_detail.html', context)

@login_required(login_url='user-login')
def product_update(request, pk):
    item = Inventory.objects.get(id=pk)
    if request.method == 'POST':
        form = InventoryForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(reverse('dashboard-product-detail', kwargs={'pk': pk}))
    else:
        form = InventoryForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/product_update.html', context)


    
@login_required(login_url='user-login')
def orders(request):
    orders = Order.objects.all()
    orders_count = orders.count()
    requests_count  = Request.objects.all().count()
    items_count = Inventory.objects.all().count()
    if request.method =='POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('dashboard-orders')
    else:
        form = OrderForm()
    context = {
        'orders': orders,
        'form': form,
        'requests_count':requests_count, 
        'orders_count' : orders_count,
        'items_count': items_count, 
    }
    return render(request, 'dashboard/orders.html', context)

@login_required(login_url='user-login')
def order_delete(request, pk):
    item = Order.objects.get(id = pk)
    if request.method == 'POST':
        item.delete()
    return redirect('dashboard-orders')

@login_required(login_url='user-login')
def order_edit (request, pk):
    order = Order.objects.get(id = pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance = order)
        if form.is_valid():
            form.save()
            return redirect('dashboard-orders')
    else:
        form = OrderForm(instance = order)
    context ={
        'form' : form
    }
    return render(request, 'dashboard/order_edit.html', context)

@login_required(login_url='user-login')
def order_received(request, pk):
    order = Order.objects.get(id=pk)
    inventory_item,created = Inventory.objects.get_or_create(catelogNumber = order.catelogNumber)
    if created:
        inventory_item.name = order.name
        inventory_item.vendor = order.vendor
        inventory_item.catelogNumber = order.catelogNumber
        inventory_item.quantity = order.quantity
        inventory_item.receivedDate = datetime.now()
        inventory_item.receivedBy = request.user.username
    else:
        inventory_item.quantity += order.quantity
        inventory_item.receivedBy = request.user.username
        inventory_item.receivedDate = datetime.now()
    inventory_item.save()
    order.delete()
    return redirect('dashboard-orders')   

@login_required(login_url='user-login')
def requests(request):
    requests = Request.objects.all()
    requests_count  = requests.count()
    orders_count = Order.objects.all().count()
    items_count = Inventory.objects.all().count()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
           model_instance = form.save(commit=False) # since form is an instance of RequestForm which do not has the 'requestedBy' field, we here call the instance of the Request model
           model_instance.personRequest = request.user # set the personRequest attribute to the user who submitted the form
           model_instance.save() # save the model instance
        return redirect ('dashboard-requests')
    else:
        form = RequestForm()
    context = {
        'requests':requests, 
        'form':form,
        'requests_count':requests_count, 
        'orders_count' : orders_count,
        'items_count': items_count, 
    }
    return render(request,'dashboard/requests.html', context)

@login_required(login_url='user-login')
def request_delete(request, pk):
    rqt = Request.objects.get(id = pk)
    if request.method == 'POST':
        rqt.delete()
    return redirect('dashboard-requests')

@login_required(login_url='user-login')
def request_ordered(request, pk):
    rqt = Request.objects.get(id = pk)
    order_instance = Order (
        name = rqt.name,
        vendor = rqt.vendor,
        quantity = rqt.quantity,
        catelogNumber = rqt.quantity,
        staff = request.user
    )
    order_instance.save()
    rqt.delete()
    return redirect('dashboard-requests')

@login_required(login_url='user-login')
def request_edit(request, pk):
    rqt = Request.objects.get(id = pk)
    if request.method == 'POST':
        form = RequestForm(request.POST, instance = rqt)
        if form.is_valid():
            form.save()
            return redirect('dashboard-requests')
    else:
        form = RequestForm(instance = rqt)
    context = {
        'form':form
    }
    return render(request, 'dashboard/request_edit.html', context)
