from django.shortcuts import render, get_object_or_404
from jbatistaconstrucao.core.models import Portfolio


def home(request):
    portfolios = Portfolio.objects.all()
    return render(request, "index.html", {"portfolios": portfolios})

def portfolio_detail(request, pk):
    portfolio = get_object_or_404(Portfolio, pk=pk)
    return render(request, "portfolio-details.html", {"portfolio": portfolio})
