import typing
import collections.abc
import bpy.ops.transform
import bpy.types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    radius: typing.Any | None = 1.0,
    type: str | None = "EMPTY",
    enter_editmode: bool | typing.Any | None = False,
    align: str | None = "WORLD",
    location: typing.Any | None = (0.0, 0.0, 0.0),
    rotation: typing.Any | None = (0.0, 0.0, 0.0),
):
    """Add an object to the scene

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param radius: Radius
        :type radius: typing.Any | None
        :param type: Type
        :type type: str | None
        :param enter_editmode: Enter Editmode, Enter editmode when adding this object
        :type enter_editmode: bool | typing.Any | None
        :param align: Align, The alignment of the new object

    WORLD World, Align the new object to the world.

    VIEW View, Align the new object to the view.

    CURSOR 3D Cursor, Use the 3D cursor orientation for the new object.
        :type align: str | None
        :param location: Location, Location for the newly added object
        :type location: typing.Any | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: typing.Any | None
    """

    ...

def add_named(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    linked: bool | typing.Any | None = False,
    name: str | typing.Any = "",
):
    """Add named object

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param linked: Linked, Duplicate object but not object data, linking to the original data
    :type linked: bool | typing.Any | None
    :param name: Name, Object name to add
    :type name: str | typing.Any
    """

    ...

def align(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    bb_quality: bool | typing.Any | None = True,
    align_mode: str | None = "OPT_2",
    relative_to: str | None = "OPT_4",
    align_axis: set[str] | None = {},
):
    """Align Objects

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param bb_quality: High Quality, Enables high quality calculation of the bounding box for perfect results on complex shape meshes with rotation/scale (Slow)
        :type bb_quality: bool | typing.Any | None
        :param align_mode: Align Mode:, Side of object to use for alignment
        :type align_mode: str | None
        :param relative_to: Relative To:, Reference location to align to

    OPT_1 Scene Origin, Use the Scene Origin as the position for the selected objects to align to.

    OPT_2 3D Cursor, Use the 3D cursor as the position for the selected objects to align to.

    OPT_3 Selection, Use the selected objects as the position for the selected objects to align to.

    OPT_4 Active, Use the active object as the position for the selected objects to align to.
        :type relative_to: str | None
        :param align_axis: Align, Align to axis
        :type align_axis: set[str] | None
    """

    ...

def anim_transforms_to_deltas(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Convert object animation for normal transforms to delta transforms

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def armature_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    radius: typing.Any | None = 1.0,
    enter_editmode: bool | typing.Any | None = False,
    align: str | None = "WORLD",
    location: typing.Any | None = (0.0, 0.0, 0.0),
    rotation: typing.Any | None = (0.0, 0.0, 0.0),
):
    """Add an armature object to the scene

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param radius: Radius
        :type radius: typing.Any | None
        :param enter_editmode: Enter Editmode, Enter editmode when adding this object
        :type enter_editmode: bool | typing.Any | None
        :param align: Align, The alignment of the new object

    WORLD World, Align the new object to the world.

    VIEW View, Align the new object to the view.

    CURSOR 3D Cursor, Use the 3D cursor orientation for the new object.
        :type align: str | None
        :param location: Location, Location for the newly added object
        :type location: typing.Any | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: typing.Any | None
    """

    ...

def assign_property_defaults(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    process_data: bool | typing.Any | None = True,
    process_bones: bool | typing.Any | None = True,
):
    """Assign the current values of custom properties as their defaults, for use as part of the rest pose state in NLA track mixing

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param process_data: Process data properties
    :type process_data: bool | typing.Any | None
    :param process_bones: Process bone properties
    :type process_bones: bool | typing.Any | None
    """

    ...

def bake(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "COMBINED",
    pass_filter: set[str] | None = {},
    filepath: str | typing.Any = "",
    width: typing.Any | None = 512,
    height: typing.Any | None = 512,
    margin: typing.Any | None = 16,
    use_selected_to_active: bool | typing.Any | None = False,
    cage_extrusion: typing.Any | None = 0.0,
    cage_object: str | typing.Any = "",
    normal_space: str | None = "TANGENT",
    normal_r: str | None = "POS_X",
    normal_g: str | None = "POS_Y",
    normal_b: str | None = "POS_Z",
    save_mode: str | None = "INTERNAL",
    use_clear: bool | typing.Any | None = False,
    use_cage: bool | typing.Any | None = False,
    use_split_materials: bool | typing.Any | None = False,
    use_automatic_name: bool | typing.Any | None = False,
    uv_layer: str | typing.Any = "",
):
    """Bake image textures of selected objects

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type, Type of pass to bake, some of them may not be supported by the current render engine
        :type type: str | None
        :param pass_filter: Pass Filter, Filter to combined, diffuse, glossy, transmission and subsurface passes
        :type pass_filter: set[str] | None
        :param filepath: File Path, Image filepath to use when saving externally
        :type filepath: str | typing.Any
        :param width: Width, Horizontal dimension of the baking map (external only)
        :type width: typing.Any | None
        :param height: Height, Vertical dimension of the baking map (external only)
        :type height: typing.Any | None
        :param margin: Margin, Extends the baked result as a post process filter
        :type margin: typing.Any | None
        :param use_selected_to_active: Selected to Active, Bake shading on the surface of selected objects to the active object
        :type use_selected_to_active: bool | typing.Any | None
        :param cage_extrusion: Cage Extrusion, Distance to use for the inward ray cast when using selected to active
        :type cage_extrusion: typing.Any | None
        :param cage_object: Cage Object, Object to use as cage, instead of calculating the cage from the active object with cage extrusion
        :type cage_object: str | typing.Any
        :param normal_space: Normal Space, Choose normal space for baking

    OBJECT Object, Bake the normals in object space.

    TANGENT Tangent, Bake the normals in tangent space.
        :type normal_space: str | None
        :param normal_r: R, Axis to bake in red channel
        :type normal_r: str | None
        :param normal_g: G, Axis to bake in green channel
        :type normal_g: str | None
        :param normal_b: B, Axis to bake in blue channel
        :type normal_b: str | None
        :param save_mode: Save Mode, Choose how to save the baking map

    INTERNAL Internal, Save the baking map in an internal image data-block.

    EXTERNAL External, Save the baking map in an external file.
        :type save_mode: str | None
        :param use_clear: Clear, Clear Images before baking (only for internal saving)
        :type use_clear: bool | typing.Any | None
        :param use_cage: Cage, Cast rays to active object from a cage
        :type use_cage: bool | typing.Any | None
        :param use_split_materials: Split Materials, Split baked maps per material, using material name in output file (external only)
        :type use_split_materials: bool | typing.Any | None
        :param use_automatic_name: Automatic Name, Automatically name the output file with the pass type
        :type use_automatic_name: bool | typing.Any | None
        :param uv_layer: UV Layer, UV layer to override active
        :type uv_layer: str | typing.Any
    """

    ...

def bake_image(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Bake image textures of selected objects

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def camera_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    enter_editmode: bool | typing.Any | None = False,
    align: str | None = "WORLD",
    location: typing.Any | None = (0.0, 0.0, 0.0),
    rotation: typing.Any | None = (0.0, 0.0, 0.0),
):
    """Add a camera object to the scene

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param enter_editmode: Enter Editmode, Enter editmode when adding this object
        :type enter_editmode: bool | typing.Any | None
        :param align: Align, The alignment of the new object

    WORLD World, Align the new object to the world.

    VIEW View, Align the new object to the view.

    CURSOR 3D Cursor, Use the 3D cursor orientation for the new object.
        :type align: str | None
        :param location: Location, Location for the newly added object
        :type location: typing.Any | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: typing.Any | None
    """

    ...

def collection_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add an object to a new collection

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def collection_instance_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    name: str | typing.Any = "Collection",
    collection: str | None = "",
    align: str | None = "WORLD",
    location: typing.Any | None = (0.0, 0.0, 0.0),
    rotation: typing.Any | None = (0.0, 0.0, 0.0),
):
    """Add a collection instance

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param name: Name, Collection name to add
        :type name: str | typing.Any
        :param collection: Collection
        :type collection: str | None
        :param align: Align, The alignment of the new object

    WORLD World, Align the new object to the world.

    VIEW View, Align the new object to the view.

    CURSOR 3D Cursor, Use the 3D cursor orientation for the new object.
        :type align: str | None
        :param location: Location, Location for the newly added object
        :type location: typing.Any | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: typing.Any | None
    """

    ...

def collection_link(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    collection: str | None = "",
):
    """Add an object to an existing collection

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param collection: Collection
    :type collection: str | None
    """

    ...

