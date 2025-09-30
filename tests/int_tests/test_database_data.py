import pytest
from app import Cliente, DatabaseManager

def test_verificar_cliente_existe():
    db = DatabaseManager()
    cliente = Cliente(1, "Julio")
    db.incluir(cliente)
    assert db.verificar(1) is True
    assert db.verificar(2) is False

def test_atualizar_cliente():
    db = DatabaseManager()
    cliente = Cliente(1, "Julio")
    db.incluir(cliente)
    atualizado = db.atualizar(1, "Julio Cesar")
    assert atualizado is True
    assert cliente.nome == "Julio Cesar"