#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sympy as sp

# Ahora importamos las funciones de PyTC2

from pytc2.sintesis_dipolo import foster
from pytc2.dibujar import dibujar_foster_serie, dibujar_foster_derivacion
from pytc2.general import print_latex, print_subtitle, a_equal_b_latex_s

# Resolución simbólica
s = sp.symbols('s ', complex=True)

# Sea la siguiente función de excitación
FF = (3*s**3 + 7*s)/(s**4 + 7*s**2 + 10)

print_latex(a_equal_b_latex_s('F(s)', FF))

# Se expande FF a la Foster
k0, koo, ki_wi, _, FF_foster = foster(FF)

print_latex(a_equal_b_latex_s('k_0', k0))

print_latex(a_equal_b_latex_s(r'k_1 = \left[ \frac{1}{ \frac{1}{s. \frac{\omega_i^2}{2.k_i} } + s . \frac{1}{2.k_i} } \right]  = \
                                             \left[ \frac{1}{ \frac{k_0}{s} + s . k_\infty } \right] = \
                                             \left[ k_0, k_\infty \right] = \
                                       \left[ \
                                             \left[ \frac{\omega_1^2}{2k_1}, \frac{1}{2k_1} \right] \
                                       \right]', ki_wi ))

print_latex(a_equal_b_latex_s('k_\infty', koo))


print_latex(a_equal_b_latex_s(a_equal_b_latex_s('F(s)', FF)[1:-1], FF_foster ))

print_subtitle('Foster derivación')

print_latex(a_equal_b_latex_s(a_equal_b_latex_s('Y(s)=F(s)', FF)[1:-1], FF_foster ))

# Tratamos a nuestra función imitancia como una Y
dibujar_foster_derivacion(k0, koo, ki_wi, y_exc = FF)