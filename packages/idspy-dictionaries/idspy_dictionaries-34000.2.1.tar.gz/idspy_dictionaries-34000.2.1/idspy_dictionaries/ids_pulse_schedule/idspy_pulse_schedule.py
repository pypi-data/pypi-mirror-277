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
class PlasmaCompositionNeutralElementConstant(IdsBaseClass):
    """
    Element entering in the composition of the neutral atom or molecule (constant)

    :ivar a: Mass of atom
    :ivar z_n: Nuclear charge
    :ivar atoms_n: Number of atoms of this element in the molecule
    :ivar multiplicity: Multiplicity of the atom
    """

    class Meta:
        name = "plasma_composition_neutral_element_constant"

    a: float = field(default=9e40)
    z_n: float = field(default=9e40)
    atoms_n: int = field(default=999999999)
    multiplicity: float = field(default=9e40)


@idspy_dataclass(repr=False, slots=True)
class PulseScheduleReferenceDensity(IdsBaseClass):
    """
    Pulse schedule reference for the density_control structure.

    :ivar reference_name: Reference name (e.g. in the native pulse
        schedule system of the device)
    :ivar reference: Reference waveform. Caution : error bars of the
        reference/data node are not used in the usual sense, instead
        they are used to describe the control envelope, with a meaning
        depending on the chosen envelope_type option.
    :ivar reference_type: Reference type:  0:relative (don't use for the
        moment, to be defined later when segments are introduced in the
        IDS structure); 1: absolute: the reference time trace is
        provided in the reference/data node
    :ivar envelope_type: Envelope type:  0:relative: means that the
        envelope upper and lower bound values are defined respectively
        as reference.data * reference.data_error_upper and
        reference.data * reference.data_error_lower. 1: absolute: the
        envelope upper and lower bound values are given respectively by
        reference/data_error_upper and reference/data_error_lower. Lower
        and upper are taken in the strict mathematical sense, without
        considering absolute values of the data
    """

    class Meta:
        name = "pulse_schedule_reference_density"

    reference_name: str = field(default="")
    reference: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    reference_type: int = field(default=999999999)
    envelope_type: int = field(default=999999999)


@idspy_dataclass(repr=False, slots=True)
class PulseScheduleReferenceEc(IdsBaseClass):
    """
    Pulse schedule reference for the ec structure.

    :ivar reference_name: Reference name (e.g. in the native pulse
        schedule system of the device)
    :ivar reference: Reference waveform. Caution : error bars of the
        reference/data node are not used in the usual sense, instead
        they are used to describe the control envelope, with a meaning
        depending on the chosen envelope_type option.
    :ivar reference_type: Reference type:  0:relative (don't use for the
        moment, to be defined later when segments are introduced in the
        IDS structure); 1: absolute: the reference time trace is
        provided in the reference/data node
    :ivar envelope_type: Envelope type:  0:relative: means that the
        envelope upper and lower bound values are defined respectively
        as reference.data * reference.data_error_upper and
        reference.data * reference.data_error_lower. 1: absolute: the
        envelope upper and lower bound values are given respectively by
        reference/data_error_upper and reference/data_error_lower. Lower
        and upper are taken in the strict mathematical sense, without
        considering absolute values of the data
    """

    class Meta:
        name = "pulse_schedule_reference_ec"

    reference_name: str = field(default="")
    reference: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    reference_type: int = field(default=999999999)
    envelope_type: int = field(default=999999999)


@idspy_dataclass(repr=False, slots=True)
class PulseScheduleReferenceIc(IdsBaseClass):
    """
    Pulse schedule reference for the ic structure.

    :ivar reference_name: Reference name (e.g. in the native pulse
        schedule system of the device)
    :ivar reference: Reference waveform. Caution : error bars of the
        reference/data node are not used in the usual sense, instead
        they are used to describe the control envelope, with a meaning
        depending on the chosen envelope_type option.
    :ivar reference_type: Reference type:  0:relative (don't use for the
        moment, to be defined later when segments are introduced in the
        IDS structure); 1: absolute: the reference time trace is
        provided in the reference/data node
    :ivar envelope_type: Envelope type:  0:relative: means that the
        envelope upper and lower bound values are defined respectively
        as reference.data * reference.data_error_upper and
        reference.data * reference.data_error_lower. 1: absolute: the
        envelope upper and lower bound values are given respectively by
        reference/data_error_upper and reference/data_error_lower. Lower
        and upper are taken in the strict mathematical sense, without
        considering absolute values of the data
    """

    class Meta:
        name = "pulse_schedule_reference_ic"

    reference_name: str = field(default="")
    reference: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    reference_type: int = field(default=999999999)
    envelope_type: int = field(default=999999999)


