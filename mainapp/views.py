import datetime

from django.shortcuts import render

# Create your views here.

def main(request):
    title = "главная"
    products = [
        {
            "name": "Отличный рабочий стул",
            "desc": "Удобно работать весь день",
            "image_src": "product-1.jpg",
            "image_href": "/product/1/",
            "alt": "рабочий стул",
        },
        {
            "name": "Стул с улучшенными характеристиками",
            "desc": "Подойдёт для работы и отдыха",
            "image_src": "product-2.jpg",
            "image_href": "/product/2/",
            "alt": "работа и отдых",
        }
    ]
    content = {"title": title, "products": products}
    return render(request, "mainapp/index.html", content)


def products(request):
    title = "продукты"
    links_menu = [
        {"href": "products_all", "name": "Все товары"},
        {"href": "products_home", "name": "Для дома"},
        {"href": "products_office", "name": "В офис"},
        {"href": "products_modern", "name": "Необычные"},
        {"href": "products_classic", "name": "Классические"},
    ]
    same_products = [
        {
            "name": "Рабочий стул",
            "desc": "Удобно весь день",
            "image_src": "product-11.jpg",
            "alt": "рабочий стул 11",
        },
        {
            "name": "Улучшенный рабочий стул",
            "desc": "Комфортно весь день",
            "image_src": "product-21.jpg",
            "alt": "рабочий стул 21",
        },
        {
            "name": "Премиальный рабочий стул",
            "desc": "Комфорт и отдых весь день",
            "image_src": "product-31.jpg",
            "alt": "рабочий стул 31",
        }
    ]
    content = {"title": title, "links_menu": links_menu, "same_products": same_products}
    return render(request, "mainapp/products.html", content)


def contact(request):
    title = "О компании"
    visit_date = datetime.datetime.now()
    locations = [
        {
            "city": "Москва",
            "phone": "+7 800 1234567890",
            "e-mail": "info@gkshop.ru",
            "address": "Не только в пределах МКАД",
        },
        {
            "city": "Екатеринбург",
            "phone": "+7 800 1234567891",
            "e-mail": "info_ekaterinburg@gkshop.ru",
            "address": "Центр России",
        },
        {
            "city": "Владивосток",
            "phone": "+7 800 1234567892",
            "e-mail": "infovladik@gkshop.ru",
            "address": "Восточный край России",
        },
    ]
    content = {"title": title, "visit_date": visit_date, "locations": locations}
    return render(request, "mainapp/contact.html", content)
