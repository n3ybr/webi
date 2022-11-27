from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .forms import UserForm
 
def index(request):
    if request.method == "POST":
        fio = request.POST.get("name")
        age = request.POST.get("age")
        adress = request.POST.get("adress")
        phone = request.POST.get("phone")
        fam = request.POST.get("fam")
        child = request.POST.get("child")
        edu_name1 = request.POST.get("edu_name1")
        edu_sta1 = request.POST.get("edu_sta1")
        edu_ed1 = request.POST.get("edu_ed1")
        spes = request.POST.get("spes")
        dop = request.POST.get("dop")
        comp = request.POST.get("comp")
        op_name1 = request.POST.get("op_name1")
        dolzh = request.POST.get("dolzh")
        op_s1 = request.POST.get("op_s1")
        op_e1 = request.POST.get("op_e1")
        fro = request.POST.get("fro")
        zp = request.POST.get("zp")
        new_dolzh = request.POST.get("new_dolzh")
        har = request.POST.get("har")
        amb = request.POST.get("amb")
        otvet = request.POST.get("otvet")
        date = request.POST.get("date")
        from docxtpl import DocxTemplate
        doc = DocxTemplate("анкета для собеседования.docx")
        context = { 'fio' : fio, "birth": age,"adress" : adress,"phone" : phone,
        "fam" : fam, "child" : child, "edu_name1" : edu_name1, "edu_sta1" : edu_sta1,
        "edu_ed1" : edu_ed1, "spes": spes,"dop" : dop, "comp" : comp, "op_name1" : op_name1, "op_s1" : op_s1, "op_e1" : op_e1, "dolzh" : dolzh,
        "fro" : fro, "zp": zp, "new_dolzh" : new_dolzh, "har" : har, "amb": amb, "otvet" : otvet, "date" : date }
        doc.render(context)
        doc.save("{}.docx".format(str(fio)))
        return HttpResponse(f"<h2>Здравствуйте, {fio}, ваша анкета была отправлена менеджеру</h2>")
    else:
        userform = UserForm()
        return render(request, "index.html", {"form": userform})