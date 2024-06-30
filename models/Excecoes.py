class ErroEntradaInvalida(Exception):
    """Exceção lançada para entradas de saque inválidas."""
    pass

class ErroCedulasIndisponiveis(Exception):
    """Exceção lançada quando não é possível processar o valor solicitado com as cédulas disponíveis."""
    pass
