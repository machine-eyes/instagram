#  Representação de imagens em Arrays

#### Tela 0

### Parte 1: O que é pixel 

As imagens são constituídas por pixeis, mas pera o que é um pixel ?

Pixel é a menor unidade que constituí a imagem.

---

#### Tela 1

Quando nós olhamos uma imagem, ela tem geralmente tamanhos como, por exemplo, 1.920 x 1.080 - o famoso *full hd*. Bom, esses números representam uma quantidade de pixeis, ou seja, o *full hd* tem 1920 pixeis de altura e 1080 pixeis de largura .

![pngwing.com](https://iconarchive.com/download/i27092/ph03nyx/super-mario/Retro-Mario.ico)

---

#### Tela 2

Ao olhar bem para o nosso querido Mário Bros podemos ver que não há cantos arredondados,  isso porquê a imagem está com uma resolução muito baixa, em outras palavras "há poucos pixeis". 

Via esse raciocínio, quanto mais pixels, mais formas arredondadas podemos criar, seguindo este conceito de: "quanto mais quinas o quadrilátero tiver, mais tende a se parecer com um circulo".

---

#### Tela 3

#### 																											Hexágono (6 lados)

![](https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Regular_hexagon.svg/350px-Regular_hexagon.svg.png)



#### Icoságono (20 lados)



 ![](https://i.pinimg.com/originals/9e/c2/c2/9ec2c2fcb01fb9e4422f039b6fa98052.png)

















### Parte 2: Armazenamento de uma imagem como vetor:

---

#### Tela 0 

Parte 2: Armazenamento de uma imagem como vetor

---

#### Tela 1

Podemos ver um sistema de divisão da imagem, caso nós esforcemos  a lembrar, isso nos retoma ao conceito de planilhas  ou até mesmo matrizes onde temos coordenadas na horizontal e na vertical. 

![](https://lh3.googleusercontent.com/proxy/UFUrKeBeXsy2oVUaShAx7Xz4sSKztXctIoG3hnG05TGswEEVUknXnZ62bSAWDwQliFbOrfidFowAGRbjKEc0gS1EHWYGi60Y6BTQ1ktp9JFtAHr4OJpp2LBWPjWVaw61g0ntnguO8glieZkV7jT4vJd8hezElv_apofGXVhAQTq7I_Jkeuix13TGtFHA3kqqos1Pz8iFBsjECFQNPpWwoGhu29AjzOmfmfgImA5UauFUScwqo_OO0voXuI5lFFJDeNuAUqAFWH0ZYaB_2XnvvFxaVIAm7oUcnjqj)

---

#### Tela 2

Usando os sistemas de cores podemos atribuir a cada pixel desse uma cor, olhando a primeira linha e levando em consideração as cores a seguir:

- Suponha que a cor branca seja o numero  "0" e exita uma escala ate "10" que é o preto absoluto
- Esta primeira linha facilmente poderia ser representada por [0, 0, 0,..., 0] repare que o numero de elemento ( números entre as virgulas )corresponde ao numero de quadrados na linha 1. Este é o conceito de uma representação por "Array".
- Agora e se fossemos representar a imagem toda [linha 1, linha 2, linha 3, linha 4 .... , ultima linha] onde cada uma dessas linha seja um outro vetor.