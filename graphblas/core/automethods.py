"""Define functions to use as property methods on expressions.

These will automatically compute the value and avoid the need for ``.new()``.

To automatically create the functions, run:

$ python -m graphblas.core.automethods

"""

from .. import config


def _get_value(self, attr=None, default=None):
    if config.get("autocompute"):
        if self._value is None:
            self._value = self.new()
        if attr is None:
            return self._value
        return getattr(self._value, attr)
    if default is not None:
        return default.__get__(self)
    raise TypeError(
        f"{attr} not enabled for objects of type {type(self)}.  "
        f"Use `.new()` to create a new {self.output_type.__name__}.\n\n"
        "Hint: use `graphblas.config.set(autocompute=True)` to enable "
        "automatic computation of expressions."
    )


def _set_name(self, name):
    self._get_value().name = name


def default__eq__(self, other):
    raise TypeError(
        f"__eq__ not enabled for objects of type {type(self)}.  "
        f"Use `.new()` to create a new {self.output_type.__name__}, then use `.isequal` method.\n\n"
        "Hint: use `graphblas.config.set(autocompute=True)` to enable "
        "automatic computation of expressions."
    )


# Begin auto-generated code
def S(self):
    return self._get_value("S")


def T(self):
    return self._get_value("T")


def V(self):
    return self._get_value("V")


def __and__(self):
    return self._get_value("__and__")


def __array__(self):
    return self._get_value("__array__")


def __bool__(self):
    return self._get_value("__bool__")


def __complex__(self):
    return self._get_value("__complex__")


def __contains__(self):
    return self._get_value("__contains__")


def __eq__(self):
    return self._get_value("__eq__", default__eq__)


def __float__(self):
    return self._get_value("__float__")


def __getitem__(self):
    return self._get_value("__getitem__")


def __index__(self):
    return self._get_value("__index__")


def __int__(self):
    return self._get_value("__int__")


def __iter__(self):
    return self._get_value("__iter__")


def __matmul__(self):
    return self._get_value("__matmul__")


def __ne__(self):
    return self._get_value("__ne__")


def __or__(self):
    return self._get_value("__or__")


def __rand__(self):
    return self._get_value("__rand__")


def __rmatmul__(self):
    return self._get_value("__rmatmul__")


def __ror__(self):
    return self._get_value("__ror__")


def _as_matrix(self):
    return self._get_value("_as_matrix")


def _as_vector(self):
    return self._get_value("_as_vector")


def _carg(self):
    return self._get_value("_carg")


def _is_empty(self):
    return self._get_value("_is_empty")


def _name_html(self):
    return self._get_value("_name_html")


def _nvals(self):
    return self._get_value("_nvals")


def apply(self):
    return self._get_value("apply")


def diag(self):
    return self._get_value("diag")


def ewise_add(self):
    return self._get_value("ewise_add")


def ewise_mult(self):
    return self._get_value("ewise_mult")


def ewise_union(self):
    return self._get_value("ewise_union")


def gb_obj(self):
    return self._get_value("gb_obj")


def get(self):
    return self._get_value("get")


def inner(self):
    return self._get_value("inner")


def is_empty(self):
    return self._get_value("is_empty")


def isclose(self):
    return self._get_value("isclose")


def isequal(self):
    return self._get_value("isequal")


def kronecker(self):
    return self._get_value("kronecker")


def mxm(self):
    return self._get_value("mxm")


def mxv(self):
    return self._get_value("mxv")


def name(self):
    return self._get_value("name")


def nvals(self):
    return self._get_value("nvals")


def outer(self):
    return self._get_value("outer")


def power(self):
    return self._get_value("power")


def reduce(self):
    return self._get_value("reduce")


def reduce_columnwise(self):
    return self._get_value("reduce_columnwise")


def reduce_rowwise(self):
    return self._get_value("reduce_rowwise")


def reduce_scalar(self):
    return self._get_value("reduce_scalar")


def reposition(self):
    return self._get_value("reposition")


def select(self):
    return self._get_value("select")


def ss(self):
    return self._get_value("ss")


def to_coo(self):
    return self._get_value("to_coo")


