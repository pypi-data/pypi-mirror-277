# __version__= "034000.2.0"
# __version_imas_dd__= "03.40.00"
# __imas_dd_git_commit__= "845f1b30816f86a3cd4d53714dc56cdd307fdca1"
#
from ..dataclasses_idsschema import idspy_dataclass,IdsBaseClass
from dataclasses import dataclass, field
from numpy import ndarray
from typing import Optional


@idspy_dataclass(repr=False, slots=True)
class Identifier(IdsBaseClass):
    """Standard type for identifiers (constant).

    The three fields: name, index and description are all
    representations of the same information. Associated with each
    application of this identifier-type, there should be a translation
    table defining the three fields for all objects to be identified.

    :ivar name: Short string identifier
    :ivar index: Integer identifier (enumeration index within a list).
        Private identifier values must be indicated by a negative index.
    :ivar description: Verbose description
    """

    class Meta:
        name = "identifier"

    name: str = field(default="")
    index: int = field(default=999999999)
    description: str = field(default="")


@idspy_dataclass(repr=False, slots=True)
class IdsProvenanceNode(IdsBaseClass):
    """
    Provenance information for a given node of the IDS.

    :ivar path: Path of the node within the IDS, following the syntax
        given in the link below. If empty, means the provenance
        information applies to the whole IDS.
    :ivar sources: List of sources used to import or calculate this
        node, identified as explained below. In case the node is the
        result of of a calculation / data processing, the source is an
        input to the process described in the "code" structure at the
        root of the IDS. The source can be an IDS (identified by a URI
        or a persitent identifier, see syntax in the link below) or non-
        IDS data imported directly from an non-IMAS database (identified
        by the command used to import the source, or the persistent
        identifier of the data source). Often data are obtained by a
        chain of processes, however only the last process input are
        recorded here. The full chain of provenance has then to be
        reconstructed recursively from the provenance information
        contained in the data sources.
    """

    class Meta:
        name = "ids_provenance_node"

    path: str = field(default="")
    sources: Optional[list[str]] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class Library(IdsBaseClass):
    """
    Library used by the code that has produced this IDS.

    :ivar name: Name of software
    :ivar description: Short description of the software (type, purpose)
    :ivar commit: Unique commit reference of software
    :ivar version: Unique version (tag) of software
    :ivar repository: URL of software repository
    :ivar parameters: List of the code specific parameters in XML format
    """

    class Meta:
        name = "library"

    name: str = field(default="")
    description: str = field(default="")
    commit: str = field(default="")
    version: str = field(default="")
    repository: str = field(default="")
    parameters: str = field(default="")


@idspy_dataclass(repr=False, slots=True)
class SignalFlt1D(IdsBaseClass):
    """
    Signal (FLT_1D) with its time base.

    :ivar time: Time
    """

    class Meta:
        name = "signal_flt_1d"

    time: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )

    @idspy_dataclass(repr=False, slots=True)
    class Data(IdsBaseClass):
        """
        :ivar class_of: Class of Data Item
        """

        class_of: str = field(init=False, default="FLT_1D")


@idspy_dataclass(repr=False, slots=True)
class SignalFlt2D(IdsBaseClass):
    """
    Signal (FLT_2D) with its time base.

    :ivar time: Time
    """

    class Meta:
        name = "signal_flt_2d"

    time: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )

    @idspy_dataclass(repr=False, slots=True)
    class Data(IdsBaseClass):
        """
        :ivar class_of: Class of Data Item
        """

        class_of: str = field(init=False, default="FLT_2D")


@idspy_dataclass(repr=False, slots=True)
class SignalFlt3D(IdsBaseClass):
    """
    Signal (FLT_3D) with its time base.

    :ivar time: Time
    """

    class Meta:
        name = "signal_flt_3d"

    time: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )

    @idspy_dataclass(repr=False, slots=True)
    class Data(IdsBaseClass):
        """
        :ivar class_of: Class of Data Item
        """

        class_of: str = field(init=False, default="FLT_3D")


