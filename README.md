# Detecção de Cor com HSV (OpenCV)

Este projeto implementa um algoritmo de **detecção de cor em imagens utilizando Python e OpenCV**, aplicando técnicas básicas de **Processamento de Imagens**.

O objetivo do algoritmo é identificar regiões de cor vermelha em uma imagem, utilizando o espaço de cores **HSV (Hue, Saturation, Value)**. Após a detecção, o programa mantém apenas as regiões vermelhas coloridas, enquanto o restante da imagem é convertido para **escala de cinza**.

## Tecnologias utilizadas

* Python
* OpenCV
* NumPy

## Funcionamento do algoritmo

O processo executado pelo programa segue as seguintes etapas:

1. Carregamento da imagem original.
2. Conversão do espaço de cores **BGR para HSV**.
3. Definição de intervalos de cor para identificar o vermelho.
4. Criação de uma **máscara de cor** para selecionar apenas os pixels dentro do intervalo definido.
5. Aplicação da máscara para extrair apenas as regiões vermelhas da imagem.
6. Conversão do restante da imagem para **escala de cinza**.
7. Combinação da imagem em cinza com as regiões vermelhas destacadas.

## Estrutura do projeto

Detectar_Cor_HSV
│
├── main.py        # Arquivo principal do programa
├── funcoes.py     # Funções auxiliares do processamento
└── img.png        # Imagem utilizada no teste

## Como executar

1. Instale as dependências necessárias:

pip install opencv-python numpy


2. Execute o programa:

python main.py

O programa exibirá:

* A imagem original
* A máscara da cor detectada
* O resultado final com o vermelho destacado