def collection_objects_select(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select all objects in collection

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def collection_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove the active object from this collection

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def collection_unlink(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Unlink the collection from all objects

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def constraint_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "",
):
    """Add a constraint to the active object

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: str | None
    """

    ...

def constraint_add_with_targets(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "",
):
    """Add a constraint to the active object, with target (where applicable) set to the selected Objects/Bones

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: str | None
    """

    ...

def constraints_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Clear all the constraints for the active Object only

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def constraints_copy(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Copy constraints to other selected objects

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def convert(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    target: str | None = "MESH",
    keep_original: bool | typing.Any | None = False,
):
    """Convert selected objects to another type

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param target: Target, Type of object to convert to
    :type target: str | None
    :param keep_original: Keep Original, Keep original objects instead of replacing them
    :type keep_original: bool | typing.Any | None
    """

    ...

def correctivesmooth_bind(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    modifier: str | typing.Any = "",
):
    """Bind base pose in Corrective Smooth modifier

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str | typing.Any
    """

    ...

def data_transfer(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_reverse_transfer: bool | typing.Any | None = False,
    use_freeze: bool | typing.Any | None = False,
    data_type: str | None = "",
    use_create: bool | typing.Any | None = True,
    vert_mapping: str | None = "NEAREST",
    edge_mapping: str | None = "NEAREST",
    loop_mapping: str | None = "NEAREST_POLYNOR",
    poly_mapping: str | None = "NEAREST",
    use_auto_transform: bool | typing.Any | None = False,
    use_object_transform: bool | typing.Any | None = True,
    use_max_distance: bool | typing.Any | None = False,
    max_distance: typing.Any | None = 1.0,
    ray_radius: typing.Any | None = 0.0,
    islands_precision: typing.Any | None = 0.1,
    layers_select_src: str | None = "ACTIVE",
    layers_select_dst: str | None = "ACTIVE",
    mix_mode: str | None = "REPLACE",
    mix_factor: typing.Any | None = 1.0,
):
    """Transfer data layer(s) (weights, edge sharp, ...) from active to selected meshes

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param use_reverse_transfer: Reverse Transfer, Transfer from selected objects to active one
        :type use_reverse_transfer: bool | typing.Any | None
        :param use_freeze: Freeze Operator, Prevent changes to settings to re-run the operator, handy to change several things at once with heavy geometry
        :type use_freeze: bool | typing.Any | None
        :param data_type: Data Type, Which data to transfer

    VGROUP_WEIGHTS Vertex Group(s), Transfer active or all vertex groups.

    BEVEL_WEIGHT_VERT Bevel Weight, Transfer bevel weights.

    SHARP_EDGE Sharp, Transfer sharp mark.

    SEAM UV Seam, Transfer UV seam mark.

    CREASE Subsurf Crease, Transfer crease values.

    BEVEL_WEIGHT_EDGE Bevel Weight, Transfer bevel weights.

    FREESTYLE_EDGE Freestyle Mark, Transfer Freestyle edge mark.

    CUSTOM_NORMAL Custom Normals, Transfer custom normals.

    VCOL VCol, Vertex (face corners) colors.

    UV UVs, Transfer UV layers.

    SMOOTH Smooth, Transfer flat/smooth mark.

    FREESTYLE_FACE Freestyle Mark, Transfer Freestyle face mark.
        :type data_type: str | None
        :param use_create: Create Data, Add data layers on destination meshes if needed
        :type use_create: bool | typing.Any | None
        :param vert_mapping: Vertex Mapping, Method used to map source vertices to destination ones

    TOPOLOGY Topology, Copy from identical topology meshes.

    NEAREST Nearest vertex, Copy from closest vertex.

    EDGE_NEAREST Nearest Edge Vertex, Copy from closest vertex of closest edge.

    EDGEINTERP_NEAREST Nearest Edge Interpolated, Copy from interpolated values of vertices from closest point on closest edge.

    POLY_NEAREST Nearest Face Vertex, Copy from closest vertex of closest face.

    POLYINTERP_NEAREST Nearest Face Interpolated, Copy from interpolated values of vertices from closest point on closest face.

    POLYINTERP_VNORPROJ Projected Face Interpolated, Copy from interpolated values of vertices from point on closest face hit by normal-projection.
        :type vert_mapping: str | None
        :param edge_mapping: Edge Mapping, Method used to map source edges to destination ones

    TOPOLOGY Topology, Copy from identical topology meshes.

    VERT_NEAREST Nearest Vertices, Copy from most similar edge (edge which vertices are the closest of destination edge's ones).

    NEAREST Nearest Edge, Copy from closest edge (using midpoints).

    POLY_NEAREST Nearest Face Edge, Copy from closest edge of closest face (using midpoints).

    EDGEINTERP_VNORPROJ Projected Edge Interpolated, Interpolate all source edges hit by the projection of destination one along its own normal (from vertices).
        :type edge_mapping: str | None
        :param loop_mapping: Face Corner Mapping, Method used to map source faces' corners to destination ones

    TOPOLOGY Topology, Copy from identical topology meshes.

    NEAREST_NORMAL Nearest Corner And Best Matching Normal, Copy from nearest corner which has the best matching normal.

    NEAREST_POLYNOR Nearest Corner And Best Matching Face Normal, Copy from nearest corner which has the face with the best matching normal to destination corner's face one.

    NEAREST_POLY Nearest Corner Of Nearest Face, Copy from nearest corner of nearest polygon.

    POLYINTERP_NEAREST Nearest Face Interpolated, Copy from interpolated corners of the nearest source polygon.

    POLYINTERP_LNORPROJ Projected Face Interpolated, Copy from interpolated corners of the source polygon hit by corner normal projection.
        :type loop_mapping: str | None
        :param poly_mapping: Face Mapping, Method used to map source faces to destination ones

    TOPOLOGY Topology, Copy from identical topology meshes.

    NEAREST Nearest Face, Copy from nearest polygon (using center points).

    NORMAL Best Normal-Matching, Copy from source polygon which normal is the closest to destination one.

    POLYINTERP_PNORPROJ Projected Face Interpolated, Interpolate all source polygons intersected by the projection of destination one along its own normal.
        :type poly_mapping: str | None
        :param use_auto_transform: Auto Transform, Automatically compute transformation to get the best possible match between source and destination meshes (WARNING: results will never be as good as manual matching of objects)
        :type use_auto_transform: bool | typing.Any | None
        :param use_object_transform: Object Transform, Evaluate source and destination meshes in global space
        :type use_object_transform: bool | typing.Any | None
        :param use_max_distance: Only Neighbor Geometry, Source elements must be closer than given distance from destination one
        :type use_max_distance: bool | typing.Any | None
        :param max_distance: Max Distance, Maximum allowed distance between source and destination element, for non-topology mappings
        :type max_distance: typing.Any | None
        :param ray_radius: Ray Radius, 'Width' of rays (especially useful when raycasting against vertices or edges)
        :type ray_radius: typing.Any | None
        :param islands_precision: Islands Precision, Factor controlling precision of islands handling (the higher, the better the results)
        :type islands_precision: typing.Any | None
        :param layers_select_src: Source Layers Selection, Which layers to transfer, in case of multi-layers types

    ACTIVE Active Layer, Only transfer active data layer.

    ALL All Layers, Transfer all data layers.

    BONE_SELECT Selected Pose Bones, Transfer all vertex groups used by selected pose bones.

    BONE_DEFORM Deform Pose Bones, Transfer all vertex groups used by deform bones.
        :type layers_select_src: str | None
        :param layers_select_dst: Destination Layers Matching, How to match source and destination layers

    ACTIVE Active Layer, Affect active data layer of all targets.

    NAME By Name, Match target data layers to affect by name.

    INDEX By Order, Match target data layers to affect by order (indices).
        :type layers_select_dst: str | None
        :param mix_mode: Mix Mode, How to affect destination elements with source values

    REPLACE Replace, Overwrite all elements' data.

    ABOVE_THRESHOLD Above Threshold, Only replace destination elements where data is above given threshold (exact behavior depends on data type).

    BELOW_THRESHOLD Below Threshold, Only replace destination elements where data is below given threshold (exact behavior depends on data type).

    MIX Mix, Mix source value into destination one, using given threshold as factor.

    ADD Add, Add source value to destination one, using given threshold as factor.

    SUB Subtract, Subtract source value to destination one, using given threshold as factor.

    MUL Multiply, Multiply source value to destination one, using given threshold as factor.
        :type mix_mode: str | None
        :param mix_factor: Mix Factor, Factor to use when applying data to destination (exact behavior depends on mix mode)
        :type mix_factor: typing.Any | None
    """

    ...

def datalayout_transfer(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    modifier: str | typing.Any = "",
    data_type: str | None = "",
    use_delete: bool | typing.Any | None = False,
    layers_select_src: str | None = "ACTIVE",
    layers_select_dst: str | None = "ACTIVE",
):
    """Transfer layout of data layer(s) from active to selected meshes

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param modifier: Modifier, Name of the modifier to edit
        :type modifier: str | typing.Any
        :param data_type: Data Type, Which data to transfer

    VGROUP_WEIGHTS Vertex Group(s), Transfer active or all vertex groups.

    BEVEL_WEIGHT_VERT Bevel Weight, Transfer bevel weights.

    SHARP_EDGE Sharp, Transfer sharp mark.

    SEAM UV Seam, Transfer UV seam mark.

    CREASE Subsurf Crease, Transfer crease values.

    BEVEL_WEIGHT_EDGE Bevel Weight, Transfer bevel weights.

    FREESTYLE_EDGE Freestyle Mark, Transfer Freestyle edge mark.

    CUSTOM_NORMAL Custom Normals, Transfer custom normals.

    VCOL VCol, Vertex (face corners) colors.

    UV UVs, Transfer UV layers.

    SMOOTH Smooth, Transfer flat/smooth mark.

    FREESTYLE_FACE Freestyle Mark, Transfer Freestyle face mark.
        :type data_type: str | None
        :param use_delete: Exact Match, Also delete some data layers from destination if necessary, so that it matches exactly source
        :type use_delete: bool | typing.Any | None
        :param layers_select_src: Source Layers Selection, Which layers to transfer, in case of multi-layers types

    ACTIVE Active Layer, Only transfer active data layer.

    ALL All Layers, Transfer all data layers.

    BONE_SELECT Selected Pose Bones, Transfer all vertex groups used by selected pose bones.

    BONE_DEFORM Deform Pose Bones, Transfer all vertex groups used by deform bones.
        :type layers_select_src: str | None
        :param layers_select_dst: Destination Layers Matching, How to match source and destination layers

    ACTIVE Active Layer, Affect active data layer of all targets.

    NAME By Name, Match target data layers to affect by name.

    INDEX By Order, Match target data layers to affect by order (indices).
        :type layers_select_dst: str | None
    """

    ...

def delete(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_global: bool | typing.Any | None = False,
    confirm: bool | typing.Any | None = True,
):
    """Delete selected objects

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_global: Delete Globally, Remove object from all scenes
    :type use_global: bool | typing.Any | None
    :param confirm: Confirm, Prompt for confirmation
    :type confirm: bool | typing.Any | None
    """

    ...

def drop_named_image(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    relative_path: bool | typing.Any | None = True,
    name: str | typing.Any = "",
    align: str | None = "WORLD",
    location: typing.Any | None = (0.0, 0.0, 0.0),
    rotation: typing.Any | None = (0.0, 0.0, 0.0),
):
    """Add an empty image type to scene with data

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: Filepath, Path to image file
        :type filepath: str | typing.Any
        :param relative_path: Relative Path, Select the file relative to the blend file
        :type relative_path: bool | typing.Any | None
        :param name: Name, Image name to assign
        :type name: str | typing.Any
        :param align: Align, The alignment of the new object

    WORLD World, Align the new object to the world.

    VIEW View, Align the new object to the view.

    CURSOR 3D Cursor, Use the 3D cursor orientation for the new object.
        :type align: str | None
        :param location: Location, Location for the newly added object
        :type location: typing.Any | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: typing.Any | None
    """

    ...

def drop_named_material(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    name: str | typing.Any = "Material",
):
    """Undocumented contribute <https://developer.blender.org/T51061>

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Material name to assign
    :type name: str | typing.Any
    """

    ...

def duplicate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    linked: bool | typing.Any | None = False,
    mode: str | None = "TRANSLATION",
):
    """Duplicate selected objects

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param linked: Linked, Duplicate object but not object data, linking to the original data
    :type linked: bool | typing.Any | None
    :param mode: Mode
    :type mode: str | None
    """

    ...

def duplicate_move(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    OBJECT_OT_duplicate: duplicate | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
):
    """Duplicate selected objects and move them

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param OBJECT_OT_duplicate: Duplicate Objects, Duplicate selected objects
    :type OBJECT_OT_duplicate: duplicate | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

    ...

def duplicate_move_linked(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    OBJECT_OT_duplicate: duplicate | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
):
    """Duplicate selected objects and move them

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param OBJECT_OT_duplicate: Duplicate Objects, Duplicate selected objects
    :type OBJECT_OT_duplicate: duplicate | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

    ...

def duplicates_make_real(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_base_parent: bool | typing.Any | None = False,
    use_hierarchy: bool | typing.Any | None = False,
):
    """Make instanced objects attached to this object real

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_base_parent: Parent, Parent newly created objects to the original duplicator
    :type use_base_parent: bool | typing.Any | None
    :param use_hierarchy: Keep Hierarchy, Maintain parent child relationships
    :type use_hierarchy: bool | typing.Any | None
    """

    ...

def editmode_toggle(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Toggle object's editmode

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def effector_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "FORCE",
    radius: typing.Any | None = 1.0,
    enter_editmode: bool | typing.Any | None = False,
    align: str | None = "WORLD",
    location: typing.Any | None = (0.0, 0.0, 0.0),
    rotation: typing.Any | None = (0.0, 0.0, 0.0),
):
    """Add an empty object with a physics effector to the scene

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type
        :type type: str | None
        :param radius: Radius
        :type radius: typing.Any | None
        :param enter_editmode: Enter Editmode, Enter editmode when adding this object
        :type enter_editmode: bool | typing.Any | None
        :param align: Align, The alignment of the new object

    WORLD World, Align the new object to the world.

    VIEW View, Align the new object to the view.

    CURSOR 3D Cursor, Use the 3D cursor orientation for the new object.
        :type align: str | None
        :param location: Location, Location for the newly added object
        :type location: typing.Any | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: typing.Any | None
    """

    ...

def empty_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "PLAIN_AXES",
    radius: typing.Any | None = 1.0,
    align: str | None = "WORLD",
    location: typing.Any | None = (0.0, 0.0, 0.0),
    rotation: typing.Any | None = (0.0, 0.0, 0.0),
):
    """Add an empty object to the scene

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type
        :type type: str | None
        :param radius: Radius
        :type radius: typing.Any | None
        :param align: Align, The alignment of the new object

    WORLD World, Align the new object to the world.

    VIEW View, Align the new object to the view.

    CURSOR 3D Cursor, Use the 3D cursor orientation for the new object.
        :type align: str | None
        :param location: Location, Location for the newly added object
        :type location: typing.Any | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: typing.Any | None
    """

    ...

