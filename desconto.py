def calcular_desconto(valor_compra, tipo_cliente):
    if valor_compra is None:
        raise TypeError("valor_compra não pode ser nulo")
    if not isinstance(valor_compra, (int, float)):
        raise TypeError("valor_compra deve ser numérico")
    if valor_compra < 0:
        raise ValueError("valor_compra não pode ser negativo")

    if tipo_cliente is None:
        raise TypeError("tipo_cliente não pode ser nulo")
    if not isinstance(tipo_cliente, str):
        raise TypeError("tipo_cliente deve ser uma string")

    tipo_cliente = tipo_cliente.strip().upper()
    if tipo_cliente not in {"COMUM", "VIP"}:
        raise ValueError("tipo_cliente inválido")

    desconto = 0

    # Validação do desconto base
    if 100 <= valor_compra < 500:
        desconto = 0.10
    elif valor_compra >= 500:
        desconto = 0.20

    # Validação do cliente VIP
    if tipo_cliente == "VIP":
        desconto += 0.05

    valor_desconto = valor_compra * desconto

    # Regra do Teto de R$ 200,00
    if valor_desconto > 200:
        valor_desconto = 200

    return round(valor_desconto, 2)