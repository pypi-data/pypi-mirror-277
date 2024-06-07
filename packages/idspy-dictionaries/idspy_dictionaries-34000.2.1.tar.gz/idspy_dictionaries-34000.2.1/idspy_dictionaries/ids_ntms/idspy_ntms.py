# __version__= "034000.2.0"
# __version_imas_dd__= "03.40.00"
# __imas_dd_git_commit__= "845f1b30816f86a3cd4d53714dc56cdd307fdca1"
#
from ..dataclasses_idsschema import idspy_dataclass,IdsBaseClass
from dataclasses import dataclass, field
from numpy import ndarray
from typing import Optional


@idspy_dataclass(repr=False, slots=True)
class BTorVacuum1(IdsBaseClass):
    """Characteristics of the vacuum toroidal field.

    Time coordinate at the root of the IDS

    :ivar r0: Reference major radius where the vacuum toroidal magnetic
        field is given (usually a fixed position such as the middle of
        the vessel at the equatorial midplane)
    :ivar b0: Vacuum toroidal field at R0 [T]; Positive sign means anti-
        clockwise when viewing from above. The product R0B0 must be
        consistent with the b_tor_vacuum_r field of the tf IDS.
    """

    class Meta:
        name = "b_tor_vacuum_1"

    r0: float = field(default=9e40)
    b0: ndarray[(int,), float] = field(
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
class NtmTimeSliceModeDetailedEvolutionDeltaw(IdsBaseClass):
    """
    deltaw contribution to the Rutherford equation (detailed evolution)

    :ivar value: Value of the contribution
    :ivar name: Name of the contribution
    """

    class Meta:
        name = "ntm_time_slice_mode_detailed_evolution_deltaw"

    value: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    name: str = field(default="")


@idspy_dataclass(repr=False, slots=True)
class NtmTimeSliceModeDetailedEvolutionTorque(IdsBaseClass):
    """
    torque contribution to the Rutherford equation (detailed evolution)

    :ivar value: Value of the contribution
    :ivar name: Name of the contribution
    """

    class Meta:
        name = "ntm_time_slice_mode_detailed_evolution_torque"

    value: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    name: str = field(default="")


@idspy_dataclass(repr=False, slots=True)
class NtmTimeSliceModeEvolutionDeltaw(IdsBaseClass):
    """
    Deltaw contribution to the Rutherford equation.

    :ivar value: Value of the contribution
    :ivar name: Name of the contribution
    """

    class Meta:
        name = "ntm_time_slice_mode_evolution_deltaw"

    value: float = field(default=9e40)
    name: str = field(default="")


@idspy_dataclass(repr=False, slots=True)
class NtmTimeSliceModeEvolutionTorque(IdsBaseClass):
    """
    Torque contribution to the Rutherford equation.

    :ivar value: Value of the contribution
    :ivar name: Name of the contribution
    """

    class Meta:
        name = "ntm_time_slice_mode_evolution_torque"

    value: float = field(default=9e40)
    name: str = field(default="")


@idspy_dataclass(repr=False, slots=True)
class NtmTimeSliceModeOnset(IdsBaseClass):
    """
    Onset characteristics of an NTM.

    :ivar width: Seed island full width at onset time
    :ivar time_onset: Onset time
    :ivar time_offset: Offset time (when a mode disappears). If the mode
        reappears later in the simulation, use another index of the mode
        array of structure
    :ivar phase: Phase of the mode at onset
    :ivar n_tor: Toroidal mode number
    :ivar m_pol: Poloidal mode number
    :ivar cause: Cause of the mode onset
    """

    class Meta:
        name = "ntm_time_slice_mode_onset"

    width: float = field(default=9e40)
    time_onset: float = field(default=9e40)
    time_offset: float = field(default=9e40)
    phase: float = field(default=9e40)
    n_tor: int = field(default=999999999)
    m_pol: int = field(default=999999999)
    cause: str = field(default="")


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
class NtmTimeSliceModeDetailedEvolution(IdsBaseClass):
    """
    Detailed NTM evolution on a finer timebase than the time_slice array of
    structure.

    :ivar time_detailed: Time array used to describe the detailed
        evolution of the NTM
    :ivar width: Full width of the mode
    :ivar dwidth_dt: Time derivative of the full width of the mode
    :ivar phase: Phase of the mode
    :ivar dphase_dt: Time derivative of the phase of the mode
    :ivar frequency: Frequency of the mode
    :ivar dfrequency_dt: Time derivative of the frequency of the mode
    :ivar n_tor: Toroidal mode number
    :ivar m_pol: Poloidal mode number
    :ivar deltaw: deltaw contributions to the Rutherford equation
    :ivar torque: torque contributions to the Rutherford equation
    :ivar calculation_method: Description of how the mode evolution is
        calculated
    :ivar delta_diff: Extra diffusion coefficient for the transport
        equations of Te, ne, Ti
    :ivar rho_tor_norm: Normalised flux coordinate on which the mode is
        centred
    :ivar rho_tor: Flux coordinate on which the mode is centred
    """

    class Meta:
        name = "ntm_time_slice_mode_detailed_evolution"

    time_detailed: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    width: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    dwidth_dt: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    phase: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    dphase_dt: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    frequency: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    dfrequency_dt: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    n_tor: int = field(default=999999999)
    m_pol: int = field(default=999999999)
    deltaw: list[NtmTimeSliceModeDetailedEvolutionDeltaw] = field(
        default_factory=list
    )
    torque: list[NtmTimeSliceModeDetailedEvolutionTorque] = field(
        default_factory=list
    )
    calculation_method: str = field(default="")
    delta_diff: ndarray[(int, int), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    rho_tor_norm: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    rho_tor: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
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
class NtmTimeSliceMode(IdsBaseClass):
    """
    Description of an NTM.

    :ivar onset: NTM onset characteristics
    :ivar width: Full width of the mode
    :ivar dwidth_dt: Time derivative of the full width of the mode
    :ivar phase: Phase of the mode
    :ivar dphase_dt: Time derivative of the phase of the mode
    :ivar frequency: Frequency of the mode
    :ivar dfrequency_dt: Time derivative of the frequency of the mode
    :ivar n_tor: Toroidal mode number
    :ivar m_pol: Poloidal mode number
    :ivar deltaw: deltaw contributions to the Rutherford equation
    :ivar torque: torque contributions to the Rutherford equation
    :ivar calculation_method: Description of how the mode evolution is
        calculated
    :ivar delta_diff: Extra diffusion coefficient for the transport
        equations of Te, ne, Ti
    :ivar rho_tor_norm: Normalised flux coordinate on which the mode is
        centred
    :ivar rho_tor: Flux coordinate on which the mode is centred
    :ivar detailed_evolution: Detailed NTM evolution on a finer timebase
        than the time_slice array of structure
    """

    class Meta:
        name = "ntm_time_slice_mode"

    onset: Optional[NtmTimeSliceModeOnset] = field(default=None)
    width: float = field(default=9e40)
    dwidth_dt: float = field(default=9e40)
    phase: float = field(default=9e40)
    dphase_dt: float = field(default=9e40)
    frequency: float = field(default=9e40)
    dfrequency_dt: float = field(default=9e40)
    n_tor: int = field(default=999999999)
    m_pol: int = field(default=999999999)
    deltaw: list[NtmTimeSliceModeEvolutionDeltaw] = field(default_factory=list)
    torque: list[NtmTimeSliceModeEvolutionTorque] = field(default_factory=list)
    calculation_method: str = field(default="")
    delta_diff: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    rho_tor_norm: float = field(default=9e40)
    rho_tor: float = field(default=9e40)
    detailed_evolution: Optional[NtmTimeSliceModeDetailedEvolution] = field(
        default=None
    )


@idspy_dataclass(repr=False, slots=True)
class NtmTimeSlice(IdsBaseClass):
    """
    Time slice description of NTMs.

    :ivar mode: List of the various NTM modes appearing during the
        simulation. If a mode appears several times, use several indices
        in this array of structure with the same m,n values.
    :ivar time: Time
    """

    class Meta:
        name = "ntm_time_slice"

    mode: list[NtmTimeSliceMode] = field(default_factory=list)
    time: Optional[float] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class Ntms(IdsBaseClass):
    """
    Description of neoclassical tearing modes.

    :ivar ids_properties:
    :ivar vacuum_toroidal_field: Characteristics of the vacuum toroidal
        field (used in rho_tor definition)
    :ivar time_slice: Description of neoclassical tearing modes for
        various time slices
    :ivar code:
    :ivar time:
    """

    class Meta:
        name = "ntms"

    ids_properties: Optional[IdsProperties] = field(default=None)
    vacuum_toroidal_field: Optional[BTorVacuum1] = field(default=None)
    time_slice: list[NtmTimeSlice] = field(default_factory=list)
    code: Optional[Code] = field(default=None)
    time: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
