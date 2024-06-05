import typing
import collections.abc
from . import action
from . import anim
from . import armature
from . import boid
from . import brush
from . import buttons
from . import cachefile
from . import camera
from . import clip
from . import cloth
from . import collection
from . import console
from . import constraint
from . import curve
from . import cycles
from . import dpaint
from . import ed
from . import export_anim
from . import export_mesh
from . import export_scene
from . import file
from . import fluid
from . import font
from . import gizmogroup
from . import gpencil
from . import graph
from . import image
from . import import_anim
from . import import_curve
from . import import_mesh
from . import import_scene
from . import info
from . import lattice
from . import marker
from . import mask
from . import material
from . import mball
from . import mesh
from . import nla
from . import node
from . import object
from . import outliner
from . import paint
from . import paintcurve
from . import palette
from . import particle
from . import pose
from . import poselib
from . import preferences
from . import ptcache
from . import render
from . import rigidbody
from . import safe_areas
from . import scene
from . import screen
from . import script
from . import sculpt
from . import sequencer
from . import simulation
from . import sound
from . import surface
from . import text
from . import texture
from . import transform
from . import ui
from . import uv
from . import view2d
from . import view3d
from . import wm
from . import workspace
from . import world

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

class BPyOps:
    """Fake module like class."""

    ...

class BPyOpsSubMod:
    """Utility class to fake submodules.eg. bpy.ops.object"""

    ...

class BPyOpsSubModOp:
    def get_rna_type(self):
        """Internal function for introspection"""
        ...

    def idname(self): ...
    def idname_py(self): ...
    def poll(self, args):
        """

        :param args:
        """
        ...