@idspy_dataclass(repr=False, slots=True)
class PulseScheduleReferenceLh(IdsBaseClass):
    """
    Pulse schedule reference for the lh structure.

    :ivar reference_name: Reference name (e.g. in the native pulse
        schedule system of the device)
    :ivar reference: Reference waveform. Caution : error bars of the
        reference/data node are not used in the usual sense, instead
        they are used to describe the control envelope, with a meaning
        depending on the chosen envelope_type option.
    :ivar reference_type: Reference type:  0:relative (don't use for the
        moment, to be defined later when segments are introduced in the
        IDS structure); 1: absolute: the reference time trace is
        provided in the reference/data node
    :ivar envelope_type: Envelope type:  0:relative: means that the
        envelope upper and lower bound values are defined respectively
        as reference.data * reference.data_error_upper and
        reference.data * reference.data_error_lower. 1: absolute: the
        envelope upper and lower bound values are given respectively by
        reference/data_error_upper and reference/data_error_lower. Lower
        and upper are taken in the strict mathematical sense, without
        considering absolute values of the data
    """

    class Meta:
        name = "pulse_schedule_reference_lh"

    reference_name: str = field(default="")
    reference: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    reference_type: int = field(default=999999999)
    envelope_type: int = field(default=999999999)


@idspy_dataclass(repr=False, slots=True)
class PulseScheduleReferenceNbi(IdsBaseClass):
    """
    Pulse schedule reference for the nbi structure.

    :ivar reference_name: Reference name (e.g. in the native pulse
        schedule system of the device)
    :ivar reference: Reference waveform. Caution : error bars of the
        reference/data node are not used in the usual sense, instead
        they are used to describe the control envelope, with a meaning
        depending on the chosen envelope_type option.
    :ivar reference_type: Reference type:  0:relative (don't use for the
        moment, to be defined later when segments are introduced in the
        IDS structure); 1: absolute: the reference time trace is
        provided in the reference/data node
    :ivar envelope_type: Envelope type:  0:relative: means that the
        envelope upper and lower bound values are defined respectively
        as reference.data * reference.data_error_upper and
        reference.data * reference.data_error_lower. 1: absolute: the
        envelope upper and lower bound values are given respectively by
        reference/data_error_upper and reference/data_error_lower. Lower
        and upper are taken in the strict mathematical sense, without
        considering absolute values of the data
    """

    class Meta:
        name = "pulse_schedule_reference_nbi"

    reference_name: str = field(default="")
    reference: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    reference_type: int = field(default=999999999)
    envelope_type: int = field(default=999999999)


@idspy_dataclass(repr=False, slots=True)
class PulseScheduleReferenceNoAos(IdsBaseClass):
    """
    Pulse schedule reference with relative path to common time not traversing an
    AoS.

    :ivar reference_name: Reference name (e.g. in the native pulse
        schedule system of the device)
    :ivar reference: Reference waveform. Caution : error bars of the
        reference/data node are not used in the usual sense, instead
        they are used to describe the control envelope, with a meaning
        depending on the chosen envelope_type option.
    :ivar reference_type: Reference type:  0:relative (don't use for the
        moment, to be defined later when segments are introduced in the
        IDS structure); 1: absolute: the reference time trace is
        provided in the reference/data node
    :ivar envelope_type: Envelope type:  0:relative: means that the
        envelope upper and lower bound values are defined respectively
        as reference.data * reference.data_error_upper and
        reference.data * reference.data_error_lower. 1: absolute: the
        envelope upper and lower bound values are given respectively by
        reference/data_error_upper and reference/data_error_lower. Lower
        are upper are taken in the strict mathematical sense, without
        considering absolute values of the data
    """

    class Meta:
        name = "pulse_schedule_reference_no_aos"

    reference_name: str = field(default="")
    reference: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    reference_type: int = field(default=999999999)
    envelope_type: int = field(default=999999999)


@idspy_dataclass(repr=False, slots=True)
class PulseScheduleReferencePfActive(IdsBaseClass):
    """
    Pulse schedule reference for the pf_active structure.

    :ivar reference_name: Reference name (e.g. in the native pulse
        schedule system of the device)
    :ivar reference: Reference waveform. Caution : error bars of the
        reference/data node are not used in the usual sense, instead
        they are used to describe the control envelope, with a meaning
        depending on the chosen envelope_type option.
    :ivar reference_type: Reference type:  0:relative (don't use for the
        moment, to be defined later when segments are introduced in the
        IDS structure); 1: absolute: the reference time trace is
        provided in the reference/data node
    :ivar envelope_type: Envelope type:  0:relative: means that the
        envelope upper and lower bound values are defined respectively
        as reference.data * reference.data_error_upper and
        reference.data * reference.data_error_lower. 1: absolute: the
        envelope upper and lower bound values are given respectively by
        reference/data_error_upper and reference/data_error_lower. Lower
        and upper are taken in the strict mathematical sense, without
        considering absolute values of the data
    """

    class Meta:
        name = "pulse_schedule_reference_pf_active"

    reference_name: str = field(default="")
    reference: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    reference_type: int = field(default=999999999)
    envelope_type: int = field(default=999999999)