@idspy_dataclass(repr=False, slots=True)
class SignalFlt4D(IdsBaseClass):
    """
    Signal (FLT_4D) with its time base.

    :ivar time: Time
    """

    class Meta:
        name = "signal_flt_4d"

    time: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )

    @idspy_dataclass(repr=False, slots=True)
    class Data(IdsBaseClass):
        """
        :ivar class_of: Class of Data Item
        """

        class_of: str = field(init=False, default="FLT_4D")


@idspy_dataclass(repr=False, slots=True)
class SignalFlt5D(IdsBaseClass):
    """
    Signal (FLT_5D) with its time base.

    :ivar time: Time
    """

    class Meta:
        name = "signal_flt_5d"

    time: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )

    @idspy_dataclass(repr=False, slots=True)
    class Data(IdsBaseClass):
        """
        :ivar class_of: Class of Data Item
        """

        class_of: str = field(init=False, default="FLT_5D")


@idspy_dataclass(repr=False, slots=True)
class SignalFlt6D(IdsBaseClass):
    """
    Signal (FLT_6D) with its time base.

    :ivar time: Time
    """

    class Meta:
        name = "signal_flt_6d"

    time: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )

    @idspy_dataclass(repr=False, slots=True)
    class Data(IdsBaseClass):
        """
        :ivar class_of: Class of Data Item
        """

        class_of: str = field(init=False, default="FLT_6D")


@idspy_dataclass(repr=False, slots=True)
class SignalInt1D(IdsBaseClass):
    """
    Signal (INT_1D) with its time base.

    :ivar time: Time
    """

    class Meta:
        name = "signal_int_1d"

    time: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )

    @idspy_dataclass(repr=False, slots=True)
    class Data(IdsBaseClass):
        """
        :ivar class_of: Class of Data Item
        """

        class_of: str = field(init=False, default="INT_1D")


@idspy_dataclass(repr=False, slots=True)
class SignalInt2D(IdsBaseClass):
    """
    Signal (INT_2D) with its time base.

    :ivar time: Time
    """

    class Meta:
        name = "signal_int_2d"

    time: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )

    @idspy_dataclass(repr=False, slots=True)
    class Data(IdsBaseClass):
        """
        :ivar class_of: Class of Data Item
        """

        class_of: str = field(init=False, default="INT_2D")


@idspy_dataclass(repr=False, slots=True)
class SignalInt3D(IdsBaseClass):
    """
    Signal (INT_3D) with its time base.

    :ivar time: Time
    """

    class Meta:
        name = "signal_int_3d"

    time: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )

    @idspy_dataclass(repr=False, slots=True)
    class Data(IdsBaseClass):
        """
        :ivar class_of: Class of Data Item
        """

        class_of: str = field(init=False, default="INT_3D")


@idspy_dataclass(repr=False, slots=True)
class Code(IdsBaseClass):
    """
    Generic decription of the code-specific parameters for the code that has
    produced this IDS.

    :ivar name: Name of software generating IDS
    :ivar description: Short description of the software (type, purpose)
    :ivar commit: Unique commit reference of software
    :ivar version: Unique version (tag) of software
    :ivar repository: URL of software repository
    :ivar parameters: List of the code specific parameters in XML format
    :ivar output_flag: Output flag : 0 means the run is successful,
        other values mean some difficulty has been encountered, the
        exact meaning is then code specific. Negative values mean the
        result shall not be used.
    :ivar library: List of external libraries used by the code that has
        produced this IDS
    """

    class Meta:
        name = "code"

    name: str = field(default="")
    description: str = field(default="")
    commit: str = field(default="")
    version: str = field(default="")
    repository: str = field(default="")
    parameters: str = field(default="")
    output_flag: ndarray[(int,), int] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    library: list[Library] = field(
        default_factory=list,
        metadata={
            "max_occurs": 10,
        },
    )


