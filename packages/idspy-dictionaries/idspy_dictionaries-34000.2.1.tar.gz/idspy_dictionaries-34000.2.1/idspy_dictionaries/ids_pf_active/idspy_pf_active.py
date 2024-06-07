# __version__= "034000.2.0"
# __version_imas_dd__= "03.40.00"
# __imas_dd_git_commit__= "845f1b30816f86a3cd4d53714dc56cdd307fdca1"
#
from ..dataclasses_idsschema import idspy_dataclass,IdsBaseClass
from dataclasses import dataclass, field
from numpy import ndarray
from typing import Optional


@idspy_dataclass(repr=False, slots=True)
class AnnulusStatic(IdsBaseClass):
    """
    Annulus description (2D object)

    :ivar r: Centre major radius
    :ivar z: Centre height
    :ivar radius_inner: Inner radius
    :ivar radius_outer: Outer radius
    """

    class Meta:
        name = "annulus_static"

    r: float = field(default=9e40)
    z: float = field(default=9e40)
    radius_inner: float = field(default=9e40)
    radius_outer: float = field(default=9e40)


@idspy_dataclass(repr=False, slots=True)
class ArcsOfCircleStatic(IdsBaseClass):
    """
    Arcs of circle description of a 2D contour.

    :ivar r: Major radii of the start point of each arc of circle
    :ivar z: Height of the start point of each arc of circle
    :ivar curvature_radii: Curvature radius of each arc of circle
    """

    class Meta:
        name = "arcs_of_circle_static"

    r: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    z: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    curvature_radii: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )


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
class IdentifierStatic(IdsBaseClass):
    """Standard type for identifiers (static).

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
        name = "identifier_static"

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
class ObliqueStatic(IdsBaseClass):
    """
    Description of a 2D parallelogram.

    :ivar r: Major radius of the reference point (from which the alpha
        and beta angles are defined, marked by a + on the diagram)
    :ivar z: Height of the reference point (from which the alpha and
        beta angles are defined, marked by a + on the diagram)
    :ivar length_alpha: Length of the parallelogram side inclined with
        angle alpha with respect to the major radius axis
    :ivar length_beta: Length of the parallelogram side inclined with
        angle beta with respect to the height axis
    :ivar alpha: Inclination of first angle measured counter-clockwise
        from horizontal outwardly directed radial vector (grad R).
    :ivar beta: Inclination of second angle measured counter-clockwise
        from vertically upwards directed vector (grad Z). If both alpha
        and beta are zero (rectangle) then the simpler rectangular
        elements description should be used.
    """

    class Meta:
        name = "oblique_static"

    r: float = field(default=9e40)
    z: float = field(default=9e40)
    length_alpha: float = field(default=9e40)
    length_beta: float = field(default=9e40)
    alpha: float = field(default=9e40)
    beta: float = field(default=9e40)


@idspy_dataclass(repr=False, slots=True)
class RectangleStatic(IdsBaseClass):
    """
    Rectangular description of a 2D object.

    :ivar r: Geometric centre R
    :ivar z: Geometric centre Z
    :ivar width: Horizontal full width
    :ivar height: Vertical full height
    """

    class Meta:
        name = "rectangle_static"

    r: float = field(default=9e40)
    z: float = field(default=9e40)
    width: float = field(default=9e40)
    height: float = field(default=9e40)


@idspy_dataclass(repr=False, slots=True)
class Rz0DStatic(IdsBaseClass):
    """
    Structure for a single R, Z position (0D, static)

    :ivar r: Major radius
    :ivar z: Height
    """

    class Meta:
        name = "rz0d_static"

    r: float = field(default=9e40)
    z: float = field(default=9e40)


@idspy_dataclass(repr=False, slots=True)
class Rz1DStatic(IdsBaseClass):
    """
    Structure for list of R, Z positions (1D, constant)

    :ivar r: Major radius
    :ivar z: Height
    """

    class Meta:
        name = "rz1d_static"

    r: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    z: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )


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
class PfCircuits(IdsBaseClass):
    """
    Circuits, connecting multiple PF coils to multiple supplies, defining the
    current and voltage relationships in the system.

    :ivar name: Name of the circuit
    :ivar identifier: ID of the circuit
    :ivar type_value: Type of the circuit
    :ivar connections: Description of the supplies and coils connections
        (nodes) across the circuit. Nodes of the circuit are listed as
        the first dimension of the matrix. Supplies (listed first) and
        coils (listed second) SIDES are listed as the second dimension.
        Thus the second dimension has a size equal to
        2*(N_supplies+N_coils). N_supplies (resp. N_coils) is the total
        number of supplies (resp. coils) listed in the supply
        (resp.coil) array of structure, i.e. including also
        supplies/coils that are not part of the actual circuit. The
        (i,j) matrix elements are 1 if the j-th supply or coil side is
        connected to the i-th node, or 0 otherwise. For coils, sides are
        listed so that a current flowing from side 1 to side 2 (inside
        the coil) is positive (i.e. counter-clockwise when seen from
        above).
    :ivar voltage: Voltage on the circuit between the sides of the group
        of supplies (only for circuits with a single supply or in which
        supplies are grouped)
    :ivar current: Current in the circuit between the sides of the group
        of supplies (only for circuits with a single supply or in which
        supplies are grouped)
    """

    class Meta:
        name = "pf_circuits"

    name: str = field(default="")
    identifier: str = field(default="")
    type_value: str = field(default="")
    connections: ndarray[(int, int), int] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    voltage: Optional[SignalFlt1D] = field(default=None)
    current: Optional[SignalFlt1D] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class PfForceLimits(IdsBaseClass):
    """
    Description of force limits.

    :ivar combination_matrix: Force limits are expressed as a linear
        combination of the forces on each individual coil. The weights
        of the linear combination are given by this matrix, while the
        limits are given by the sibling nodes limit_min and limit_max.
        Each row of this matrix corresponds to a force limit. The
        columns represent, for each coil, the 4 types of forces on the
        coil namely [coil1_radial, coil1_vertical, coil1_radial_crush,
        coil1_vertical_crush, coil2_radial, coil2_vertical,
        coil2_radial_crush, coil2_vertical_crush, ...]. There are
        therefore 4*coils_n columns.
    :ivar limit_max: Maximum force limit, for each limit (line of the
        combination matrix). EMPTY_FLT value means unbounded
    :ivar limit_min: Minimum force limit, for each limit (line of the
        combination matrix). EMPTY_FLT value means unbounded
    :ivar force: Force (positive when upwards for a vertical force,
        positive when outwards for a radial force)
    """

    class Meta:
        name = "pf_force_limits"

    combination_matrix: ndarray[(int, int), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    limit_max: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    limit_min: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    force: Optional[SignalFlt1D] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class PfForces(IdsBaseClass):
    """
    Forces on the axisymmetric PF+CS coil system.

    :ivar name: Name of the force combination
    :ivar combination: Coils involved in the force combinations.
        Normally the force would be the full set of coils, but in some
        cases, we want to have a difference in forces, such as a CS coil
        separation force. We therefore give each coil a force weight
        which we call the combination
    :ivar limit_max: Maximum force combination limit
    :ivar limit_min: Minimum force combination limit
    :ivar force: Force (positive when upwards for a vertical force,
        positive when outwards for a radial force)
    """

    class Meta:
        name = "pf_forces"

    name: str = field(default="")
    combination: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    limit_max: float = field(default=9e40)
    limit_min: float = field(default=9e40)
    force: Optional[SignalFlt1D] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class PfSupplies(IdsBaseClass):
    """
    PF power supplies.

    :ivar name: Name of the PF supply
    :ivar identifier: Identifier of the supply
    :ivar type_value: Type of the supply; TBD add free description of
        non-linear power supplies
    :ivar resistance: Power supply internal resistance
    :ivar delay: Pure delay in the supply
    :ivar filter_numerator: Coefficients of the numerator, in increasing
        order : a0 + a1*s + ... + an*s^n; used for a linear supply
        description
    :ivar filter_denominator: Coefficients of the denominator, in
        increasing order : b0 + b1*s + ... + bm*s^m; used for a linear
        supply description
    :ivar current_limit_max: Maximum current in the supply
    :ivar current_limit_min: Minimum current in the supply
    :ivar voltage_limit_max: Maximum voltage from the supply
    :ivar voltage_limit_min: Minimum voltage from the supply
    :ivar current_limiter_gain: Gain to prevent overcurrent in a linear
        model of the supply
    :ivar energy_limit_max: Maximum energy to be dissipated in the
        supply during a pulse
    :ivar nonlinear_model: Description of the nonlinear transfer
        function of the supply
    :ivar voltage: Voltage at the supply output (Vside1-Vside2)
    :ivar current: Current at the supply output, defined positive if it
        flows from point 1 to point 2 in the circuit connected to the
        supply (outside the supply)
    """

    class Meta:
        name = "pf_supplies"

    name: str = field(default="")
    identifier: str = field(default="")
    type_value: int = field(default=999999999)
    resistance: float = field(default=9e40)
    delay: float = field(default=9e40)
    filter_numerator: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    filter_denominator: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    current_limit_max: float = field(default=9e40)
    current_limit_min: float = field(default=9e40)
    voltage_limit_max: float = field(default=9e40)
    voltage_limit_min: float = field(default=9e40)
    current_limiter_gain: float = field(default=9e40)
    energy_limit_max: float = field(default=9e40)
    nonlinear_model: str = field(default="")
    voltage: Optional[SignalFlt1D] = field(default=None)
    current: Optional[SignalFlt1D] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class ThickLineStatic(IdsBaseClass):
    """
    2D contour approximated by two points and a thickness (in the direction
    perpendicular to the segment) in the poloidal cross-section.

    :ivar first_point: Position of the first point
    :ivar second_point: Position of the second point
    :ivar thickness: Thickness
    """

    class Meta:
        name = "thick_line_static"

    first_point: Optional[Rz0DStatic] = field(default=None)
    second_point: Optional[Rz0DStatic] = field(default=None)
    thickness: float = field(default=9e40)


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
class Outline2DGeometryStatic(IdsBaseClass):
    """
    Description of 2D geometry.

    :ivar geometry_type: Type used to describe the element shape
        (1:'outline', 2:'rectangle', 3:'oblique', 4:'arcs of circle, 5:
        'annulus', 6 : 'thick line')
    :ivar outline: Irregular outline of the element. Do NOT repeat the
        first point.
    :ivar rectangle: Rectangular description of the element
    :ivar oblique: Parallelogram description of the element
    :ivar arcs_of_circle: Description of the element contour by a set of
        arcs of circle. For each of these, the position of the start
        point is given together with the curvature radius. The end point
        is given by the start point of the next arc of circle.
    :ivar annulus: The element is an annulus of centre R, Z, with inner
        radius radius_inner and outer radius radius_outer
    :ivar thick_line: The element is approximated by a rectangle defined
        by a central segment and a thickness in the direction
        perpendicular to the segment
    """

    class Meta:
        name = "outline_2d_geometry_static"

    geometry_type: int = field(default=999999999)
    outline: Optional[Rz1DStatic] = field(default=None)
    rectangle: Optional[RectangleStatic] = field(default=None)
    oblique: Optional[ObliqueStatic] = field(default=None)
    arcs_of_circle: Optional[ArcsOfCircleStatic] = field(default=None)
    annulus: Optional[AnnulusStatic] = field(default=None)
    thick_line: Optional[ThickLineStatic] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class PfCoilsElements(IdsBaseClass):
    """
    Each PF coil is comprised of a number of cross-section elements described
    individually.

    :ivar name: Name of this element
    :ivar identifier: Identifier of this element
    :ivar turns_with_sign: Number of effective turns in the element for
        calculating magnetic fields of the coil/loop; includes the sign
        of the number of turns (positive means current is counter-
        clockwise when seen from above)
    :ivar area: Cross-sectional areas of the element
    :ivar geometry: Cross-sectional shape of the element
    """

    class Meta:
        name = "pf_coils_elements"

    name: str = field(default="")
    identifier: str = field(default="")
    turns_with_sign: float = field(default=9e40)
    area: float = field(default=9e40)
    geometry: Optional[Outline2DGeometryStatic] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class PfCoils(IdsBaseClass):
    """
    Active PF coils.

    :ivar name: Name of the coil
    :ivar identifier: Alphanumeric identifier of coils used for
        convenience
    :ivar function: Set of functions for which this coil may be used
    :ivar resistance: Coil resistance
    :ivar resistance_additional: Additional resistance due to e.g.
        dynamically switchable resistors. The coil effective resistance
        is obtained by adding this dynamic quantity to the static
        resistance of the coil.
    :ivar energy_limit_max: Maximum Energy to be dissipated in the coil
    :ivar current_limit_max: Maximum tolerable current in the conductor
    :ivar b_field_max: List of values of the maximum magnetic field on
        the conductor surface (coordinate for current_limit_max)
    :ivar temperature: List of values of the conductor temperature
        (coordinate for current_limit_max)
    :ivar b_field_max_timed: Maximum absolute value of the magnetic
        field on the conductor surface
    :ivar element: Each PF coil is comprised of a number of cross-
        section elements described  individually
    :ivar current: Current fed in the coil (for 1 turn, to be multiplied
        by the number of turns to obtain the generated magnetic field),
        positive when flowing from side 1 to side 2 of the coil (inside
        the coil), this numbering being made consistently with the
        convention that the current is counter-clockwise when seen from
        above.
    :ivar voltage: Voltage on the coil terminals (Vside1-Vside2) -
        including additional resistors if any
    :ivar force_radial: Radial force applied on this coil (positive when
        outwards)
    :ivar force_vertical: Vertical force applied on this coil (positive
        when upwards)
    :ivar force_radial_crushing: Radial crushing force applied on this
        coil (positive when compressive)
    :ivar force_vertical_crushing: Vertical crushing force applied on
        this coil (positive when compressive)
    """

    class Meta:
        name = "pf_coils"

    name: str = field(default="")
    identifier: str = field(default="")
    function: list[IdentifierStatic] = field(
        default_factory=list,
        metadata={
            "max_occurs": 6,
        },
    )
    resistance: float = field(default=9e40)
    resistance_additional: Optional[SignalFlt1D] = field(default=None)
    energy_limit_max: float = field(default=9e40)
    current_limit_max: ndarray[(int, int), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    b_field_max: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    temperature: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    b_field_max_timed: Optional[SignalFlt1D] = field(default=None)
    element: list[PfCoilsElements] = field(
        default_factory=list,
        metadata={
            "max_occurs": 328,
        },
    )
    current: Optional[SignalFlt1D] = field(default=None)
    voltage: Optional[SignalFlt1D] = field(default=None)
    force_radial: Optional[SignalFlt1D] = field(default=None)
    force_vertical: Optional[SignalFlt1D] = field(default=None)
    force_radial_crushing: Optional[SignalFlt1D] = field(default=None)
    force_vertical_crushing: Optional[SignalFlt1D] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class PfActive(IdsBaseClass):
    """
    Description of the axisymmetric active poloidal field (PF) coils and supplies;
    includes the limits of these systems; includes the forces on them; does not
    include non-axisymmetric coil systems.

    :ivar ids_properties:
    :ivar coil: Active PF coils
    :ivar vertical_force: Vertical forces on the axisymmetric PF coil
        system
    :ivar radial_force: Radial forces on the axisymmetric PF coil system
    :ivar force_limits: Description of force limits on the axisymmetric
        PF coil system
    :ivar circuit: Circuits, connecting multiple PF coils to multiple
        supplies, defining the current and voltage relationships in the
        system
    :ivar supply: PF power supplies
    :ivar latency: Upper bound of the delay between input command
        received from the RT network and actuator starting to react.
        Applies globally to the system described by this IDS unless
        specific latencies (e.g. channel-specific or antenna-specific)
        are provided at a deeper level in the IDS structure.
    :ivar code:
    :ivar time:
    """

    class Meta:
        name = "pf_active"

    ids_properties: Optional[IdsProperties] = field(default=None)
    coil: list[PfCoils] = field(
        default_factory=list,
        metadata={
            "max_occurs": 32,
        },
    )
    vertical_force: list[PfForces] = field(
        default_factory=list,
        metadata={
            "max_occurs": 20,
        },
    )
    radial_force: list[PfForces] = field(
        default_factory=list,
        metadata={
            "max_occurs": 20,
        },
    )
    force_limits: Optional[PfForceLimits] = field(default=None)
    circuit: list[PfCircuits] = field(
        default_factory=list,
        metadata={
            "max_occurs": 32,
        },
    )
    supply: list[PfSupplies] = field(
        default_factory=list,
        metadata={
            "max_occurs": 32,
        },
    )
    latency: float = field(default=9e40)
    code: Optional[Code] = field(default=None)
    time: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
