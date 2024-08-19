import calc
import pytest


def test_soma():
    c = calc.Calc()
    result = c.somar(1, 2)
    assert result == 3


@pytest.mark.sub
@pytest.mark.parametrize("a,b,result", [(1, 2, -1), (2, 2, 0), (0, 0, 0), (-2, -2, 0)])
def test_subtrair(a, b, result, cria_calc):
    result_func = cria_calc.faz_subtracao(a, b)
    assert result_func == result


@pytest.fixture
def cria_calc():
    c = calc.Calc()
    return c


@pytest.mark.parametrize("a,b,result", [(1, 2, 2), (2, 2, 4), (0, 0, 0), (-2, -2, 4)])
@pytest.mark.mult
def test_mult(a, b, result, cria_calc):
    result_func = cria_calc.mult(a, b)
    assert result_func == result


@pytest.mark.parametrize("a,b,result", [(1, 2, 0.5), (2, 2, 1), (-2, -2, 1)])
@pytest.mark.div
def test_div(a, b, result, cria_calc):
    result_func = cria_calc.div(a, b)
    assert result_func == result


@pytest.mark.parametrize(
    "a,b,result",
    [(1, 0, ZeroDivisionError), (2, 0, ZeroDivisionError), (-2, 0, ZeroDivisionError)],
)
@pytest.mark.div_zero
def test_div_zero(a, b, result, cria_calc):
    with pytest.raises(ZeroDivisionError) as exc_info:
        cria_calc.div(a, b)
    assert "ZeroDivisionError" in str(exc_info)
