from datetime import date
from decimal import Decimal

from app.regras import calcular_valor_pagamento

VENCIMENTO = date(2026, 11, 10)


def test_pagamento_no_vencimento_e_valor_cheio():
    valor = calcular_valor_pagamento(
        Decimal("1000.00"),
        VENCIMENTO,
        VENCIMENTO
    )

    assert valor == Decimal("1000.00")


def test_pagamento_com_dez_dias_de_antecedencia_tem_cinco_por_cento_de_desconto():
    valor = calcular_valor_pagamento(
        Decimal("1000.00"),
        VENCIMENTO,
        date(2026, 10, 31)
    )

    assert valor == Decimal("950.00")


def test_pagamento_com_nove_dias_de_antecedencia_paga_valor_cheio():
    valor = calcular_valor_pagamento(
        Decimal("1000.00"),
        VENCIMENTO,
        date(2026, 11, 1)
    )

    assert valor == Decimal("1000.00")




def test_pagamento_um_dia_depois_do_vencimento_tem_encargos():
    valor = calcular_valor_pagamento(
        Decimal("1000.00"),
        VENCIMENTO,
        date(2026, 11, 11)
    )

    assert valor == Decimal("1020.33")


def test_desconto_considera_data_original_do_vencimento():
    valor = calcular_valor_pagamento(
        Decimal("1000.00"),
        date(2026, 11, 14),
        date(2026, 11, 6)
    )

    assert valor == Decimal("1000.00")


def test_pagamento_na_segunda_apos_vencimento_no_sabado_nao_tem_encargos():
    valor = calcular_valor_pagamento(
        Decimal("1000.00"),
        date(2026, 11, 14),
        date(2026, 11, 16)
    )

    assert valor == Decimal("1000.00")


def test_pagamento_na_terca_apos_vencimento_no_sabado_tem_encargos():
    valor = calcular_valor_pagamento(
        Decimal("1000.00"),
        date(2026, 11, 14),
        date(2026, 11, 17)
    )

    assert valor == Decimal("1020.33")


def test_desconto_de_meio_centavo_arredonda_para_cima():
    valor = calcular_valor_pagamento(
        Decimal("0.10"),
        VENCIMENTO,
        date(2026, 10, 31)
    )

    assert valor == Decimal("0.09")
