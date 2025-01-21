# Greed

**Número da Lista**: 17<br>
**Conteúdo da Disciplina**: GREED<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 21/1030700  |  Chaydson Ferreira da Aparecida |
| 21/1030676  |  Ana Luíza Rodrigues da Silva |

# Visualizador de Árvore de Huffman

Este projeto é um visualizador gráfico do algoritmo de Huffman, que é utilizado para compressão de dados. O projeto permite que os usuários insiram um texto e visualizem a construção da árvore de Huffman correspondente.

## Funcionalidades

- **Entrada de Texto**: Pode inserir qualquer texto para ser processado.
- **Construção da Árvore**: Ao clicar no botão "Construir Árvore", calcula-se as frequências dos caracteres e constrói-se a árvore de Huffman.
- **Visualização Passo a Passo**: É possível navegar pela construção da árvore, visualizando cada etapa do processo.

## Estrutura do Código

O código é dividido em três classes principais:

1. **HuffmanNode**: Representa um nó na árvore de Huffman, contendo um caractere, sua frequência e referências para os nós filhos.
2. **HuffmanAlgorithm**: Contém a lógica para calcular as frequências dos caracteres e construir a árvore de Huffman.
3. **HuffmanViewer**: Gerencia a interface gráfica e a interação do usuário, permitindo a entrada de texto e a visualização da árvore.

### Requisitos
- Python 3.x
- Tkinter (geralmente está incluído na instalação do Python)
- Caso nao, sudo apt-get install python3-tk

### Como Executar
1. Certifique-se de ter o Python instalado no seu sistema
2. Execute o aplicativo:
```bash
python huffman_viewer.py
```

## Como Usar

1. Execute o script.
2. Insira um texto no campo de entrada.
3. Clique no botão "Construir Árvore" para iniciar o processo.
4. Use os botões "Anterior" e "Próximo" para navegar pelas etapas da construção da árvore.

## Apresentação

[Link do vídeo de explicação e execução](https://youtu.be/6zigpEVmDxo)