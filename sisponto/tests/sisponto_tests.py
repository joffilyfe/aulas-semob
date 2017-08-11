import sisponto
import unittest


class SISPontoTestCase(unittest.TestCase):

    def setUp(self):
        sisponto.app.testing = True
        self.app = sisponto.app.test_client()

    def login(self, user=None, password=None):
        return self.app.post('/login', data=dict(login=user, password=password),
                            follow_redirects=True)

    def test_index_should_require_login(self):
        response = self.app.get('/', follow_redirects=True)
        assert bytes("Por favor, faça o login", 'utf-8') in response.data

    def test_should_login_an_user(self):
        response = self.login('admin', 'admin')
        assert b"Login realizado com sucesso" in response.data

    def test_should_logout_an_user(self):
        response = self.app.get('/logout', follow_redirects=True)
        assert b"Logout realizado com sucesso" in response.data

    def skip_should_have_admin_page(self):
        response = self.app.get('/admin', follow_redirects=True)
        assert bytes("Por favor, faça o login", 'utf-8') in response.data
        response = self.login()
        

if __name__ == '__main__':
    unittest.main()