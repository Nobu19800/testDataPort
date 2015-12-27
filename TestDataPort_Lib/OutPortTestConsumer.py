#!/usr/bin/env python
# -*- coding: euc-jp -*-



import OpenRTM_aist
import OpenRTM
from omniORB import cdrUnmarshal
import CORBA


class OutPortTestConsumer(OpenRTM_aist.OutPortCorbaCdrConsumer):

  def __init__(self):
    OpenRTM_aist.OutPortCorbaCdrConsumer.__init__(self)


    

  def get(self, data):
    
    try:
      outportcdr = self.getObject()._narrow(OpenRTM.OutPortCdr)
      ret,cdr_data = outportcdr.get()
      
      if ret == OpenRTM.PORT_OK:
        
        
        file_path = cdrUnmarshal(CORBA.TC_string, cdr_data)
        
        
        with open(file_path, "rb") as fin:
          data[0] = fin.read()
          self._buffer.put(data[0])
          self._buffer.advanceWptr()
          self._buffer.advanceRptr()

          return self.PORT_OK
        return self.convertReturn(ret,data[0])

    except:
      return self.CONNECTION_LOST

    return self.UNKNOWN_ERROR





def OutPortTestConsumerInit():
  factory = OpenRTM_aist.OutPortConsumerFactory.instance()
  factory.addFactory("test",
                     OutPortTestConsumer,
                     OpenRTM_aist.Delete)
  return
