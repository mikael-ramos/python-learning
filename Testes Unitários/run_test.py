import pandas as pd
from run import add_two

def test_add_two():
    val = 3
    resp = add_two(val)
    
    assert isinstance(resp,int)

def test_hello():
    pass


def test_create_pd():
    
    val = pd.DataFrame({})
    assert isinstance(val,pd.DataFrame)
    assert val.empty == True