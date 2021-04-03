from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Profile, certifs
from generate_certificate.cert_gen import cert_enc_gen

def index(request):
    context = {}
    return render(request, 'certificates/index.html', context)

# def certi_list(request, email_id):
#     name = get_object_or_404(Profile, email=email_id).name
#     certs = certifs.objects.filter(email=email_id)
#     context = {
#         'name': name,
#         'certs': certs,
#     }
#     return render(request, 'certificates/certi_list.html', context)

def certi_list(request):
    email_id = request.POST['email']
    name = get_object_or_404(Profile, email=email_id).name
    certs = certifs.objects.filter(email=email_id)
    encs = [('data:image/jpg;base64,' + cert_enc_gen(name, cert.certificate_name)) for cert in certs]
    context = {
        'name': name,
        'certs': certs,
        'encs' : encs,
        'zipped' : zip(certs, encs)
    }
    return render(request, 'certificates/certi_list.html', context)


def get_certlist(request):
    
    email_id = request.POST['email']

    try:
        get_person = Profile.objects.get(email=request.POST['email'])
    except (KeyError):
        return HttpResponse("Unregisteres/Invalid email id enteres. Please Check!!")
    else:
        return HttpResponseRedirect(reverse('certificates:certi_list', args=(email_id, ))) 