def to_csc(self):
    return self._get_value("to_csc")


def to_csr(self):
    return self._get_value("to_csr")


def to_dcsc(self):
    return self._get_value("to_dcsc")


def to_dcsr(self):
    return self._get_value("to_dcsr")


def to_dense(self):
    return self._get_value("to_dense")


def to_dict(self):
    return self._get_value("to_dict")


def to_dicts(self):
    return self._get_value("to_dicts")


def to_edgelist(self):
    return self._get_value("to_edgelist")


def value(self):
    return self._get_value("value")


def vxm(self):
    return self._get_value("vxm")


def wait(self):
    return self._get_value("wait")


def __iadd__(self, other):
    raise TypeError(f"'__iadd__' not supported for {type(self).__name__}")


def __iand__(self, other):
    raise TypeError(f"'__iand__' not supported for {type(self).__name__}")


def __ifloordiv__(self, other):
    raise TypeError(f"'__ifloordiv__' not supported for {type(self).__name__}")


def __imatmul__(self, other):
    raise TypeError(f"'__imatmul__' not supported for {type(self).__name__}")


def __imod__(self, other):
    raise TypeError(f"'__imod__' not supported for {type(self).__name__}")


def __imul__(self, other):
    raise TypeError(f"'__imul__' not supported for {type(self).__name__}")


def __ior__(self, other):
    raise TypeError(f"'__ior__' not supported for {type(self).__name__}")


def __ipow__(self, other):
    raise TypeError(f"'__ipow__' not supported for {type(self).__name__}")


def __isub__(self, other):
    raise TypeError(f"'__isub__' not supported for {type(self).__name__}")


def __itruediv__(self, other):
    raise TypeError(f"'__itruediv__' not supported for {type(self).__name__}")


def __ixor__(self, other):
    raise TypeError(f"'__ixor__' not supported for {type(self).__name__}")


