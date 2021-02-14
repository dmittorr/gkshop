from django.shortcuts import render

<<<<<<< HEAD

# Create your views here.


=======
# Create your views here.

>>>>>>> a8a45b5351b6bef9480f13403f1c60f33bf79939
def main(request):
    return render(request, "mainapp/index.html")


def products(request):
    return render(request, "mainapp/products.html")


def contact(request):
<<<<<<< HEAD
    return render(request, "mainapp/contact.html")
=======
    return render(request, "mainapp/contact.html")
>>>>>>> a8a45b5351b6bef9480f13403f1c60f33bf79939
