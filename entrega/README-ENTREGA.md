# Relatório de Entrega

## Problemas

### 1. Conversão de Moedas

Arquivo: `src/onfly_report/services/currency_converter.py`

 - Defeito: conversão cambial incorreta e utilização de float, contrariando a precisão decimal esperada para operações monetárias.
 - Causa Raiz: o conversor dividia o valor pela taxa de câmbio e utilizava conversão para float.
 - Investigação e abordagem: análise da implementação e comparação da operação utilizada com a regra de conversão para BRL, utilizando os testes fornecidos como referência.
 - Correção: substituição da divisão por multiplicação e utilização de `Decimal`, eliminando a conversão intermediária para `float`.

### 2. Cálculo de Noites

Arquivo: `src/onfly_report/services/stay_calculator.py`

 - Defeito: cálculo de noites incorreto em reservas que atravessam meses ou anos.
 - Causa raiz: o cálculo considerava apenas o dia do mês, ignorando mês e ano.
 - Investigação e abordagem: análise da implementação, consulta à documentação de `date` e `timedelta` para identificar a forma de calcular a diferença entre datas completas.
 - Correção: utilização da diferença entre objetos `date`, extraindo a quantidade de dias e multiplicando pela quantidade de quartos.

### 3. Regras de Faturamento

Arquivo: `src/onfly_report/services/status_policy.py`

 - Defeito: reservas com status "NO_SHOW" eram incluídas nos totais financeiros e de noites.
 - Causa raiz: a implementação anterior apenas excluía o status "CANCELLED".
 - Investigação e abordagem: comparação entre a implementação e a regra de negócio especificada, que determinava apenas "CONFIRMED" como status faturável.
 - Correção: substituição da condição de exclusão por uma comparação explícita de "CONFIRMED"

### 4. Ordenação do Ranking de Hotéis

Arquivo: `src/onfly_report/services/report_builder.py`

 - Defeito: os hotéis eram apresentados em ordem crescente de valor, contrariando o ranking decrescente especificado.
 - Causa raiz: a ordenação utilizava o valor total como critério principal sem inverter sua ordem.
 - Investigação e abordagem: análise da ordenação implementada, comparação com a regra de negócio e validação com os testes automatizados e o CSV de exemplo.
 - Correção: ordenação estável em duas etapas, primeiro por `hotel_id` crescente e depois por valor total decrescente, preservando o critério de desempate.

### 5. Leitura Completa do CSV de Reservas

Arquivo: `src/onfly_report/repositories/csv_reservation_repository.py`

 - Defeito: reservas após a linha 200 eram ignoradas durante a leitura do CSV.
 - Causa raiz: a implementação continha uma interrupção explícita da leitura após 200 registros.
 - Investigação e abordagem: análise do código responsável por ler o CSV e criação de um teste com 201 reservas para reproduzir o problema e validar a correção.
 - Correção: remoção do limite manual de 200 registros, permitindo que o `csv.DictReader` percorra o arquivo inteiro.

## Validação

 - Testes automatizados: execução da suíte completa, incluindo os testes originais e os adicinados, com `pytest -q`.
 - Resultado: 7 testes aprovados, sem falhas.
 - Validação adicional: execução do CLI com o CSV de exemplo e comparação do relatório gerado com o resultado esperado, confirmando a correspondência dos dados.
