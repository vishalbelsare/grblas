from .. import binary, unary
from ..dtypes import BOOL
from .infix import MatrixInfixExpr, ScalarInfixExpr, VectorInfixExpr
from .matrix import Matrix, MatrixExpression, MatrixIndexExpr, TransposedMatrix
from .scalar import Scalar, ScalarExpression, ScalarIndexExpr
from .utils import output_type
from .vector import Vector, VectorExpression, VectorIndexExpr


def call_op(self, other, op, *, outer=False, union=False):
    type1 = output_type(self)
    type2 = output_type(other)
    types = {Matrix, TransposedMatrix, Vector}
    if type1 in types:
        if type2 in types:
            if outer:
                return self.ewise_add(other, op)
            if union:
                return self.ewise_union(other, op, False, False)
            return self.ewise_mult(other, op)
        return op(self, other)
    if type2 in types:
        return op(self, other)
    # Scalars
    if outer:
        if type1 is Scalar:
            return self.ewise_add(other, op)
        return other.ewise_add(self, op.commutes_to)
    if union:
        if type1 is Scalar:
            return self.ewise_union(other, op, False, False)
        return other.ewise_union(self, op.commutes_to, False, False)
    if type1 is Scalar:
        return self.ewise_mult(other, op)
    return other.ewise_mult(self, op.commutes_to)


def __divmod__(self, other):
    return (__floordiv__(self, other), __mod__(self, other))


def __rdivmod__(self, other):
    return (__floordiv__(other, self), __mod__(other, self))


def __abs__(self):
    return unary.abs(self)


def __invert__(self):
    if self.dtype != BOOL:
        raise TypeError(
            f"The invert operator, `~`, is not supported for {self.dtype.name} dtype."
            "  It is only supported for BOOL dtype."
        )
    return unary.lnot(self)


def __neg__(self):
    return unary.ainv(self)


def __xor__(self, other):
    expr = call_op(self, other, binary.lxor, outer=True)
    if expr.dtype != BOOL:
        raise TypeError(
            f"The __xor__ infix operator, `x ^ y`, is not supported for {expr.dtype.name} dtype."
            "  It is only supported for BOOL dtype (and it uses ewise_add--the union)."
        )
    return expr


def __rxor__(self, other):
    expr = call_op(other, self, binary.lxor, outer=True)
    if expr.dtype != BOOL:
        raise TypeError(
            f"The __xor__ infix operator, `x ^ y`, is not supported for {expr.dtype.name} dtype."
            "  It is only supported for BOOL dtype (and it uses ewise_add--the union)."
        )
    return expr


def __ixor__(self, other):
    other_type = output_type(other)
    if (
        other_type is Vector
        and self.ndim == 2
        or not self._is_scalar
        and other_type not in {Vector, Matrix, TransposedMatrix}
    ):
        self << __xor__(self, other)
    elif other.dtype != BOOL:
        raise TypeError(
            f"The __ixor__ infix operator, `x ^= y`, is not supported for {other.dtype.name} "
            "dtype.  It is only supported for BOOL dtype (and it uses ewise_add--the union)."
        )
    else:
        self(binary.lxor) << other
    return self


def __ior__(self, other):
    other_type = output_type(other)
    if (
        other_type is Vector
        and self.ndim == 2
        or not self._is_scalar
        and other_type not in {Vector, Matrix, TransposedMatrix}
    ):
        expr = call_op(self, other, binary.lor, outer=True)
        if expr.dtype != BOOL:
            raise TypeError(
                f"The __ior__ infix operator, `x |= y`, is not supported for {expr.dtype.name} "
                "dtype.  It is only supported for BOOL dtype (and it uses ewise_add--the union)."
            )
        self << expr
    elif other.dtype != BOOL:
        raise TypeError(
            f"The __ior__ infix operator, `x |= y`, is not supported for {other.dtype.name} "
            "dtype.  It is only supported for BOOL dtype (and it uses ewise_add--the union)."
        )
    else:
        self(binary.lor) << other
    return self


