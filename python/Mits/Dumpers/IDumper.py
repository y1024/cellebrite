import Mits.Configuration.Config as MitsConfig
from Mits.Utils.upy import upy

class IDumperBase(object):
    def dump(self):
    def open_output(self, prefix, middle, start=None, end=None, baseAddr=None) :
    def write_to_output(self, data, offset = None) :
    def close_output(self) :

class IDumperMitsBase(IDumperBase):
    def open_output(self, prefix, middle, start=None, end=None, baseAddr=None) :
    def write_to_output(self, data, offset = None) :
    def close_output(self) :
class IDumperUFEDBase(IDumperBase):
    def __init__(self, protocol):

    def open_output(self, prefix, middle, start=None, end=None, baseAddr=None) :
    def write_to_output(self, data, offset = None) :
    def close_output(self) :

if MitsConfig.IS_UFED :