@idspy_dataclass(repr=False, slots=True)
class PulseScheduleReferencePosition(IdsBaseClass):
    """
    Pulse schedule reference for the position_control structure.

    :ivar reference_name: Reference name (e.g. in the native pulse
        schedule system of the device)
    :ivar reference: Reference waveform. Caution : error bars of the
        reference/data node are not used in the usual sense, instead
        they are used to describe the control envelope, with a meaning
        depending on the chosen envelope_type option.
    :ivar reference_type: Reference type:  0:relative (don't use for the
        moment, to be defined later when segments are introduced in the
        IDS structure); 1: absolute: the reference time trace is
        provided in the reference/data node
    :ivar envelope_type: Envelope type:  0:relative: means that the
        envelope upper and lower bound values are defined respectively
        as reference.data * reference.data_error_upper and
        reference.data * reference.data_error_lower. 1: absolute: the
        envelope upper and lower bound values are given respectively by
        reference/data_error_upper and reference/data_error_lower. Lower
        are upper are taken in the strict mathematical sense, without
        considering absolute values of the data
    """

    class Meta:
        name = "pulse_schedule_reference_position"

    reference_name: str = field(default="")
    reference: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    reference_type: int = field(default=999999999)
    envelope_type: int = field(default=999999999)


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
class GasMixtureConstant(IdsBaseClass):
    """
    Description of a neutral species within a gas mixture (constant)

    :ivar element: List of elements forming the atom or molecule
    :ivar label: String identifying neutral (e.g. H, D, T, He, C, ...)
    :ivar fraction: Relative fraction of this species (in molecules) in
        the gas mixture
    """

    class Meta:
        name = "gas_mixture_constant"

    element: list[PlasmaCompositionNeutralElementConstant] = field(
        default_factory=list,
        metadata={
            "max_occurs": 5,
        },
    )
    label: str = field(default="")
    fraction: float = field(default=9e40)


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
class PulseScheduleDensityControlIon(IdsBaseClass):
    """
    References for ion species.

    :ivar element: List of elements forming the atom or molecule
    :ivar z_ion: Ion charge
    :ivar label: String identifying ion (e.g. H, D, T, He, C, D2, ...)
    :ivar n_i_volume_average: Volume averaged ion density (average over
        the plasma volume up to the LCFS)
    """

    class Meta:
        name = "pulse_schedule_density_control_ion"

    element: list[PlasmaCompositionNeutralElementConstant] = field(
        default_factory=list,
        metadata={
            "max_occurs": 5,
        },
    )
    z_ion: float = field(default=9e40)
    label: str = field(default="")
    n_i_volume_average: Optional[PulseScheduleReferenceDensity] = field(
        default=None
    )


@idspy_dataclass(repr=False, slots=True)
class PulseScheduleEcBeam(IdsBaseClass):
    """
    EC beam.

    :ivar name: Name of the beam
    :ivar identifier: Identifier of the beam
    :ivar power_launched: Beam power launched into the vacuum vessel
    :ivar frequency: Frequency
    :ivar deposition_rho_tor_norm: Normalised toroidal flux coordinate
        at which the main deposition should occur
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
    """

    class Meta:
        name = "pulse_schedule_ec_beam"

    name: str = field(default="")
    identifier: str = field(default="")
    power_launched: Optional[PulseScheduleReferenceEc] = field(default=None)
    frequency: Optional[PulseScheduleReferenceEc] = field(default=None)
    deposition_rho_tor_norm: Optional[PulseScheduleReferenceEc] = field(
        default=None
    )
    steering_angle_pol: Optional[PulseScheduleReferenceEc] = field(
        default=None
    )
    steering_angle_tor: Optional[PulseScheduleReferenceEc] = field(
        default=None
    )


