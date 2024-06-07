# __version__= "034000.2.0"
# __version_imas_dd__= "03.40.00"
# __imas_dd_git_commit__= "845f1b30816f86a3cd4d53714dc56cdd307fdca1"
#
from ..dataclasses_idsschema import idspy_dataclass,IdsBaseClass
from dataclasses import dataclass, field
from numpy import ndarray
from typing import Optional


@idspy_dataclass(repr=False, slots=True)
class DetectorEnergyBand(IdsBaseClass):
    """
    Detector energy band.

    :ivar lower_bound: Lower bound of the energy band
    :ivar upper_bound: Upper bound of the energy band
    :ivar energies: Array of discrete energy values inside the band
    :ivar detection_efficiency: Probability of detection of a photon
        impacting the detector as a function of its energy
    """

    class Meta:
        name = "detector_energy_band"

    lower_bound: float = field(default=9e40)
    upper_bound: float = field(default=9e40)
    energies: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    detection_efficiency: ndarray[(int,), float] = field(
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
class NeutronDiagnosticAdc(IdsBaseClass):
    """
    ADC.

    :ivar power_switch: Power switch (1=on, 0=off)
    :ivar discriminator_level_lower: Lower level discriminator of ADC
    :ivar discriminator_level_upper: Upper level discriminator of ADC
    :ivar sampling_rate: Number of samples recorded per second
    :ivar bias: ADC signal bias
    :ivar input_range: ADC input range
    :ivar impedance: ADC impedance
    """

    class Meta:
        name = "neutron_diagnostic_adc"

    power_switch: int = field(default=999999999)
    discriminator_level_lower: int = field(default=999999999)
    discriminator_level_upper: int = field(default=999999999)
    sampling_rate: int = field(default=999999999)
    bias: float = field(default=9e40)
    input_range: float = field(default=9e40)
    impedance: float = field(default=9e40)


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
class Rzphi1DGrid(IdsBaseClass):
    """
    R, Z, Phi structured grid, in which R, Z and phi don't necessarily have the
    same number of elements.

    :ivar r: Major radius
    :ivar z: Height
    :ivar phi: Toroidal angle (oriented counter-clockwise when viewing
        from above)
    """

    class Meta:
        name = "rzphi1d_grid"

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
    phi: ndarray[(int,), float] = field(
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
class X1X21DStatic(IdsBaseClass):
    """
    Structure for list of X1, X2 positions (1D, static)

    :ivar x1: Positions along x1 axis
    :ivar x2: Positions along x2 axis
    """

    class Meta:
        name = "x1x21d_static"

    x1: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    x2: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )


@idspy_dataclass(repr=False, slots=True)
class Xyz0DStatic(IdsBaseClass):
    """
    Structure for list of X, Y, Z components (0D, static)

    :ivar x: Component along X axis
    :ivar y: Component along Y axis
    :ivar z: Component along Z axis
    """

    class Meta:
        name = "xyz0d_static"

    x: float = field(default=9e40)
    y: float = field(default=9e40)
    z: float = field(default=9e40)


@idspy_dataclass(repr=False, slots=True)
class Xyz3DStatic(IdsBaseClass):
    """
    Structure for list of X, Y, Z components (3D, static), one set of X,Y,Z
    components being given for each voxel of the emission grid.

    :ivar x: Components along X axis for each voxel
    :ivar y: Component along Y axis  for each voxel
    :ivar z: Component along Z axis  for each voxel
    """

    class Meta:
        name = "xyz3d_static"

    x: ndarray[(int, int, int), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    y: ndarray[(int, int, int), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    z: ndarray[(int, int, int), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )


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
class DetectorAperture(IdsBaseClass):
    """
    Generic description of a plane detector or collimating aperture.

    :ivar geometry_type: Type of geometry used to describe the surface
        of the detector or aperture (1:'outline', 2:'circular',
        3:'rectangle'). In case of 'outline', the surface is described
        by an outline of point in a local coordinate system defined by a
        centre and three unit vectors X1, X2, X3. Note that there is
        some flexibility here and the data provider should choose the
        most convenient coordinate system for the object, respecting the
        definitions of (X1,X2,X3) indicated below. In case of
        'circular', the surface is a circle defined by its centre,
        radius, and normal vector oriented towards the plasma X3.  In
        case of 'rectangle', the surface is a rectangle defined by its
        centre, widths in the X1 and X2 directions, and normal vector
        oriented towards the plasma X3.
    :ivar centre: If geometry_type=2, coordinates of the centre of the
        circle. If geometry_type=1 or 3, coordinates of the origin of
        the local coordinate system (X1,X2,X3) describing the plane
        detector/aperture. This origin is located within the
        detector/aperture area.
    :ivar radius: Radius of the circle, used only if geometry_type = 2
    :ivar x1_unit_vector: Components of the X1 direction unit vector in
        the (X,Y,Z) coordinate system, where X is the major radius axis
        for phi = 0, Y is the major radius axis for phi = pi/2, and Z is
        the height axis. The X1 vector is more horizontal than X2 (has a
        smaller abs(Z) component) and oriented in the positive phi
        direction (counter-clockwise when viewing from above).
    :ivar x2_unit_vector: Components of the X2 direction unit vector in
        the (X,Y,Z) coordinate system, where X is the major radius axis
        for phi = 0, Y is the major radius axis for phi = pi/2, and Z is
        the height axis. The X2 axis is orthonormal so that uX2 = uX3 x
        uX1.
    :ivar x3_unit_vector: Components of the X3 direction unit vector in
        the (X,Y,Z) coordinate system, where X is the major radius axis
        for phi = 0, Y is the major radius axis for phi = pi/2, and Z is
        the height axis. The X3 axis is normal to the detector/aperture
        plane and oriented towards the plasma.
    :ivar x1_width: Full width of the aperture in the X1 direction, used
        only if geometry_type = 3
    :ivar x2_width: Full width of the aperture in the X2 direction, used
        only if geometry_type = 3
    :ivar outline: Irregular outline of the detector/aperture in the
        (X1, X2) coordinate system. Do NOT repeat the first point.
    :ivar surface: Surface of the detector/aperture, derived from the
        above geometric data
    """

    class Meta:
        name = "detector_aperture"

    geometry_type: int = field(default=999999999)
    centre: Optional[Rzphi0DStatic] = field(default=None)
    radius: float = field(default=9e40)
    x1_unit_vector: Optional[Xyz0DStatic] = field(default=None)
    x2_unit_vector: Optional[Xyz0DStatic] = field(default=None)
    x3_unit_vector: Optional[Xyz0DStatic] = field(default=None)
    x1_width: float = field(default=9e40)
    x2_width: float = field(default=9e40)
    outline: Optional[X1X21DStatic] = field(default=None)
    surface: float = field(default=9e40)


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
class NeutronDiagnosticBFieldSensor(IdsBaseClass):
    """
    Magnetic field sensor.

    :ivar power_switch: Power switch (1=on, 0=off)
    :ivar b_field: Magnetic field measured by the sensor
    """

    class Meta:
        name = "neutron_diagnostic_b_field_sensor"

    power_switch: int = field(default=999999999)
    b_field: Optional[SignalFlt1D] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class NeutronDiagnosticDetectorMode(IdsBaseClass):
    """
    :ivar identifier: Identifier of the measuring mode
    :ivar counting: Detected counts per second as a function of time
    :ivar count_limit_max: Maximum count limit under which the detector
        response is linear
    :ivar count_limit_min: Minimum count limit above which the detector
        response is linear
    :ivar spectrum: Detected counts per second per energy channel as a
        function of time (in case of spectroscopic measurement mode)
    """

    class Meta:
        name = "neutron_diagnostic_detector_mode"

    identifier: Optional[IdentifierStatic] = field(default=None)
    counting: Optional[SignalFlt1D] = field(default=None)
    count_limit_max: float = field(default=9e40)
    count_limit_min: float = field(default=9e40)
    spectrum: Optional[SignalFlt2D] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class NeutronDiagnosticEvent(IdsBaseClass):
    """
    Event in the detector.

    :ivar type_value: Type of the event
    :ivar values: Array of values for the event
    """

    class Meta:
        name = "neutron_diagnostic_event"

    type_value: Optional[IdentifierStatic] = field(default=None)
    values: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )


@idspy_dataclass(repr=False, slots=True)
class NeutronDiagnosticFieldOfView(IdsBaseClass):
    """
    Field of view.

    :ivar solid_angle: Average solid angle that the detector covers
        within the voxel
    :ivar emission_grid: Grid defining the neutron emission cells in the
        plasma
    :ivar direction_to_detector: Vector that points from the centre of
        the voxel to the centre of the detector, described in the
        (X,Y,Z) coordinate system, where X is the major radius axis for
        phi = 0, Y is the major radius axis for phi = pi/2, and Z is the
        height axis.
    """

    class Meta:
        name = "neutron_diagnostic_field_of_view"

    solid_angle: ndarray[(int, int, int), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    emission_grid: Optional[Rzphi1DGrid] = field(default=None)
    direction_to_detector: Optional[Xyz3DStatic] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class NeutronDiagnosticSupply(IdsBaseClass):
    """
    Power supply.

    :ivar power_switch: Power switch (1=on, 0=off)
    :ivar voltage_set: Voltage set
    :ivar voltage_out: Voltage at the supply output
    """

    class Meta:
        name = "neutron_diagnostic_supply"

    power_switch: int = field(default=999999999)
    voltage_set: Optional[SignalFlt1D] = field(default=None)
    voltage_out: Optional[SignalFlt1D] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class NeutronDiagnosticTemperatureSensor(IdsBaseClass):
    """
    Temperature sensor.

    :ivar power_switch: Power switch (1=on, 0=off)
    :ivar temperature: Temperature measured by the sensor
    """

    class Meta:
        name = "neutron_diagnostic_temperature_sensor"

    power_switch: int = field(default=999999999)
    temperature: Optional[SignalFlt1D] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class NeutronDiagnosticTestGenerator(IdsBaseClass):
    """
    Test generator.

    :ivar power_switch: Power switch (1=on, 0=off)
    :ivar shape: Signal shape. Index : 1 – rectangular, 2 – gaussian
    :ivar rise_time: Peak rise time
    :ivar fall_time: Peak fall time
    :ivar frequency: Generated signal frequency
    :ivar amplitude: Generated signal amplitude
    """

    class Meta:
        name = "neutron_diagnostic_test_generator"

    power_switch: int = field(default=999999999)
    shape: Optional[Identifier] = field(default=None)
    rise_time: float = field(default=9e40)
    fall_time: float = field(default=9e40)
    frequency: Optional[SignalFlt1D] = field(default=None)
    amplitude: Optional[SignalFlt1D] = field(default=None)


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
class NeutronDiagnosticGreen(IdsBaseClass):
    """
    Green functions.

    :ivar source_neutron_energies: Array of source neutron energy bins
    :ivar event_in_detector_neutron_flux: 5th dimension for the
        neutron_flux Green function representing values of events
        measured in the detector. The type of events monitored depends
        on the detector and can be defined by the user. It can be energy
        of neutrons, or electrical signal, or time of flight ...
        (defined by type below)
    :ivar neutron_flux_integrated_flags: Array of flags telling, for
        each coordinate of the neutron_flux, whether the neutron_flux
        has been integrated over this coordinate (1) or not (0). If it
        has been integrated over a coordinate, the size related to this
        coordinate must be equal to 1
    :ivar neutron_flux: Grouped neutron flux in the detector from one
        neutron energy bin emitted by the current plasma voxel towards
        the detector
    :ivar event_in_detector_response_function: 5th dimension for the
        response_function Green function representing values of events
        measured in the detector. The type of events monitored depends
        on the detector and can be defined by the user. It can be energy
        of neutrons, or electrical signal, or time of flight ...
        (defined by type below)
    :ivar response_function_integrated_flags: Array of flags telling,
        for each coordinate of the response_function, whether the
        response_function has been integrated over this coordinate (1)
        or not (0). If it has been integrated over a coordinate, the
        size related to this coordinate must be equal to 1
    :ivar response_function: Number of events occurring in the detector
        from one neutron energy bin emitted by the current plasma voxel
        towards the detector
    """

    class Meta:
        name = "neutron_diagnostic_green"

    source_neutron_energies: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    event_in_detector_neutron_flux: Optional[NeutronDiagnosticEvent] = field(
        default=None
    )
    neutron_flux_integrated_flags: ndarray[(int,), int] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    neutron_flux: ndarray[(int, int, int, int, int), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    event_in_detector_response_function: Optional[NeutronDiagnosticEvent] = (
        field(default=None)
    )
    response_function_integrated_flags: ndarray[(int,), int] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    response_function: ndarray[(int, int, int, int, int), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )


@idspy_dataclass(repr=False, slots=True)
class NeutronDiagnosticDetectors(IdsBaseClass):
    """
    :ivar name: Name of the detector
    :ivar geometry: Detector geometry
    :ivar material: Name of detector's converter for resent particle
    :ivar nuclei_n: Number of target nuclei in the dectector
    :ivar temperature: Temperature of the detector
    :ivar aperture: Description of a set of collimating apertures
    :ivar mode: Set of Measuring Modes simultaneously used by the
        detector
    :ivar energy_band: Set of energy bands in which neutrons are counted
        by the detector
    :ivar exposure_time: Exposure time
    :ivar adc: Description of analogic-digital converter
    :ivar supply_high_voltage: Description of high voltage power supply
    :ivar supply_low_voltage: Description of low voltage power supply
    :ivar test_generator: Test generator characteristics
    :ivar b_field_sensor: Magnetic field sensor
    :ivar temperature_sensor: Temperature sensor
    :ivar field_of_view: Field of view associated to this detector. The
        field of view is described by a voxelized plasma volume. Each
        voxel, with indexes i_R, i_Z, and i_phi, has an associated solid
        angle scalar and a detector direction vector.
    :ivar green_functions: Green function coefficients used to represent
        the detector response based on its field of view
    """

    class Meta:
        name = "neutron_diagnostic_detectors"

    name: str = field(default="")
    geometry: Optional[DetectorAperture] = field(default=None)
    material: Optional[IdentifierStatic] = field(default=None)
    nuclei_n: int = field(default=999999999)
    temperature: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    aperture: list[DetectorAperture] = field(
        default_factory=list,
        metadata={
            "max_occurs": 2,
        },
    )
    mode: list[NeutronDiagnosticDetectorMode] = field(
        default_factory=list,
        metadata={
            "max_occurs": 5,
        },
    )
    energy_band: list[DetectorEnergyBand] = field(
        default_factory=list,
        metadata={
            "max_occurs": 1000,
        },
    )
    exposure_time: float = field(default=9e40)
    adc: Optional[NeutronDiagnosticAdc] = field(default=None)
    supply_high_voltage: Optional[NeutronDiagnosticSupply] = field(
        default=None
    )
    supply_low_voltage: Optional[NeutronDiagnosticSupply] = field(default=None)
    test_generator: Optional[NeutronDiagnosticTestGenerator] = field(
        default=None
    )
    b_field_sensor: Optional[NeutronDiagnosticTestGenerator] = field(
        default=None
    )
    temperature_sensor: Optional[NeutronDiagnosticTestGenerator] = field(
        default=None
    )
    field_of_view: Optional[NeutronDiagnosticFieldOfView] = field(default=None)
    green_functions: Optional[NeutronDiagnosticGreen] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class NeutronDiagnostic(IdsBaseClass):
    """
    Neutron diagnostic.

    :ivar ids_properties:
    :ivar detector: Set of neutron detection systems
    :ivar neutron_flux_total: Total Neutron Flux reconstructed from the
        detectors signals
    :ivar fusion_power: Fusion power reconstructed from the detectors
        signals
    :ivar latency: Upper bound of the delay between physical information
        received by the detector and data available on the real-time
        (RT) network.
    :ivar code:
    :ivar time:
    """

    class Meta:
        name = "neutron_diagnostic"

    ids_properties: Optional[IdsProperties] = field(default=None)
    detector: list[NeutronDiagnosticDetectors] = field(
        default_factory=list,
        metadata={
            "max_occurs": 60,
        },
    )
    neutron_flux_total: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    fusion_power: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
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
