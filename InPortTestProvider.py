#!/usr/bin/env python
# -*- coding: euc-jp -*-



import OpenRTM_aist
import OpenRTM
from omniORB import cdrUnmarshal
import CORBA


class InPortTestProvider(OpenRTM_aist.InPortCorbaCdrProvider):

  def __init__(self):
    OpenRTM_aist.InPortCorbaCdrProvider.__init__(self)
    self.setInterfaceType("test")

  def put(self, data):
    try:

      if not self._connector:
        return OpenRTM.PORT_ERROR

      file_path = cdrUnmarshal(CORBA.TC_string, data)
      
      if file_path:
        with open(file_path, "rb") as fin:
          d = fin.read()
          ret = self._connector.write(d)
      

          return self.convertReturn(ret, d)

    except:
      self._rtcout.RTC_TRACE(OpenRTM_aist.Logger.print_exception())
      return OpenRTM.UNKNOWN_ERROR
    return OpenRTM.UNKNOWN_ERROR
    
      
      
      
    return self.convertReturn(ret, data)


def InPortTestProviderInit(manager):
  factory = OpenRTM_aist.InPortProviderFactory.instance()
  factory.addFactory("test",
                     InPortTestProvider,
                     OpenRTM_aist.Delete)
