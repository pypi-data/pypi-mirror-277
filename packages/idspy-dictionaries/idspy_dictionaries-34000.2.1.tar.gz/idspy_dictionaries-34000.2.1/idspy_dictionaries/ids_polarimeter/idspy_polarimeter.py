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
class Rzphi0DStatic(IdsBaseClass):
    """
    Structure for R, Z, Phi positions (0D, static)

    :ivar r: Major radius
    :ivar z: Height
    :ivar phi: Toroidal angle (oriented counter-clockwise when viewing
        from above)
    """

    class Meta:
        name = "rzphi0d_static"

    r: float = field(default=9e40)
    z: float = field(default=9e40)
    phi: float = field(default=9e40)


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
class SignalFlt1DValidity(IdsBaseClass):
    """
    Signal (FLT_1D) with its time base and validity flags.

    :ivar validity_timed: Indicator of the validity of the data for each
        time slice. 0: valid from automated processing, 1: valid and
        certified by the diagnostic RO; - 1 means problem identified in
        the data processing (request verification by the diagnostic RO),
        -2: invalid data, should not be used (values lower than -2 have
        a code-specific meaning detailing the origin of their
        invalidity)
    :ivar validity: Indicator of the validity of the data for the whole
        acquisition period. 0: valid from automated processing, 1: valid
        and certified by the diagnostic RO; - 1 means problem identified
        in the data processing (request verification by the diagnostic
        RO), -2: invalid data, should not be used (values lower than -2
        have a code-specific meaning detailing the origin of their
        invalidity)
    :ivar time: Time
    """

    class Meta:
        name = "signal_flt_1d_validity"

    validity_timed: ndarray[(int,), int] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    validity: int = field(default=999999999)
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
class LineOfSight3Points(IdsBaseClass):
    """
    Generic description of a line of sight, defined by two points (one way) and an
    optional third point to indicate the direction of reflection if the second
    point is e.g. the position of a mirror reflecting the line-of-sight.

    :ivar first_point: Position of the first point
    :ivar second_point: Position of the second point
    :ivar third_point: Position of the third point
    """

    class Meta:
        name = "line_of_sight_3points"

    first_point: Optional[Rzphi0DStatic] = field(default=None)
    second_point: Optional[Rzphi0DStatic] = field(default=None)
    third_point: Optional[Rzphi0DStatic] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class PolarimeterChannelWavelengthInterf(IdsBaseClass):
    """
    Value of the wavelength and density estimators associated to an interferometry
    wavelength.

    :ivar value: Wavelength value
    :ivar phase_corrected: Phase measured for this wavelength, corrected
        from fringe jumps
    :ivar fring_jump_correction: Signed number of 2pi phase corrections
        applied to remove a fringe jump, for each time slice on which a
        correction has been made
    :ivar fring_jump_correction_times: List of time slices of the pulse
        on which a fringe jump correction has been made
    :ivar phase_to_n_e_line: Conversion factor to be used to convert
        phase into line density for this wavelength
    """

    class Meta:
        name = "polarimeter_channel_wavelength_interf"

    value: float = field(default=9e40)
    phase_corrected: Optional[SignalFlt1D] = field(default=None)
    fring_jump_correction: ndarray[(int,), int] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    fring_jump_correction_times: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    phase_to_n_e_line: float = field(default=9e40)


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
class PolarimeterChannel(IdsBaseClass):
    """
    Charge exchange channel.

    :ivar name: Name of the channel
    :ivar identifier: ID of the channel
    :ivar line_of_sight: Description of the line of sight of the
        channel, defined by two points when the beam is not reflected, a
        third point is added to define the reflected beam path
    :ivar wavelength: Wavelength used for polarimetry
    :ivar polarisation_initial: Initial polarisation vector before
        entering the plasma
    :ivar ellipticity_initial: Initial ellipticity before entering the
        plasma
    :ivar faraday_angle: Faraday angle (variation of the Faraday angle
        induced by crossing the plasma)
    :ivar ellipticity: Ellipticity
    """

    class Meta:
        name = "polarimeter_channel"

    name: str = field(default="")
    identifier: str = field(default="")
    line_of_sight: Optional[LineOfSight3Points] = field(default=None)
    wavelength: float = field(default=9e40)
    polarisation_initial: float = field(default=9e40)
    ellipticity_initial: float = field(default=9e40)
    faraday_angle: Optional[SignalFlt1DValidity] = field(default=None)
    ellipticity: Optional[SignalFlt1DValidity] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class Polarimeter(IdsBaseClass):
    """
    Polarimeter diagnostic.

    :ivar ids_properties:
    :ivar channel: Set of channels (lines-of-sight)
    :ivar latency: Upper bound of the delay between physical information
        received by the detector and data available on the real-time
        (RT) network.
    :ivar code:
    :ivar time:
    """

    class Meta:
        name = "polarimeter"

    ids_properties: Optional[IdsProperties] = field(default=None)
    channel: list[PolarimeterChannel] = field(
        default_factory=list,
        metadata={
            "max_occurs": 15,
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
