import pytest

from jbatistaconstrucao.core.models import Portfolio


@pytest.mark.django_db
def test_create():
    portfolio = Portfolio.objects.create(
        name="Teste", photo="", content="Descrição do serviço efetuado no " "cliente."
    )
    assert portfolio == Portfolio.objects.get(name="Teste")
