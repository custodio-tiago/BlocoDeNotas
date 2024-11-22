# Bloco de Notas em Python com Tkinter

Este é um bloco de notas simples desenvolvido em Python usando o Tkinter para a interface gráfica. O aplicativo permite criar, editar, salvar e abrir arquivos de texto, além de realizar operações básicas de edição como recortar, copiar e colar.
  
![image](https://github.com/user-attachments/assets/a6e4f97d-5e49-4527-921f-eaced595dc41)

## Funcionalidades

- **Arquivo**:
  - **Novo**: Cria um novo arquivo em branco.
  - **Salvar**: Salva o arquivo atual.
  - **Abrir**: Abre um arquivo de texto existente.
  - **Sair**: Fecha o aplicativo.
  
- **Editar**:
  - **Recortar**: Recorta o texto selecionado.
  - **Copiar**: Copia o texto selecionado.
  - **Colar**: Cola o texto copiado ou cortado.

- **Ferramentas**:
  - Opções adicionais podem ser configuradas no futuro (ainda não implementadas no projeto).

- **Ajuda**:
  - **Sobre**: Exibe informações sobre o Bloco de Notas.

## Estrutura do Projeto

O projeto é dividido em vários arquivos Python para organizar a lógica e a interface gráfica:

- **main.py**: Contém a lógica principal do bloco de notas, incluindo a criação da interface gráfica com Tkinter.
- **text_operations.py**: Contém funções para as operações de edição (recortar, copiar e colar).
- **file_operations.py**: Contém funções para salvar, abrir e criar novos arquivos.
- **about.py**: Contém a função que exibe a janela "Sobre".

## Requisitos

- Python 3.x
- Tkinter (já incluso no Python por padrão)
