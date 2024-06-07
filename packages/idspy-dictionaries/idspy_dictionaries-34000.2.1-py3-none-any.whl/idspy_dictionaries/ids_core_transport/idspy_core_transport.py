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
class CoreRadialGrid(IdsBaseClass):
    """
    1D radial grid for core* IDSs.

    :ivar rho_tor_norm: Normalised toroidal flux coordinate. The
        normalizing value for rho_tor_norm, is the toroidal flux
        coordinate at the equilibrium boundary (LCFS or 99.x % of the
        LCFS in case of a fixed boundary equilibium calculation, see
        time_slice/boundary/b_flux_pol_norm in the equilibrium IDS)
    :ivar rho_tor: Toroidal flux coordinate. rho_tor =
        sqrt(b_flux_tor/(pi*b0)) ~ sqrt(pi*r^2*b0/(pi*b0)) ~ r [m]. The
        toroidal field used in its definition is indicated under
        vacuum_toroidal_field/b0
    :ivar rho_pol_norm: Normalised poloidal flux coordinate =
        sqrt((psi(rho)-psi(magnetic_axis)) /
        (psi(LCFS)-psi(magnetic_axis)))
    :ivar psi: Poloidal magnetic flux
    :ivar volume: Volume enclosed inside the magnetic surface
    :ivar area: Cross-sectional area of the flux surface
    :ivar surface: Surface area of the toroidal flux surface
    :ivar psi_magnetic_axis: Value of the poloidal magnetic flux at the
        magnetic axis (useful to normalize the psi array values when the
        radial grid doesn't go from the magnetic axis to the plasma
        boundary)
    :ivar psi_boundary: Value of the poloidal magnetic flux at the
        plasma boundary (useful to normalize the psi array values when
        the radial grid doesn't go from the magnetic axis to the plasma
        boundary)
    """

    class Meta:
        name = "core_radial_grid"

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
    rho_pol_norm: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    psi: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    volume: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    area: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    surface: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    psi_magnetic_axis: float = field(default=9e40)
    psi_boundary: float = field(default=9e40)


@idspy_dataclass(repr=False, slots=True)
class CoreTransportModel1Energy(IdsBaseClass):
    """Transport coefficients for energy equations.

    Coordinates one level above.

    :ivar d: Effective diffusivity
    :ivar v: Effective convection
    :ivar flux: Flux
    """

    class Meta:
        name = "core_transport_model_1_energy"

    d: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    v: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    flux: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )


@idspy_dataclass(repr=False, slots=True)
class CoreTransportModel1Momentum(IdsBaseClass):
    """Transport coefficients for momentum equations.

    Coordinates one level above.

    :ivar d: Effective diffusivity
    :ivar v: Effective convection
    :ivar flux: Flux
    """

    class Meta:
        name = "core_transport_model_1_momentum"

    d: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    v: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    flux: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )


@idspy_dataclass(repr=False, slots=True)
class CoreTransportModel2Density(IdsBaseClass):
    """Transport coefficients for density equations.

    Coordinates two levels above.

    :ivar d: Effective diffusivity
    :ivar v: Effective convection
    :ivar flux: Flux
    """

    class Meta:
        name = "core_transport_model_2_density"

    d: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    v: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    flux: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )


@idspy_dataclass(repr=False, slots=True)
class CoreTransportModel2Energy(IdsBaseClass):
    """Transport coefficients for energy equations.

    Coordinates two levels above.

    :ivar d: Effective diffusivity
    :ivar v: Effective convection
    :ivar flux: Flux
    """

    class Meta:
        name = "core_transport_model_2_energy"

    d: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    v: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    flux: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )


@idspy_dataclass(repr=False, slots=True)
class CoreTransportModel3Density(IdsBaseClass):
    """Transport coefficients for density equations.

    Coordinates three levels above.

    :ivar d: Effective diffusivity
    :ivar v: Effective convection
    :ivar flux: Flux
    """

    class Meta:
        name = "core_transport_model_3_density"

    d: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    v: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    flux: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )


@idspy_dataclass(repr=False, slots=True)
class CoreTransportModel3Energy(IdsBaseClass):
    """Transport coefficients for energy equations.

    Coordinates three levels above.

    :ivar d: Effective diffusivity
    :ivar v: Effective convection
    :ivar flux: Flux
    """

    class Meta:
        name = "core_transport_model_3_energy"

    d: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    v: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    flux: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )


@idspy_dataclass(repr=False, slots=True)
class CoreTransportModel3Momentum(IdsBaseClass):
    """Transport coefficients for momentum equation in a given direction.

    Coordinates three levels above.

    :ivar d: Effective diffusivity
    :ivar v: Effective convection
    :ivar flux: Flux
    :ivar flow_damping_rate: Damping rate for this flow component (e.g.
        due to collisions, calculated from a neoclassical model)
    """

    class Meta:
        name = "core_transport_model_3_momentum"

    d: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    v: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    flux: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    flow_damping_rate: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )


@idspy_dataclass(repr=False, slots=True)
class CoreTransportModel4Momentum(IdsBaseClass):
    """Transport coefficients for momentum equation in a given direction.

    Coordinates four levels above.

    :ivar d: Effective diffusivity
    :ivar v: Effective convection
    :ivar flux: Flux
    :ivar flow_damping_rate: Damping rate for this flow component (e.g.
        due to collisions, calculated from a neoclassical model)
    """

    class Meta:
        name = "core_transport_model_4_momentum"

    d: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    v: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    flux: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    flow_damping_rate: ndarray[(int,), float] = field(
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
class IdentifierDynamicAos3(IdsBaseClass):
    """Standard type for identifiers (dynamic within type 3 array of structures
    (index on time)).

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
        name = "identifier_dynamic_aos3"

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
class PlasmaCompositionNeutralElement(IdsBaseClass):
    """
    Element entering in the composition of the neutral atom or molecule (within a
    type 3 AoS)

    :ivar a: Mass of atom
    :ivar z_n: Nuclear charge
    :ivar atoms_n: Number of atoms of this element in the molecule
    :ivar multiplicity: Multiplicity of the atom
    """

    class Meta:
        name = "plasma_composition_neutral_element"

    a: float = field(default=9e40)
    z_n: float = field(default=9e40)
    atoms_n: int = field(default=999999999)
    multiplicity: float = field(default=9e40)


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
class CodeWithTimebase(IdsBaseClass):
    """Description of code-specific parameters when they are gathered below an
    array of structure (e.g. in case of multiple models or sources gathered in a
    single IDS).

    The only difference with the generic code element is the existence
    of a data+time structure for the dynamic signals (output_flag)

    :ivar name: Name of software used
    :ivar description: Short description of the software (type, purpose)
    :ivar commit: Unique commit reference of software
    :ivar version: Unique version (tag) of software
    :ivar repository: URL of software repository
    :ivar parameters: List of the code specific parameters in XML format
    :ivar output_flag: Output flag : 0 means the run is successful,
        other values mean some difficulty has been encountered, the
        exact meaning is then code specific. Negative values mean the
        result shall not be used.
    """

    class Meta:
        name = "code_with_timebase"

    name: str = field(default="")
    description: str = field(default="")
    commit: str = field(default="")
    version: str = field(default="")
    repository: str = field(default="")
    parameters: str = field(default="")
    output_flag: Optional[SignalInt1D] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class CoreTransportModelComponents3Momentum(IdsBaseClass):
    """Transport coefficients for momentum equations on various components.

    Coordinates three levels above the leaves

    :ivar radial: Radial component
    :ivar diamagnetic: Diamagnetic component
    :ivar parallel: Parallel component
    :ivar poloidal: Poloidal component
    :ivar toroidal: Toroidal component
    """

    class Meta:
        name = "core_transport_model_components_3_momentum"

    radial: Optional[CoreTransportModel3Momentum] = field(default=None)
    diamagnetic: Optional[CoreTransportModel3Momentum] = field(default=None)
    parallel: Optional[CoreTransportModel3Momentum] = field(default=None)
    poloidal: Optional[CoreTransportModel3Momentum] = field(default=None)
    toroidal: Optional[CoreTransportModel3Momentum] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class CoreTransportModelComponents4Momentum(IdsBaseClass):
    """Transport coefficients for momentum equations on various components.

    Coordinates four levels above the leaves

    :ivar radial: Radial component
    :ivar diamagnetic: Diamagnetic component
    :ivar parallel: Parallel component
    :ivar poloidal: Poloidal component
    :ivar toroidal: Toroidal component
    """

    class Meta:
        name = "core_transport_model_components_4_momentum"

    radial: Optional[CoreTransportModel4Momentum] = field(default=None)
    diamagnetic: Optional[CoreTransportModel4Momentum] = field(default=None)
    parallel: Optional[CoreTransportModel4Momentum] = field(default=None)
    poloidal: Optional[CoreTransportModel4Momentum] = field(default=None)
    toroidal: Optional[CoreTransportModel4Momentum] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class CoreTransportModelElectrons(IdsBaseClass):
    """
    Transport coefficients related to electrons.

    :ivar particles: Transport quantities for the electron density
        equation
    :ivar energy: Transport quantities for the electron energy equation
    """

    class Meta:
        name = "core_transport_model_electrons"

    particles: Optional[CoreTransportModel2Density] = field(default=None)
    energy: Optional[CoreTransportModel2Energy] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class CoreTransportModelNeutralState(IdsBaseClass):
    """
    Transport coefficients related to the a given state of the neutral species.

    :ivar label: String identifying state
    :ivar vibrational_level: Vibrational level (can be bundled)
    :ivar vibrational_mode: Vibrational mode of this state, e.g. "A_g".
        Need to define, or adopt a standard nomenclature.
    :ivar electron_configuration: Configuration of atomic orbitals of
        this state, e.g. 1s2-2s1
    :ivar particles: Transport quantities related to density equation of
        the charge state considered (thermal+non-thermal)
    :ivar energy: Transport quantities related to the energy equation of
        the charge state considered
    """

    class Meta:
        name = "core_transport_model_neutral_state"

    label: str = field(default="")
    vibrational_level: float = field(default=9e40)
    vibrational_mode: str = field(default="")
    electron_configuration: str = field(default="")
    particles: Optional[CoreTransportModel3Density] = field(default=None)
    energy: Optional[CoreTransportModel3Energy] = field(default=None)


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
class CoreTransportModelIonsChargeStates(IdsBaseClass):
    """
    Transport coefficients related to the a given state of the ion species.

    :ivar z_min: Minimum Z of the charge state bundle
    :ivar z_max: Maximum Z of the charge state bundle
    :ivar label: String identifying charge state (e.g. C+, C+2 , C+3,
        C+4, C+5, C+6, ...)
    :ivar vibrational_level: Vibrational level (can be bundled)
    :ivar vibrational_mode: Vibrational mode of this state, e.g. "A_g".
        Need to define, or adopt a standard nomenclature.
    :ivar is_neutral: Flag specifying if this state corresponds to a
        neutral (1) or not (0)
    :ivar neutral_type: Neutral type (if the considered state is a
        neutral), in terms of energy. ID =1: cold; 2: thermal; 3: fast;
        4: NBI
    :ivar electron_configuration: Configuration of atomic orbitals of
        this state, e.g. 1s2-2s1
    :ivar particles: Transport quantities related to density equation of
        the charge state considered (thermal+non-thermal)
    :ivar energy: Transport quantities related to the energy equation of
        the charge state considered
    :ivar momentum: Transport coefficients related to the state momentum
        equations for various components (directions)
    """

    class Meta:
        name = "core_transport_model_ions_charge_states"

    z_min: float = field(default=9e40)
    z_max: float = field(default=9e40)
    label: str = field(default="")
    vibrational_level: float = field(default=9e40)
    vibrational_mode: str = field(default="")
    is_neutral: int = field(default=999999999)
    neutral_type: Optional[IdentifierDynamicAos3] = field(default=None)
    electron_configuration: str = field(default="")
    particles: Optional[CoreTransportModel3Density] = field(default=None)
    energy: Optional[CoreTransportModel3Energy] = field(default=None)
    momentum: Optional[CoreTransportModelComponents4Momentum] = field(
        default=None
    )


@idspy_dataclass(repr=False, slots=True)
class CoreTransportModelNeutral(IdsBaseClass):
    """
    Transport coefficients related to a given neutral species.

    :ivar element: List of elements forming the atom or molecule
    :ivar label: String identifying ion (e.g. H+, D+, T+, He+2, C+, ...)
    :ivar ion_index: Index of the corresponding ion species in the
        ../../ion array
    :ivar particles: Transport related to the neutral density equation
    :ivar energy: Transport coefficients related to the neutral energy
        equation
    :ivar multiple_states_flag: Multiple states calculation flag :
        0-Only one state is considered; 1-Multiple states are considered
        and are described in the state structure
    :ivar state: Transport coefficients related to the different states
        of the species
    """

    class Meta:
        name = "core_transport_model_neutral"

    element: list[PlasmaCompositionNeutralElement] = field(
        default_factory=list
    )
    label: str = field(default="")
    ion_index: int = field(default=999999999)
    particles: Optional[CoreTransportModel2Density] = field(default=None)
    energy: Optional[CoreTransportModel2Energy] = field(default=None)
    multiple_states_flag: int = field(default=999999999)
    state: list[CoreTransportModelNeutralState] = field(default_factory=list)


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
class CoreTransportModelIons(IdsBaseClass):
    """
    Transport coefficients related to a given ion species.

    :ivar element: List of elements forming the atom or molecule
    :ivar z_ion: Ion charge (of the dominant ionisation state; lumped
        ions are allowed)
    :ivar label: String identifying ion (e.g. H, D, T, He, C, D2, ...)
    :ivar neutral_index: Index of the corresponding neutral species in
        the ../../neutral array
    :ivar particles: Transport related to the ion density equation
    :ivar energy: Transport coefficients related to the ion energy
        equation
    :ivar momentum: Transport coefficients related to the ion momentum
        equations for various components (directions)
    :ivar multiple_states_flag: Multiple states calculation flag :
        0-Only the 'ion' level is considered and the 'state' array of
        structure is empty; 1-Ion states are considered and are
        described in the 'state' array of structure
    :ivar state: Transport coefficients related to the different states
        of the species
    """

    class Meta:
        name = "core_transport_model_ions"

    element: list[PlasmaCompositionNeutralElement] = field(
        default_factory=list
    )
    z_ion: float = field(default=9e40)
    label: str = field(default="")
    neutral_index: int = field(default=999999999)
    particles: Optional[CoreTransportModel2Density] = field(default=None)
    energy: Optional[CoreTransportModel2Energy] = field(default=None)
    momentum: Optional[CoreTransportModelComponents3Momentum] = field(
        default=None
    )
    multiple_states_flag: int = field(default=999999999)
    state: list[CoreTransportModelIonsChargeStates] = field(
        default_factory=list
    )


@idspy_dataclass(repr=False, slots=True)
class CoreTransportModelProfiles1D(IdsBaseClass):
    """
    Transport coefficient profiles at a given time slice.

    :ivar grid_d: Grid for effective diffusivities and parallel
        conductivity
    :ivar grid_v: Grid for effective convections
    :ivar grid_flux: Grid for fluxes
    :ivar conductivity_parallel: Parallel conductivity
    :ivar electrons: Transport quantities related to the electrons
    :ivar total_ion_energy: Transport coefficients for the total (summed
        over ion  species) energy equation
    :ivar momentum_tor: Transport coefficients for total toroidal
        momentum equation
    :ivar e_field_radial: Radial component of the electric field
        (calculated e.g. by a neoclassical model)
    :ivar ion: Transport coefficients related to the various ion
        species, in the sense of isonuclear or isomolecular sequences.
        Ionisation states (and other types of states) must be
        differentiated at the state level below
    :ivar neutral: Transport coefficients related to the various neutral
        species
    :ivar time: Time
    """

    class Meta:
        name = "core_transport_model_profiles_1d"

    grid_d: Optional[CoreRadialGrid] = field(default=None)
    grid_v: Optional[CoreRadialGrid] = field(default=None)
    grid_flux: Optional[CoreRadialGrid] = field(default=None)
    conductivity_parallel: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    electrons: Optional[CoreTransportModelElectrons] = field(default=None)
    total_ion_energy: Optional[CoreTransportModel1Energy] = field(default=None)
    momentum_tor: Optional[CoreTransportModel1Momentum] = field(default=None)
    e_field_radial: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    ion: list[CoreTransportModelIons] = field(default_factory=list)
    neutral: list[CoreTransportModelNeutral] = field(default_factory=list)
    time: Optional[float] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class CoreTransportModel(IdsBaseClass):
    """
    Transport coefficients for a given model.

    :ivar comment: Any comment describing the model
    :ivar identifier: Transport model identifier
    :ivar flux_multiplier: Multiplier applied to the particule flux when
        adding its contribution in the expression of the heat flux : can
        be 0, 3/2 or 5/2
    :ivar profiles_1d: Transport coefficient profiles for various time
        slices. Fluxes and convection are positive (resp. negative) when
        outwards i.e. towards the LCFS (resp. inwards i.e.  towards the
        magnetic axes).
    :ivar code: Code-specific parameters used for this model
    """

    class Meta:
        name = "core_transport_model"

    comment: str = field(default="")
    identifier: Optional[Identifier] = field(default=None)
    flux_multiplier: float = field(default=9e40)
    profiles_1d: list[CoreTransportModelProfiles1D] = field(
        default_factory=list
    )
    code: Optional[CodeWithTimebase] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class CoreTransport(IdsBaseClass):
    """Core plasma transport of particles, energy, momentum and poloidal flux.

    The transport of particles, energy and momentum is described by diffusion coefficients, D, and convection velocities, v. These are defined by the total fluxes of particles, energy and momentum, across a flux surface given by : V' [-D Y' &lt;|grad(rho_tor_norm)|^2&gt; + v Y &lt;|grad(rho_tor_norm)|&gt;], where Y represents the particles, energy and momentum density, respectively, while V is the volume inside a flux surface, the primes denote derivatives with respect to rho_tor_norm and &lt; X &gt; is the flux surface average of a quantity X. This formulation remains valid when changing simultaneously rho_tor_norm into rho_tor in the gradient terms and in the derivatives denoted by the prime. The average flux stored in the IDS as sibling of D and v is the total flux described above divided by the flux surface area V' &lt;|grad(rho_tor_norm)|&gt;. Note that the energy flux includes the energy transported by the particle flux, in this form: Q =  V' [- n D (T)' &lt;|grad(rho_tor_norm)|^2&gt; + v (nT) &lt;|grad(rho_tor_norm)|&gt;] + flux_multiplier * T * particle_flux

    :ivar ids_properties:
    :ivar vacuum_toroidal_field: Characteristics of the vacuum toroidal
        field (used in Rho_Tor definition and in the normalization of
        current densities)
    :ivar model: Transport is described by a combination of various
        transport models
    :ivar code:
    :ivar time:
    """

    class Meta:
        name = "core_transport"

    ids_properties: Optional[IdsProperties] = field(default=None)
    vacuum_toroidal_field: Optional[BTorVacuum1] = field(default=None)
    model: list[CoreTransportModel] = field(
        default_factory=list,
        metadata={
            "max_occurs": 18,
        },
    )
    code: Optional[Code] = field(default=None)
    time: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