def __iand__(self, other):
    expr = call_op(self, other, binary.land)
    if expr.dtype != BOOL:
        raise TypeError(
            f"The __iand__ infix operator, `x &= y`, is not supported for {expr.dtype.name} dtype."
            "  It is only supported for BOOL dtype (and it uses ewise_mult--the intersection)."
        )
    self << expr
    return self


# Begin auto-generated code
def __eq__(self, other):
    return call_op(self, other, binary.eq)


def __ge__(self, other):
    return call_op(self, other, binary.ge)


def __gt__(self, other):
    return call_op(self, other, binary.gt)


def __le__(self, other):
    return call_op(self, other, binary.le)


def __lt__(self, other):
    return call_op(self, other, binary.lt)


def __ne__(self, other):
    return call_op(self, other, binary.ne)


def __add__(self, other):
    return call_op(self, other, binary.plus, outer=True)


def __radd__(self, other):
    return call_op(other, self, binary.plus, outer=True)


def __iadd__(self, other):
    other_type = output_type(other)
    if (
        other_type is Vector
        and self.ndim == 2
        or not self._is_scalar
        and other_type not in {Vector, Matrix, TransposedMatrix}
    ):
        self << __add__(self, other)
    else:
        self(binary.plus) << other
    return self


def __floordiv__(self, other):
    return call_op(self, other, binary.floordiv)


def __rfloordiv__(self, other):
    return call_op(other, self, binary.floordiv)


def __ifloordiv__(self, other):
    self << __floordiv__(self, other)
    return self


def __mod__(self, other):
    return call_op(self, other, binary.numpy.mod)


def __rmod__(self, other):
    return call_op(other, self, binary.numpy.mod)


def __imod__(self, other):
    self << __mod__(self, other)
    return self


def __mul__(self, other):
    return call_op(self, other, binary.times)


def __rmul__(self, other):
    return call_op(other, self, binary.times)


def __imul__(self, other):
    self << __mul__(self, other)
    return self


def __pow__(self, other):
    return call_op(self, other, binary.pow)


def __rpow__(self, other):
    return call_op(other, self, binary.pow)


def __ipow__(self, other):
    self << __pow__(self, other)
    return self


def __sub__(self, other):
    return call_op(self, other, binary.minus, union=True)


def __rsub__(self, other):
    return call_op(other, self, binary.minus, union=True)


def __isub__(self, other):
    self << __sub__(self, other)
    return self


def __truediv__(self, other):
    return call_op(self, other, binary.truediv)


def __rtruediv__(self, other):
    return call_op(other, self, binary.truediv)


def __itruediv__(self, other):
    self << __truediv__(self, other)
    return self


d = globals()
for name in [
    "__abs__",
    "__add__",
    "__divmod__",
    "__eq__",
    "__floordiv__",
    "__ge__",
    "__gt__",
    "__iadd__",
    "__iand__",
    "__ifloordiv__",
    "__imod__",
    "__imul__",
    "__invert__",
    "__ior__",
    "__ipow__",
    "__isub__",
    "__itruediv__",
    "__ixor__",
    "__le__",
    "__lt__",
    "__mod__",
    "__mul__",
    "__ne__",
    "__neg__",
    "__pow__",
    "__radd__",
    "__rdivmod__",
    "__rfloordiv__",
    "__rmod__",
    "__rmul__",
    "__rpow__",
    "__rsub__",
    "__rtruediv__",
    "__rxor__",
    "__sub__",
    "__truediv__",
    "__xor__",
]:
    val = d[name]
    if name not in {"__eq__", "__ne__"}:
        setattr(Scalar, name, val)
        if not name.startswith("__i") or name == "__invert__":
            setattr(ScalarExpression, name, val)
            setattr(ScalarInfixExpr, name, val)
            setattr(ScalarIndexExpr, name, val)
    setattr(Vector, name, val)
    setattr(Matrix, name, val)
    if not name.startswith("__i") or name == "__invert__":
        setattr(TransposedMatrix, name, val)
        setattr(VectorExpression, name, val)
        setattr(MatrixExpression, name, val)
        setattr(VectorInfixExpr, name, val)
        setattr(MatrixInfixExpr, name, val)
        setattr(VectorIndexExpr, name, val)
        setattr(MatrixIndexExpr, name, val)
