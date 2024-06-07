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
class Rzphi1DDynamicAos1CommonTime(IdsBaseClass):
    """
    Structure for R, Z, Phi positions (1D, dynamic within a type 1 array of
    structure and with a common time base at the same level)

    :ivar r: Major radius
    :ivar z: Height
    :ivar phi: Toroidal angle
    :ivar time: Time for the R,Z,phi coordinates
    """

    class Meta:
        name = "rzphi1d_dynamic_aos1_common_time"

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
    time: ndarray[(int,), float] = field(
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
class SpectroUvChannelWavelengthCalibration(IdsBaseClass):
    """
    Wavelength calibration.

    :ivar offset: Offset
    :ivar gain: Gain
    """

    class Meta:
        name = "spectro_uv_channel_wavelength_calibration"

    offset: float = field(default=9e40)
    gain: float = field(default=9e40)


@idspy_dataclass(repr=False, slots=True)
class SpectroUvDetector(IdsBaseClass):
    """
    Characteristics of the detector.

    :ivar pixel_dimensions: Pixel dimension in each direction
        (horizontal, vertical)
    :ivar pixel_n: Number of pixels in each direction (horizontal,
        vertical)
    :ivar detector_dimensions: Total detector dimension in each
        direction (horizontal, vertical)
    """

    class Meta:
        name = "spectro_uv_detector"

    pixel_dimensions: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    pixel_n: ndarray[(int,), int] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    detector_dimensions: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )


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
class LineOfSight2PointsDynamicAos1(IdsBaseClass):
    """
    Generic description of a line of sight, defined by two points, dynamic within
    an AoS1 (1st point fixed, 2nd point is dynamic)

    :ivar first_point: Position of the first point
    :ivar second_point: Position of the second point (possibly dynamic)
    :ivar moving_mode: Moving mode of the line of sight. Index = 0 : no
        movement, fixed position. Index = 1 : oscillating
    :ivar position_parameter: In case of line of sight moving during a
        pulse, position parameter allowing to record and compute the
        line of sight position as a function of time
    :ivar amplitude_parameter: Amplitude of the line of sight position
        parameter oscillation (in case moving_mode/index = 1)
    :ivar period: Period of the line of sight oscillation (in case
        moving_mode/index = 1)
    """

    class Meta:
        name = "line_of_sight_2points_dynamic_aos1"

    first_point: Optional[Rzphi0DStatic] = field(default=None)
    second_point: Optional[Rzphi1DDynamicAos1CommonTime] = field(default=None)
    moving_mode: Optional[Identifier] = field(default=None)
    position_parameter: Optional[SignalFlt1D] = field(default=None)
    amplitude_parameter: float = field(default=9e40)
    period: float = field(default=9e40)


