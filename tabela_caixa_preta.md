# Aula 6 - Tabela de caixa-preta

Título de referência: R$ 1.000,00
Vencimento: 10/11/2026

| Classe de equivalência | Valor representativo | Valores limite | Resultado esperado |
|---|---|---|---|
| Pagamento com 10 dias ou mais de antecedência | 31/10/2026 | Exatamente 10 dias | R$ 950,00 |
| Pagamento com mais de 10 dias de antecedência | 30/10/2026 | 11 dias antes | R$ 950,00 |
| Pagamento com 9 dias de antecedência | 01/11/2026 | Exatamente 9 dias | R$ 1.000,00 |
| Pagamento no vencimento | 10/11/2026 | Zero dias | R$ 1.000,00 |
| Pagamento após vencimento | 11/11/2026 | Primeiro dia de atraso | R$ 1.020,33 |
| Vencimento no sábado e pagamento na segunda | 16/11/2026 | Segunda-feira prorrogada | R$ 1.000,00 |
| Vencimento no sábado e pagamento na terça | 17/11/2026 | Primeiro dia após prorrogação | R$ 1.020,33 |

## Teste adicional de arredondamento

Título de R$ 0,10, vencimento em 10/11/2026 e pagamento em 31/10/2026.

Desconto de 5%: R$ 0,005.
Arredondamento: R$ 0,01.
Resultado esperado: R$ 0,09.

## Antecedência sobre a data original

Vencimento original em 14/11/2026 (sábado).
Pagamento em 06/11/2026: oito dias de antecedência.
Resultado esperado: R$ 1.000,00, sem desconto.
