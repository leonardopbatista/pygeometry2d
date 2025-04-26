# Biblioteca de Geometria 2D em Python
[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/leonardopbatista/pygeometry2d/blob/master/README.md)

Esta é uma biblioteca leve e simples para manipulação de geometrias 2D utilizando apenas bibliotecas nativas do Python. Com ela, é possível realizar operações comuns em geometria, como cálculo de distâncias, interseções, rotações e outras transformações geométricas.

## Recursos Principais
- Manipulação de pontos (`XY`).
- Criação e operações com linhas (`Line`).
- Suporte a arcos (`Arc`) e círculos (`Circle`).
- Geração de bounding boxes (`BoundingBox`).
- Manipulação de polylines (`Polyline`) e retângulos (`Rectangle`).
- Utilitários geométricos como normalização de ângulos, verificação de ortogonalidade e interseções entre formas.

## Instalação
Instale a biblioteca via pip:
```sh
pip install pygeometry2d
```
Depois, importe no seu projeto:
```python
from pygeometry2d import XY, Line, Circle, Polyline
```

## Basic Usage

### Criando pontos e linhas
```python
from pygeometry2d import XY, Line

p1 = XY(0, 0)
p2 = XY(4, 4)
line = Line(p1, p2)
print(line.length)  # 5.65685
```

## Examples

### Unindo segmentos conectados de forma desordenada em polylines
```python
from pygeometry2d import XY, Line, GeomUtils

segments = [
    Line(XY(1, 0), XY(2, 0)),
    Line(XY(10, 10), XY(11, 10)),
    Line(XY(0, 0), XY(1, 0)),
    Line(XY(2, 0), XY(3, 5))
]

joined_polylines = GeomUtils.join(segments)
for polyline in joined_polylines:
    print(polyline.points)
```

**Output:**
```
[(10, 10), (11, 10)]
[(0, 0), (1, 0), (2, 0), (3, 5)]
```

### Encontrando o circulo que passa por três pontos
```python
from pygeometry2d import XY, GeomUtils

p1 = XY(0, 1)
p2 = XY(1, 0)
p3 = XY(2, 1)

center, radius = GeomUtils.circle_by_3_points(p1, p2, p3)
print(f"Center: {center}, Radius: {radius}")
```

**Output:**
```
Center: (1.0, 1.0), Radius: 1.0
```

### Otimizando segmentos conectados de linhas
```python
from pygeometry2d import XY, Line, GeomUtils

segments = [
    Line(XY(0, 0), XY(1, 0)),
    Line(XY(2, 0), XY(3, 0)),
    Line(XY(1, 0), XY(2, 0)),
]

optimized = GeomUtils.optimize_segments(segments)
for line in optimized:
    print(line.start, line.end)
```

**Output:**
```
(0,0) (3,0)
```

### Encontrado a intersecção entre duas linhas
```python
from pygeometry2d import XY, Line

line1 = Line(XY(0, 0), XY(1, 1))
line2 = Line(XY(0, 1), XY(1, 0))

intersection = line1.intersection(line2)
print(intersection)
```

**Output:**
```
(0.5, 0.5)
```

### Obtendo a equação geral da reta (Ax + By + C = 0)
```python
from pygeometry2d import XY, Line

line = Line(XY(0, 0), XY(2, 2))
a, b, c = line.general_equation_coefficients
print(f"{a}x + {b}y + {c} = 0")
```

**Output:**
```
1x + -1.0y + 0.0 = 0
```

## Documentação

A documentação completa está disponível em [readthedocs](https://pygeometry2d.readthedocs.io/).

## Contribuição

Se quiser contribuir com melhorias ou sugerir novos recursos, fique à vontade para abrir um PR ou criar uma issue no repositório do GitHub.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.