@idspy_dataclass(repr=False, slots=True)
class SpectroUvChannelGratingImage(IdsBaseClass):
    """
    Grating image_field.

    :ivar geometry_type: Surface geometry. Index = 1 : spherical. Index
        = 2 : plane
    :ivar centre: Centre of the image surface in case it is spherical,
        or position of a point on the surface in case it is a plane
    :ivar curvature_radius: Curvature radius of the image surface
    :ivar x3_unit_vector: Components of the X3 direction unit vector in
        the (X,Y,Z) coordinate system, where X is the major radius axis
        for phi = 0, Y is the major radius axis for phi = pi/2, and Z is
        the height axis. The X3 axis is normal to the surface ( in case
        it is plane) and oriented towards the plasma.
    """

    class Meta:
        name = "spectro_uv_channel_grating_image"

    geometry_type: Optional[IdentifierStatic] = field(default=None)
    centre: Optional[Rzphi0DStatic] = field(default=None)
    curvature_radius: float = field(default=9e40)
    x3_unit_vector: Optional[Xyz0DStatic] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class SpectroUvChannelProcessedLine(IdsBaseClass):
    """
    Description of a processed line.

    :ivar label: String identifying the processed line. To avoid
        ambiguities, the following syntax is used : element with
        ionization state_wavelength in Angstrom (e.g. WI_4000)
    :ivar wavelength_central: Central wavelength of the processed line
    :ivar radiance: Calibrated, background subtracted radiance
        (integrated over the spectrum for this line)
    :ivar intensity: Non-calibrated intensity (integrated over the
        spectrum for this line)
    """

    class Meta:
        name = "spectro_uv_channel_processed_line"

    label: str = field(default="")
    wavelength_central: float = field(default=9e40)
    radiance: Optional[SignalFlt1D] = field(default=None)
    intensity: Optional[SignalFlt1D] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class SpectroUvSupply(IdsBaseClass):
    """
    Power supply.

    :ivar object_value: Name of the object connected to the power supply
    :ivar voltage_set: Voltage set at the power supply
    """

    class Meta:
        name = "spectro_uv_supply"

    object_value: str = field(default="")
    voltage_set: Optional[SignalFlt1D] = field(default=None)


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
class SpectroUvChannelGrating(IdsBaseClass):
    """
    Grating description.

    :ivar type_value: Grating type. Index = 1 : ruled. Index = 2 :
        holographic
    :ivar groove_density: Number of grooves per unit length
    :ivar geometry_type: Grating geometry. Index = 1 : spherical. Index
        = 2 : toric
    :ivar centre: Centre of the grating sphere (if grating is spherical)
        or torus (if grating is toric)
    :ivar curvature_radius: Curvature radius of the spherical grating
    :ivar summit: Position of the grating summit (defined as the point
        of contact of its concave side if the grating were put on a
        table). Used as the origin of the x1, x2, x3 vectors defined
        below
    :ivar x1_unit_vector: Components of the X1 direction unit vector in
        the (X,Y,Z) coordinate system, where X is the major radius axis
        for phi = 0, Y is the major radius axis for phi = pi/2, and Z is
        the height axis. The X1 vector is horizontal and oriented in the
        positive phi direction (counter-clockwise when viewing from
        above).
    :ivar x2_unit_vector: Components of the X2 direction unit vector in
        the (X,Y,Z) coordinate system, where X is the major radius axis
        for phi = 0, Y is the major radius axis for phi = pi/2, and Z is
        the height axis. The X2 axis is orthonormal so that uX2 = uX3 x
        uX1.
    :ivar x3_unit_vector: Components of the X3 direction unit vector in
        the (X,Y,Z) coordinate system, where X is the major radius axis
        for phi = 0, Y is the major radius axis for phi = pi/2, and Z is
        the height axis. The X3 axis is normal to the grating at its
        summit and oriented towards the plasma.
    :ivar outline: List of the 4 extreme points of the spherical grating
        in the (X1, X2) coordinate system, using the summit as the
        origin. Do NOT repeat the first point.
    :ivar image_field: Surface on which the grating image is focused
    """

    class Meta:
        name = "spectro_uv_channel_grating"

    type_value: Optional[IdentifierStatic] = field(default=None)
    groove_density: float = field(default=9e40)
    geometry_type: Optional[IdentifierStatic] = field(default=None)
    centre: Optional[Rzphi0DStatic] = field(default=None)
    curvature_radius: float = field(default=9e40)
    summit: Optional[Rzphi0DStatic] = field(default=None)
    x1_unit_vector: Optional[Xyz0DStatic] = field(default=None)
    x2_unit_vector: Optional[Xyz0DStatic] = field(default=None)
    x3_unit_vector: Optional[Xyz0DStatic] = field(default=None)
    outline: Optional[X1X21DStatic] = field(default=None)
    image_field: Optional[SpectroUvChannelGratingImage] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class SpectroUvChannel(IdsBaseClass):
    """
    Charge exchange channel.

    :ivar name: Name of the channel
    :ivar detector_layout: Dimensions of pixels and detector
    :ivar detector: Description of the front face of the micro channel
        plate
    :ivar detector_position_parameter: In case of detector moving during
        a pulse, position parameter allowing to record and compute the
        detector position as a function of time
    :ivar aperture: Description of a set of collimating apertures
    :ivar line_of_sight: Description of the line of sight of the
        channel, given by 2 points. The 2nd point is allowed to evolve
        in case of dynamic line of sight.
    :ivar supply_high_voltage: Set of high voltage power supplies
        applied to various parts of the diagnostic
    :ivar grating: Description of the grating
    :ivar wavelengths: Measured wavelengths
    :ivar radiance_spectral: Calibrated spectral radiance (radiance per
        unit wavelength)
    :ivar intensity_spectrum: Intensity spectrum (not calibrated), i.e.
        number of photoelectrons detected by unit time by a wavelength
        pixel of the channel, taking into account electronic gain
        compensation and channels relative calibration
    :ivar exposure_time: Exposure time
    :ivar processed_line: Set of processed spectral lines
    :ivar radiance_calibration: Radiance calibration
    :ivar radiance_calibration_date: Date of the radiance calibration
        (yyyy_mm_dd)
    :ivar wavelength_calibration: Wavelength calibration data. The
        wavelength is obtained from the pixel index k by: wavelength =
        k * gain + offset. k is starting from 1.
    :ivar wavelength_calibration_date: Date of the wavelength
        calibration (yyyy_mm_dd)
    :ivar validity_timed: Indicator of the validity of the data for each
        wavelength and each time slice. 0: valid from automated
        processing, 1: valid and certified by the diagnostic RO; - 1
        means problem identified in the data processing (request
        verification by the diagnostic RO), -2: invalid data, should not
        be used (values lower than -2 have a code-specific meaning
        detailing the origin of their invalidity)
    :ivar validity: Indicator of the validity of the data for the whole
        acquisition period. 0: valid from automated processing, 1: valid
        and certified by the diagnostic RO; - 1 means problem identified
        in the data processing (request verification by the diagnostic
        RO), -2: invalid data, should not be used (values lower than -2
        have a code-specific meaning detailing the origin of their
        invalidity)
    """

    class Meta:
        name = "spectro_uv_channel"

    name: str = field(default="")
    detector_layout: Optional[SpectroUvDetector] = field(default=None)
    detector: Optional[DetectorAperture] = field(default=None)
    detector_position_parameter: Optional[SignalFlt1D] = field(default=None)
    aperture: list[DetectorAperture] = field(
        default_factory=list,
        metadata={
            "max_occurs": 5,
        },
    )
    line_of_sight: Optional[LineOfSight2PointsDynamicAos1] = field(
        default=None
    )
    supply_high_voltage: list[SpectroUvSupply] = field(
        default_factory=list,
        metadata={
            "max_occurs": 2,
        },
    )
    grating: Optional[SpectroUvChannelGrating] = field(default=None)
    wavelengths: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    radiance_spectral: Optional[SignalFlt2D] = field(default=None)
    intensity_spectrum: Optional[SignalFlt2D] = field(default=None)
    exposure_time: float = field(default=9e40)
    processed_line: list[SpectroUvChannelProcessedLine] = field(
        default_factory=list,
        metadata={
            "max_occurs": 20,
        },
    )
    radiance_calibration: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    radiance_calibration_date: str = field(default="")
    wavelength_calibration: Optional[SpectroUvChannelWavelengthCalibration] = (
        field(default=None)
    )
    wavelength_calibration_date: str = field(default="")
    validity_timed: Optional[SignalInt2D] = field(default=None)
    validity: int = field(default=999999999)


@idspy_dataclass(repr=False, slots=True)
class SpectrometerUv(IdsBaseClass):
    """
    Spectrometer in uv light range diagnostic.

    :ivar ids_properties:
    :ivar etendue: Etendue (geometric extent) of the optical system
    :ivar etendue_method: Method used to calculate the etendue. Index =
        0 : exact calculation with a 4D integral; 1 : approximation with
        first order formula (detector surface times solid angle
        subtended by the apertures); 2 : other methods
    :ivar channel: Set of channels (detector or pixel of a camera)
    :ivar latency: Upper bound of the delay between physical information
        received by the detector and data available on the real-time
        (RT) network.
    :ivar code:
    :ivar time:
    """

    class Meta:
        name = "spectrometer_uv"

    ids_properties: Optional[IdsProperties] = field(default=None)
    etendue: float = field(default=9e40)
    etendue_method: Optional[IdentifierStatic] = field(default=None)
    channel: list[SpectroUvChannel] = field(
        default_factory=list,
        metadata={
            "max_occurs": 10,
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
