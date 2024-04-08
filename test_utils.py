# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 23:27:01 2024

@author: Elisabeth Seifried
"""

from utils import triangular_surface_area

from utils import circular_surface_area

from utils import cylinder_volume

from utils import ms2kmh


def test_triangular_surface_area():
    assert triangular_surface_area(1, 2) == 1
    assert triangular_surface_area(2, 2) == 2
    assert triangular_surface_area(4, 2) == 4


def test_circular_surface_area():
    assert circular_surface_area(3) == 28.26
    assert circular_surface_area(6) == 113.04
    assert circular_surface_area(30) == 2826.0


def test_cylinder_volume():
    assert cylinder_volume(1, 2) == 6.28
    assert cylinder_volume(2, 2) == 25.12
    assert cylinder_volume(4, 3) == 150.72


def test_ms2kmh():
    assert ms2kmh(10) == 36.0
    assert ms2kmh(20) == 72.0
    assert ms2kmh(30) == 108.0