@idspy_dataclass(repr=False, slots=True)
class PulseScheduleEvent(IdsBaseClass):
    """
    Event.

    :ivar type_value: Type of this event
    :ivar identifier: Unique identifier of this event provided by the
        scheduling / event handler
    :ivar time_stamp: Time stamp of this event
    :ivar duration: Duration of this event
    :ivar acquisition_strategy: Acquisition strategy related to this
        event: index = 1 : on-trigger; index = 2 : pre-trigger; index =
        3 : post-trigger
    :ivar acquisition_state: Acquisition state of the related system :
        index = 1 : armed; index = 2 : on; index = 3 : off; index = 4 :
        closed
    :ivar provider: System having generated this event
    :ivar listeners: Systems listening to this event
    """

    class Meta:
        name = "pulse_schedule_event"

    type_value: Optional[Identifier] = field(default=None)
    identifier: str = field(default="")
    time_stamp: float = field(default=9e40)
    duration: float = field(default=9e40)
    acquisition_strategy: Optional[Identifier] = field(default=None)
    acquisition_state: Optional[Identifier] = field(default=None)
    provider: str = field(default="")
    listeners: Optional[list[str]] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class PulseScheduleFluxControl(IdsBaseClass):
    """
    Flux control references.

    :ivar i_plasma: Plasma current
    :ivar loop_voltage: Loop voltage
    :ivar li_3: Internal inductance
    :ivar beta_normal: Normalised toroidal beta, defined as 100 *
        beta_tor * a[m] * B0 [T] / ip [MA]
    :ivar mode: Control mode (operation mode and/or settings used by the
        controller)
    :ivar time: Timebase for the dynamic nodes located at this level of
        the IDS structure and below
    """

    class Meta:
        name = "pulse_schedule_flux_control"

    i_plasma: Optional[PulseScheduleReferenceNoAos] = field(default=None)
    loop_voltage: Optional[PulseScheduleReferenceNoAos] = field(default=None)
    li_3: Optional[PulseScheduleReferenceNoAos] = field(default=None)
    beta_normal: Optional[PulseScheduleReferenceNoAos] = field(default=None)
    mode: ndarray[(int,), int] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    time: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )


@idspy_dataclass(repr=False, slots=True)
class PulseScheduleGap(IdsBaseClass):
    """
    Gap for describing the plasma boundary.

    :ivar name: Name of the gap
    :ivar identifier: Identifier of the gap
    :ivar r: Major radius of the reference point
    :ivar z: Height of the reference point
    :ivar angle: Angle between the direction in which the gap is
        measured (in the poloidal cross-section) and the horizontal
        axis.
    :ivar value: Value of the gap, i.e. distance between the reference
        point and the separatrix along the gap direction
    """

    class Meta:
        name = "pulse_schedule_gap"

    name: str = field(default="")
    identifier: str = field(default="")
    r: float = field(default=9e40)
    z: float = field(default=9e40)
    angle: float = field(default=9e40)
    value: Optional[PulseScheduleReferencePosition] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class PulseScheduleIcAntenna(IdsBaseClass):
    """
    IC antenna.

    :ivar name: Name of the antenna
    :ivar identifier: Identifier of the antenna
    :ivar power_type: Type of power used in the sibling power node
        (defining which power is referred to in this pulse_schedule).
        Index = 1: power_launched, 2: power_forward (see definitions in
        the ic_antennas  IDS)
    :ivar power: Power
    :ivar phase: Phase
    :ivar frequency: Frequency
    """

    class Meta:
        name = "pulse_schedule_ic_antenna"

    name: str = field(default="")
    identifier: str = field(default="")
    power_type: Optional[IdentifierStatic] = field(default=None)
    power: Optional[PulseScheduleReferenceIc] = field(default=None)
    phase: Optional[PulseScheduleReferenceIc] = field(default=None)
    frequency: Optional[PulseScheduleReferenceIc] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class PulseScheduleLhAntenna(IdsBaseClass):
    """
    LH antenna.

    :ivar name: Name of the antenna
    :ivar identifier: Identifier of the antenna
    :ivar power_type: Type of power used in the sibling power node
        (defining which power is referred to in this pulse_schedule).
        Index = 1: power_launched, 2: power_forward (see definitions in
        the lh_antennas  IDS)
    :ivar power: Power
    :ivar phase: Phasing between neighbour waveguides (in the toroidal
        direction)
    :ivar n_parallel: Main parallel refractive index of the injected
        wave power spectrum
    :ivar frequency: Frequency
    """

    class Meta:
        name = "pulse_schedule_lh_antenna"

    name: str = field(default="")
    identifier: str = field(default="")
    power_type: Optional[IdentifierStatic] = field(default=None)
    power: Optional[PulseScheduleReferenceLh] = field(default=None)
    phase: Optional[PulseScheduleReferenceLh] = field(default=None)
    n_parallel: Optional[PulseScheduleReferenceLh] = field(default=None)
    frequency: Optional[PulseScheduleReferenceLh] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class PulseScheduleOutline(IdsBaseClass):
    """
    RZ outline.

    :ivar r: Major radius
    :ivar z: Height
    """

    class Meta:
        name = "pulse_schedule_outline"

    r: Optional[PulseScheduleReferencePosition] = field(default=None)
    z: Optional[PulseScheduleReferencePosition] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class PulseSchedulePfActiveCoil(IdsBaseClass):
    """
    PF coil.

    :ivar name: Name of the coil
    :ivar identifier: Identifier of the coil
    :ivar current: Current fed in the coil (for 1 turn, to be multiplied
        by the number of turns to obtain the generated magnetic field),
        positive when flowing from side 1 to side 2 of the coil (inside
        the coil), this numbering being made consistently with the
        convention that the current is counter-clockwise when seen from
        above.
    :ivar resistance_additional: Additional resistance due to e.g.
        dynamically switchable resistors
    """

    class Meta:
        name = "pulse_schedule_pf_active_coil"

    name: str = field(default="")
    identifier: str = field(default="")
    current: Optional[PulseScheduleReferencePfActive] = field(default=None)
    resistance_additional: Optional[PulseScheduleReferencePfActive] = field(
        default=None
    )


