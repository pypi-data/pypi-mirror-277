#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests pdfo on a few VERY simple problems.

Notes
-----
Do NOT follow the syntax here when you use pdfo. This file is written for
testing purpose, and it uses quite atypical syntax. See rosenbrock.py for an
illustration about how to use pdfo.
"""
import os
import struct
import sys
import unittest
import warnings

import numpy as np
from pdfo import pdfo
from scipy.optimize import Bounds, LinearConstraint


class TestPDFO(unittest.TestCase):
    SOLVERS = ['uobyqa', 'newuoa', 'bobyqa', 'lincoa', 'cobyla', 'pdfo']
    RELEASE = True
    PRECISION = np.float64(1e-6)
    QUIET = False
    NRUN = 1
    EPS = np.finfo(np.float64).eps

    def setUp(self):
        """Initializes the pdfo tests."""
        self.module_pdfo = __import__('pdfo')
        self.options = {'debug': True, 'chkfunval': True}
        self.type_list = ['unconstrained', 'bound-constrained', 'linearly-constrained', 'nonlinearly-constrained']
        self.solver_list = [['uobyqa', 'newuoa', 'bobyqa', 'lincoa', 'cobyla'],
                            ['bobyqa', 'lincoa', 'cobyla'],
                            ['lincoa', 'cobyla'],
                            ['cobyla']]
        self.fun_list = [self.goldp, self.mcc, lambda x: self.hmlb(x)[0], lambda x: self.chrosen(x)[0], self.chebquad]
        self.fun_list_name = \
            [self.goldp.__name__, self.mcc.__name__, self.hmlb.__name__, self.chrosen.__name__, self.chebquad.__name__]
        self.x0_list = [np.zeros(2), np.zeros(2), np.zeros(2), np.zeros(3), np.zeros(4)]
        self.fopt_list = [[3., -1.913222954981037, 0., 0., 0.],
                          [32.57759829292702, -0.507689349668105, 144.125, 0.7, 0.2127291653880991],
                          [600., 0.934627336363561, 136, 0.601538194898651, 0.29733407628744646],
                          [600., 0.934627336363561, 129.3402195198189, 0.24054273877510723, 0.02614379108922064]]
        self.clflag_list = [False] if self.RELEASE else [True, False]
        self.PERTURB = 0 if self.NRUN == 1 else 1e-15
        warnings.filterwarnings('ignore')

    def runTest(self):
        """PDFO tests on unconstrained and constrained problems."""
        devnull = open(os.devnull, 'w')  # The empty stdout redirection
        default_stdout = sys.stdout  # The default value of stdout (screen)

        for irun in range(1, self.NRUN + 1):
            if not self.QUIET and self.NRUN > 1:
                print('\nTest {}:\n'.format(irun))
            for i_type, p_type in enumerate(self.type_list):
                if not self.QUIET:
                    print('\nTesting {} problems...'.format(p_type.replace('-', ' ')))
                    if not self.RELEASE:
                        print()

                for solver in self.solver_list[i_type]:
                    for x0, fun, fun_name, fopt in zip(self.x0_list, self.fun_list, self.fun_list_name, self.fopt_list[i_type]):
                        for clflag in self.clflag_list:
                            n = x0.size
                            if solver != 'cobyla' or fun_name != 'chebquad':
                                r = np.abs(np.sin(1e3 * np.array(solver + fun_name + p_type, 'c').view(np.uint8).sum() * irun * (np.arange(n) + 1)))
                                x0r = x0 + self.PERTURB * r
                            else:
                                x0r = x0

                            linear_constraints = LinearConstraint(np.ones((1, n)), None, 1)
                            lb, ub = -0.5 * np.ones(n), 0.5 * np.ones(n)
                            zeros_n = np.zeros(n)
                            inf_n = np.full(n, np.inf)
                            nonlinear_constraints = {'type': 'ineq', 'fun': lambda x: self.ballcon(x, np.zeros(n), 1)}
                            options = self.options.copy()
                            options['classical'] = clflag

                            sys.stdout = devnull

                            args = {'fun': fun, 'x0': x0r, 'options': options}
                            if p_type == 'unconstrained':
                                # DO NOT REMOVE: it is necessary for unconstrained iteration not to execute the 'else'
                                # statement
                                pass
                            elif p_type == 'bound-constrained':
                                args['bounds'] = Bounds(lb, ub)
                            elif p_type == 'linearly-constrained':
                                args['bounds'] = Bounds(zeros_n, inf_n)
                                args['constraints'] = linear_constraints
                            else:
                                args['bounds'] = Bounds(zeros_n, inf_n)
                                args['constraints'] = nonlinear_constraints
                            func_solver = getattr(self.module_pdfo, solver)
                            global_res = func_solver(**args)

                            args['method'] = solver
                            pdfo_res = pdfo(**args)
                            x = pdfo_res.x
                            fx = pdfo_res.fun

                            sys.stdout = default_stdout

                            # the precision for cobyla is lower
                            tol = self.PRECISION
                            if solver == 'cobyla' and struct.calcsize('P') == 8:
                                tol = max(1e3 * tol, 1e-2)
                            elif solver == 'cobyla':
                                tol = max(1e4 * tol, 1e-1)

                            if not self.QUIET and not self.RELEASE:
                                print('solver = {},\tfun = {}'.format(solver, fun_name), end='\t\t')
                                print('fx = {0:1.15e},\tfopt={1:1.15e}'.format(fx, fopt))

                            self.assertLessEqual(np.linalg.norm(global_res.x - x),  tol)
                            self.assertLessEqual((fx - fopt) / max(1., abs(fopt)),  tol)
                if not self.QUIET:
                    print('Success.')

    @staticmethod
    def chrosen(x):
        """Chained Rosenbrock function."""
        alpha = 4

        f = 0  # Function value
        g = np.zeros_like(x)  # Gradient
        n = g.size
        h = np.zeros((n, n))  # Hessian

        for i in range(n - 1):
            f += (x[i] - 1) ** 2 + alpha * (x[i] ** 2 - x[i + 1]) ** 2

            g[i] += 2 * (x[i] - 1) + 4 * alpha * (x[i] ** 2 - x[i + 1]) * x[i]
            g[i + 1] -= 2 * alpha * (x[i] ** 2 - x[i + 1])

            h[i, i] += 2 + 4 * alpha * (3 * x[i] ** 2 - x[i + 1])
            h[i, i + 1] -= 4 * alpha * x[i]
            h[i + 1, i] -= 4 * alpha * x[i]
            h[i + 1, i + 1] += 2 * alpha
        return f, g, h

    @staticmethod
    def chebquad(x):
        """Chebyquad function."""
        n = x.size
        y = np.ones((n + 1, n))
        y[1, :] = 2 * x - 1
        for i in range(1, n):
            y[i + 1, :] = 2 * y[1, :] * y[i, :] - y[i - 1, :]
        f = 0
        for i in range(1, n + 2):
            tmp = np.mean(y[i - 1, :])
            if i % 2 == 1:
                tmp += 1 / float(i * i - 2 * i)
            f += tmp * tmp
        return f

    @staticmethod
    def hmlb(x):
        """Himmelblau's function."""
        f = (x[0] ** 2 + x[1] - 11) ** 2 + (x[0] + x[1] ** 2 - 7) ** 2
        g = np.empty(2, dtype=np.float64)
        g[0] = -7 + x[1] + x[1] ** 2 + 2 * x[0] * (-11 + x[0] ** 2 + x[1])
        g[1] = -11 + x[0] ** 2 + x[1] + 2 * x[1] * (-7 + x[0] + x[1] ** 2)
        g *= 2
        return f, g

    @staticmethod
    def goldp(x):
        """Goldstein-Price function."""
        f1a = (x[0] + x[1] + 1) ** 2
        f1b = 19 - 14 * x[0] + 3 * x[0] ** 2 - 14 * x[1] + 6 * x[0] * x[1] - 3 * x[1] ** 2
        f1 = 1 + f1a * f1b
        f2a = (2 * x[0] - 3 * x[1]) ** 2
        f2b = 18 - 32 * x[0] + 12 * x[0] ** 2 + 48 * x[1] - 36 * x[0] * x[1] + 27 * x[1] ** 2
        f2 = 30 + f2a * f2b
        return f1 * f2

    @staticmethod
    def mcc(x):
        """McCormick function."""
        f1 = np.sin(x[0] + x[1])
        f2 = (x[0] - x[1]) ** 2
        f3 = -1.5 * x[0]
        f4 = 2.5 * x[1]
        return f1 + f2 + f3 + f4 + 1

    @staticmethod
    def ballcon(x, center, radius):
        """Represents the ball constraints ||x - center||_2 <= radius."""
        return radius ** 2 - np.linalg.norm(x - center) ** 2


if __name__ == '__main__':
    # Get the release flag.
    if len(sys.argv) > 1:
        release = sys.argv.pop(1)
        TestPDFO.RELEASE = False if release == '0' else True

    # Get the required precision.
    if len(sys.argv) > 1:
        precision_str = sys.argv.pop(1)
        try:
            precision = np.float64(precision_str)
            TestPDFO.PRECISION = precision
        except ValueError:
            w_message = 'The precision cannot be read: {} received.'.format(precision_str)
            warnings.warn(w_message, Warning)

    # Get the required number of run.
    if len(sys.argv) > 1:
        nrun_str = sys.argv.pop(1)
        try:
            nrun = int(nrun_str)
            TestPDFO.NRUN = nrun
        except ValueError:
            w_message = 'The number of run cannot be read: {} received.'.format(nrun_str)
            warnings.warn(w_message, Warning)

    # Launch the main tests.
    unittest.main()
