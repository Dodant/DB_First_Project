from django.shortcuts import render, get_object_or_404
from mutation.models import Autosome, Auto_Mutation, Auto_Syndrome, Allo_Mutation, Allo_Syndrome


def index(request):
    auto_mutation_list = Auto_Mutation.objects.all().order_by('auto_pri')
    allo_mutation_list = Allo_Mutation.objects.all().order_by('linked')
    context = {'auto_mutation_list':auto_mutation_list, 'allo_mutation_list':allo_mutation_list}
    return render(request, 'mutation/index.html', context)

def chrono(request, auto_no):
    autosome = get_object_or_404(Autosome, pk=auto_no)
    return render(request, 'mutation/chrono.html', {'autosome':autosome})


def syndro(request, auto_syn_code):
    syn_info = get_object_or_404(Auto_Syndrome, pk=auto_syn_code)
    return render(request, 'mutation/syndro.html', {'syn_info':syn_info})

def xysyndro(request, allo_syn_code):
    xysyn_info = get_object_or_404(Allo_Syndrome, pk=allo_syn_code)
    return render(request, 'mutation/xysyndro.html', {'xysyn_info':xysyn_info})
