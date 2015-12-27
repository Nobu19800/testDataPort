#!/usr/bin/env python
# -*- coding: euc-jp -*-


import os
import OpenRTM_aist
import OpenRTM
import CORBA
from omniORB import cdrMarshal


class OutPortTestProvider(OpenRTM_aist.OutPortCorbaCdrProvider):

  def __init__(self):
    OpenRTM_aist.OutPortCorbaCdrProvider.__init__(self)
    self.setInterfaceType("test")
    self.file_path = os.path.abspath(str(OpenRTM_aist.uuid1())+".dat")

  def __del__(self):
    OpenRTM_aist.OutPortCorbaCdrProvider.__del__(self)
    if os.path.exists(self.file_path):
      os.remove(self.file_path)

  def get(self):
    
    try:
      if self._buffer.empty():
        return (OpenRTM.BUFFER_EMPTY, None)
      
      cdr = [None]
      ret = self._buffer.read(cdr)
      
      with open(self.file_path, "wb") as fout:
          fout.write(cdr[0])
      

      
    except:
      self._rtcout.RTC_TRACE(OpenRTM_aist.Logger.print_exception())
      return (OpenRTM.UNKNOWN_ERROR, None)
    
    mar_file_path = cdrMarshal(CORBA.TC_string, self.file_path)
    return self.convertReturn(ret, mar_file_path)
    



def OutPortTestProviderInit():
  factory = OpenRTM_aist.OutPortProviderFactory.instance()
  factory.addFactory("test",
                     OutPortTestProvider,
                     OpenRTM_aist.Delete)
