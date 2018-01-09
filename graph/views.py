from django.shortcuts import render
from django.db import models
from django.template import loader
from django.http import HttpResponse
from django.views import View
from .forms import SubmitUrlForm
from .functions import matrix_adjacency_undirected, cycle_Euler_undirected, cycle_Hamiltonian_undirected, is_Bipartite, \
    paint, matrix_incidence_undirected
from .graphType import parallelEdges, isMulti, isPseudo, isSimple, isComplete, isCycle, isWheel

# Create your views here.
def home_view_fbv(request, *args, **kwargs):
    if request.method == "POST":
        print(request.POST)
    return render(request, "form.html", {})


class home_view(View):
    def get(self, request, *args, **kwargs):
        The_form = SubmitUrlForm()
        context = {
            "form": The_form
        }
        return render(request, "form.html", context)

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        lst_graph = []
        if form.is_valid():
            print(list(form.cleaned_data.get("url")))
        for i in range(len(form.cleaned_data.get("url"))):
            if form.cleaned_data.get("url")[i] == ",":
                lst_graph.append([int(form.cleaned_data.get("url")[i - 1]), int(form.cleaned_data.get("url")[i + 1])])
        print(lst_graph)
        context = {
            "graph_lst": lst_graph,
            "matrix_adjacency_undirected": matrix_adjacency_undirected(lst_graph),
            "cycle_Euler_undirected": cycle_Euler_undirected(lst_graph),
            "cycle_Hamiltonian_undirected": cycle_Hamiltonian_undirected(lst_graph),
            "is_Bipartite": is_Bipartite(lst_graph),
            "matrix_incidence_undirected": matrix_incidence_undirected(lst_graph),
            "form": form,

            "parallelEdges": parallelEdges(lst_graph),
            "isMulti": isMulti(lst_graph),
            "isPseudo": isPseudo(lst_graph),
            "isSimple": isSimple(lst_graph),
            "isComplete": isComplete(lst_graph),
            "isCycle": isCycle(lst_graph),
            "isWheel": isWheel(lst_graph),
        }
        return render(request, "add_home.html", context)


class graph_view(View):
    def get(self, request, *args, **kwargs):
        context = {
        }
        return render(request, "graph_picture.html", context)
