from django.shortcuts import render
from django.db import models
from django.template import loader
from django.http import HttpResponse
from django.views import View
from .forms import SubmitUrlForm
from .functions import matrix_adjacency_undirected, cycle_Euler_undirected, cycle_Hamiltonian_undirected, is_Bipartite, \
    paint, matrix_incidence_undirected
from .graphType import parallelEdges, isMulti, isPseudo, isSimple, isComplete, isCycle, isWheel

import copy
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

        if form.is_valid():
            print((form.cleaned_data.get("url")))
        lst = list(form.cleaned_data.get("url"))

        def graph(lst):
            lst_graph = [[]]
            number = ""
            for i in range(len(lst)):
                if lst[i].isdigit():
                    number += lst[i]
                elif lst[i] == ",":
                    try:
                        lst_graph[-1].append(int(number))
                        number = ""
                    except:
                        pass
                elif lst[i] == ")" or lst[i] == "}" or lst[i] == "]":
                    lst_graph[-1].append(int(number))
                    number = ""
                    lst_graph.append([])
            lst_graph.pop()
            lst_graph.sort(key=lambda x: x[0])
            return lst_graph

        try:
            lst_graph = graph(lst)
        except:
            lst_graph = []

        if not lst_graph:
            The_form = SubmitUrlForm()
            context = {
                "form": The_form
            }

            return render(request, "error.html", context)
        print(lst_graph, type(lst_graph[0]))
        context = {
            "graph_lst":lst_graph.copy(),
            "matrix_adjacency_undirected": matrix_adjacency_undirected(lst_graph),

            "cycle_Hamiltonian_undirected": cycle_Hamiltonian_undirected(lst_graph),
            "is_Bipartite": is_Bipartite(lst_graph),
            "matrix_incidence_undirected": matrix_incidence_undirected(lst_graph),
            "form": form,

            "parallelEdges": parallelEdges(lst_graph),
            ""
            "isMulti": isMulti(lst_graph),
            "isPseudo": isPseudo(lst_graph),
            "isSimple": isSimple(lst_graph),
            "isComplete": isComplete(lst_graph),
            "isCycle": isCycle(lst_graph),
            "isWheel": isWheel(lst_graph),
            "cycle_Euler_undirected": cycle_Euler_undirected(lst_graph)
        }

        print("Here#####")
        return render(request, "add_home.html", context)



class graph_view(View):
    def get(self, request, *args, **kwargs):
        context = {
        }
        return render(request, "graph_picture.html", context)
