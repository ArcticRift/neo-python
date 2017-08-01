
from .MemoryStream import MemoryStream
from .BinaryReader import BinaryReader
import importlib


class Helper(object):

    @staticmethod
    def AsSerializableWithType(buffer, class_name):

        module = '.'.join(class_name.split('.')[:-1])
        klassname = class_name.split('.')[-1]
        klass = getattr(importlib.import_module(module), klassname)
        serializable = klass()

        mstream = MemoryStream(buffer)
        reader = BinaryReader(mstream)

        serializable.Deserialize(reader)

        return serializable