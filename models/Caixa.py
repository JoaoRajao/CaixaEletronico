from models.Excecoes import ErroEntradaInvalida, ErroCedulasIndisponiveis

class CAIXA:
    """
    Classe que simula o funcionamento de um caixa eletrônico, controlando a
    distribuição de cédulas para um saque solicitado.

    Attributes:
        cedulas (list of int): Lista das cédulas disponíveis no caixa eletrônico.
    """

    def __init__(self):
        """
        Inicializa o caixa eletrônico com um conjunto pré-definido de cédulas.
        """
        self.cedulas = [100, 50, 20, 10, 5, 2]

    def sacar(self, valor):
        """
        Processa o pedido de saque e determina o número de cédulas de cada valor
        que serão entregues ao usuário.

        Args:
            valor (int): O valor do saque solicitado pelo usuário.

        Returns:
            dict: Um dicionário contendo a quantidade de cédulas de cada valor.

        Raises:
            ErroEntradaInvalida: Se o valor solicitado é menor ou igual a zero.
            ErroCedulasIndisponiveis: Se o valor solicitado não pode ser atendido com
                                      as cédulas disponíveis.
        """
        if valor <= 0:
            raise ErroEntradaInvalida("O valor deve ser um inteiro positivo maior que zero.")

        resultado = {}
        for cedula in self.cedulas:
            if valor >= cedula:
                num_cedulas = valor // cedula
                valor -= num_cedulas * cedula
                resultado[str(cedula)] = num_cedulas
            else:
                resultado[str(cedula)] = 0

        if valor > 0:
            raise ErroCedulasIndisponiveis("O valor solicitado não pode ser processado com as cédulas disponíveis.")

        return resultado
