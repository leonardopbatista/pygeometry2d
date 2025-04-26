# 2D Geometry Library in Python
[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/leonardopbatista/pygeometry2d/blob/master/README.md)
[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](https://github.com/leonardopbatista/pygeometry2d/blob/master/README.pt-br.md)

This is a lightweight and simple library for handling 2D geometries using only Python's native libraries. It allows performing common geometric operations such as distance calculations, intersections, rotations, and other geometric transformations.

## Main Features

- Point manipulation (`XY` class).
- Creation and operations with lines (`Line`).
- Support for arcs (`Arc`) and circles (`Circle`).
- Bounding box generation (`BoundingBox`).
- Handling polylines (`Polyline`) and rectangles (`Rectangle`).
- Geometric utilities such as angle normalization, orthogonality checking, shape intersections and polyline optimization.

## Installation

Install the library via pip:

```sh
pip install pygeometry2d
```

Then, import it into your project:

```python
from pygeometry2d import XY, Line, Circle, Polyline
```

## Basic Usage

### Create points and lines
```python
from pygeometry2d import XY, Line

p1 = XY(0, 0)
p2 = XY(4, 4)
line = Line(p1, p2)
print(line.length)  # 5.65685
```

## Examples

### Join disordered connected segments into polylines
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

### Find circle passing through three points
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

### Optimize connected line segments
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

### Find intersection between two lines
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

### Get the general equation of a line (Ax + By + C = 0)
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

## Documentation

Full documentation is available on [readthedocs](https://pygeometry2d.readthedocs.io/).

## Contribution

If you would like to contribute with improvements or suggest new features, feel free to open a PR or create an issue on the GitHub repository.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

