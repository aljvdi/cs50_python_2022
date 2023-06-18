import pytest
from jar import Jar

class TestJar:
    def test_init(self):
        jar = Jar()
        assert str(jar) == ""

    def test_str(self):
        jar = Jar()
        jar.deposit(3)
        assert str(jar) == "🍪🍪🍪"

    def test_deposit(self):
        jar = Jar()
        jar.deposit(5)
        assert jar.size == 5
        jar.deposit(1)
        assert jar.size == 6

    def test_withdraw(self):
        jar = Jar()
        jar.deposit(5)
        jar.withdraw(4)
        assert jar.size == 1
        with pytest.raises(ValueError):
            jar.withdraw(10)


if __name__ == "__main__":
    tj = TestJar()
    tj.test_withdraw()