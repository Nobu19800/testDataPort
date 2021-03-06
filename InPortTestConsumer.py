#!/usr/bin/env python
# -*- coding: euc-jp -*-


import OpenRTM_aist
import OpenRTM
import CORBA
from omniORB import cdrMarshal


class InPortTestConsumer(OpenRTM_aist.InPortCorbaCdrConsumer):

  def __init__(self):
    OpenRTM_aist.InPortCorbaCdrConsumer.__init__(self)
    self.file_path = str(OpenRTM_aist.uuid1())+".dat"

  def put(self, data):
    try:
      ref_ = self.getObject()
      if ref_:
        inportcdr = ref_._narrow(OpenRTM.InPortCdr)
        with open(self.file_path, "wb") as fout:
          fout.write(data)
          
        mar_file_path = cdrMarshal(CORBA.TC_string, self.file_path)
        
        return self.convertReturnCode(inportcdr.put(mar_file_path))
      return self.CONNECTION_LOST
    except:
      self._rtcout.RTC_ERROR(OpenRTM_aist.Logger.print_exception())
      return self.CONNECTION_LOST
    
      
      
      
    return self.convertReturn(ret, data)

def InPortTestConsumerInit(manager):
  factory = OpenRTM_aist.InPortConsumerFactory.instance()
  factory.addFactory("test",
                     InPortTestConsumer,
                     OpenRTM_aist.Delete)
