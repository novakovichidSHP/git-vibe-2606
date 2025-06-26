import pytest
from main import solve_quadratic

def test_two_roots():
    # x^2 - 3x + 2 = 0 => x1=2, x2=1
    result = solve_quadratic(1, -3, 2)
    assert "Два корня" in result
    assert "x1 = 2.0" in result or "x2 = 2.0" in result
    assert "x1 = 1.0" in result or "x2 = 1.0" in result

def test_one_root():
    # x^2 + 2x + 1 = 0 => x=-1
    result = solve_quadratic(1, 2, 1)
    assert result.startswith("Один корень")
    assert "x = -1.0" in result

def test_no_roots():
    # x^2 + x + 1 = 0 => нет корней
    result = solve_quadratic(1, 1, 1)
    assert result == "Корней нет (дискриминант < 0)"

def test_a_zero():
    # a=0, не квадратное уравнение
    with pytest.raises(ZeroDivisionError):
        solve_quadratic(0, 2, 1) 