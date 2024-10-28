import itertools

from .. import backend
from ..exceptions import check_status, check_status_carg
from . import NULL, ffi, lib


class Descriptor:
    _name_counter = itertools.count()

    def __init__(
        self,
        gb_obj,
        output_replace=False,
        mask_complement=False,
        mask_structure=False,
        transpose_first=False,
        transpose_second=False,
        *,
        name=None,
    ):
        self.gb_obj = gb_obj
        self.name = f"Desc_{next(Descriptor._name_counter)}" if name is None else name
        self.output_replace = output_replace
        self.mask_complement = mask_complement
        self.mask_structure = mask_structure
        self.transpose_first = transpose_first
        self.transpose_second = transpose_second
        self._context = None  # Used by SuiteSparse:GraphBLAS 8

    @property
    def _carg(self):
        return self.gb_obj[0]

    def __del__(self):
        gb_obj = getattr(self, "gb_obj", None)
        if gb_obj is not None and lib is not None:  # pragma: no branch (safety)
            # it's difficult/dangerous to record the call, b/c `self.name` may not exist
            check_status(lib.GrB_Descriptor_free(gb_obj), self)


class BuiltinDescriptor(Descriptor):
    @property
    def _carg(self):
        return self.gb_obj

    def __del__(self):  # pragma: no cover (safety)
        pass


_desc_names = {
    # OUTP, MSK_COMP, MSK_STRUCT, TRANS0, TRANS1
    (False, False, False, False, True): "GrB_DESC_T1",
    (False, False, False, True, False): "GrB_DESC_T0",
    (False, False, False, True, True): "GrB_DESC_T0T1",
    (False, True, False, False, False): "GrB_DESC_C",
    (False, False, True, False, False): "GrB_DESC_S",
    (False, True, False, False, True): "GrB_DESC_CT1",
    (False, False, True, False, True): "GrB_DESC_ST1",
    (False, True, False, True, False): "GrB_DESC_CT0",
    (False, False, True, True, False): "GrB_DESC_ST0",
    (False, True, False, True, True): "GrB_DESC_CT0T1",
    (False, False, True, True, True): "GrB_DESC_ST0T1",
    (False, True, True, False, False): "GrB_DESC_SC",
    (False, True, True, False, True): "GrB_DESC_SCT1",
    (False, True, True, True, False): "GrB_DESC_SCT0",
    (False, True, True, True, True): "GrB_DESC_SCT0T1",
    (True, False, False, False, False): "GrB_DESC_R",
    (True, False, False, False, True): "GrB_DESC_RT1",
    (True, False, False, True, False): "GrB_DESC_RT0",
    (True, False, False, True, True): "GrB_DESC_RT0T1",
    (True, True, False, False, False): "GrB_DESC_RC",
    (True, False, True, False, False): "GrB_DESC_RS",
    (True, True, False, False, True): "GrB_DESC_RCT1",
    (True, False, True, False, True): "GrB_DESC_RST1",
    (True, True, False, True, False): "GrB_DESC_RCT0",
    (True, False, True, True, False): "GrB_DESC_RST0",
    (True, True, False, True, True): "GrB_DESC_RCT0T1",
    (True, False, True, True, True): "GrB_DESC_RST0T1",
    (True, True, True, False, False): "GrB_DESC_RSC",
    (True, True, True, False, True): "GrB_DESC_RSCT1",
    (True, True, True, True, False): "GrB_DESC_RSCT0",
    (True, True, True, True, True): "GrB_DESC_RSCT0T1",
}
_desc_map = {
    key: BuiltinDescriptor(getattr(lib, val), *key, name=val) for key, val in _desc_names.items()
}
_desc_names[(False, False, False, False, False)] = "NULL"
_desc_map[(False, False, False, False, False)] = None


def lookup(
    *,
    output_replace=False,
    mask_complement=False,
    mask_structure=False,
    transpose_first=False,
    transpose_second=False,
    **opts,
):
    if opts:
        # Normalize opts by making all keys lowercase and raise if duplicates
        new_opts = {key.lower(): val for key, val in opts.items()}
        if len(opts) != len(new_opts):
            extra = opts.keys() - new_opts.keys()
            extra |= opts.keys() & {x.lower() for x in extra}
            raise ValueError(
                "Duplicate descriptor options given (descriptor options are case-insensitive): "
                + ", ".join(sorted(extra, key=lambda x: (x.lower(), x)))
            )
        if backend == "suitesparse":
            from .ss.descriptor import get_descriptor

            return get_descriptor(
                output_replace=output_replace,
                mask_complement=mask_complement,
                mask_structure=mask_structure,
                transpose_first=transpose_first,
                transpose_second=transpose_second,
                **opts,
            )
        raise ValueError(
            f"Extra descriptor options not possible with {backend!r} backend; "
            f"got {', '.join(str(x) for x in opts)}"
        )
    key = (
        output_replace,
        mask_complement,
        mask_structure,
        transpose_first,
        transpose_second,
    )
    if key not in _desc_map:  # pragma: no cover (unnecessary)
        # We currently don't need this block of code!
        # All 32 possible descriptors are currently already added to _desc_map.
        # Nevertheless, this code may be useful some day, because we will want
        # to expose extension descriptors.
        desc = ffi.new("GrB_Descriptor*")
        if not any(key):
            # Default descriptor stays a NULL pointer
            desc[0] = NULL
        else:
            check_status_carg(lib.GrB_Descriptor_new(desc), "Descriptor", desc[0])
            for cond, field, val in [
                (output_replace, lib.GrB_OUTP, lib.GrB_REPLACE),
                (mask_complement, lib.GrB_MASK, lib.GrB_COMP),
                (mask_structure, lib.GrB_MASK, lib.GrB_STRUCTURE),
                (transpose_first, lib.GrB_INP0, lib.GrB_TRAN),
                (transpose_second, lib.GrB_INP1, lib.GrB_TRAN),
            ]:
                if cond:
                    check_status_carg(
                        lib.GrB_Descriptor_set(desc[0], field, val), "Descriptor", desc[0]
                    )
        _desc_map[key] = Descriptor(desc, *key)
    return _desc_map[key]
