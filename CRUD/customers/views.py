from django.shortcuts import get_object_or_404, render, redirect
from customers.models import Customer
from customers.forms import CustomerForm

def list_customers(request):
    """
    Esta função lista todos os cliente disponíveis.
    """
    customers = Customer.objects.all()
    qtd = len(customers)
    return render(request, 'customers/list.html', {'customers': customers, 'qtd': qtd})


def create_customer(request):
    """
    Esta função recebe os dados do formulário, ou envia um vazio, e então salva os dados no banco de dados.
    """
    form = CustomerForm()

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            new_customer = form.save(commit=False)

            new_customer.name = form.cleaned_data['name']
            new_customer.operation = form.cleaned_data['operation']
            new_customer.cnpj = form.cleaned_data['cnpj']
            new_customer.employees = form.cleaned_data['employees']
            new_customer.billing = form.cleaned_data['billing']
            new_customer.phone = form.cleaned_data['phone']
            new_customer.mobile = form.cleaned_data['mobile']
            new_customer.adress = form.cleaned_data['adress']
            new_customer.district = form.cleaned_data['district']
            new_customer.city = form.cleaned_data['city']
            new_customer.state = form.cleaned_data['state']
            new_customer.zip_code = form.cleaned_data['zip_code']

            new_customer.save()

            return redirect(f'/customers/{new_customer.pk}/read/')
        else:
            return render(request, 'customers/form.html', {'form': form, 'title': 'Cadastrar'})
    else:
        return render(request, 'customers/form.html', {'form': form, 'title': 'Cadastrar'})


def delete_customer(request, pk):
    """
    Esta função pega o id do usuário, deleta do banco de dados e redireciona para a página principal.
    """
    customer = get_object_or_404(Customer, pk=pk)
    customer.delete()
    return redirect('/customers/list/')


def update_customer(request, pk):
    """
    Esta função recebe os dados e então grava no banco de dados.
    """
    customer =  get_object_or_404(Customer, pk=pk)
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            updated_customer = form.save(commit=False)

            updated_customer.name = form.cleaned_data['name']
            updated_customer.operation = form.cleaned_data['operation']
            updated_customer.cnpj = form.cleaned_data['cnpj']
            updated_customer.employees = form.cleaned_data['employees']
            updated_customer.billing = form.cleaned_data['billing']
            updated_customer.phone = form.cleaned_data['phone']
            updated_customer.mobile = form.cleaned_data['mobile']
            updated_customer.adress = form.cleaned_data['adress']
            updated_customer.district = form.cleaned_data['district']
            updated_customer.city = form.cleaned_data['city']
            updated_customer.state = form.cleaned_data['state']
            updated_customer.zip_code = form.cleaned_data['zip_code']

            updated_customer.save()

            return redirect(f'/customers/{updated_customer.pk}/read/')
        else:
            return render(request, 'customers/form.html', {'form': form, 'customer': customer, 'title': 'Atualizar'})
            
    else:
        return render(request, 'customers/form.html', {'form': form, 'customer': customer, 'title': 'Atualizar'})


def read_customer(request, pk):
    """
    Esta função retorna os detalhes do cliente clicado.
    """
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'customers/read.html', {'customer': customer})