@idspy_dataclass(repr=False, slots=True)
class PulseSchedulePfActiveSupply(IdsBaseClass):
    """
    PF supply.

    :ivar name: Name of the supply
    :ivar identifier: Identifier of the supply
    :ivar voltage: Voltage at the supply output (Vside1-Vside2)
    :ivar current: Current fed into one turn of the coil. (Multiply by
        number of turns to obtain generated magnetic field). Positive
        when flowing from side 1 to side 2 of the coil, this numbering
        being made consistently with the convention that the current
        flows counter-clockwise when viewed from above.
    """

    class Meta:
        name = "pulse_schedule_pf_active_supply"

    name: str = field(default="")
    identifier: str = field(default="")
    voltage: Optional[PulseScheduleReferencePfActive] = field(default=None)
    current: Optional[PulseScheduleReferencePfActive] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class PulseScheduleRz(IdsBaseClass):
    """
    R,Z position.

    :ivar r: Major radius
    :ivar z: Height
    """

    class Meta:
        name = "pulse_schedule_rz"

    r: Optional[PulseScheduleReferencePosition] = field(default=None)
    z: Optional[PulseScheduleReferencePosition] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class PulseScheduleTf(IdsBaseClass):
    """
    Toroidal field references.

    :ivar b_field_tor_vacuum_r: Vacuum field times major radius in the
        toroidal field magnet. Positive sign means anti-clockwise when
        viewed from above
    :ivar mode: Control mode (operation mode and/or settings used by the
        controller)
    :ivar time: Timebase for the dynamic nodes located at this level of
        the IDS structure and below
    """

    class Meta:
        name = "pulse_schedule_tf"

    b_field_tor_vacuum_r: Optional[PulseScheduleReferenceNoAos] = field(
        default=None
    )
    mode: ndarray[(int,), int] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    time: ndarray[(int,), float] = field(
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
class PulseScheduleDensityControlValve(IdsBaseClass):
    """
    Gas injection valve.

    :ivar name: Name of the valve
    :ivar identifier: Identifier of the valve
    :ivar flow_rate: Flow rate of the valve
    :ivar species: Species injected by the valve (may be more than one
        in case the valve injects a gas mixture)
    """

    class Meta:
        name = "pulse_schedule_density_control_valve"

    name: str = field(default="")
    identifier: str = field(default="")
    flow_rate: Optional[PulseScheduleReferenceDensity] = field(default=None)
    species: list[GasMixtureConstant] = field(
        default_factory=list,
        metadata={
            "max_occurs": 3,
        },
    )


@idspy_dataclass(repr=False, slots=True)
class PulseScheduleEc(IdsBaseClass):
    """
    Electron cyclotron heating and current drive system.

    :ivar beam: Set of Electron Cyclotron beams
    :ivar power_launched: Total EC power launched in the plasma (sum
        over the beams)
    :ivar mode: Control mode (operation mode and/or settings used by the
        controller)
    :ivar time: Timebase for the dynamic nodes located at this level of
        the IDS structure and below
    """

    class Meta:
        name = "pulse_schedule_ec"

    beam: list[PulseScheduleEcBeam] = field(
        default_factory=list,
        metadata={
            "max_occurs": 100,
        },
    )
    power_launched: Optional[PulseScheduleReferenceEc] = field(default=None)
    mode: ndarray[(int,), int] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    time: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )


