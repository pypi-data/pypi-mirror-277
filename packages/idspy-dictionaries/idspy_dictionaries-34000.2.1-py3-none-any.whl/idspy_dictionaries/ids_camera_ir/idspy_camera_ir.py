# __version__= "034000.2.0"
# __version_imas_dd__= "03.40.00"
# __imas_dd_git_commit__= "845f1b30816f86a3cd4d53714dc56cdd307fdca1"
#
from ..dataclasses_idsschema import idspy_dataclass,IdsBaseClass
from dataclasses import dataclass, field
from numpy import ndarray
from typing import Optional


@idspy_dataclass(repr=False, slots=True)
class CameraIrCalibration(IdsBaseClass):
    """
    Calibration data.

    :ivar luminance_to_temperature: Luminance to temperature conversion
        table
    :ivar transmission_barrel: Transmission of the optical barrel
    :ivar transmission_mirror: Transmission of the mirror
    :ivar transmission_window: Transmission of the window
    :ivar optical_temperature: Temperature of the optical components
        (digital levels)
    """

    class Meta:
        name = "camera_ir_calibration"

    luminance_to_temperature: ndarray[(int, int), int] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    transmission_barrel: ndarray[(int, int), int] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    transmission_mirror: ndarray[(int, int), int] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    transmission_window: ndarray[(int, int), int] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    optical_temperature: ndarray[(int, int), int] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )


@idspy_dataclass(repr=False, slots=True)
class CameraIrFrame(IdsBaseClass):
    """
    Frame of a camera.

    :ivar surface_temperature: Surface temperature image. First
        dimension : line index (horizontal axis). Second dimension:
        column index (vertical axis). The size of this matrix is assumed
        to be constant over time
    :ivar time: Time
    """

    class Meta:
        name = "camera_ir_frame"

    surface_temperature: ndarray[(int, int), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    time: Optional[float] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class CameraIrFrameAnalysis(IdsBaseClass):
    """
    Frame analysis.

    :ivar sol_heat_decay_length: Heat flux decay length in SOL at
        divertor entrance, mapped to the mid-plane, this is the lambda_q
        parameter defined in reference T. Eich et al, Nucl. Fusion 53
        (2013) 093031
    :ivar distance_separatrix_midplane: Distance between the measurement
        position and the separatrix, mapped along flux surfaces to the
        outboard midplane, in the major radius direction. Positive value
        means the measurement is outside of the separatrix.
    :ivar power_flux_parallel: Parallel heat flux received by the
        element monitored by the camera, along the
        distance_separatrix_midplane coordinate
    :ivar time: Time
    """

    class Meta:
        name = "camera_ir_frame_analysis"

    sol_heat_decay_length: float = field(default=9e40)
    distance_separatrix_midplane: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    power_flux_parallel: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    time: Optional[float] = field(default=None)


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
class CurvedSurface(IdsBaseClass):
    """
    Curvature of a surface.

    :ivar curvature_type: Curvature of the surface
    :ivar x1_curvature: Radius of curvature in the X1 direction, to be
        filled only for curvature_type/index = 2, 4 or 5
    :ivar x2_curvature: Radius of curvature in the X2 direction, to be
        filled only for curvature_type/index = 3 or 5
    """

    class Meta:
        name = "curved_surface"

    curvature_type: Optional[IdentifierStatic] = field(default=None)
    x1_curvature: float = field(default=9e40)
    x2_curvature: float = field(default=9e40)


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
class OpticalElementMaterial(IdsBaseClass):
    """
    Material of an optical element of a camera.

    :ivar type_value: Type of optical element material. In case of
        'metal' refractive_index and extinction_coefficient are used. In
        case of 'dielectric' refractive_index and
        transmission_coefficient are used.
    :ivar wavelengths: Wavelengths array for refractive_index,
        extinction_coefficient and transmission_coefficient
    :ivar refractive_index: Refractive index (for metal and dielectric)
    :ivar extinction_coefficient: Extinction coefficient (for metal)
    :ivar transmission_coefficient: Transmission coefficient (for
        dielectric)
    :ivar roughness: Roughness parameter of the material. Varies in
        range [0, 1]. 0 is perfectly specular, 1 is perfectly rough
    """

    class Meta:
        name = "optical_element_material"

    type_value: Optional[IdentifierStatic] = field(default=None)
    wavelengths: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    refractive_index: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    extinction_coefficient: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    transmission_coefficient: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
    roughness: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )


@idspy_dataclass(repr=False, slots=True)
class FibreBundle(IdsBaseClass):
    """
    Fibre bundle.

    :ivar geometry: Geometry of the fibre bundle entrance
    :ivar fibre_radius: Radius of a single fibre
    :ivar fibre_positions: Individual fibres centres positions in the
        (X1, X2) coordinate system
    """

    class Meta:
        name = "fibre_bundle"

    geometry: Optional[DetectorAperture] = field(default=None)
    fibre_radius: float = field(default=9e40)
    fibre_positions: Optional[X1X21DStatic] = field(default=None)


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
class OpticalElement(IdsBaseClass):
    """
    Optical element of a camera.

    :ivar type_value: Type of optical element. In case of 'mirror' and
        'diaphragm', the element is described by one 'front_surface'. In
        case of 'lens', the element is described by 'front_surface' and
        'back_surface'.
    :ivar front_surface: Curvature of the front surface
    :ivar back_surface: Curvature of the front surface
    :ivar thickness: Distance between front_surface and back_surface
        along the X3 vector
    :ivar material_properties: Material properties of the optical
        element
    :ivar geometry: Further geometrical description of the element
    """

    class Meta:
        name = "optical_element"

    type_value: Optional[IdentifierStatic] = field(default=None)
    front_surface: Optional[CurvedSurface] = field(default=None)
    back_surface: Optional[CurvedSurface] = field(default=None)
    thickness: float = field(default=9e40)
    material_properties: Optional[OpticalElementMaterial] = field(default=None)
    geometry: Optional[DetectorAperture] = field(default=None)


@idspy_dataclass(repr=False, slots=True)
class CameraIr(IdsBaseClass):
    """
    Infrared camera for monitoring of Plasma Facing Components.

    :ivar ids_properties:
    :ivar name: Name of the camera
    :ivar calibration: Calibration data
    :ivar frame: Set of frames
    :ivar midplane: Choice of midplane definition for the mapping of
        measurements on an equilibrium
    :ivar frame_analysis: Quantities deduced from frame analysis for a
        set of time slices
    :ivar optical_element: Set of optical elements
    :ivar fibre_bundle: Description of the fibre bundle
    :ivar latency: Upper bound of the delay between physical information
        received by the detector and data available on the real-time
        (RT) network.
    :ivar code:
    :ivar time:
    """

    class Meta:
        name = "camera_ir"

    ids_properties: Optional[IdsProperties] = field(default=None)
    name: str = field(default="")
    calibration: Optional[CameraIrCalibration] = field(default=None)
    frame: list[CameraIrFrame] = field(default_factory=list)
    midplane: Optional[IdentifierStatic] = field(default=None)
    frame_analysis: list[CameraIrFrameAnalysis] = field(default_factory=list)
    optical_element: list[OpticalElement] = field(
        default_factory=list,
        metadata={
            "max_occurs": 10,
        },
    )
    fibre_bundle: Optional[FibreBundle] = field(default=None)
    latency: float = field(default=9e40)
    code: Optional[Code] = field(default=None)
    time: ndarray[(int,), float] = field(
        default_factory=list,
        metadata={
            "max_occurs": 999,
        },
    )
