"""
Copyright 2013 Steven Diamond

This file is part of CVXPY.

CVXPY is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

CVXPY is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with CVXPY.  If not, see <http://www.gnu.org/licenses/>.
"""

# Utility functions to solve circular imports.


def expression():
    from cvxpy.expressions import expression
    return expression.Expression


def add_expr():
    from cvxpy.atoms.affine import add_expr
    return add_expr.AddExpression


def constant():
    from cvxpy.expressions import constants
    return constants.Constant


def variable():
    from cvxpy.expressions import variable
    return variable.Variable


def index():
    from cvxpy.atoms.affine import index
    return index.index


def minimize():
    from cvxpy.problems import objective
    return objective.Minimize


def mul_expr():
    from cvxpy.atoms.affine import binary_operators
    return binary_operators.MulExpression


def div_expr():
    from cvxpy.atoms.affine import binary_operators
    return binary_operators.DivExpression


def neg_expr():
    from cvxpy.atoms.affine import unary_operators
    return unary_operators.NegExpression


def abs():
    from cvxpy.atoms.elementwise import abs
    return abs.abs


def lambda_min():
    from cvxpy.atoms import lambda_min
    return lambda_min


def pos():
    from cvxpy.atoms.elementwise import pos
    return pos.pos


def neg():
    from cvxpy.atoms.elementwise import neg
    return neg.neg


def partial_optimize():
    from cvxpy.transforms import partial_optimize
    return partial_optimize


def partial_problem():
    from cvxpy.transforms.partial_optimize import PartialProblem
    return PartialProblem


def power():
    from cvxpy.atoms.elementwise import power
    return power.power


def problem():
    from cvxpy.problems import problem
    return problem.Problem


def reshape():
    from cvxpy.atoms.affine import reshape
    return reshape.reshape


def transpose():
    from cvxpy.atoms.affine import transpose
    return transpose.transpose


def vec():
    from cvxpy.atoms.affine import vec
    return vec.vec
