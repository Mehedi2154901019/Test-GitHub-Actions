from src.math_operation import add,sub

def test_add():
    assert add(2,3) == 5
    assert add(5,-1) == 4
    

def test_sub():
    assert sub(4,3) ==1
    assert sub(-1,-2)==1