def explode_refresh(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    modifier: str | typing.Any = "",
):
    """Refresh data in the Explode modifier

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str | typing.Any
    """

    ...

def face_map_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add a new face map to the active object

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def face_map_assign(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Assign faces to a face map

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def face_map_deselect(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Deselect faces belonging to a face map

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def face_map_move(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    direction: str | None = "UP",
):
    """Move the active face map up/down in the list

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Direction, Direction to move, UP or DOWN
    :type direction: str | None
    """

    ...

def face_map_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove a face map from the active object

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def face_map_remove_from(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove faces from a face map

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def face_map_select(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select faces belonging to a face map

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def forcefield_toggle(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Toggle object's force field

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def gpencil_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    radius: typing.Any | None = 1.0,
    align: str | None = "WORLD",
    location: typing.Any | None = (0.0, 0.0, 0.0),
    rotation: typing.Any | None = (0.0, 0.0, 0.0),
    type: str | None = "EMPTY",
):
    """Add a Grease Pencil object to the scene

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param radius: Radius
        :type radius: typing.Any | None
        :param align: Align, The alignment of the new object

    WORLD World, Align the new object to the world.

    VIEW View, Align the new object to the view.

    CURSOR 3D Cursor, Use the 3D cursor orientation for the new object.
        :type align: str | None
        :param location: Location, Location for the newly added object
        :type location: typing.Any | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: typing.Any | None
        :param type: Type

    EMPTY Blank, Create an empty grease pencil object.

    STROKE Stroke, Create a simple stroke with basic colors.

    MONKEY Monkey, Construct a Suzanne grease pencil object.
        :type type: str | None
    """

    ...

def gpencil_modifier_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "CURVE",
):
    """Add a procedural operation/effect to the active grease pencil object

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type

    DATA_TRANSFER Data Transfer, Transfer several types of data (vertex groups, UV maps, vertex colors, custom normals) from one mesh to another.

    MESH_CACHE Mesh Cache, Deform the mesh using an external frame-by-frame vertex transform cache.

    MESH_SEQUENCE_CACHE Mesh Sequence Cache, Deform the mesh or curve using an external mesh cache in Alembic format.

    NORMAL_EDIT Normal Edit, Modify the direction of the surface normals.

    WEIGHTED_NORMAL Weighted Normal, Modify the direction of the surface normals using a weighting method.

    UV_PROJECT UV Project, Project the UV map coordinates from the negative Z axis of another object.

    UV_WARP UV Warp, Transform the UV map using the the difference between two objects.

    VERTEX_WEIGHT_EDIT Vertex Weight Edit, Modify of the weights of a vertex group.

    VERTEX_WEIGHT_MIX Vertex Weight Mix, Mix the weights of two vertex groups.

    VERTEX_WEIGHT_PROXIMITY Vertex Weight Proximity, Set the vertex group weights based on the distance to another target object.

    ARRAY Array, Create copies of the shape with offsets.

    BEVEL Bevel, Generate sloped corners by adding geometry to the mesh's edges or vertices.

    BOOLEAN Boolean, Use another shape to cut, combine or perform a difference operation.

    BUILD Build, Cause the faces of the mesh object to appear or disappear one after the other over time.

    DECIMATE Decimate, Reduce the geometry density.

    EDGE_SPLIT Edge Split, Split away joined faces at the edges.

    MASK Mask, Dynamically hide vertices based on a vertex group or armature.

    MIRROR Mirror, Mirror along the local X, Y and/or Z axes, over the object origin.

    MULTIRES Multiresolution, Subdivide the mesh in a way that allows editing the higher subdivision levels.

    REMESH Remesh, Generate new mesh topology based on the current shape.

    SCREW Screw, Lathe around an axis, treating the inout mesh as a profile.

    SKIN Skin, Create a solid shape from vertices and edges, using the vertex radius to define the thickness.

    SOLIDIFY Solidify,  Make the surface thick.

    SUBSURF Subdivision Surface, Split the faces into smaller parts, giving it a smoother appearance.

    TRIANGULATE Triangulate, Convert all polygons to triangles.

    WIREFRAME Wireframe, Convert faces into thickened edges.

    WELD Weld, Find groups of vertices closer then dist and merges them together.

    ARMATURE Armature, Deform the shape using an armature object.

    CAST Cast, Shift the shape towards a predefined primitive.

    CURVE Curve, Bend the mesh using a curve object.

    DISPLACE Displace, Offset vertices based on a texture.

    HOOK Hook, Deform specific points using another object.

    LAPLACIANDEFORM Laplacian Deform, Deform based a series of anchor points.

    LATTICE Lattice, Deform using the shape of a lattice object.

    MESH_DEFORM Mesh Deform, Deform using a different mesh, which acts as a deformation cage.

    SHRINKWRAP Shrinkwrap, Project the shape onto another object.

    SIMPLE_DEFORM Simple Deform, Deform the shape by twisting, bending, tapering or stretching.

    SMOOTH Smooth, Smooth the mesh by flattening the angles between adjacent faces.

    CORRECTIVE_SMOOTH Smooth Corrective, Smooth the mesh while still preserving the volume.

    LAPLACIANSMOOTH Smooth Laplacian, Reduce the noise on a mesh surface with minimal changes to its shape.

    SURFACE_DEFORM Surface Deform, Transfer motion from another mesh.

    WARP Warp, Warp parts of a mesh to a new location in a very flexible way thanks to 2 specified objects.

    WAVE Wave, Adds a ripple-like motion to an object’s geometry.

    CLOTH Cloth.

    COLLISION Collision.

    DYNAMIC_PAINT Dynamic Paint.

    EXPLODE Explode, Break apart the mesh faces and let them follow particles.

    OCEAN Ocean, Generate a moving ocean surface.

    PARTICLE_INSTANCE Particle Instance.

    PARTICLE_SYSTEM Particle System, Spawn particles from the shape.

    FLUID Fluid Simulation.

    SOFT_BODY Soft Body.

    SURFACE Surface.
        :type type: str | None
    """

    ...

def gpencil_modifier_apply(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    apply_as: str | None = "DATA",
    modifier: str | typing.Any = "",
):
    """Apply modifier and remove from the stack

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param apply_as: Apply as, How to apply the modifier to the geometry

    DATA Object Data, Apply modifier to the object's data.

    SHAPE New Shape, Apply deform-only modifier to a new shape on this object.
        :type apply_as: str | None
        :param modifier: Modifier, Name of the modifier to edit
        :type modifier: str | typing.Any
    """

    ...

def gpencil_modifier_copy(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    modifier: str | typing.Any = "",
):
    """Duplicate modifier at the same position in the stack

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str | typing.Any
    """

    ...

def gpencil_modifier_move_down(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    modifier: str | typing.Any = "",
):
    """Move modifier down in the stack

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str | typing.Any
    """

    ...

def gpencil_modifier_move_up(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    modifier: str | typing.Any = "",
):
    """Move modifier up in the stack

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str | typing.Any
    """

    ...

def gpencil_modifier_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    modifier: str | typing.Any = "",
):
    """Remove a modifier from the active grease pencil object

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str | typing.Any
    """

    ...

def hide_collection(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    collection_index: typing.Any | None = -1,
    toggle: bool | typing.Any | None = False,
):
    """Show only objects in collection (Shift to extend)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param collection_index: Collection Index, Index of the collection to change visibility
    :type collection_index: typing.Any | None
    :param toggle: Toggle, Toggle visibility
    :type toggle: bool | typing.Any | None
    """

    ...

def hide_render_clear_all(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Reveal all render objects by setting the hide render flag

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def hide_view_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    select: bool | typing.Any | None = True,
):
    """Reveal temporarily hidden objects

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param select: Select
    :type select: bool | typing.Any | None
    """

    ...

def hide_view_set(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    unselected: bool | typing.Any | None = False,
):
    """Temporarily hide objects from the viewport

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param unselected: Unselected, Hide unselected rather than selected objects
    :type unselected: bool | typing.Any | None
    """

    ...

def hook_add_newob(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Hook selected vertices to a newly created object

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def hook_add_selob(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_bone: bool | typing.Any | None = False,
):
    """Hook selected vertices to the first selected object

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_bone: Active Bone, Assign the hook to the hook objects active bone
    :type use_bone: bool | typing.Any | None
    """

    ...

def hook_assign(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    modifier: str | None = "",
):
    """Assign the selected vertices to a hook

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param modifier: Modifier, Modifier number to assign to
    :type modifier: str | None
    """

    ...

def hook_recenter(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    modifier: str | None = "",
):
    """Set hook center to cursor position

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param modifier: Modifier, Modifier number to assign to
    :type modifier: str | None
    """

    ...

def hook_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    modifier: str | None = "",
):
    """Remove a hook from the active object

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param modifier: Modifier, Modifier number to remove
    :type modifier: str | None
    """

    ...

def hook_reset(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    modifier: str | None = "",
):
    """Recalculate and clear offset transformation

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param modifier: Modifier, Modifier number to assign to
    :type modifier: str | None
    """

    ...

def hook_select(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    modifier: str | None = "",
):
    """Select affected vertices on mesh

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param modifier: Modifier, Modifier number to remove
    :type modifier: str | None
    """

    ...

def instance_offset_from_cursor(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Set offset used for collection instances based on cursor position

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def isolate_type_render(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Hide unselected render objects of same type as active by setting the hide render flag

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def join(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Join selected objects into active object

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def join_shapes(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Copy the current resulting shape of another selected object to this one

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def join_uvs(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Transfer UV Maps from active to selected objects (needs matching geometry)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def laplaciandeform_bind(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    modifier: str | typing.Any = "",
):
    """Bind mesh to system in laplacian deform modifier

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str | typing.Any
    """

    ...

def light_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "POINT",
    radius: typing.Any | None = 1.0,
    align: str | None = "WORLD",
    location: typing.Any | None = (0.0, 0.0, 0.0),
    rotation: typing.Any | None = (0.0, 0.0, 0.0),
):
    """Add a light object to the scene

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type

    POINT Point, Omnidirectional point light source.

    SUN Sun, Constant direction parallel ray light source.

    SPOT Spot, Directional cone light source.

    AREA Area, Directional area light source.
        :type type: str | None
        :param radius: Radius
        :type radius: typing.Any | None
        :param align: Align, The alignment of the new object

    WORLD World, Align the new object to the world.

    VIEW View, Align the new object to the view.

    CURSOR 3D Cursor, Use the 3D cursor orientation for the new object.
        :type align: str | None
        :param location: Location, Location for the newly added object
        :type location: typing.Any | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: typing.Any | None
    """

    ...

def lightprobe_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "CUBEMAP",
    radius: typing.Any | None = 1.0,
    enter_editmode: bool | typing.Any | None = False,
    align: str | None = "WORLD",
    location: typing.Any | None = (0.0, 0.0, 0.0),
    rotation: typing.Any | None = (0.0, 0.0, 0.0),
):
    """Add a light probe object

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type

    CUBEMAP Reflection Cubemap, Reflection probe with spherical or cubic attenuation.

    PLANAR Reflection Plane, Planar reflection probe.

    GRID Irradiance Volume, Irradiance probe to capture diffuse indirect lighting.
        :type type: str | None
        :param radius: Radius
        :type radius: typing.Any | None
        :param enter_editmode: Enter Editmode, Enter editmode when adding this object
        :type enter_editmode: bool | typing.Any | None
        :param align: Align, The alignment of the new object

    WORLD World, Align the new object to the world.

    VIEW View, Align the new object to the view.

    CURSOR 3D Cursor, Use the 3D cursor orientation for the new object.
        :type align: str | None
        :param location: Location, Location for the newly added object
        :type location: typing.Any | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: typing.Any | None
    """

    ...

def link_to_collection(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    collection_index: typing.Any | None = -1,
    is_new: bool | typing.Any | None = False,
    new_collection_name: str | typing.Any = "",
):
    """Link objects to a collection

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param collection_index: Collection Index, Index of the collection to move to
    :type collection_index: typing.Any | None
    :param is_new: New, Move objects to a new collection
    :type is_new: bool | typing.Any | None
    :param new_collection_name: Name, Name of the newly added collection
    :type new_collection_name: str | typing.Any
    """

    ...

def load_background_image(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    filter_image: bool | typing.Any | None = True,
    filter_folder: bool | typing.Any | None = True,
    view_align: bool | typing.Any | None = True,
):
    """Add a reference image into the background behind objects

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param filepath: filepath
    :type filepath: str | typing.Any
    :param filter_image: filter_image
    :type filter_image: bool | typing.Any | None
    :param filter_folder: filter_folder
    :type filter_folder: bool | typing.Any | None
    :param view_align: Align to view
    :type view_align: bool | typing.Any | None
    """

    ...

def load_reference_image(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    filter_image: bool | typing.Any | None = True,
    filter_folder: bool | typing.Any | None = True,
    view_align: bool | typing.Any | None = True,
):
    """Add a reference image into the scene between objects

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param filepath: filepath
    :type filepath: str | typing.Any
    :param filter_image: filter_image
    :type filter_image: bool | typing.Any | None
    :param filter_folder: filter_folder
    :type filter_folder: bool | typing.Any | None
    :param view_align: Align to view
    :type view_align: bool | typing.Any | None
    """

    ...

def location_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    clear_delta: bool | typing.Any | None = False,
):
    """Clear the object's location

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param clear_delta: Clear Delta, Clear delta location in addition to clearing the normal location transform
    :type clear_delta: bool | typing.Any | None
    """

    ...

def make_dupli_face(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Convert objects into instanced faces

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def make_links_data(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "OBDATA",
):
    """Apply active object links to other selected objects

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: str | None
    """

    ...

def make_links_scene(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    scene: str | None = "",
):
    """Link selection to another scene

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param scene: Scene
    :type scene: str | None
    """

    ...

def make_local(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "SELECT_OBJECT",
):
    """Make library linked data-blocks local to this file

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: str | None
    """

    ...

def make_override_library(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    object: str | None = "DEFAULT",
):
    """Make a local override of this library linked data-block

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param object: Override Object, Name of lib-linked/collection object to make an override from
    :type object: str | None
    """

    ...

def make_single_user(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "SELECTED_OBJECTS",
    object: bool | typing.Any | None = False,
    obdata: bool | typing.Any | None = False,
    material: bool | typing.Any | None = False,
    animation: bool | typing.Any | None = False,
):
    """Make linked data local to each object

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: str | None
    :param object: Object, Make single user objects
    :type object: bool | typing.Any | None
    :param obdata: Object Data, Make single user object data
    :type obdata: bool | typing.Any | None
    :param material: Materials, Make materials local to each data-block
    :type material: bool | typing.Any | None
    :param animation: Object Animation, Make animation data local to each object
    :type animation: bool | typing.Any | None
    """

    ...

def material_slot_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add a new material slot

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def material_slot_assign(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Assign active material slot to selection

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def material_slot_copy(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Copy material to selected objects

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def material_slot_deselect(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Deselect by active material slot

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def material_slot_move(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    direction: str | None = "UP",
):
    """Move the active material up/down in the list

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Direction, Direction to move the active material towards
    :type direction: str | None
    """

    ...

def material_slot_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove the selected material slot

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def material_slot_remove_unused(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove unused material slots

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def material_slot_select(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select by active material slot

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def meshdeform_bind(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    modifier: str | typing.Any = "",
):
    """Bind mesh to cage in mesh deform modifier

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str | typing.Any
    """

    ...

def metaball_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "BALL",
    radius: typing.Any | None = 1.0,
    enter_editmode: bool | typing.Any | None = False,
    align: str | None = "WORLD",
    location: typing.Any | None = (0.0, 0.0, 0.0),
    rotation: typing.Any | None = (0.0, 0.0, 0.0),
):
    """Add an metaball object to the scene

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Primitive
        :type type: str | None
        :param radius: Radius
        :type radius: typing.Any | None
        :param enter_editmode: Enter Editmode, Enter editmode when adding this object
        :type enter_editmode: bool | typing.Any | None
        :param align: Align, The alignment of the new object

    WORLD World, Align the new object to the world.

    VIEW View, Align the new object to the view.

    CURSOR 3D Cursor, Use the 3D cursor orientation for the new object.
        :type align: str | None
        :param location: Location, Location for the newly added object
        :type location: typing.Any | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: typing.Any | None
    """

    ...

def mode_set(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: str | None = "OBJECT",
    toggle: bool | typing.Any | None = False,
):
    """Sets the object interaction mode

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param mode: Mode

    OBJECT Object Mode.

    EDIT Edit Mode.

    POSE Pose Mode.

    SCULPT Sculpt Mode.

    VERTEX_PAINT Vertex Paint.

    WEIGHT_PAINT Weight Paint.

    TEXTURE_PAINT Texture Paint.

    PARTICLE_EDIT Particle Edit.

    EDIT_GPENCIL Edit Mode, Edit Grease Pencil Strokes.

    SCULPT_GPENCIL Sculpt Mode, Sculpt Grease Pencil Strokes.

    PAINT_GPENCIL Draw, Paint Grease Pencil Strokes.

    WEIGHT_GPENCIL Weight Paint, Grease Pencil Weight Paint Strokes.
        :type mode: str | None
        :param toggle: Toggle
        :type toggle: bool | typing.Any | None
    """

    ...

def mode_set_with_submode(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: str | None = "OBJECT",
    toggle: bool | typing.Any | None = False,
    mesh_select_mode: set[str] | None = {},
):
    """Sets the object interaction mode

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param mode: Mode

    OBJECT Object Mode.

    EDIT Edit Mode.

    POSE Pose Mode.

    SCULPT Sculpt Mode.

    VERTEX_PAINT Vertex Paint.

    WEIGHT_PAINT Weight Paint.

    TEXTURE_PAINT Texture Paint.

    PARTICLE_EDIT Particle Edit.

    EDIT_GPENCIL Edit Mode, Edit Grease Pencil Strokes.

    SCULPT_GPENCIL Sculpt Mode, Sculpt Grease Pencil Strokes.

    PAINT_GPENCIL Draw, Paint Grease Pencil Strokes.

    WEIGHT_GPENCIL Weight Paint, Grease Pencil Weight Paint Strokes.
        :type mode: str | None
        :param toggle: Toggle
        :type toggle: bool | typing.Any | None
        :param mesh_select_mode: Mesh Mode

    VERT Vertex, Vertex selection mode.

    EDGE Edge, Edge selection mode.

    FACE Face, Face selection mode.
        :type mesh_select_mode: set[str] | None
    """

    ...

def modifier_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "SUBSURF",
):
    """Add a procedural operation/effect to the active object

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type

    DATA_TRANSFER Data Transfer, Transfer several types of data (vertex groups, UV maps, vertex colors, custom normals) from one mesh to another.

    MESH_CACHE Mesh Cache, Deform the mesh using an external frame-by-frame vertex transform cache.

    MESH_SEQUENCE_CACHE Mesh Sequence Cache, Deform the mesh or curve using an external mesh cache in Alembic format.

    NORMAL_EDIT Normal Edit, Modify the direction of the surface normals.

    WEIGHTED_NORMAL Weighted Normal, Modify the direction of the surface normals using a weighting method.

    UV_PROJECT UV Project, Project the UV map coordinates from the negative Z axis of another object.

    UV_WARP UV Warp, Transform the UV map using the the difference between two objects.

    VERTEX_WEIGHT_EDIT Vertex Weight Edit, Modify of the weights of a vertex group.

    VERTEX_WEIGHT_MIX Vertex Weight Mix, Mix the weights of two vertex groups.

    VERTEX_WEIGHT_PROXIMITY Vertex Weight Proximity, Set the vertex group weights based on the distance to another target object.

    ARRAY Array, Create copies of the shape with offsets.

    BEVEL Bevel, Generate sloped corners by adding geometry to the mesh's edges or vertices.

    BOOLEAN Boolean, Use another shape to cut, combine or perform a difference operation.

    BUILD Build, Cause the faces of the mesh object to appear or disappear one after the other over time.

    DECIMATE Decimate, Reduce the geometry density.

    EDGE_SPLIT Edge Split, Split away joined faces at the edges.

    MASK Mask, Dynamically hide vertices based on a vertex group or armature.

    MIRROR Mirror, Mirror along the local X, Y and/or Z axes, over the object origin.

    MULTIRES Multiresolution, Subdivide the mesh in a way that allows editing the higher subdivision levels.

    REMESH Remesh, Generate new mesh topology based on the current shape.

    SCREW Screw, Lathe around an axis, treating the inout mesh as a profile.

    SKIN Skin, Create a solid shape from vertices and edges, using the vertex radius to define the thickness.

    SOLIDIFY Solidify,  Make the surface thick.

    SUBSURF Subdivision Surface, Split the faces into smaller parts, giving it a smoother appearance.

    TRIANGULATE Triangulate, Convert all polygons to triangles.

    WIREFRAME Wireframe, Convert faces into thickened edges.

    WELD Weld, Find groups of vertices closer then dist and merges them together.

    ARMATURE Armature, Deform the shape using an armature object.

    CAST Cast, Shift the shape towards a predefined primitive.

    CURVE Curve, Bend the mesh using a curve object.

    DISPLACE Displace, Offset vertices based on a texture.

    HOOK Hook, Deform specific points using another object.

    LAPLACIANDEFORM Laplacian Deform, Deform based a series of anchor points.

    LATTICE Lattice, Deform using the shape of a lattice object.

    MESH_DEFORM Mesh Deform, Deform using a different mesh, which acts as a deformation cage.

    SHRINKWRAP Shrinkwrap, Project the shape onto another object.

    SIMPLE_DEFORM Simple Deform, Deform the shape by twisting, bending, tapering or stretching.

    SMOOTH Smooth, Smooth the mesh by flattening the angles between adjacent faces.

    CORRECTIVE_SMOOTH Smooth Corrective, Smooth the mesh while still preserving the volume.

    LAPLACIANSMOOTH Smooth Laplacian, Reduce the noise on a mesh surface with minimal changes to its shape.

    SURFACE_DEFORM Surface Deform, Transfer motion from another mesh.

    WARP Warp, Warp parts of a mesh to a new location in a very flexible way thanks to 2 specified objects.

    WAVE Wave, Adds a ripple-like motion to an object’s geometry.

    CLOTH Cloth.

    COLLISION Collision.

    DYNAMIC_PAINT Dynamic Paint.

    EXPLODE Explode, Break apart the mesh faces and let them follow particles.

    OCEAN Ocean, Generate a moving ocean surface.

    PARTICLE_INSTANCE Particle Instance.

    PARTICLE_SYSTEM Particle System, Spawn particles from the shape.

    FLUID Fluid Simulation.

    SOFT_BODY Soft Body.

    SURFACE Surface.
        :type type: str | None
    """

    ...

def modifier_apply(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    apply_as: str | None = "DATA",
    modifier: str | typing.Any = "",
):
    """Apply modifier and remove from the stack

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param apply_as: Apply as, How to apply the modifier to the geometry

    DATA Object Data, Apply modifier to the object's data.

    SHAPE New Shape, Apply deform-only modifier to a new shape on this object.
        :type apply_as: str | None
        :param modifier: Modifier, Name of the modifier to edit
        :type modifier: str | typing.Any
    """

    ...

def modifier_convert(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    modifier: str | typing.Any = "",
):
    """Convert particles to a mesh object

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str | typing.Any
    """

    ...

def modifier_copy(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    modifier: str | typing.Any = "",
):
    """Duplicate modifier at the same position in the stack

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str | typing.Any
    """

    ...

def modifier_move_down(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    modifier: str | typing.Any = "",
):
    """Move modifier down in the stack

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str | typing.Any
    """

    ...

def modifier_move_up(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    modifier: str | typing.Any = "",
):
    """Move modifier up in the stack

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str | typing.Any
    """

    ...

def modifier_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    modifier: str | typing.Any = "",
):
    """Remove a modifier from the active object

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str | typing.Any
    """

    ...

def move_to_collection(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    collection_index: typing.Any | None = -1,
    is_new: bool | typing.Any | None = False,
    new_collection_name: str | typing.Any = "",
):
    """Move objects to a collection

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param collection_index: Collection Index, Index of the collection to move to
    :type collection_index: typing.Any | None
    :param is_new: New, Move objects to a new collection
    :type is_new: bool | typing.Any | None
    :param new_collection_name: Name, Name of the newly added collection
    :type new_collection_name: str | typing.Any
    """

    ...

def multires_base_apply(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    modifier: str | typing.Any = "",
):
    """Modify the base mesh to conform to the displaced mesh

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str | typing.Any
    """

    ...

def multires_external_pack(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Pack displacements from an external file

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def multires_external_save(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str | typing.Any = "",
    hide_props_region: bool | typing.Any | None = True,
    check_existing: bool | typing.Any | None = True,
    filter_blender: bool | typing.Any | None = False,
    filter_backup: bool | typing.Any | None = False,
    filter_image: bool | typing.Any | None = False,
    filter_movie: bool | typing.Any | None = False,
    filter_python: bool | typing.Any | None = False,
    filter_font: bool | typing.Any | None = False,
    filter_sound: bool | typing.Any | None = False,
    filter_text: bool | typing.Any | None = False,
    filter_archive: bool | typing.Any | None = False,
    filter_btx: bool | typing.Any | None = True,
    filter_collada: bool | typing.Any | None = False,
    filter_alembic: bool | typing.Any | None = False,
    filter_usd: bool | typing.Any | None = False,
    filter_folder: bool | typing.Any | None = True,
    filter_blenlib: bool | typing.Any | None = False,
    filemode: typing.Any | None = 9,
    relative_path: bool | typing.Any | None = True,
    display_type: str | None = "DEFAULT",
    sort_method: str | None = "FILE_SORT_ALPHA",
    modifier: str | typing.Any = "",
):
    """Save displacements to an external file

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str | typing.Any
        :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
        :type hide_props_region: bool | typing.Any | None
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | typing.Any | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | typing.Any | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | typing.Any | None
        :param filter_image: Filter image files
        :type filter_image: bool | typing.Any | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | typing.Any | None
        :param filter_python: Filter python files
        :type filter_python: bool | typing.Any | None
        :param filter_font: Filter font files
        :type filter_font: bool | typing.Any | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | typing.Any | None
        :param filter_text: Filter text files
        :type filter_text: bool | typing.Any | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | typing.Any | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | typing.Any | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | typing.Any | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | typing.Any | None
        :param filter_usd: Filter USD files
        :type filter_usd: bool | typing.Any | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | typing.Any | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | typing.Any | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: typing.Any | None
        :param relative_path: Relative Path, Select the file relative to the blend file
        :type relative_path: bool | typing.Any | None
        :param display_type: Display Type

    DEFAULT Default, Automatically determine display type for files.

    LIST_VERTICAL Short List, Display files as short list.

    LIST_HORIZONTAL Long List, Display files as a detailed list.

    THUMBNAIL Thumbnails, Display files as thumbnails.
        :type display_type: str | None
        :param sort_method: File sorting mode

    FILE_SORT_ALPHA Name, Sort the file list alphabetically.

    FILE_SORT_EXTENSION Extension, Sort the file list by extension/type.

    FILE_SORT_TIME Modified Date, Sort files by modification time.

    FILE_SORT_SIZE Size, Sort files by size.
        :type sort_method: str | None
        :param modifier: Modifier, Name of the modifier to edit
        :type modifier: str | typing.Any
    """

    ...

def multires_higher_levels_delete(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    modifier: str | typing.Any = "",
):
    """Deletes the higher resolution mesh, potential loss of detail

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str | typing.Any
    """

    ...

def multires_reshape(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    modifier: str | typing.Any = "",
):
    """Copy vertex coordinates from other object

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str | typing.Any
    """

    ...

def multires_subdivide(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    modifier: str | typing.Any = "",
):
    """Add a new level of subdivision

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str | typing.Any
    """

    ...

def ocean_bake(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    modifier: str | typing.Any = "",
    free: bool | typing.Any | None = False,
):
    """Bake an image sequence of ocean data

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str | typing.Any
    :param free: Free, Free the bake, rather than generating it
    :type free: bool | typing.Any | None
    """

    ...

def origin_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Clear the object's origin

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def origin_set(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "GEOMETRY_ORIGIN",
    center: str | None = "MEDIAN",
):
    """Set the object's origin, by either moving the data, or set to center of data, or use 3D cursor

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type

    GEOMETRY_ORIGIN Geometry to Origin, Move object geometry to object origin.

    ORIGIN_GEOMETRY Origin to Geometry, Calculate the center of geometry based on the current pivot point (median, otherwise bounding-box).

    ORIGIN_CURSOR Origin to 3D Cursor, Move object origin to position of the 3D cursor.

    ORIGIN_CENTER_OF_MASS Origin to Center of Mass (Surface), Calculate the center of mass from the surface area.

    ORIGIN_CENTER_OF_VOLUME Origin to Center of Mass (Volume), Calculate the center of mass from the volume (must be manifold geometry with consistent normals).
        :type type: str | None
        :param center: Center
        :type center: str | None
    """

    ...

def parent_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "CLEAR",
):
    """Clear the object's parenting

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type

    CLEAR Clear Parent, Completely clear the parenting relationship, including involved modifiers if any.

    CLEAR_KEEP_TRANSFORM Clear and Keep Transformation, As 'Clear Parent', but keep the current visual transformations of the object.

    CLEAR_INVERSE Clear Parent Inverse, Reset the transform corrections applied to the parenting relationship, does not remove parenting itself.
        :type type: str | None
    """

    ...

def parent_no_inverse_set(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Set the object's parenting without setting the inverse parent correction

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def parent_set(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "OBJECT",
    xmirror: bool | typing.Any | None = False,
    keep_transform: bool | typing.Any | None = False,
):
    """Set the object's parenting

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: str | None
    :param xmirror: X Mirror, Apply weights symmetrically along X axis, for Envelope/Automatic vertex groups creation
    :type xmirror: bool | typing.Any | None
    :param keep_transform: Keep Transform, Apply transformation before parenting
    :type keep_transform: bool | typing.Any | None
    """

    ...

def particle_system_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add a particle system

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def particle_system_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove the selected particle system

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def paths_calculate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    start_frame: typing.Any | None = 1,
    end_frame: typing.Any | None = 250,
):
    """Calculate motion paths for the selected objects

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param start_frame: Start, First frame to calculate object paths on
    :type start_frame: typing.Any | None
    :param end_frame: End, Last frame to calculate object paths on
    :type end_frame: typing.Any | None
    """

    ...

def paths_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    only_selected: bool | typing.Any | None = False,
):
    """Clear path caches for all objects, hold Shift key for selected objects only

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param only_selected: Only Selected, Only clear paths from selected objects
    :type only_selected: bool | typing.Any | None
    """

    ...

def paths_range_update(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Update frame range for motion paths from the Scene's current frame range

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def paths_update(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Recalculate paths for selected objects

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def posemode_toggle(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Enable or disable posing/selecting bones

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def proxy_make(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    object: str | None = "DEFAULT",
):
    """Add empty object to become local replacement data of a library-linked object

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param object: Proxy Object, Name of lib-linked/collection object to make a proxy for
    :type object: str | None
    """

    ...

def quadriflow_remesh(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_paint_symmetry: bool | typing.Any | None = True,
    use_preserve_sharp: bool | typing.Any | None = False,
    use_preserve_boundary: bool | typing.Any | None = False,
    use_mesh_curvature: bool | typing.Any | None = False,
    preserve_paint_mask: bool | typing.Any | None = False,
    smooth_normals: bool | typing.Any | None = False,
    mode: str | None = "FACES",
    target_ratio: typing.Any | None = 1.0,
    target_edge_length: typing.Any | None = 0.1,
    target_faces: typing.Any | None = 4000,
    mesh_area: typing.Any | None = -1,
    seed: typing.Any | None = 0,
):
    """Create a new quad based mesh using the surface data of the current mesh. All data layers will be lost

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param use_paint_symmetry: Use Paint Symmetry, Generates a symmetrycal mesh using the paint symmetry configuration
        :type use_paint_symmetry: bool | typing.Any | None
        :param use_preserve_sharp: Preserve Sharp, Try to preserve sharp features on the mesh
        :type use_preserve_sharp: bool | typing.Any | None
        :param use_preserve_boundary: Preserve Mesh Boundary, Try to preserve mesh boundary on the mesh
        :type use_preserve_boundary: bool | typing.Any | None
        :param use_mesh_curvature: Use Mesh Curvature, Take the mesh curvature into account when remeshing
        :type use_mesh_curvature: bool | typing.Any | None
        :param preserve_paint_mask: Preserve Paint Mask, Reproject the paint mask onto the new mesh
        :type preserve_paint_mask: bool | typing.Any | None
        :param smooth_normals: Smooth Normals, Set the output mesh normals to smooth
        :type smooth_normals: bool | typing.Any | None
        :param mode: Mode, How to specify the amount of detail for the new mesh

    RATIO Ratio, Specify target number of faces relative to the current mesh.

    EDGE Edge Length, Input target edge length in the new mesh.

    FACES Faces, Input target number of faces in the new mesh.
        :type mode: str | None
        :param target_ratio: Ratio, Relative number of faces compared to the current mesh
        :type target_ratio: typing.Any | None
        :param target_edge_length: Edge Length, Target edge length in the new mesh
        :type target_edge_length: typing.Any | None
        :param target_faces: Number of Faces, Approximate number of faces (quads) in the new mesh
        :type target_faces: typing.Any | None
        :param mesh_area: Old Object Face Area, This property is only used to cache the object area for later calculations
        :type mesh_area: typing.Any | None
        :param seed: Seed, Random seed to use with the solver. Different seeds will cause the remesher to come up with different quad layouts on the mesh
        :type seed: typing.Any | None
    """

    ...

def quick_explode(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    style: str | None = "EXPLODE",
    amount: typing.Any | None = 100,
    frame_duration: typing.Any | None = 50,
    frame_start: typing.Any | None = 1,
    frame_end: typing.Any | None = 10,
    velocity: typing.Any | None = 1.0,
    fade: bool | typing.Any | None = True,
):
    """Make selected objects explode

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param style: Explode Style
    :type style: str | None
    :param amount: Amount of pieces
    :type amount: typing.Any | None
    :param frame_duration: Duration
    :type frame_duration: typing.Any | None
    :param frame_start: Start Frame
    :type frame_start: typing.Any | None
    :param frame_end: End Frame
    :type frame_end: typing.Any | None
    :param velocity: Outwards Velocity
    :type velocity: typing.Any | None
    :param fade: Fade, Fade the pieces over time
    :type fade: bool | typing.Any | None
    """

    ...

def quick_fur(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    density: str | None = "MEDIUM",
    view_percentage: typing.Any | None = 10,
    length: typing.Any | None = 0.1,
):
    """Add fur setup to the selected objects

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param density: Fur Density
    :type density: str | None
    :param view_percentage: View %
    :type view_percentage: typing.Any | None
    :param length: Length
    :type length: typing.Any | None
    """

    ...

def quick_liquid(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    show_flows: bool | typing.Any | None = False,
):
    """Undocumented contribute <https://developer.blender.org/T51061>

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param show_flows: Render Liquid Objects, Keep the liquid objects visible during rendering
    :type show_flows: bool | typing.Any | None
    """

    ...

def quick_smoke(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    style: str | None = "SMOKE",
    show_flows: bool | typing.Any | None = False,
):
    """Use selected objects as smoke emitters

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param style: Smoke Style
    :type style: str | None
    :param show_flows: Render Smoke Objects, Keep the smoke objects visible during rendering
    :type show_flows: bool | typing.Any | None
    """

    ...

def randomize_transform(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    random_seed: typing.Any | None = 0,
    use_delta: bool | typing.Any | None = False,
    use_loc: bool | typing.Any | None = True,
    loc: typing.Any | None = (0.0, 0.0, 0.0),
    use_rot: bool | typing.Any | None = True,
    rot: typing.Any | None = (0.0, 0.0, 0.0),
    use_scale: bool | typing.Any | None = True,
    scale_even: bool | typing.Any | None = False,
    scale: typing.Any | None = (1.0, 1.0, 1.0),
):
    """Randomize objects loc/rot/scale

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param random_seed: Random Seed, Seed value for the random generator
    :type random_seed: typing.Any | None
    :param use_delta: Transform Delta, Randomize delta transform values instead of regular transform
    :type use_delta: bool | typing.Any | None
    :param use_loc: Randomize Location, Randomize the location values
    :type use_loc: bool | typing.Any | None
    :param loc: Location, Maximum distance the objects can spread over each axis
    :type loc: typing.Any | None
    :param use_rot: Randomize Rotation, Randomize the rotation values
    :type use_rot: bool | typing.Any | None
    :param rot: Rotation, Maximum rotation over each axis
    :type rot: typing.Any | None
    :param use_scale: Randomize Scale, Randomize the scale values
    :type use_scale: bool | typing.Any | None
    :param scale_even: Scale Even, Use the same scale value for all axis
    :type scale_even: bool | typing.Any | None
    :param scale: Scale, Maximum scale randomization over each axis
    :type scale: typing.Any | None
    """

    ...

def rotation_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    clear_delta: bool | typing.Any | None = False,
):
    """Clear the object's rotation

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param clear_delta: Clear Delta, Clear delta rotation in addition to clearing the normal rotation transform
    :type clear_delta: bool | typing.Any | None
    """

    ...

def scale_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    clear_delta: bool | typing.Any | None = False,
):
    """Clear the object's scale

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param clear_delta: Clear Delta, Clear delta scale in addition to clearing the normal scale transform
    :type clear_delta: bool | typing.Any | None
    """

    ...

def select_all(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    action: str | None = "TOGGLE",
):
    """Change selection of all visible objects in scene

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param action: Action, Selection action to execute

    TOGGLE Toggle, Toggle selection for all elements.

    SELECT Select, Select all elements.

    DESELECT Deselect, Deselect all elements.

    INVERT Invert, Invert selection of all elements.
        :type action: str | None
    """

    ...

def select_by_type(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    extend: bool | typing.Any | None = False,
    type: str | None = "MESH",
):
    """Select all visible objects that are of a type

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: bool | typing.Any | None
    :param type: Type
    :type type: str | None
    """

    ...

def select_camera(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    extend: bool | typing.Any | None = False,
):
    """Select the active camera

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend the selection
    :type extend: bool | typing.Any | None
    """

    ...

def select_grouped(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    extend: bool | typing.Any | None = False,
    type: str | None = "CHILDREN_RECURSIVE",
):
    """Select all visible objects grouped by various properties

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param extend: Extend, Extend selection instead of deselecting everything first
        :type extend: bool | typing.Any | None
        :param type: Type

    CHILDREN_RECURSIVE Children.

    CHILDREN Immediate Children.

    PARENT Parent.

    SIBLINGS Siblings, Shared Parent.

    TYPE Type, Shared object type.

    COLLECTION Collection, Shared collection.

    HOOK Hook.

    PASS Pass, Render pass Index.

    COLOR Color, Object Color.

    KEYINGSET Keying Set, Objects included in active Keying Set.

    LIGHT_TYPE Light Type, Matching light types.
        :type type: str | None
    """

    ...

def select_hierarchy(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    direction: str | None = "PARENT",
    extend: bool | typing.Any | None = False,
):
    """Select object relative to the active object's position in the hierarchy

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Direction, Direction to select in the hierarchy
    :type direction: str | None
    :param extend: Extend, Extend the existing selection
    :type extend: bool | typing.Any | None
    """

    ...

def select_less(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Deselect objects at the boundaries of parent/child relationships

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def select_linked(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    extend: bool | typing.Any | None = False,
    type: str | None = "OBDATA",
):
    """Select all visible objects that are linked

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: bool | typing.Any | None
    :param type: Type
    :type type: str | None
    """

    ...

def select_mirror(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    extend: bool | typing.Any | None = False,
):
    """Select the Mirror objects of the selected object eg. L.sword -> R.sword

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: bool | typing.Any | None
    """

    ...

def select_more(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select connected parent/child objects

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def select_pattern(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    pattern: str | typing.Any = "*",
    case_sensitive: bool | typing.Any | None = False,
    extend: bool | typing.Any | None = True,
):
    """Select objects matching a naming pattern

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param pattern: Pattern, Name filter using '*', '?' and '[abc]' unix style wildcards
    :type pattern: str | typing.Any
    :param case_sensitive: Case Sensitive, Do a case sensitive compare
    :type case_sensitive: bool | typing.Any | None
    :param extend: Extend, Extend the existing selection
    :type extend: bool | typing.Any | None
    """

    ...

def select_random(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    percent: typing.Any | None = 50.0,
    seed: typing.Any | None = 0,
    action: str | None = "SELECT",
):
    """Set select on random visible objects

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param percent: Percent, Percentage of objects to select randomly
        :type percent: typing.Any | None
        :param seed: Random Seed, Seed for the random number generator
        :type seed: typing.Any | None
        :param action: Action, Selection action to execute

    SELECT Select, Select all elements.

    DESELECT Deselect, Deselect all elements.
        :type action: str | None
    """

    ...

def select_same_collection(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    collection: str | typing.Any = "",
):
    """Select object in the same collection

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param collection: Collection, Name of the collection to select
    :type collection: str | typing.Any
    """

    ...

def shade_flat(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Render and display faces uniform, using Face Normals

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def shade_smooth(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Render and display faces smooth, using interpolated Vertex Normals

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def shaderfx_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "FX_BLUR",
):
    """Add a visual effect to the active object

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type

    FX_BLUR Blur, Apply Gaussian Blur to object.

    FX_COLORIZE Colorize, Apply different tint effects.

    FX_FLIP Flip, Flip image.

    FX_GLOW Glow, Create a glow effect.

    FX_LIGHT Light, Simulate illumination.

    FX_PIXEL Pixelate, Pixelate image.

    FX_RIM Rim, Add a rim to the image.

    FX_SHADOW Shadow, Create a shadow effect.

    FX_SWIRL Swirl, Create a rotation distortion.

    FX_WAVE Wave Distortion, Apply sinusoidal deformation.
        :type type: str | None
    """

    ...

def shaderfx_move_down(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    shaderfx: str | typing.Any = "",
):
    """Move shaderfx down in the stack

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param shaderfx: Shader, Name of the shaderfx to edit
    :type shaderfx: str | typing.Any
    """

    ...

def shaderfx_move_up(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    shaderfx: str | typing.Any = "",
):
    """Move shaderfx up in the stack

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param shaderfx: Shader, Name of the shaderfx to edit
    :type shaderfx: str | typing.Any
    """

    ...

def shaderfx_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    shaderfx: str | typing.Any = "",
):
    """Remove a shaderfx from the active grease pencil object

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param shaderfx: Shader, Name of the shaderfx to edit
    :type shaderfx: str | typing.Any
    """

    ...

def shape_key_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    from_mix: bool | typing.Any | None = True,
):
    """Add shape key to the object

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param from_mix: From Mix, Create the new shape key from the existing mix of keys
    :type from_mix: bool | typing.Any | None
    """

    ...

def shape_key_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Clear weights for all shape keys

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def shape_key_mirror(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_topology: bool | typing.Any | None = False,
):
    """Mirror the current shape key along the local X axis

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_topology: Topology Mirror, Use topology based mirroring (for when both sides of mesh have matching, unique topology)
    :type use_topology: bool | typing.Any | None
    """

    ...

def shape_key_move(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "TOP",
):
    """Move the active shape key up/down in the list

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type

    TOP Top, Top of the list.

    UP Up.

    DOWN Down.

    BOTTOM Bottom, Bottom of the list.
        :type type: str | None
    """

    ...

def shape_key_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    all: bool | typing.Any | None = False,
):
    """Remove shape key from the object

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param all: All, Remove all shape keys
    :type all: bool | typing.Any | None
    """

    ...

def shape_key_retime(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Resets the timing for absolute shape keys

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def shape_key_transfer(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: str | None = "OFFSET",
    use_clamp: bool | typing.Any | None = False,
):
    """Copy the active shape key of another selected object to this one

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param mode: Transformation Mode, Relative shape positions to the new shape method

    OFFSET Offset, Apply the relative positional offset.

    RELATIVE_FACE Relative Face, Calculate relative position (using faces).

    RELATIVE_EDGE Relative Edge, Calculate relative position (using edges).
        :type mode: str | None
        :param use_clamp: Clamp Offset, Clamp the transformation to the distance each vertex moves in the original shape
        :type use_clamp: bool | typing.Any | None
    """

    ...

def skin_armature_create(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    modifier: str | typing.Any = "",
):
    """Create an armature that parallels the skin layout

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str | typing.Any
    """

    ...

def skin_loose_mark_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    action: str | None = "MARK",
):
    """Mark/clear selected vertices as loose

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param action: Action

    MARK Mark, Mark selected vertices as loose.

    CLEAR Clear, Set selected vertices as not loose.
        :type action: str | None
    """

    ...

def skin_radii_equalize(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Make skin radii of selected vertices equal on each axis

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def skin_root_mark(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Mark selected vertices as roots

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def speaker_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    enter_editmode: bool | typing.Any | None = False,
    align: str | None = "WORLD",
    location: typing.Any | None = (0.0, 0.0, 0.0),
    rotation: typing.Any | None = (0.0, 0.0, 0.0),
):
    """Add a speaker object to the scene

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param enter_editmode: Enter Editmode, Enter editmode when adding this object
        :type enter_editmode: bool | typing.Any | None
        :param align: Align, The alignment of the new object

    WORLD World, Align the new object to the world.

    VIEW View, Align the new object to the view.

    CURSOR 3D Cursor, Use the 3D cursor orientation for the new object.
        :type align: str | None
        :param location: Location, Location for the newly added object
        :type location: typing.Any | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: typing.Any | None
    """

    ...

def subdivision_set(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    level: typing.Any | None = 1,
    relative: bool | typing.Any | None = False,
):
    """Sets a Subdivision Surface Level (1-5)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param level: Level
    :type level: typing.Any | None
    :param relative: Relative, Apply the subsurf level as an offset relative to the current level
    :type relative: bool | typing.Any | None
    """

    ...

def surfacedeform_bind(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    modifier: str | typing.Any = "",
):
    """Bind mesh to target in surface deform modifier

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str | typing.Any
    """

    ...

def text_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    radius: typing.Any | None = 1.0,
    enter_editmode: bool | typing.Any | None = False,
    align: str | None = "WORLD",
    location: typing.Any | None = (0.0, 0.0, 0.0),
    rotation: typing.Any | None = (0.0, 0.0, 0.0),
):
    """Add a text object to the scene

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param radius: Radius
        :type radius: typing.Any | None
        :param enter_editmode: Enter Editmode, Enter editmode when adding this object
        :type enter_editmode: bool | typing.Any | None
        :param align: Align, The alignment of the new object

    WORLD World, Align the new object to the world.

    VIEW View, Align the new object to the view.

    CURSOR 3D Cursor, Use the 3D cursor orientation for the new object.
        :type align: str | None
        :param location: Location, Location for the newly added object
        :type location: typing.Any | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: typing.Any | None
    """

    ...

def track_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "CLEAR",
):
    """Clear tracking constraint or flag from object

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: str | None
    """

    ...

def track_set(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: str | None = "DAMPTRACK",
):
    """Make the object track another object, using various methods/constraints

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: str | None
    """

    ...

def transform_apply(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    location: bool | typing.Any | None = True,
    rotation: bool | typing.Any | None = True,
    scale: bool | typing.Any | None = True,
    properties: bool | typing.Any | None = True,
):
    """Apply the object's transformation to its data

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param location: Location
    :type location: bool | typing.Any | None
    :param rotation: Rotation
    :type rotation: bool | typing.Any | None
    :param scale: Scale
    :type scale: bool | typing.Any | None
    :param properties: Apply Properties, Modify properties such as curve vertex radius, font size and bone envelope
    :type properties: bool | typing.Any | None
    """

    ...

def transform_axis_target(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Interactively point cameras and lights to a location (Ctrl translates)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def transforms_to_deltas(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: str | None = "ALL",
    reset_values: bool | typing.Any | None = True,
):
    """Convert normal object transforms to delta transforms, any existing delta transforms will be included as well

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param mode: Mode, Which transforms to transfer

    ALL All Transforms, Transfer location, rotation, and scale transforms.

    LOC Location, Transfer location transforms only.

    ROT Rotation, Transfer rotation transforms only.

    SCALE Scale, Transfer scale transforms only.
        :type mode: str | None
        :param reset_values: Reset Values, Clear transform values after transferring to deltas
        :type reset_values: bool | typing.Any | None
    """

    ...

def unlink_data(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Undocumented contribute <https://developer.blender.org/T51061>

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def vertex_group_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add a new vertex group to the active object

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def vertex_group_assign(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Assign the selected vertices to the active vertex group

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def vertex_group_assign_new(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Assign the selected vertices to a new vertex group

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def vertex_group_clean(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    group_select_mode: str | None = "",
    limit: typing.Any | None = 0.0,
    keep_single: bool | typing.Any | None = False,
):
    """Remove vertex group assignments which are not required

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param group_select_mode: Subset, Define which subset of Groups shall be used
    :type group_select_mode: str | None
    :param limit: Limit, Remove vertices which weight is below or equal to this limit
    :type limit: typing.Any | None
    :param keep_single: Keep Single, Keep verts assigned to at least one group when cleaning
    :type keep_single: bool | typing.Any | None
    """

    ...

def vertex_group_copy(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Make a copy of the active vertex group

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def vertex_group_copy_to_linked(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Replace vertex groups of all users of the same geometry data by vertex groups of active object

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def vertex_group_copy_to_selected(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Replace vertex groups of selected objects by vertex groups of active object

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def vertex_group_deselect(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Deselect all selected vertices assigned to the active vertex group

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def vertex_group_fix(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    dist: typing.Any | None = 0.0,
    strength: typing.Any | None = 1.0,
    accuracy: typing.Any | None = 1.0,
):
    """Modify the position of selected vertices by changing only their respective groups' weights (this tool may be slow for many vertices)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param dist: Distance, The distance to move to
    :type dist: typing.Any | None
    :param strength: Strength, The distance moved can be changed by this multiplier
    :type strength: typing.Any | None
    :param accuracy: Change Sensitivity, Change the amount weights are altered with each iteration: lower values are slower
    :type accuracy: typing.Any | None
    """

    ...

def vertex_group_invert(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    group_select_mode: str | None = "",
    auto_assign: bool | typing.Any | None = True,
    auto_remove: bool | typing.Any | None = True,
):
    """Invert active vertex group's weights

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param group_select_mode: Subset, Define which subset of Groups shall be used
    :type group_select_mode: str | None
    :param auto_assign: Add Weights, Add verts from groups that have zero weight before inverting
    :type auto_assign: bool | typing.Any | None
    :param auto_remove: Remove Weights, Remove verts from groups that have zero weight after inverting
    :type auto_remove: bool | typing.Any | None
    """

    ...

def vertex_group_levels(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    group_select_mode: str | None = "",
    offset: typing.Any | None = 0.0,
    gain: typing.Any | None = 1.0,
):
    """Add some offset and multiply with some gain the weights of the active vertex group

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param group_select_mode: Subset, Define which subset of Groups shall be used
    :type group_select_mode: str | None
    :param offset: Offset, Value to add to weights
    :type offset: typing.Any | None
    :param gain: Gain, Value to multiply weights by
    :type gain: typing.Any | None
    """

    ...

def vertex_group_limit_total(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    group_select_mode: str | None = "",
    limit: typing.Any | None = 4,
):
    """Limit deform weights associated with a vertex to a specified number by removing lowest weights

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param group_select_mode: Subset, Define which subset of Groups shall be used
    :type group_select_mode: str | None
    :param limit: Limit, Maximum number of deform weights
    :type limit: typing.Any | None
    """

    ...

def vertex_group_lock(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    action: str | None = "TOGGLE",
):
    """Change the lock state of all vertex groups of active object

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param action: Action, Lock action to execute on vertex groups

    TOGGLE Toggle, Unlock all vertex groups if there is at least one locked group, lock all in other case.

    LOCK Lock, Lock all vertex groups.

    UNLOCK Unlock, Unlock all vertex groups.

    INVERT Invert, Invert the lock state of all vertex groups.
        :type action: str | None
    """

    ...

def vertex_group_mirror(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mirror_weights: bool | typing.Any | None = True,
    flip_group_names: bool | typing.Any | None = True,
    all_groups: bool | typing.Any | None = False,
    use_topology: bool | typing.Any | None = False,
):
    """Mirror vertex group, flip weights and/or names, editing only selected vertices, flipping when both sides are selected otherwise copy from unselected

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mirror_weights: Mirror Weights, Mirror weights
    :type mirror_weights: bool | typing.Any | None
    :param flip_group_names: Flip Group Names, Flip vertex group names
    :type flip_group_names: bool | typing.Any | None
    :param all_groups: All Groups, Mirror all vertex groups weights
    :type all_groups: bool | typing.Any | None
    :param use_topology: Topology Mirror, Use topology based mirroring (for when both sides of mesh have matching, unique topology)
    :type use_topology: bool | typing.Any | None
    """

    ...

def vertex_group_move(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    direction: str | None = "UP",
):
    """Move the active vertex group up/down in the list

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Direction, Direction to move the active vertex group towards
    :type direction: str | None
    """

    ...

def vertex_group_normalize(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Normalize weights of the active vertex group, so that the highest ones are now 1.0

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def vertex_group_normalize_all(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    group_select_mode: str | None = "",
    lock_active: bool | typing.Any | None = True,
):
    """Normalize all weights of all vertex groups, so that for each vertex, the sum of all weights is 1.0

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param group_select_mode: Subset, Define which subset of Groups shall be used
    :type group_select_mode: str | None
    :param lock_active: Lock Active, Keep the values of the active group while normalizing others
    :type lock_active: bool | typing.Any | None
    """

    ...

def vertex_group_quantize(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    group_select_mode: str | None = "",
    steps: typing.Any | None = 4,
):
    """Set weights to a fixed number of steps

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param group_select_mode: Subset, Define which subset of Groups shall be used
    :type group_select_mode: str | None
    :param steps: Steps, Number of steps between 0 and 1
    :type steps: typing.Any | None
    """

    ...

def vertex_group_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    all: bool | typing.Any | None = False,
    all_unlocked: bool | typing.Any | None = False,
):
    """Delete the active or all vertex groups from the active object

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param all: All, Remove all vertex groups
    :type all: bool | typing.Any | None
    :param all_unlocked: All Unlocked, Remove all unlocked vertex groups
    :type all_unlocked: bool | typing.Any | None
    """

    ...

def vertex_group_remove_from(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    use_all_groups: bool | typing.Any | None = False,
    use_all_verts: bool | typing.Any | None = False,
):
    """Remove the selected vertices from active or all vertex group(s)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_all_groups: All Groups, Remove from all groups
    :type use_all_groups: bool | typing.Any | None
    :param use_all_verts: All Verts, Clear the active group
    :type use_all_verts: bool | typing.Any | None
    """

    ...

def vertex_group_select(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select all the vertices assigned to the active vertex group

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def vertex_group_set_active(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    group: str | None = "",
):
    """Set the active vertex group

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param group: Group, Vertex group to set as active
    :type group: str | None
    """

    ...

def vertex_group_smooth(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    group_select_mode: str | None = "",
    factor: typing.Any | None = 0.5,
    repeat: typing.Any | None = 1,
    expand: typing.Any | None = 0.0,
):
    """Smooth weights for selected vertices

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param group_select_mode: Subset, Define which subset of Groups shall be used
    :type group_select_mode: str | None
    :param factor: Factor
    :type factor: typing.Any | None
    :param repeat: Iterations
    :type repeat: typing.Any | None
    :param expand: Expand/Contract, Expand/contract weights
    :type expand: typing.Any | None
    """

    ...

def vertex_group_sort(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    sort_type: str | None = "NAME",
):
    """Sort vertex groups

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param sort_type: Sort type, Sort type
    :type sort_type: str | None
    """

    ...

def vertex_parent_set(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Parent selected objects to the selected vertices

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def vertex_weight_copy(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Copy weights from active to selected

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def vertex_weight_delete(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    weight_group: typing.Any | None = -1,
):
    """Delete this weight from the vertex (disabled if vertex group is locked)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param weight_group: Weight Index, Index of source weight in active vertex group
    :type weight_group: typing.Any | None
    """

    ...

def vertex_weight_normalize_active_vertex(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Normalize active vertex's weights

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def vertex_weight_paste(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    weight_group: typing.Any | None = -1,
):
    """Copy this group's weight to other selected verts (disabled if vertex group is locked)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param weight_group: Weight Index, Index of source weight in active vertex group
    :type weight_group: typing.Any | None
    """

    ...

def vertex_weight_set_active(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    weight_group: typing.Any | None = -1,
):
    """Set as active vertex group

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param weight_group: Weight Index, Index of source weight in active vertex group
    :type weight_group: typing.Any | None
    """

    ...

def visual_transform_apply(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Apply the object's visual transformation to its data

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def voxel_remesh(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Calculates a new manifold mesh based on the volume of the current mesh. All data layers will be lost

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...