# End auto-generated code


def _main():
    # Run via `python -m graphblas.core.infixmethods`
    comparisons = {
        "lt": "lt",
        "le": "le",
        "gt": "gt",
        "ge": "ge",
        "eq": "eq",
        "ne": "ne",
    }
    operations = {
        "add": "plus",
        "mul": "times",
        "truediv": "truediv",
        "floordiv": "floordiv",
        "mod": "numpy.mod",
        "pow": "pow",
        "sub": "minus",
    }
    # monoids with 0 identity use outer (ewise_add): + | ^
    outer = {
        "add",
    }
    union = {
        "sub",
    }
    custom = {
        "abs",
        "divmod",
        "invert",
        "neg",
        "rdivmod",
        "xor",
        "rxor",
        "ixor",
        "ior",
        "iand",
    }
    # Skipped: rshift, pos
    # Already used for syntax: lshift, and, or

    lines = []
    for method, op in sorted(comparisons.items()):
        lines.append(
            f"def __{method}__(self, other):\n    return call_op(self, other, binary.{op})\n\n"
        )
    for method, op in sorted(operations.items()):
        if method in outer:
            out = ", outer=True"
        elif method in union:
            out = ", union=True"
        else:
            out = ""
        lines.append(
            f"def __{method}__(self, other):\n"
            f"    return call_op(self, other, binary.{op}{out})\n\n"
        )
        lines.append(
            f"def __r{method}__(self, other):\n"
            f"    return call_op(other, self, binary.{op}{out})\n\n"
        )
        lines.append(f"def __i{method}__(self, other):")
        if method in outer:
            lines.append(
                "    other_type = output_type(other)\n"
                "    if (\n"
                "        other_type is Vector\n"
                "        and self.ndim == 2\n"
                "        or not self._is_scalar\n"
                "        and other_type not in {Vector, Matrix, TransposedMatrix}\n"
                "    ):\n"
                f"        self << __{method}__(self, other)\n"
                "    else:\n"
                f"        self(binary.{op}) << other"
            )
        else:
            lines.append(f"    self << __{method}__(self, other)")
        lines.append("    return self\n\n")
    methods = sorted(
        {f"__{x}__" for x in custom}
        | {f"__{x}__" for x in comparisons}
        | {f"__{x}__" for x in operations}
        | {f"__r{x}__" for x in operations}
        | {f"__i{x}__" for x in operations}
    )
    lines.append(
        "d = globals()\n"
        f"for name in {methods}:\n"
        "    val = d[name]\n"
        "    if name not in {'__eq__', '__ne__'}:\n"
        "        setattr(Scalar, name, val)\n"
        "        if not name.startswith('__i') or name == '__invert__':\n"
        "            setattr(ScalarExpression, name, val)\n"
        "            setattr(ScalarInfixExpr, name, val)\n"
        "            setattr(ScalarIndexExpr, name, val)\n"
        "    setattr(Vector, name, val)\n"
        "    setattr(Matrix, name, val)\n"
        "    if not name.startswith('__i') or name == '__invert__':\n"
        "        setattr(TransposedMatrix, name, val)\n"
        "        setattr(VectorExpression, name, val)\n"
        "        setattr(MatrixExpression, name, val)\n"
        "        setattr(VectorInfixExpr, name, val)\n"
        "        setattr(MatrixInfixExpr, name, val)\n"
        "        setattr(VectorIndexExpr, name, val)\n"
        "        setattr(MatrixIndexExpr, name, val)\n"
    )
    from pathlib import Path

    from .utils import _autogenerate_code

    _autogenerate_code(Path(__file__), "\n".join(lines))


if __name__ == "__main__":
    _main()
