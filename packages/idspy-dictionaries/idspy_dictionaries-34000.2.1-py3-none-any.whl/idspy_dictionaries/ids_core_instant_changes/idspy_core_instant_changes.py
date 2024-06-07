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
class CoreProfilesVectorComponents1(IdsBaseClass):
    """
    Vector components in predefined directions for 1D profiles, assuming
    core_radial_grid one level above.

    :ivar radial: Radial component
    :ivar diamagnetic: Diamagnetic component
    :ivar parallel: Parallel component
    :ivar poloidal: Poloidal component
    :ivar toroidal: Toroidal component
    """

    class Meta:
        name = "core_profiles_vector_components_1"

    radial: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    diamagnetic: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    parallel: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    poloidal: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    toroidal: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )


@idspy_dataclass(repr=False, slots=True)
class CoreProfilesVectorComponents2(IdsBaseClass):
    """
    Vector components in predefined directions for 1D profiles, assuming
    core_radial_grid two levels above.

    :ivar radial: Radial component
    :ivar diamagnetic: Diamagnetic component
    :ivar parallel: Parallel component
    :ivar poloidal: Poloidal component
    :ivar toroidal: Toroidal component
    """

    class Meta:
        name = "core_profiles_vector_components_2"

    radial: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    diamagnetic: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    parallel: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    poloidal: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    toroidal: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )


@idspy_dataclass(repr=False, slots=True)
class CoreProfilesVectorComponents3(IdsBaseClass):
    """
    Vector components in predefined directions for 1D profiles, assuming
    core_radial_grid 3 levels above.

    :ivar radial: Radial component
    :ivar diamagnetic: Diamagnetic component
    :ivar parallel: Parallel component
    :ivar poloidal: Poloidal component
    :ivar toroidal: Toroidal component
    """

    class Meta:
        name = "core_profiles_vector_components_3"

    radial: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    diamagnetic: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    parallel: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    poloidal: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    toroidal: ndarray[(int,), float] = field(
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
class CoreProfiles1DFit(IdsBaseClass):
    """
    Core profile fit information.

    :ivar measured: Measured values
    :ivar source: Path to the source data for each measurement in the
        IMAS data dictionary, e.g. ece/channel(i)/t_e for the electron
        temperature on the i-th channel in the ECE IDS
    :ivar time_measurement: Exact time slices used from the time array
        of the measurement source data. If the time slice does not exist
        in the time array of the source data, it means linear
        interpolation has been used
    :ivar time_measurement_slice_method: Method used to slice the data :
        index = 0 means using exact time slice of the measurement, 1
        means linear interpolation, ...
    :ivar time_measurement_width: In case the measurements are averaged
        over a time interval, this node is the full width of this time
        interval (empty otherwise). In case the slicing/averaging method
        doesn't use a hard time interval cutoff, this width is the
        characteristic time span of the slicing/averaging method. By
        convention, the time interval starts at time_measurement-
        time_width and ends at time_measurement.
    :ivar local: Integer flag : 1 means local measurement, 0 means line-
        integrated measurement
    :ivar rho_tor_norm: Normalised toroidal flux coordinate of each
        measurement (local value for a local measurement, minimum value
        reached by the line of sight for a line measurement)
    :ivar weight: Weight given to each measured value
    :ivar reconstructed: Value reconstructed from the fit
    :ivar chi_squared: Squared error normalized by the weighted standard
        deviation considered in the minimization process : chi_squared =
        weight^2 *(reconstructed - measured)^2 / sigma^2, where sigma is
        the standard deviation of the measurement error
    :ivar parameters: List of the fit specific parameters in XML format
    """

    class Meta:
        name = "core_profiles_1D_fit"

    measured: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    source: Optional[list[str]] = field(default=None)
    time_measurement: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    time_measurement_slice_method: Optional[IdentifierDynamicAos3] = field(
        default=None
    )
    time_measurement_width: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    local: ndarray[(int,), int] = field(
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
    weight: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    reconstructed: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    chi_squared: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    parameters: str = field(default="")


@idspy_dataclass(repr=False, slots=True)
class CoreProfilesNeutralState(IdsBaseClass):
    """
    Quantities related to the a given state of the neutral species.

    :ivar label: String identifying state
    :ivar electron_configuration: Configuration of atomic orbitals of
        this state, e.g. 1s2-2s1
    :ivar vibrational_level: Vibrational level (can be bundled)
    :ivar vibrational_mode: Vibrational mode of this state, e.g. "A_g".
        Need to define, or adopt a standard nomenclature.
    :ivar neutral_type: Neutral type (if the considered state is a
        neutral), in terms of energy. ID =1: cold; 2: thermal; 3: fast;
        4: NBI
    :ivar velocity: Velocity
    :ivar temperature: Temperature
    :ivar density: Density (thermal+non-thermal)
    :ivar density_thermal: Density of thermal particles
    :ivar density_fast: Density of fast (non-thermal) particles
    :ivar pressure: Pressure (thermal+non-thermal)
    :ivar pressure_thermal: Pressure (thermal) associated with random
        motion ~average((v-average(v))^2)
    :ivar pressure_fast_perpendicular: Fast (non-thermal) perpendicular
        pressure
    :ivar pressure_fast_parallel: Fast (non-thermal) parallel pressure
    """

    class Meta:
        name = "core_profiles_neutral_state"

    label: str = field(default="")
    electron_configuration: str = field(default="")
    vibrational_level: float = field(default=9e40)
    vibrational_mode: str = field(default="")
    neutral_type: Optional[IdentifierDynamicAos3] = field(default=None)
    velocity: Optional[CoreProfilesVectorComponents3] = field(default=None)
    temperature: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    density: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    density_thermal: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    density_fast: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    pressure: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    pressure_thermal: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    pressure_fast_perpendicular: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    pressure_fast_parallel: ndarray[(int,), float] = field(
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
class CoreProfileNeutral(IdsBaseClass):
    """
    Quantities related to a given neutral species.

    :ivar element: List of elements forming the atom or molecule
    :ivar label: String identifying the species (e.g. H, D, T, He, C,
        D2, DT, CD4, ...)
    :ivar ion_index: Index of the corresponding ion species in the
        ../../ion array
    :ivar temperature: Temperature (average over charge states when
        multiple charge states are considered)
    :ivar density: Density (thermal+non-thermal) (sum over charge states
        when multiple charge states are considered)
    :ivar density_thermal: Density (thermal) (sum over charge states
        when multiple charge states are considered)
    :ivar density_fast: Density of fast (non-thermal) particles (sum
        over charge states when multiple charge states are considered)
    :ivar pressure: Pressure (thermal+non-thermal) (sum over charge
        states when multiple charge states are considered)
    :ivar pressure_thermal: Pressure (thermal) associated with random
        motion ~average((v-average(v))^2) (sum over charge states when
        multiple charge states are considered)
    :ivar pressure_fast_perpendicular: Fast (non-thermal) perpendicular
        pressure  (sum over charge states when multiple charge states
        are considered)
    :ivar pressure_fast_parallel: Fast (non-thermal) parallel pressure
        (sum over charge states when multiple charge states are
        considered)
    :ivar velocity: Velocity (average over charge states when multiple
        charge states are considered)
    :ivar multiple_states_flag: Multiple states calculation flag :
        0-Only one state is considered; 1-Multiple states are considered
        and are described in the state structure
    :ivar state: Quantities related to the different states of the
        species (energy, excitation, ...)
    """

    class Meta:
        name = "core_profile_neutral"

    element: list[PlasmaCompositionNeutralElement] = field(
        default_factory=list
    )
    label: str = field(default="")
    ion_index: int = field(default=999999999)
    temperature: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    density: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    density_thermal: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    density_fast: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    pressure: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    pressure_thermal: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    pressure_fast_perpendicular: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    pressure_fast_parallel: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    velocity: Optional[CoreProfilesVectorComponents2] = field(default=None)
    multiple_states_flag: int = field(default=999999999)
    state: list[CoreProfilesNeutralState] = field(default_factory=list)


@idspy_dataclass(repr=False, slots=True)
class CoreProfilesIonsChargeStates2(IdsBaseClass):
    """
    Quantities related to the a given state of the ion species.

    :ivar z_min: Minimum Z of the charge state bundle
    :ivar z_max: Maximum Z of the charge state bundle (equal to z_min if
        no bundle)
    :ivar z_average: Average Z of the charge state bundle, volume
        averaged over the plasma radius (equal to z_min if no bundle), =
        sum (Z*x_z) where x_z is the relative concentration of a given
        charge state in the bundle, i.e. sum(x_z) = 1 over the bundle.
    :ivar z_square_average: Average Z square of the charge state bundle,
        volume averaged over the plasma radius (equal to z_min squared
        if no bundle), = sum (Z^2*x_z) where x_z is the relative
        concentration of a given charge state in the bundle, i.e.
        sum(x_z) = 1 over the bundle.
    :ivar z_average_1d: Average charge profile of the charge state
        bundle (equal to z_min if no bundle), = sum (Z*x_z) where x_z is
        the relative concentration of a given charge state in the
        bundle, i.e. sum(x_z) = 1 over the bundle.
    :ivar z_average_square_1d: Average square charge profile of the
        charge state bundle (equal to z_min squared if no bundle), = sum
        (Z^2*x_z) where x_z is the relative concentration of a given
        charge state in the bundle, i.e. sum(x_z) = 1 over the bundle.
    :ivar ionisation_potential: Cumulative and average ionisation
        potential to reach a given bundle. Defined as sum (x_z* (sum of
        Epot from z'=0 to z-1)), where Epot is the ionisation potential
        of ion Xz’+, and x_z is the relative concentration of a given
        charge state in the bundle, i.e. sum(x_z) = 1 over the bundle.
    :ivar label: String identifying state (e.g. C+, C+2 , C+3, C+4, C+5,
        C+6, ...)
    :ivar electron_configuration: Configuration of atomic orbitals of
        this state, e.g. 1s2-2s1
    :ivar vibrational_level: Vibrational level (can be bundled)
    :ivar vibrational_mode: Vibrational mode of this state, e.g. "A_g".
        Need to define, or adopt a standard nomenclature.
    :ivar velocity: Velocity
    :ivar rotation_frequency_tor: Toroidal rotation frequency (i.e.
        toroidal velocity divided by the major radius at which the
        toroidal velocity is taken)
    :ivar temperature: Temperature
    :ivar density: Density (thermal+non-thermal)
    :ivar density_fit: Information on the fit used to obtain the density
        profile
    :ivar density_thermal: Density of thermal particles
    :ivar density_fast: Density of fast (non-thermal) particles
    :ivar pressure: Pressure (thermal+non-thermal)
    :ivar pressure_thermal: Pressure (thermal) associated with random
        motion ~average((v-average(v))^2)
    :ivar pressure_fast_perpendicular: Fast (non-thermal) perpendicular
        pressure
    :ivar pressure_fast_parallel: Fast (non-thermal) parallel pressure
    """

    class Meta:
        name = "core_profiles_ions_charge_states2"

    z_min: float = field(default=9e40)
    z_max: float = field(default=9e40)
    z_average: float = field(default=9e40)
    z_square_average: float = field(default=9e40)
    z_average_1d: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    z_average_square_1d: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    ionisation_potential: float = field(default=9e40)
    label: str = field(default="")
    electron_configuration: str = field(default="")
    vibrational_level: float = field(default=9e40)
    vibrational_mode: str = field(default="")
    velocity: Optional[CoreProfilesVectorComponents3] = field(default=None)
    rotation_frequency_tor: ndarray[(int,), float] = field(
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
    density: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    density_fit: Optional[CoreProfiles1DFit] = field(default=None)
    density_thermal: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    density_fast: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    pressure: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    pressure_thermal: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    pressure_fast_perpendicular: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    pressure_fast_parallel: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )


@idspy_dataclass(repr=False, slots=True)
class CoreProfilesProfiles1DElectrons(IdsBaseClass):
    """
    Quantities related to electrons.

    :ivar temperature: Temperature
    :ivar temperature_validity: Indicator of the validity of the
        temperature profile. 0: valid from automated processing, 1:
        valid and certified by the RO; - 1 means problem identified in
        the data processing (request verification by the RO), -2:
        invalid data, should not be used
    :ivar temperature_fit: Information on the fit used to obtain the
        temperature profile
    :ivar density: Density (thermal+non-thermal)
    :ivar density_validity: Indicator of the validity of the density
        profile. 0: valid from automated processing, 1: valid and
        certified by the RO; - 1 means problem identified in the data
        processing (request verification by the RO), -2: invalid data,
        should not be used
    :ivar density_fit: Information on the fit used to obtain the density
        profile
    :ivar density_thermal: Density of thermal particles
    :ivar density_fast: Density of fast (non-thermal) particles
    :ivar pressure: Pressure (thermal+non-thermal)
    :ivar pressure_thermal: Pressure (thermal) associated with random
        motion ~average((v-average(v))^2)
    :ivar pressure_fast_perpendicular: Fast (non-thermal) perpendicular
        pressure
    :ivar pressure_fast_parallel: Fast (non-thermal) parallel pressure
    :ivar velocity_tor: Toroidal velocity
    :ivar velocity_pol: Poloidal velocity
    :ivar velocity: Velocity
    :ivar collisionality_norm: Collisionality normalised to the bounce
        frequency
    """

    class Meta:
        name = "core_profiles_profiles_1d_electrons"

    temperature: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    temperature_validity: int = field(default=999999999)
    temperature_fit: Optional[CoreProfiles1DFit] = field(default=None)
    density: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    density_validity: int = field(default=999999999)
    density_fit: Optional[CoreProfiles1DFit] = field(default=None)
    density_thermal: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    density_fast: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    pressure: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    pressure_thermal: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    pressure_fast_perpendicular: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    pressure_fast_parallel: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    velocity_tor: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    velocity_pol: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    velocity: Optional[CoreProfilesVectorComponents2] = field(default=None)
    collisionality_norm: ndarray[(int,), float] = field(
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
class CoreProfileIons(IdsBaseClass):
    """
    Quantities related to a given ion species.

    :ivar element: List of elements forming the atom or molecule
    :ivar z_ion: Ion charge (of the dominant ionisation state; lumped
        ions are allowed), volume averaged over plasma radius
    :ivar label: String identifying ion (e.g. H, D, T, He, C, D2, ...)
    :ivar neutral_index: Index of the corresponding neutral species in
        the ../../neutral array
    :ivar z_ion_1d: Average charge of the ion species (sum of states
        charge weighted by state density and divided by ion density)
    :ivar z_ion_square_1d: Average square charge of the ion species (sum
        of states square charge weighted by state density and divided by
        ion density)
    :ivar temperature: Temperature (average over charge states when
        multiple charge states are considered)
    :ivar temperature_validity: Indicator of the validity of the
        temperature profile. 0: valid from automated processing, 1:
        valid and certified by the RO; - 1 means problem identified in
        the data processing (request verification by the RO), -2:
        invalid data, should not be used
    :ivar temperature_fit: Information on the fit used to obtain the
        temperature profile
    :ivar density: Density (thermal+non-thermal) (sum over charge states
        when multiple charge states are considered)
    :ivar density_validity: Indicator of the validity of the density
        profile. 0: valid from automated processing, 1: valid and
        certified by the RO; - 1 means problem identified in the data
        processing (request verification by the RO), -2: invalid data,
        should not be used
    :ivar density_fit: Information on the fit used to obtain the density
        profile
    :ivar density_thermal: Density (thermal) (sum over charge states
        when multiple charge states are considered)
    :ivar density_fast: Density of fast (non-thermal) particles (sum
        over charge states when multiple charge states are considered)
    :ivar pressure: Pressure (thermal+non-thermal) (sum over charge
        states when multiple charge states are considered)
    :ivar pressure_thermal: Pressure (thermal) associated with random
        motion ~average((v-average(v))^2) (sum over charge states when
        multiple charge states are considered)
    :ivar pressure_fast_perpendicular: Fast (non-thermal) perpendicular
        pressure  (sum over charge states when multiple charge states
        are considered)
    :ivar pressure_fast_parallel: Fast (non-thermal) parallel pressure
        (sum over charge states when multiple charge states are
        considered)
    :ivar velocity_tor: Toroidal velocity (average over charge states
        when multiple charge states are considered)
    :ivar velocity_pol: Poloidal velocity (average over charge states
        when multiple charge states are considered)
    :ivar rotation_frequency_tor: Toroidal rotation frequency  (i.e.
        toroidal velocity divided by the major radius at which the
        toroidal velocity is taken) (average over charge states when
        multiple charge states are considered)
    :ivar velocity: Velocity (average over charge states when multiple
        charge states are considered) at the position of maximum major
        radius on every flux surface
    :ivar multiple_states_flag: Multiple states calculation flag :
        0-Only the 'ion' level is considered and the 'state' array of
        structure is empty; 1-Ion states are considered and are
        described in the 'state' array of structure
    :ivar state: Quantities related to the different states of the
        species (ionisation, energy, excitation, ...)
    """

    class Meta:
        name = "core_profile_ions"

    element: list[PlasmaCompositionNeutralElement] = field(
        default_factory=list
    )
    z_ion: float = field(default=9e40)
    label: str = field(default="")
    neutral_index: int = field(default=999999999)
    z_ion_1d: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    z_ion_square_1d: ndarray[(int,), float] = field(
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
    temperature_validity: int = field(default=999999999)
    temperature_fit: Optional[CoreProfiles1DFit] = field(default=None)
    density: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    density_validity: int = field(default=999999999)
    density_fit: Optional[CoreProfiles1DFit] = field(default=None)
    density_thermal: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    density_fast: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    pressure: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    pressure_thermal: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    pressure_fast_perpendicular: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    pressure_fast_parallel: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    velocity_tor: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    velocity_pol: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    rotation_frequency_tor: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    velocity: Optional[CoreProfilesVectorComponents2] = field(default=None)
    multiple_states_flag: int = field(default=999999999)
    state: list[CoreProfilesIonsChargeStates2] = field(default_factory=list)


@idspy_dataclass(repr=False, slots=True)
class CoreInstantChangesChangeProfiles(IdsBaseClass):
    """
    Instant_change terms for a given time slice.

    :ivar grid: Radial grid
    :ivar electrons: Change of electrons-related quantities
    :ivar t_i_average: change of average ion temperature
    :ivar momentum_tor: change of total toroidal momentum
    :ivar ion: changes related to the different ions species
    :ivar neutral: changes related to the different neutral species
    :ivar time: Time
    """

    class Meta:
        name = "core_instant_changes_change_profiles"

    grid: Optional[CoreRadialGrid] = field(default=None)
    electrons: Optional[CoreProfilesProfiles1DElectrons] = field(default=None)
    t_i_average: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    momentum_tor: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    ion: list[CoreProfileIons] = field(default_factory=list)
    neutral: list[CoreProfileNeutral] = field(default_factory=list)
    time: Optional[float] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class CoreProfilesProfiles1D(IdsBaseClass):
    """
    1D radial profiles for core and edge.

    :ivar grid: Radial grid
    :ivar electrons: Quantities related to the electrons
    :ivar ion: Quantities related to the different ion species, in the
        sense of isonuclear or isomolecular sequences. Ionisation states
        (or other types of states) must be differentiated at the state
        level below
    :ivar neutral: Quantities related to the different neutral species
    :ivar t_i_average: Ion temperature (averaged on charge states and
        ion species)
    :ivar t_i_average_fit: Information on the fit used to obtain the
        t_i_average profile
    :ivar n_i_total_over_n_e: Ratio of total ion density (sum over
        species and charge states) over electron density. (thermal+non-
        thermal)
    :ivar n_i_thermal_total: Total ion thermal density (sum over species
        and charge states)
    :ivar momentum_tor: Total plasma toroidal momentum, summed over ion
        species and electrons weighted by their density and major
        radius, i.e. sum_over_species(n*R*m*Vphi)
    :ivar zeff: Effective charge
    :ivar zeff_fit: Information on the fit used to obtain the zeff
        profile
    :ivar pressure_ion_total: Total (sum over ion species) thermal ion
        pressure
    :ivar pressure_thermal: Thermal pressure (electrons+ions)
    :ivar pressure_perpendicular: Total perpendicular pressure
        (electrons+ions, thermal+non-thermal)
    :ivar pressure_parallel: Total parallel pressure (electrons+ions,
        thermal+non-thermal)
    :ivar j_total: Total parallel current density = average(jtot.B) /
        B0, where B0 = Core_Profiles/Vacuum_Toroidal_Field/ B0
    :ivar current_parallel_inside: Parallel current driven inside the
        flux surface. Cumulative surface integral of j_total
    :ivar j_tor: Total toroidal current density = average(J_Tor/R) /
        average(1/R)
    :ivar j_ohmic: Ohmic parallel current density = average(J_Ohmic.B) /
        B0, where B0 = Core_Profiles/Vacuum_Toroidal_Field/ B0
    :ivar j_non_inductive: Non-inductive (includes bootstrap) parallel
        current density = average(jni.B) / B0, where B0 =
        Core_Profiles/Vacuum_Toroidal_Field/ B0
    :ivar j_bootstrap: Bootstrap current density =
        average(J_Bootstrap.B) / B0, where B0 =
        Core_Profiles/Vacuum_Toroidal_Field/ B0
    :ivar conductivity_parallel: Parallel conductivity
    :ivar e_field_parallel: Parallel electric field = average(E.B) / B0,
        where Core_Profiles/Vacuum_Toroidal_Field/ B0
    :ivar e_field: Electric field, averaged on the magnetic surface. E.g
        for the parallel component, average(E.B) / B0, using
        core_profiles/vacuum_toroidal_field/b0
    :ivar phi_potential: Electrostatic potential, averaged on the
        magnetic flux surface
    :ivar rotation_frequency_tor_sonic: Derivative of the flux surface
        averaged electrostatic potential with respect to the poloidal
        flux, multiplied by -1. This quantity is the toroidal angular
        rotation frequency due to the ExB drift, introduced in formula
        (43) of Hinton and Wong, Physics of Fluids 3082 (1985), also
        referred to as sonic flow in regimes in which the toroidal
        velocity is dominant over the poloidal velocity
    :ivar q: Safety factor (IMAS uses COCOS=11: only positive when
        toroidal current and magnetic field are in same direction)
    :ivar magnetic_shear: Magnetic shear, defined as rho_tor/q .
        dq/drho_tor
    :ivar time: Time
    """

    class Meta:
        name = "core_profiles_profiles_1d"

    grid: Optional[CoreRadialGrid] = field(default=None)
    electrons: Optional[CoreProfilesProfiles1DElectrons] = field(default=None)
    ion: list[CoreProfileIons] = field(default_factory=list)
    neutral: list[CoreProfileNeutral] = field(default_factory=list)
    t_i_average: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    t_i_average_fit: Optional[CoreProfiles1DFit] = field(default=None)
    n_i_total_over_n_e: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    n_i_thermal_total: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    momentum_tor: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    zeff: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    zeff_fit: Optional[CoreProfiles1DFit] = field(default=None)
    pressure_ion_total: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    pressure_thermal: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    pressure_perpendicular: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    pressure_parallel: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    j_total: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    current_parallel_inside: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    j_tor: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    j_ohmic: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    j_non_inductive: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    j_bootstrap: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    conductivity_parallel: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    e_field_parallel: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    e_field: Optional[CoreProfilesVectorComponents1] = field(default=None)
    phi_potential: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    rotation_frequency_tor_sonic: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    q: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    magnetic_shear: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    time: Optional[float] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class CoreInstantChangesChange(IdsBaseClass):
    """
    Instant_change terms for a given instant_change.

    :ivar identifier: Instant change term identifier
    :ivar profiles_1d: Changes in 1D core profiles for various time
        slices. This structure mirrors core_profiles/profiles_1d and
        describes instant changes to each of these physical quantities
        (i.e. a signed difference quantity after change - quantity
        before change)
    """

    class Meta:
        name = "core_instant_changes_change"

    identifier: Optional[Identifier] = field(default=None)
    profiles_1d: list[CoreProfilesProfiles1D] = field(default_factory=list)


@idspy_dataclass(repr=False, slots=True)
class CoreInstantChanges(IdsBaseClass):
    """
    Instant changes of the radial core plasma profiles due to pellet, MHD, ...

    :ivar ids_properties:
    :ivar vacuum_toroidal_field: Characteristics of the vacuum toroidal
        field (used in Rho_Tor definition and in the normalization of
        current densities)
    :ivar change: Set of instant change terms (each being due to a
        different phenomenon)
    :ivar code:
    :ivar time:
    """

    class Meta:
        name = "core_instant_changes"

    ids_properties: Optional[IdsProperties] = field(default=None)
    vacuum_toroidal_field: Optional[BTorVacuum1] = field(default=None)
    change: list[CoreInstantChangesChange] = field(
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
