import pytest
from app import Cliente, DatabaseManager

def test_inclusao_falha_com_dados_invalidos():
    db = DatabaseManager()
    with pytest.raises(ValueError):
        Cliente(1, "")  # nome vazio → inválido