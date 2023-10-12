# Try to import the module "mymodule"
try:
    import components.mymodule
except ImportError:
    components.mymodule = None

# test functions of "mymodule" 
from components.mymodule import add , mul
class Test_Mymodule():

    def test_add(self):
        assert add(5,2) == 7, "addition is looking not ok"

    def test_mul(self):
        assert mul(5,2) == 10
    