@idspy_dataclass(repr=False, slots=True)
class PulseScheduleIc(IdsBaseClass):
    """
    Ion cyclotron heating and current drive system.

    :ivar antenna: Set of ICRH antennas
    :ivar power: Total IC power (sum over the antennas)
    :ivar mode: Control mode (operation mode and/or settings used by the
        controller)
    :ivar time: Timebase for the dynamic nodes located at this level of
        the IDS structure and below
    """

    class Meta:
        name = "pulse_schedule_ic"

    antenna: list[PulseScheduleIcAntenna] = field(
        default_factory=list,
        metadata={
            "max_occurs": 3,
        },
    )
    power: Optional[PulseScheduleReferenceIc] = field(default=None)
    mode: ndarray[(int,), int] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    time: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )


@idspy_dataclass(repr=False, slots=True)
class PulseScheduleLh(IdsBaseClass):
    """
    Lower hybrid heating and current drive system.

    :ivar antenna: Set of LH antennas
    :ivar power: Total LH power (sum over the antennas)
    :ivar mode: Control mode (operation mode and/or settings used by the
        controller)
    :ivar time: Timebase for the dynamic nodes located at this level of
        the IDS structure and below
    """

    class Meta:
        name = "pulse_schedule_lh"

    antenna: list[PulseScheduleLhAntenna] = field(
        default_factory=list,
        metadata={
            "max_occurs": 3,
        },
    )
    power: Optional[PulseScheduleReferenceLh] = field(default=None)
    mode: ndarray[(int,), int] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    time: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )


@idspy_dataclass(repr=False, slots=True)
class PulseScheduleNbiUnit(IdsBaseClass):
    """
    NBI unit.

    :ivar name: Name of the NBI unit
    :ivar identifier: Identifier of the NBI unit
    :ivar species: Species injected by the NBI unit (may be more than
        one in case the unit injects a gas mixture)
    :ivar power: Power launched from this unit into the vacuum vessel
    :ivar energy: Full energy of the injected species (acceleration of a
        single atom)
    """

    class Meta:
        name = "pulse_schedule_nbi_unit"

    name: str = field(default="")
    identifier: str = field(default="")
    species: list[GasMixtureConstant] = field(
        default_factory=list,
        metadata={
            "max_occurs": 3,
        },
    )
    power: Optional[PulseScheduleReferenceNbi] = field(default=None)
    energy: Optional[PulseScheduleReferenceNbi] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class PulseSchedulePfActive(IdsBaseClass):
    """
    PF coils references.

    :ivar coil: Set of poloidal field coils
    :ivar supply: Set of PF power supplies
    :ivar mode: Control mode (operation mode and/or settings used by the
        controller)
    :ivar time: Timebase for the dynamic nodes located at this level of
        the IDS structure and below
    """

    class Meta:
        name = "pulse_schedule_pf_active"

    coil: list[PulseSchedulePfActiveCoil] = field(
        default_factory=list,
        metadata={
            "max_occurs": 32,
        },
    )
    supply: list[PulseSchedulePfActiveSupply] = field(
        default_factory=list,
        metadata={
            "max_occurs": 32,
        },
    )
    mode: ndarray[(int,), int] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    time: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )


