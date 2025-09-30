class Cliente:
    def __init__(self, id, nome):
        if not nome:  # validação mínima
            raise ValueError("Nome do cliente não pode ser vazio.")
        self.id = id
        self.nome = nome


class DatabaseManager:
    def __init__(self):
        self.usuarios = []  # simula um banco

    def incluir(self, cliente):
        """Inclui um cliente na lista"""
        self.usuarios.append(cliente)

    def verificar(self, id):
        """Retorna True se cliente existe"""
        return any(c.id == id for c in self.usuarios)

    def atualizar(self, id, novo_nome):
        """Atualiza nome do cliente"""
        for c in self.usuarios:
            if c.id == id:
                c.nome = novo_nome
                return True
        return False
