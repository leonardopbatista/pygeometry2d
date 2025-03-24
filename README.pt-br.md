# Biblioteca de Geometria 2D em Python
[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/leonardopbatista/pygeometry2d/blob/master/README.md)

Esta é uma biblioteca leve e simples para manipulação de geometrias 2D utilizando apenas bibliotecas nativas do Python. Com ela, é possível realizar operações comuns em geometria, como cálculo de distâncias, interseções, rotações e outras transformações geométricas.

### Recursos Principais
- Manipulação de pontos (`XY`).
- Criação e operações com linhas (`Line`).
- Suporte a arcos (`Arc`) e círculos (`Circle`).
- Geração de bounding boxes (`BoundingBox`).
- Manipulação de polylines (`Polyline`) e retângulos (`Rectangle`).
- Utilitários geométricos como normalização de ângulos, verificação de ortogonalidade e interseções entre formas.

### Instalação
Instale a biblioteca via pip:
```sh
pip install pygeometry2d
```
Depois, importe no seu projeto:
```python
from pygeometry2d import XY, Line, Circle, Polyline
```

### Exemplos de Uso

#### Criando e Manipulando Pontos

```python
p1 = XY(3, 4)
p2 = XY(6, 8)
distance = p1.distance(p2)
print(distance)  # 5.0
```

#### Criando e Manipulando Linhas

```python
line = Line(XY(0, 0), XY(3, 4))
print(line.length)  # Comprimento da linha
```

#### Criando um Círculo e Verificando Interseções

```python
circle = Circle(XY(0, 0), 10)
line = Line(XY(-10, 0), XY(10, 0))
intersections = circle.intersection(line)
print(intersections)  # Lista de pontos de interseção
```

#### Trabalhando com Polylines

```python
polyline = Polyline([XY(0, 0), XY(3, 4), XY(6, 0)])
print(polyline.length)  # Comprimento total da polyline
```

## Documentação

A documentação completa está disponível em [readthedocs](https://pygeometry2d.readthedocs.io/).

### Contribuição
Se quiser contribuir com melhorias ou sugerir novos recursos, fique à vontade para abrir um PR ou criar uma issue no repositório do GitHub.

### Licença
Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.

