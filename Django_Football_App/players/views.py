from django.shortcuts import render, get_object_or_404

# from .forms import PlayersForm
from .models import (
    Players,
)

# from django.views.generic import (
#     ListView,
#     # DetailView,
#     # CreateView,
# )


def PlayersView(request):  # , DetailsView):
    # form = PlayersForm(request.POST or None)
    # if form.is_valid():
    #     form.save()
    #     form = PlayersForm()
    # context = {"form": form}
    return render(request, "players/players_home.html")  # , context)
