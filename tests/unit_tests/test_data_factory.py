import pytest
from utils.data_factory import DataFactory

class TestDataFactory:
    
    @pytest.fixture
    def user_data(self):
        """Fixture que gera os dados uma vez para ser usada nos testes abaixo"""
        return DataFactory.generate_user_data()

    def test_generate_user_data_returns_dict(self, user_data):
        """Valida se o retorno da fábrica é realmente um dicionário"""
        assert isinstance(user_data, dict), "O retorno deveria ser um dicionário (dict)"

    def test_user_data_contains_required_keys(self, user_data):
        """Valida se todas as chaves obrigatórias para a API e UI estão presentes"""
        expected_keys = [
            "name", "email", "password", "first_name", "last_name", 
            "address", "country", "state", "city", "zipcode", "mobile_number"
        ]
        for key in expected_keys:
            assert key in user_data, f"A chave '{key}' está faltando nos dados gerados"

    def test_generated_email_format(self, user_data):
        """Valida se o e-mail gerado tem o formato correto (contém @ e ponto)"""
        email = user_data["email"]
        assert "@" in email, f"O e-mail gerado '{email}' não contém '@'"
        assert "." in email, f"O e-mail gerado '{email}' não contém '.'"

    def test_generated_password_length(self, user_data):
        """Valida se a senha gerada obedece ao tamanho mínimo que configuramos (12)"""
        password = user_data["password"]
        assert len(password) >= 12, f"A senha gerada '{password}' tem menos de 12 caracteres"