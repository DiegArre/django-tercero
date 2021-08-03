from django.shortcuts import redirect, render
from django.utils.crypto import get_random_string
# Create your views here.

# hola = get_random_string(length=14, allowed_chars= "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ").capitalize()
# print(hola)
def red(request):
    return redirect("/random_word")

def login(request):
    if request.method =="POST":
        request.session["name"] =  request.POST["name"]
        request.session["contador"] = 0
        print("Se ha creado la sesion" , request.session["name"])
        return redirect ("/random_word")

def logout(request):
    if request.method =="POST":
        del request.session["name"] 
        del request.session["contador"]
        return redirect("/random_word")

def random(request):

    context = {
        "palabra" : get_random_string(length=14, allowed_chars= "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ").capitalize()
    }

    return render(request,"index.html",context)


def contador(request):
    if request.method == "POST":
        if "name" in request.session:
            request.session["contador"] += 1 
            return redirect("/random_word")
        else:
            return redirect("/error")

def error(request):
    return render(request,"error.html")


def reset(request):
    if request.method == "POST":
        request.session["contador"] = 0
        return redirect("/random_word")