@idspy_dataclass(repr=False, slots=True)
class PulseSchedulePosition(IdsBaseClass):
    """
    Position control references.

    :ivar magnetic_axis: Magnetic axis position
    :ivar geometric_axis: RZ position of the geometric axis (defined as
        (Rmin+Rmax) / 2 and (Zmin+Zmax) / 2 of the boundary)
    :ivar minor_radius: Minor radius of the plasma boundary (defined as
        (Rmax-Rmin) / 2 of the boundary)
    :ivar elongation: Elongation of the plasma boundary
    :ivar elongation_upper: Elongation (upper half w.r.t. geometric
        axis) of the plasma boundary
    :ivar elongation_lower: Elongation (lower half w.r.t. geometric
        axis) of the plasma boundary
    :ivar triangularity: Triangularity of the plasma boundary
    :ivar triangularity_upper: Upper triangularity of the plasma
        boundary
    :ivar triangularity_lower: Lower triangularity of the plasma
        boundary
    :ivar triangularity_inner: Inner triangularity of the plasma
        boundary
    :ivar triangularity_outer: Outer triangularity of the plasma
        boundary
    :ivar triangularity_minor: Minor triangularity of the plasma
        boundary
    :ivar squareness_upper_outer: Upper outer squareness of the plasma
        boundary (definition from T. Luce, Plasma Phys. Control. Fusion
        55 (2013) 095009)
    :ivar squareness_upper_inner: Upper inner squareness of the plasma
        boundary (definition from T. Luce, Plasma Phys. Control. Fusion
        55 (2013) 095009)
    :ivar squareness_lower_outer: Lower outer squareness of the plasma
        boundary (definition from T. Luce, Plasma Phys. Control. Fusion
        55 (2013) 095009)
    :ivar squareness_lower_inner: Lower inner squareness of the plasma
        boundary (definition from T. Luce, Plasma Phys. Control. Fusion
        55 (2013) 095009)
    :ivar x_point: Array of X-points, for each of them the RZ position
        is given
    :ivar strike_point: Array of strike points, for each of them the RZ
        position is given
    :ivar active_limiter_point: RZ position of the active limiter point
        (point of the plasma boundary in contact with the limiter)
    :ivar boundary_outline: Set of (R,Z) points defining the outline of
        the plasma boundary
    :ivar z_r_max: Height of the separatrix point of maximum major
        radius
    :ivar z_r_min: Height of the separatrix point of minimum major
        radius
    :ivar gap: Set of gaps, defined by a reference point and a
        direction.
    :ivar current_centroid: RZ position of the current centroid
    :ivar mode: Control mode (operation mode and/or settings used by the
        controller)
    :ivar time: Timebase for the dynamic nodes located at this level of
        the IDS structure and below
    """

    class Meta:
        name = "pulse_schedule_position"

    magnetic_axis: Optional[PulseScheduleRz] = field(default=None)
    geometric_axis: Optional[PulseScheduleRz] = field(default=None)
    minor_radius: Optional[PulseScheduleReferencePosition] = field(
        default=None
    )
    elongation: Optional[PulseScheduleReferencePosition] = field(default=None)
    elongation_upper: Optional[PulseScheduleReferencePosition] = field(
        default=None
    )
    elongation_lower: Optional[PulseScheduleReferencePosition] = field(
        default=None
    )
    triangularity: Optional[PulseScheduleReferencePosition] = field(
        default=None
    )
    triangularity_upper: Optional[PulseScheduleReferencePosition] = field(
        default=None
    )
    triangularity_lower: Optional[PulseScheduleReferencePosition] = field(
        default=None
    )
    triangularity_inner: Optional[PulseScheduleReferencePosition] = field(
        default=None
    )
    triangularity_outer: Optional[PulseScheduleReferencePosition] = field(
        default=None
    )
    triangularity_minor: Optional[PulseScheduleReferencePosition] = field(
        default=None
    )
    squareness_upper_outer: Optional[PulseScheduleReferencePosition] = field(
        default=None
    )
    squareness_upper_inner: Optional[PulseScheduleReferencePosition] = field(
        default=None
    )
    squareness_lower_outer: Optional[PulseScheduleReferencePosition] = field(
        default=None
    )
    squareness_lower_inner: Optional[PulseScheduleReferencePosition] = field(
        default=None
    )
    x_point: list[PulseScheduleRz] = field(
        default_factory=list,
        metadata={
            "max_occurs": 2,
        },
    )
    strike_point: list[PulseScheduleRz] = field(
        default_factory=list,
        metadata={
            "max_occurs": 4,
        },
    )
    active_limiter_point: Optional[PulseScheduleRz] = field(default=None)
    boundary_outline: list[PulseScheduleOutline] = field(
        default_factory=list,
        metadata={
            "max_occurs": 301,
        },
    )
    z_r_max: Optional[PulseScheduleReferencePosition] = field(default=None)
    z_r_min: Optional[PulseScheduleReferencePosition] = field(default=None)
    gap: list[PulseScheduleGap] = field(
        default_factory=list,
        metadata={
            "max_occurs": 51,
        },
    )
    current_centroid: Optional[PulseScheduleRz] = field(default=None)
    mode: ndarray[(int,), int] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    time: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )


