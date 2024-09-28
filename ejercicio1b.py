#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sympy as sp

# Ahora importamos las funciones de PyTC2

from pytc2.sintesis_dipolo import foster
from pytc2.dibujar import dibujar_foster_serie, dibujar_foster_derivacion
from pytc2.general import print_latex, print_subtitle, a_equal_b_latex_s

from pytc2.sintesis_dipolo import cauer_LC
from pytc2.dibujar import dibujar_cauer_LC

# Resolución simbólica
s = sp.symbols('s ', complex=True)
# Sea la siguiente función de excitación
FF = (3*s**3 + 7*s)/(s**4 + 7*s**2 + 10)

print_latex(a_equal_b_latex_s('F(s)', FF))

# Implementaremos FF mediante Cauer 1 o remociones continuas en infinito
koo, F_cauer_oo, rem = cauer_LC(FF, remover_en_inf=True)

print_latex(a_equal_b_latex_s(a_equal_b_latex_s('F(s)', FF)[1:-1], F_cauer_oo ))

# Tratamos a nuestra función inmitancia como una Z
dibujar_cauer_LC(koo, z_exc = F_cauer_oo)

# Tratamos a nuestra función inmitancia como una Y
dibujar_cauer_LC(koo, y_exc = F_cauer_oo)

# Implementaremos F mediante Cauer 2 o remociones continuas en cero
k0, F_cauer_0, rem = cauer_LC(FF, remover_en_inf=False)

print_latex(a_equal_b_latex_s(a_equal_b_latex_s('F(s)', FF)[1:-1], F_cauer_0 ))

# Tratamos a nuestra función inmitancia como una Z
dibujar_cauer_LC(k0, z_exc = F_cauer_0)

# Tratamos a nuestra función inmitancia como una Y
dibujar_cauer_LC(k0, y_exc = F_cauer_0)