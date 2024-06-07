# __version__= "034000.2.0"
# __version_imas_dd__= "03.40.00"
# __imas_dd_git_commit__= "845f1b30816f86a3cd4d53714dc56cdd307fdca1"
#
from ..dataclasses_idsschema import idspy_dataclass,IdsBaseClass
from dataclasses import dataclass, field
from numpy import ndarray
from typing import Optional


@idspy_dataclass(repr=False, slots=True)
class EcLaunchersBeamPhase(IdsBaseClass):
    """
    Phase ellipse characteristics.

    :ivar curvature: Inverse curvature radii for the phase ellipse,
        positive/negative for divergent/convergent beams, in the
        horizontal direction (first index of the first coordinate) and
        in the vertical direction (second index of the first coordinate)
    :ivar angle: Rotation angle for the phase ellipse
    """

    class Meta:
        name = "ec_launchers_beam_phase"

    curvature: ndarray[(int, int), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    angle: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )


@idspy_dataclass(repr=False, slots=True)
class EcLaunchersBeamSpot(IdsBaseClass):
    """
    Spot ellipse characteristics.

    :ivar size: Size of the spot ellipse: distance between the central
        ray and the peripheral rays in the horizontal (first index of
        the first coordinate) and vertical direction (second index of
        the first coordinate)
    :ivar angle: Rotation angle for the spot ellipse
    """

    class Meta:
        name = "ec_launchers_beam_spot"

    size: ndarray[(int, int), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    angle: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )


@idspy_dataclass(repr=False, slots=True)
class EcLaunchersLaunchingPosition(IdsBaseClass):
    """
    Structure for R, Z, Phi positions and min max values of R (1D, dynamic within a
    type 1 array of structure and with a common time base at the same level)

    :ivar r: Major radius
    :ivar r_limit_min: Major radius lower limit for the system
    :ivar r_limit_max: Major radius upper limit for the system
    :ivar z: Height
    :ivar phi: Toroidal angle
    """

    class Meta:
        name = "ec_launchers_launching_position"

    r: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    r_limit_min: float = field(default=9e40)
    r_limit_max: float = field(default=9e40)
    z: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    phi: ndarray[(int,), float] = field(
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
class EcLaunchersBeam(IdsBaseClass):
    """
    Electron Cyclotron beam.

    :ivar name: Beam name
    :ivar identifier: Beam identifier
    :ivar frequency: Frequency
    :ivar power_launched: Beam power launched into the vacuum vessel
    :ivar mode: Identifier for the main plasma wave mode excited by the
        EC beam. For the ordinary mode (O-mode), mode=1. For the
        extraordinary mode (X-mode), mode=-1
    :ivar o_mode_fraction: Fraction of EC beam power launched in
        ordinary (O) mode. If all power is launched in ordinary mode
        (O-mode), o_mode_fraction = 1.0. If all  power is launched in
        extraordinary mode (X-mode), o_mode_fraction = 0.0
    :ivar launching_position: Launching position of the beam
    :ivar steering_angle_pol: Steering angle of the EC beam in the R,Z
        plane (from the -R axis towards the -Z axis),
        angle_pol=atan2(-k_Z,-k_R), where k_Z and k_R are the Z and R
        components of the mean wave vector in the EC beam
    :ivar steering_angle_tor: Steering angle of the EC beam away from
        the poloidal plane that is increasing towards the positive phi
        axis, angle_tor=arcsin(k_phi/k), where k_phi is the component of
        the wave vector in the phi direction and k is the length of the
        wave vector. Here the term wave vector refers to the mean wave
        vector in the EC beam
    :ivar spot: Spot ellipse characteristics at launch
    :ivar phase: Phase ellipse characteristics at launch
    :ivar time: Time base used for launching_position, o_mode_fraction,
        angle, spot and phase quantities
    """

    class Meta:
        name = "ec_launchers_beam"

    name: str = field(default="")
    identifier: str = field(default="")
    frequency: Optional[SignalFlt1D] = field(default=None)
    power_launched: Optional[SignalFlt1D] = field(default=None)
    mode: int = field(default=999999999)
    o_mode_fraction: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    launching_position: Optional[EcLaunchersLaunchingPosition] = field(
        default=None
    )
    steering_angle_pol: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    steering_angle_tor: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    spot: Optional[EcLaunchersBeamSpot] = field(default=None)
    phase: Optional[EcLaunchersBeamPhase] = field(default=None)
    time: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
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
class EcLaunchers(IdsBaseClass):
    """
    Launchers for heating and current drive in the electron cyclotron (EC)
    frequencies.

    :ivar ids_properties:
    :ivar beam: Set of Electron Cyclotron beams
    :ivar latency: Upper bound of the delay between input command
        received from the RT network and actuator starting to react.
        Applies globally to the system described by this IDS unless
        specific latencies (e.g. channel-specific or antenna-specific)
        are provided at a deeper level in the IDS structure.
    :ivar code:
    :ivar time:
    """

    class Meta:
        name = "ec_launchers"

    ids_properties: Optional[IdsProperties] = field(default=None)
    beam: list[EcLaunchersBeam] = field(
        default_factory=list,
        metadata={
            "max_occurs": 100,
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
