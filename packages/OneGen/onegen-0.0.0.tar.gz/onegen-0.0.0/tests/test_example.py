import pytest
import pyotp

from OneGen.example import add_one


class TestExample():

    def test_add_one(self):
        assert add_one(5)==6

    def test_2(self):
        

        code = 'STWYCKOIOLEA4X72AINOATYDAVGEWE7T'
        totp = pyotp.TOTP(code)
        print(totp.now())
if __name__ == '__main__':
    pytest.main()