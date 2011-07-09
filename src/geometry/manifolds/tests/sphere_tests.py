from . import np
from geometry.manifolds import S1
from geometry.basic_utils import assert_allclose
from geometry.formatting import printm

def test_wrap_around():
    a = np.array([+1, 0])
    b = np.array([-1, 0])
    
    vel = S1.logmap(a, b)
    b2 = S1.expmap(a, vel)
    d = S1.distance(b, b2)
    
    printm('a', a, 'b', b, 'vel', vel, 'd', np.array(d))
    assert_allclose(d, 0, atol=1e-7)