# End auto-generated code
def _main():
    from pathlib import Path

    from .utils import _autogenerate_code

    common = {
        "_name_html",
        "_nvals",
        "gb_obj",
        "get",
        "isclose",
        "isequal",
        "name",
        "nvals",
        "wait",
        # For infix
        "__and__",
        "__or__",
        "__rand__",
        "__ror__",
        # Delayed methods
        "apply",
        "ewise_add",
        "ewise_mult",
        "ewise_union",
        "select",
    }
    scalar = {
        "__array__",
        "__bool__",
        "__complex__",
        "__eq__",
        "__float__",
        "__index__",
        "__int__",
        "__ne__",
        "_as_matrix",
        "_as_vector",
        "_is_empty",
        "is_empty",
        "value",
    }
    vector_matrix = {
        "S",
        "V",
        "__contains__",
        "__getitem__",
        "__iter__",
        "__matmul__",
        "__rmatmul__",
        "_carg",
        "diag",
        "reposition",
        "ss",
        "to_coo",
        "to_dense",
    }
    vector = {
        "_as_matrix",
        "inner",
        "outer",
        "reduce",
        "to_dict",
        "vxm",
    }
    matrix = {
        "_as_vector",
        "T",
        "kronecker",
        "mxm",
        "mxv",
        "power",
        "reduce_columnwise",
        "reduce_rowwise",
        "reduce_scalar",
        "to_csc",
        "to_csr",
        "to_dcsc",
        "to_dcsr",
        "to_dicts",
        "to_edgelist",
    }
    common_raises = set()
    scalar_raises = {
        "__matmul__",
        "__rmatmul__",
    }
    vector_matrix_raises = {
        "__array__",
        "__bool__",
    }
    has_defaults = {
        "__eq__",
    }
    # no inplace math for expressions
    bad_sugar = {
        "__iadd__",
        "__ifloordiv__",
        "__imod__",
        "__imul__",
        "__ipow__",
        "__isub__",
        "__itruediv__",
        "__ixor__",
        "__ior__",
        "__iand__",
        "__imatmul__",
    }
    # Copy the result of this above
    lines = []
    for name in sorted(common | scalar | vector_matrix | vector | matrix):
        lines.append(f"def {name}(self):")
        if name in has_defaults:
            lines.append(f"    return self._get_value({name!r}, default{name})\n\n")
        else:
            lines.append(f"    return self._get_value({name!r})\n\n")
    for name in sorted(bad_sugar):
        lines.append(f"def {name}(self, other):")
        lines.append(
            f'    raise TypeError(f"{name!r} not supported for {{type(self).__name__}}")\n\n'
        )

    _autogenerate_code(Path(__file__), "\n".join(lines))

    # Copy to scalar.py and infix.py
    lines = []
    lines.append("    _get_value = automethods._get_value")
    for name in sorted(common | scalar):
        if name == "name":
            lines.append(
                "    name = wrapdoc(Scalar.name)(property(automethods.name))"
                ".setter(automethods._set_name)"
            )
        else:
            lines.append(f"    {name} = wrapdoc(Scalar.{name})(property(automethods.{name}))")
    lines.append("    # These raise exceptions")
    for name in sorted(common_raises | scalar_raises):
        lines.append(f"    {name} = Scalar.{name}")
    for name in sorted(bad_sugar):
        if name == "__imatmul__":
            continue
        lines.append(f"    {name} = automethods.{name}")

    thisdir = Path(__file__).parent
    infix_exclude = {"_get_value"}

    def get_name(line):
        return line.strip().split(" ", 1)[0]

    text = "\n".join(lines) + "\n    "
    _autogenerate_code(thisdir / "scalar.py", text, "Scalar")
    text = "\n".join(line for line in lines if get_name(line) not in infix_exclude) + "\n    "
    _autogenerate_code(thisdir / "infix.py", text, "Scalar")

    # Copy to vector.py and infix.py
    lines = []
    lines.append("    _get_value = automethods._get_value")
    for name in sorted(common | vector_matrix | vector):
        if name == "ss":
            lines.append('    if backend == "suitesparse":')
            indent = "    "
        else:
            indent = ""
        if name == "name":
            lines.append(
                "    name = wrapdoc(Vector.name)(property(automethods.name))"
                ".setter(automethods._set_name)"
            )
        else:
            lines.append(
                f"    {indent}{name} = wrapdoc(Vector.{name})(property(automethods.{name}))"
            )
        if name == "ss":
            lines.append('    else:\n        ss = Vector.__dict__["ss"]  # raise if used')
    lines.append("    # These raise exceptions")
    for name in sorted(common_raises | vector_matrix_raises):
        lines.append(f"    {name} = Vector.{name}")
    for name in sorted(bad_sugar):
        lines.append(f"    {name} = automethods.{name}")

    text = "\n".join(lines) + "\n    "
    _autogenerate_code(thisdir / "vector.py", text, "Vector")
    text = "\n".join(line for line in lines if get_name(line) not in infix_exclude) + "\n    "
    _autogenerate_code(thisdir / "infix.py", text, "Vector")

    # Copy to matrix.py and infix.py
    lines = []
    lines.append("    _get_value = automethods._get_value")
    for name in sorted(common | vector_matrix | matrix):
        if name == "ss":
            lines.append('    if backend == "suitesparse":')
            indent = "    "
        else:
            indent = ""
        if name == "name":
            lines.append(
                "    name = wrapdoc(Matrix.name)(property(automethods.name))"
                ".setter(automethods._set_name)"
            )
        else:
            lines.append(
                f"    {indent}{name} = wrapdoc(Matrix.{name})(property(automethods.{name}))"
            )
        if name == "ss":
            lines.append('    else:\n        ss = Matrix.__dict__["ss"]  # raise if used')
    lines.append("    # These raise exceptions")
    for name in sorted(common_raises | vector_matrix_raises):
        lines.append(f"    {name} = Matrix.{name}")
    for name in sorted(bad_sugar):
        lines.append(f"    {name} = automethods.{name}")

    text = "\n".join(lines) + "\n    "
    _autogenerate_code(thisdir / "matrix.py", text, "Matrix")
    text = "\n".join(line for line in lines if get_name(line) not in infix_exclude) + "\n    "
    _autogenerate_code(thisdir / "infix.py", text, "Matrix")


if __name__ == "__main__":
    _main()
