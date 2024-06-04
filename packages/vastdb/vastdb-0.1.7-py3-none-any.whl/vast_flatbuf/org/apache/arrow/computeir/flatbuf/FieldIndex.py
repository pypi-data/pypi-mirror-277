# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuf

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

# Field name in a relation, in ordinal position of the relation's schema.
class FieldIndex(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FieldIndex()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsFieldIndex(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # FieldIndex
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # FieldIndex
    def Position(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(1)
def FieldIndexStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddPosition(builder, position): builder.PrependUint32Slot(0, position, 0)
def FieldIndexAddPosition(builder, position):
    """This method is deprecated. Please switch to AddPosition."""
    return AddPosition(builder, position)
def End(builder): return builder.EndObject()
def FieldIndexEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)