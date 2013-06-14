#!/usr/bin/env python
'''
COPYRIGHT 2013 David Stuebe

This file is part of Wicken.

    Wicken is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Wicken is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Wicken.  If not, see <http://www.gnu.org/licenses/>.

@author David Stuebe <dstuebe@asasscience.com>
@file netcdf_dogma.py
@date 06/03/13
@description Implementation of the Dogma Metadata class for NetCDF IO using NetCDF4-Python
'''

from netCDF4 import Dataset
import dogma
from exceptions import WickenException

class NetCDFDogmaException(WickenException):
    """
    An exception class for catching problems in the NetCDF Dogma class
    """
    pass

class NetCDFDogma(dogma.Dogma):


    def __init__(self, religion, beliefs, dataObject=None):
    
        if dataObject is None: # allow none - what is the title?
            dataObject = Dataset('junk_metadata.nc','w')
            
        if not isinstance(dataObject, Dataset):
            raise TypeError('NetCDFDogma only allows NetCDF4 Dataset data objects!')

        super(NetCDFDogma, self).__init__(religion, beliefs, dataObject)   

    def _get(self,key):        
        try:
            return getattr(self._dataObject,key)
        except AttributeError:
            return None
        
    def _set(self,key,value):
        setattr(self._dataObject,key,value)
        
    def _write(self):
    
        self._dataObject.close()