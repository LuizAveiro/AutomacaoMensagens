# AutomacaoMensagens

Sistema desenvolvido em Python para automatizar o envio de mensagens via WhatsApp utilizando dados armazenados em uma planilha Excel.

## Funcionalidades

* Leitura de planilha Excel
* Listagem de dizimistas
* Envio de mensagem de teste
* Envio automático para múltiplos contatos
* Integração com WhatsApp Web
* Mensagens personalizadas

## Tecnologias Utilizadas

* Python
* Pandas
* PyWhatKit
* PyAutoGUI
* Excel
* Git
* GitHub

## Estrutura da Planilha

Colunas utilizadas:

* ID
* Nome
* Encontro
* Telefone
* Email
* Valor
* Último Envio
* Status
* DataCadastro

## Problemas Encontrados

### Mensagem não era enviada

O sistema conseguia abrir o WhatsApp Web e preencher a mensagem, porém ela permanecia na caixa de texto.

### Solução

Foi utilizada a biblioteca PyAutoGUI para simular o pressionamento da tecla Enter após a abertura da conversa.

### Envio apenas para um contato

Inicialmente o sistema utilizava:

dados.iloc[0]

o que permitia o envio apenas para a primeira linha da planilha.

### Solução

Foi implementado:

for index, linha in dados.iterrows()

permitindo percorrer todos os registros da planilha.

## Próximas Melhorias

* Cadastro de dizimistas pelo sistema
* Atualização automática do último envio
* Relatórios de acompanhamento
* Controle de pagamentos
* Integração com e-mail

## Autor

Luiz Aveiro