@idspy_dataclass(repr=False, slots=True)
class PulseScheduleDensityControl(IdsBaseClass):
    """
    Gas injection system.

    :ivar valve: Set of injection valves. Time-dependent
    :ivar n_e_line: Line integrated electron density over a line of
        sight in the whole vacuum chamber
    :ivar n_e_line_lcfs: Line integrated electron density over a line of
        sight within the LCFS
    :ivar n_e_profile_average: Integral of a 1D core profile over
        rho_tor_norm up to the LCFS
    :ivar n_e_line_of_sight: Description of the line of sight for
        calculating n_e, defined by two points when the beam is not
        reflected, a third point is added to define the reflected beam
        path
    :ivar n_e_volume_average: Volume averaged electron density (average
        over the plasma volume up to the LCFS)
    :ivar zeff: Line averaged effective charge
    :ivar zeff_method: Method for zeff calculation : Index = 1: average
        over a line of sight in the whole vacuum chamber, 2 : average
        over a line of sight within the LCFS, 3 : average of a 1D core
        profile over rho_tor_norm up to the LCFS
    :ivar zeff_line_of_sight: Description of the line of sight for
        calculating zeff, defined by two points when the beam is not
        reflected, a third point is added to define the reflected beam
        path
    :ivar n_t_over_n_d: Average ratio of tritium over deuterium density
    :ivar n_h_over_n_d: Average ratio of hydrogen over deuterium density
    :ivar ion: Quantities related to the different ion species, in the
        sense of isonuclear or isomolecular sequences
    :ivar mode: Control mode (operation mode and/or settings used by the
        controller)
    :ivar time: Timebase for the dynamic nodes located at this level of
        the IDS structure and below
    """

    class Meta:
        name = "pulse_schedule_density_control"

    valve: list[PulseScheduleDensityControlValve] = field(
        default_factory=list,
        metadata={
            "max_occurs": 20,
        },
    )
    n_e_line: Optional[PulseScheduleReferenceDensity] = field(default=None)
    n_e_line_lcfs: Optional[PulseScheduleReferenceDensity] = field(
        default=None
    )
    n_e_profile_average: Optional[PulseScheduleReferenceDensity] = field(
        default=None
    )
    n_e_line_of_sight: Optional[LineOfSight3Points] = field(default=None)
    n_e_volume_average: Optional[PulseScheduleReferenceDensity] = field(
        default=None
    )
    zeff: Optional[PulseScheduleReferenceDensity] = field(default=None)
    zeff_method: Optional[IdentifierStatic] = field(default=None)
    zeff_line_of_sight: Optional[LineOfSight3Points] = field(default=None)
    n_t_over_n_d: Optional[PulseScheduleReferenceDensity] = field(default=None)
    n_h_over_n_d: Optional[PulseScheduleReferenceDensity] = field(default=None)
    ion: list[PulseScheduleDensityControlIon] = field(
        default_factory=list,
        metadata={
            "max_occurs": 20,
        },
    )
    mode: ndarray[(int,), int] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    time: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )


@idspy_dataclass(repr=False, slots=True)
class PulseScheduleNbi(IdsBaseClass):
    """
    Neutral beam heating and current drive system.

    :ivar unit: Set of NBI units
    :ivar power: Total NBI power (sum over the units)
    :ivar mode: Control mode (operation mode and/or settings used by the
        controller)
    :ivar time: Timebase for the dynamic nodes located at this level of
        the IDS structure and below
    """

    class Meta:
        name = "pulse_schedule_nbi"

    unit: list[PulseScheduleNbiUnit] = field(
        default_factory=list,
        metadata={
            "max_occurs": 36,
        },
    )
    power: Optional[PulseScheduleReferenceNbi] = field(default=None)
    mode: ndarray[(int,), int] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    time: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )


@idspy_dataclass(repr=False, slots=True)
class PulseSchedule(IdsBaseClass):
    """Description of Pulse Schedule, described by subsystems waveform references
    and an enveloppe around them.

    The controllers, pulse schedule and SDN are defined in separate
    IDSs. All names and identifiers of subsystems appearing in the
    pulse_schedule must be identical to those used in the IDSs
    describing the related subsystems.

    :ivar ids_properties:
    :ivar ic: Ion cyclotron heating and current drive system
    :ivar ec: Electron cyclotron heating and current drive system
    :ivar lh: Lower Hybrid heating and current drive system
    :ivar nbi: Neutral beam heating and current drive system
    :ivar density_control: Gas injection system and density control
        references
    :ivar event: List of events, either predefined triggers  or events
        recorded during the pulse
    :ivar flux_control: Magnetic flux control references
    :ivar pf_active: Poloidal field coil references
    :ivar position_control: Plasma position and shape control references
    :ivar tf: Toroidal field references
    :ivar code:
    :ivar time:
    """

    class Meta:
        name = "pulse_schedule"

    ids_properties: Optional[IdsProperties] = field(default=None)
    ic: Optional[PulseScheduleIc] = field(default=None)
    ec: Optional[PulseScheduleEc] = field(default=None)
    lh: Optional[PulseScheduleLh] = field(default=None)
    nbi: Optional[PulseScheduleNbi] = field(default=None)
    density_control: Optional[PulseScheduleDensityControl] = field(
        default=None
    )
    event: list[PulseScheduleEvent] = field(
        default_factory=list,
        metadata={
            "max_occurs": 130,
        },
    )
    flux_control: Optional[PulseScheduleFluxControl] = field(default=None)
    pf_active: Optional[PulseSchedulePfActive] = field(default=None)
    position_control: Optional[PulseSchedulePosition] = field(default=None)
    tf: Optional[PulseScheduleTf] = field(default=None)
    code: Optional[Code] = field(default=None)
    time: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
