from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Y(_BaseTraceHierarchyType):
    # class properties
    # --------------------
    _parent_path_str = "volume.caps"
    _path_str = "volume.caps.y"
    _valid_props = {"fill", "show"}

    # fill
    # ----
    @property
    def fill(self):
        """
        Sets the fill ratio of the `caps`. The default fill value of
        the `caps` is 1 meaning that they are entirely shaded. On the
        other hand Applying a `fill` ratio less than one would allow
        the creation of openings parallel to the edges.

        The 'fill' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self["fill"]

    @fill.setter
    def fill(self, val):
        self["fill"] = val

    # show
    # ----
    @property
    def show(self):
        """
        Sets the fill ratio of the `slices`. The default fill value of
        the y `slices` is 1 meaning that they are entirely shaded. On
        the other hand Applying a `fill` ratio less than one would
        allow the creation of openings parallel to the edges.

        The 'show' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self["show"]

    @show.setter
    def show(self, val):
        self["show"] = val

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        fill
            Sets the fill ratio of the `caps`. The default fill
            value of the `caps` is 1 meaning that they are entirely
            shaded. On the other hand Applying a `fill` ratio less
            than one would allow the creation of openings parallel
            to the edges.
        show
            Sets the fill ratio of the `slices`. The default fill
            value of the y `slices` is 1 meaning that they are
            entirely shaded. On the other hand Applying a `fill`
            ratio less than one would allow the creation of
            openings parallel to the edges.
        """

    def __init__(self, arg=None, fill=None, show=None, **kwargs):
        """
        Construct a new Y object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.volume.caps.Y`
        fill
            Sets the fill ratio of the `caps`. The default fill
            value of the `caps` is 1 meaning that they are entirely
            shaded. On the other hand Applying a `fill` ratio less
            than one would allow the creation of openings parallel
            to the edges.
        show
            Sets the fill ratio of the `slices`. The default fill
            value of the y `slices` is 1 meaning that they are
            entirely shaded. On the other hand Applying a `fill`
            ratio less than one would allow the creation of
            openings parallel to the edges.

        Returns
        -------
        Y
        """
        super(Y, self).__init__("y")

        if "_parent" in kwargs:
            self._parent = kwargs["_parent"]
            return

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = _copy.copy(arg)
        else:
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.volume.caps.Y
constructor must be a dict or
an instance of :class:`plotly.graph_objs.volume.caps.Y`"""
            )

        # Handle skip_invalid
        # -------------------
        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop("fill", None)
        _v = fill if fill is not None else _v
        if _v is not None:
            self["fill"] = _v
        _v = arg.pop("show", None)
        _v = show if show is not None else _v
        if _v is not None:
            self["show"] = _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))

        # Reset skip_invalid
        # ------------------
        self._skip_invalid = False