@idspy_dataclass(repr=False, slots=True)
class IdsProvenance(IdsBaseClass):
    """
    Provenance information about the IDS.

    :ivar node: Set of IDS nodes for which the provenance is given. The
        provenance information applies to the whole structure below the
        IDS node. For documenting provenance information for the whole
        IDS, set the size of this array of structure to 1 and leave the
        child "path" node empty
    """

    class Meta:
        name = "ids_provenance"

    node: list[IdsProvenanceNode] = field(
        default_factory=list,
        metadata={
            "max_occurs": 20,
        },
    )


@idspy_dataclass(repr=False, slots=True)
class TemporaryConstantQuantitiesFloat0D(IdsBaseClass):
    """
    Temporary constant Float_0D.

    :ivar value: Value
    :ivar identifier: Description of the quantity using the standard
        identifier structure
    """

    class Meta:
        name = "temporary_constant_quantities_float_0d"

    value: float = field(default=9e40)
    identifier: Optional[Identifier] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class TemporaryConstantQuantitiesFloat1D(IdsBaseClass):
    """
    Temporary constant Float_1D.

    :ivar value: Value
    :ivar identifier: Description of the quantity using the standard
        identifier structure
    """

    class Meta:
        name = "temporary_constant_quantities_float_1d"

    value: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    identifier: Optional[Identifier] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class TemporaryConstantQuantitiesFloat2D(IdsBaseClass):
    """
    Temporary constant Float_2D.

    :ivar value: Value
    :ivar identifier: Description of the quantity using the standard
        identifier structure
    """

    class Meta:
        name = "temporary_constant_quantities_float_2d"

    value: ndarray[(int, int), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    identifier: Optional[Identifier] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class TemporaryConstantQuantitiesFloat3D(IdsBaseClass):
    """
    Temporary constant Float_3D.

    :ivar value: Value
    :ivar identifier: Description of the quantity using the standard
        identifier structure
    """

    class Meta:
        name = "temporary_constant_quantities_float_3d"

    value: ndarray[(int, int, int), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    identifier: Optional[Identifier] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class TemporaryConstantQuantitiesFloat4D(IdsBaseClass):
    """
    Temporary constant Float_4D.

    :ivar value: Value
    :ivar identifier: Description of the quantity using the standard
        identifier structure
    """

    class Meta:
        name = "temporary_constant_quantities_float_4d"

    value: ndarray[(int, int, int, int), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    identifier: Optional[Identifier] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class TemporaryConstantQuantitiesFloat5D(IdsBaseClass):
    """
    Temporary constant Float_5D.

    :ivar value: Value
    :ivar identifier: Description of the quantity using the standard
        identifier structure
    """

    class Meta:
        name = "temporary_constant_quantities_float_5d"

    value: ndarray[(int, int, int, int, int), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    identifier: Optional[Identifier] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class TemporaryConstantQuantitiesFloat6D(IdsBaseClass):
    """
    Temporary constant Float_6D.

    :ivar value: Value
    :ivar identifier: Description of the quantity using the standard
        identifier structure
    """

    class Meta:
        name = "temporary_constant_quantities_float_6d"

    value: ndarray[(int, int, int, int, int, int), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    identifier: Optional[Identifier] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class TemporaryConstantQuantitiesInt0D(IdsBaseClass):
    """
    Temporary constant INT_0D.

    :ivar value: Value
    :ivar identifier: Description of the quantity using the standard
        identifier structure
    """

    class Meta:
        name = "temporary_constant_quantities_int_0d"

    value: int = field(default=999999999)
    identifier: Optional[Identifier] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class TemporaryConstantQuantitiesInt1D(IdsBaseClass):
    """
    Temporary constant INT_1D.

    :ivar value: Value
    :ivar identifier: Description of the quantity using the standard
        identifier structure
    """

    class Meta:
        name = "temporary_constant_quantities_int_1d"

    value: ndarray[(int,), int] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    identifier: Optional[Identifier] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class TemporaryConstantQuantitiesInt2D(IdsBaseClass):
    """
    Temporary constant INT_2D.

    :ivar value: Value
    :ivar identifier: Description of the quantity using the standard
        identifier structure
    """

    class Meta:
        name = "temporary_constant_quantities_int_2d"

    value: ndarray[(int, int), int] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    identifier: Optional[Identifier] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class TemporaryConstantQuantitiesInt3D(IdsBaseClass):
    """
    Temporary constant INT_3D.

    :ivar value: Value
    :ivar identifier: Description of the quantity using the standard
        identifier structure
    """

    class Meta:
        name = "temporary_constant_quantities_int_3d"

    value: ndarray[(int, int, int), int] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    identifier: Optional[Identifier] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class TemporaryConstantQuantitiesString0D(IdsBaseClass):
    """
    Temporary constant STR_0D.

    :ivar value: Value
    :ivar identifier: Description of the quantity using the standard
        identifier structure
    """

    class Meta:
        name = "temporary_constant_quantities_string_0d"

    value: str = field(default="")
    identifier: Optional[Identifier] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class TemporaryConstantQuantitiesString1D(IdsBaseClass):
    """
    Temporary constant STR_1D.

    :ivar value: Value
    :ivar identifier: Description of the quantity using the standard
        identifier structure
    """

    class Meta:
        name = "temporary_constant_quantities_string_1d"

    value: Optional[list[str]] = field(default=None)
    identifier: Optional[Identifier] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class TemporaryDynamicQuantitiesFloat1D(IdsBaseClass):
    """
    Temporary dynamic Float_1D.

    :ivar value: Value
    :ivar identifier: Description of the quantity using the standard
        identifier structure
    """

    class Meta:
        name = "temporary_dynamic_quantities_float_1d"

    value: Optional[SignalFlt1D] = field(default=None)
    identifier: Optional[Identifier] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class TemporaryDynamicQuantitiesFloat2D(IdsBaseClass):
    """
    Temporary dynamic Float_2D.

    :ivar value: Value
    :ivar identifier: Description of the quantity using the standard
        identifier structure
    """

    class Meta:
        name = "temporary_dynamic_quantities_float_2d"

    value: Optional[SignalFlt2D] = field(default=None)
    identifier: Optional[Identifier] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class TemporaryDynamicQuantitiesFloat3D(IdsBaseClass):
    """
    Temporary dynamic Float_3D.

    :ivar value: Value
    :ivar identifier: Description of the quantity using the standard
        identifier structure
    """

    class Meta:
        name = "temporary_dynamic_quantities_float_3d"

    value: Optional[SignalFlt3D] = field(default=None)
    identifier: Optional[Identifier] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class TemporaryDynamicQuantitiesFloat4D(IdsBaseClass):
    """
    Temporary dynamic Float_4D.

    :ivar value: Value
    :ivar identifier: Description of the quantity using the standard
        identifier structure
    """

    class Meta:
        name = "temporary_dynamic_quantities_float_4d"

    value: Optional[SignalFlt4D] = field(default=None)
    identifier: Optional[Identifier] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class TemporaryDynamicQuantitiesFloat5D(IdsBaseClass):
    """
    Temporary dynamic Float_5D.

    :ivar value: Value
    :ivar identifier: Description of the quantity using the standard
        identifier structure
    """

    class Meta:
        name = "temporary_dynamic_quantities_float_5d"

    value: Optional[SignalFlt5D] = field(default=None)
    identifier: Optional[Identifier] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class TemporaryDynamicQuantitiesFloat6D(IdsBaseClass):
    """
    Temporary dynamic Float_6D.

    :ivar value: Value
    :ivar identifier: Description of the quantity using the standard
        identifier structure
    """

    class Meta:
        name = "temporary_dynamic_quantities_float_6d"

    value: Optional[SignalFlt6D] = field(default=None)
    identifier: Optional[Identifier] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class TemporaryDynamicQuantitiesInt1D(IdsBaseClass):
    """
    Temporary dynamic Int_1D.

    :ivar value: Value
    :ivar identifier: Description of the quantity using the standard
        identifier structure
    """

    class Meta:
        name = "temporary_dynamic_quantities_int_1d"

    value: Optional[SignalInt1D] = field(default=None)
    identifier: Optional[Identifier] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class TemporaryDynamicQuantitiesInt2D(IdsBaseClass):
    """
    Temporary dynamic INT_2D.

    :ivar value: Value
    :ivar identifier: Description of the quantity using the standard
        identifier structure
    """

    class Meta:
        name = "temporary_dynamic_quantities_int_2d"

    value: Optional[SignalInt2D] = field(default=None)
    identifier: Optional[Identifier] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class TemporaryDynamicQuantitiesInt3D(IdsBaseClass):
    """
    Temporary dynamic INT_3D.

    :ivar value: Value
    :ivar identifier: Description of the quantity using the standard
        identifier structure
    """

    class Meta:
        name = "temporary_dynamic_quantities_int_3d"

    value: Optional[SignalInt3D] = field(default=None)
    identifier: Optional[Identifier] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class IdsProperties(IdsBaseClass):
    """Interface Data Structure properties.

    This element identifies the node above as an IDS

    :ivar comment: Any comment describing the content of this IDS
    :ivar name: User-defined name for this IDS occurrence
    :ivar homogeneous_time: This node must be filled (with 0, 1, or 2)
        for the IDS to be valid. If 1, the time of this IDS is
        homogeneous, i.e. the time values for this IDS are stored in the
        time node just below the root of this IDS. If 0, the time values
        are stored in the various time fields at lower levels in the
        tree. In the case only constant or static nodes are filled
        within the IDS, homogeneous_time must be set to 2
    :ivar occurrence_type: Type of data contained in this occurrence
    :ivar provider: Name of the person in charge of producing this data
    :ivar creation_date: Date at which this data has been produced
    :ivar provenance: Provenance information about this IDS
    """

    class Meta:
        name = "ids_properties"

    comment: str = field(default="")
    name: str = field(default="")
    homogeneous_time: int = field(default=999999999)
    occurrence_type: Optional[Identifier] = field(default=None)
    provider: str = field(default="")
    creation_date: str = field(default="")
    provenance: Optional[IdsProvenance] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class Temporary(IdsBaseClass):
    """
    Storage of undeclared data model components.

    :ivar ids_properties:
    :ivar constant_float0d: Constant 0D float
    :ivar constant_integer0d: Constant 0D integer
    :ivar constant_string0d: Constant 0D string
    :ivar constant_integer1d: Constant 1D integer
    :ivar constant_string1d: Constant 1D string
    :ivar constant_float1d: Constant 1D float
    :ivar dynamic_float1d: Dynamic 1D float
    :ivar dynamic_integer1d: Dynamic 1D integer
    :ivar constant_float2d: Constant 2D float
    :ivar constant_integer2d: Constant 2D integer
    :ivar dynamic_float2d: Dynamic 2D float
    :ivar dynamic_integer2d: Dynamic 2D integer
    :ivar constant_float3d: Constant 3D float
    :ivar constant_integer3d: Constant 3D integer
    :ivar dynamic_float3d: Dynamic 3D float
    :ivar dynamic_integer3d: Dynamic 3D integer
    :ivar constant_float4d: Constant 4D float
    :ivar dynamic_float4d: Dynamic 4D float
    :ivar constant_float5d: Constant 5D float
    :ivar dynamic_float5d: Dynamic 5D float
    :ivar constant_float6d: Constant 6D float
    :ivar dynamic_float6d: Dynamic 6D float
    :ivar code:
    :ivar time:
    """

    class Meta:
        name = "temporary"

    ids_properties: Optional[IdsProperties] = field(default=None)
    constant_float0d: list[TemporaryConstantQuantitiesFloat0D] = field(
        default_factory=list,
        metadata={
            "max_occurs": 10,
        },
    )
    constant_integer0d: list[TemporaryConstantQuantitiesInt0D] = field(
        default_factory=list,
        metadata={
            "max_occurs": 10,
        },
    )
    constant_string0d: list[TemporaryConstantQuantitiesString0D] = field(
        default_factory=list,
        metadata={
            "max_occurs": 10,
        },
    )
    constant_integer1d: list[TemporaryConstantQuantitiesInt1D] = field(
        default_factory=list,
        metadata={
            "max_occurs": 10,
        },
    )
    constant_string1d: list[TemporaryConstantQuantitiesString1D] = field(
        default_factory=list,
        metadata={
            "max_occurs": 10,
        },
    )
    constant_float1d: list[TemporaryConstantQuantitiesFloat1D] = field(
        default_factory=list,
        metadata={
            "max_occurs": 10,
        },
    )
    dynamic_float1d: list[TemporaryDynamicQuantitiesFloat1D] = field(
        default_factory=list,
        metadata={
            "max_occurs": 10,
        },
    )
    dynamic_integer1d: list[TemporaryDynamicQuantitiesInt1D] = field(
        default_factory=list,
        metadata={
            "max_occurs": 10,
        },
    )
    constant_float2d: list[TemporaryConstantQuantitiesFloat2D] = field(
        default_factory=list,
        metadata={
            "max_occurs": 10,
        },
    )
    constant_integer2d: list[TemporaryConstantQuantitiesInt2D] = field(
        default_factory=list,
        metadata={
            "max_occurs": 10,
        },
    )
    dynamic_float2d: list[TemporaryDynamicQuantitiesFloat2D] = field(
        default_factory=list,
        metadata={
            "max_occurs": 10,
        },
    )
    dynamic_integer2d: list[TemporaryDynamicQuantitiesInt2D] = field(
        default_factory=list,
        metadata={
            "max_occurs": 10,
        },
    )
    constant_float3d: list[TemporaryConstantQuantitiesFloat3D] = field(
        default_factory=list,
        metadata={
            "max_occurs": 10,
        },
    )
    constant_integer3d: list[TemporaryConstantQuantitiesInt3D] = field(
        default_factory=list,
        metadata={
            "max_occurs": 10,
        },
    )
    dynamic_float3d: list[TemporaryDynamicQuantitiesFloat3D] = field(
        default_factory=list,
        metadata={
            "max_occurs": 10,
        },
    )
    dynamic_integer3d: list[TemporaryDynamicQuantitiesInt3D] = field(
        default_factory=list,
        metadata={
            "max_occurs": 10,
        },
    )
    constant_float4d: list[TemporaryConstantQuantitiesFloat4D] = field(
        default_factory=list,
        metadata={
            "max_occurs": 10,
        },
    )
    dynamic_float4d: list[TemporaryDynamicQuantitiesFloat4D] = field(
        default_factory=list,
        metadata={
            "max_occurs": 10,
        },
    )
    constant_float5d: list[TemporaryConstantQuantitiesFloat5D] = field(
        default_factory=list,
        metadata={
            "max_occurs": 10,
        },
    )
    dynamic_float5d: list[TemporaryDynamicQuantitiesFloat5D] = field(
        default_factory=list,
        metadata={
            "max_occurs": 10,
        },
    )
    constant_float6d: list[TemporaryConstantQuantitiesFloat6D] = field(
        default_factory=list,
        metadata={
            "max_occurs": 10,
        },
    )
    dynamic_float6d: list[TemporaryDynamicQuantitiesFloat6D] = field(
        default_factory=list,
        metadata={
            "max_occurs": 10,
        },
    )
    code: Optional[Code] = field(default=None)
    time: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
