from django.shortcuts import render,redirect
from curdapp.models import empData
def inputPage(req):
    if req.method=='GET':
        return render(req,'curdapp/input.html')
    else:
        empData(
            first_name=req.POST['fname'],
            last_name=req.POST['lname'],
            email=req.POST['email'],
            mobile=req.POST['mobile'],
            company=req.POST['company'],
            salary=req.POST['salary'],
            location=req.POST['location'],
            ).save()
        return redirect(resultPage)
def resultPage(req):
    emp=empData.objects.all()
    return render(req,'curdapp/result.html',{'emps':emp})
def updatePage(req,id):
    updateddata=empData.objects.get(id=id)
    return render(req, 'curdapp/update.html',{'emp':updateddata})
def updatedPage(req,id):
    updatedData=empData.objects.get(id=id)
    updatedData.first_name=req.POST['fname']
    updatedData.last_name=req.POST['lname']
    updatedData.email=req.POST['email']
    updatedData.mobile=req.POST['mobile']
    updatedData.company=req.POST['company']
    updatedData.salary=req.POST['salary']
    updatedData.location=req.POST['location']
    updatedData.save()
    return redirect(resultPage)
def deletePage(req, id):
    emp=empData.objects.get(id=id)
    emp.delete()
    return redirect(resultPage)
        





