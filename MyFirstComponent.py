#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file MyFirstComponent.py
 @brief ${rtcParam.description}
 @date $Date$


"""
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist
import CosNaming

import MoveService_idl

# Import Service implementation class
# <rtc-template block="service_impl">
from MoveService_idl_example import *

import InPortTestConsumer, InPortTestProvider

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
myfirstcomponent_spec = ["implementation_id", "MyFirstComponent", 
		 "type_name",         "MyFirstComponent", 
		 "description",       "${rtcParam.description}", 
		 "version",           "1.0", 
		 "vendor",            "Vendor", 
		 "category",          "Category", 
		 "activity_type",     "STATIC", 
		 "max_instance",      "0", 
		 "language",          "Python", 
		 "lang_type",         "SCRIPT",
		 ""]
# </rtc-template>

##
# @class MyFirstComponent
# @brief ${rtcParam.description}
# 
# 
class MyFirstComponent(OpenRTM_aist.DataFlowComponentBase):
	
	##
	# @brief constructor
	# @param manager Maneger Object
	# 
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		self._d_in = RTC.TimedDouble(RTC.Time(0,0),0)
		"""
		"""
		self._inIn = OpenRTM_aist.InPort("in", self._d_in)
		self._d_out = RTC.TimedDouble(RTC.Time(0,0),0)
		"""
		"""
		self._outOut = OpenRTM_aist.OutPort("out", self._d_out)

		"""
		"""
		self._servicePort = OpenRTM_aist.CorbaPort("service")

		"""
		"""
		self._moveService = MoveService_i()
		


		# initialize of configuration-data.
		# <rtc-template block="init_conf_param">
		
		# </rtc-template>


		 
	##
	#
	# The initialize action (on CREATED->ALIVE transition)
	# formaer rtc_init_entry() 
	# 
	# @return RTC::ReturnCode_t
	# 
	#
	def onInitialize(self):
		# Bind variables and configuration variable
		
		# Set InPort buffers
		self.addInPort("in",self._inIn)
		
		# Set OutPort buffers
		self.addOutPort("out",self._outOut)
		
		# Set service provider to Ports
		self._servicePort.registerProvider("moveService", "MoveService", self._moveService)
		
		# Set service consumers to Ports
		
		# Set CORBA Service Ports
		self.addPort(self._servicePort)
		self.flag = 0

		mgr = OpenRTM_aist.Manager.instance()
		port = mgr.getPOA().reference_to_servant(self.get_ports()[0])

				
		
		
		name  = "dataports.port_cxt/"
		name += "test.topic_cxt/"
		name += "in"
		name += ".inport"
		#print dir(port)
		#mgr._namingManager.bindPortObject(name, port)
		#mgr._namingManager.bindObject(name, self._moveService)
		p = self.get_ports()[0]
		prof = p.get_port_profile()
		#prop = OpenRTM_aist.Properties()
		#OpenRTM_aist.NVUtil.copyToProperties(prop, prof.properties)
		#prop.setProperty("publish_topic","test")
		#OpenRTM_aist.NVUtil.copyFromProperties(prof.properties,prop)
		OpenRTM_aist.CORBA_SeqUtil.push_back(prof.properties, OpenRTM_aist.NVUtil.newNV("publish_topic","test"))
		#print prof.properties
		#prop.setProperty("publish_topic","test")
		mgr = OpenRTM_aist.Manager.instance()
		#mgr.publishPorts(self)
		ns = mgr._namingManager._names
		name  = "dataports.port_cxt/"
		name += "test.topic_cxt"
		#print mgr.getPortsOnNameServers(name,"outport")
		#mgr.subscribePorts(self)
		#print dir(RTC._objref_PortService)
		
		for n in ns:
			noc = n.ns
			if noc is None:
				continue
			cns = noc._cosnaming
			name  = "dataports.port_cxt/"
			name += "test.topic_cxt"
			
			"""orb = mgr.getORB()
			poa = mgr.getPOA()
			obj = noc._cosnaming.getRootContext()
			rootContext = obj._narrow(CosNaming.NamingContext)
			name = [CosNaming.NameComponent("test", "my_context")]
			testContext = rootContext.bind_new_context(name)
			name = [CosNaming.NameComponent("ExampleEcho", "Object")]
			testContext.bind(name, port._this())"""
			
			#print cns.resolveStr("Owner.host_cxt/MyFirstComponent0.rtc")
			#print cns.listByKind(name,"inport")
			#bl = cns.getRootContext().list(100)
			#bl = tuple()
			#bl =  CosNaming.Binding("","")
			
			#print dir(cns)
			#name = "MyFirstComponent0"
			#print cns.resolveStr(name)
		
		return RTC.RTC_OK
	
	#	##
	#	# 
	#	# The finalize action (on ALIVE->END transition)
	#	# formaer rtc_exiting_entry()
	#	# 
	#	# @return RTC::ReturnCode_t
	#
	#	# 
	#def onFinalize(self):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The startup action when ExecutionContext startup
	#	# former rtc_starting_entry()
	#	# 
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onStartup(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The shutdown action when ExecutionContext stop
	#	# former rtc_stopping_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onShutdown(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The activated action (Active state entry action)
	#	# former rtc_active_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	# 
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	def onActivated(self, ec_id):
		
		
		return RTC.RTC_OK
	
	#	##
	#	#
	#	# The deactivated action (Active state exit action)
	#	# former rtc_active_exit()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onDeactivated(self, ec_id):
	#
	#	return RTC.RTC_OK
	
		##
		#
		# The execution action that is invoked periodically
		# former rtc_active_do()
		#
		# @param ec_id target ExecutionContext Id
		#
		# @return RTC::ReturnCode_t
		#
		#
	def onExecute(self, ec_id):
		
		self.flag += 1
		if self.flag % 2 == 0:
			self._d_out.data = 100
			self._outOut.write()
		#print self._inIn.isNew()
		if self._inIn.isNew() or True:
			data = self._inIn.read()
			print data
		#print "MyFirstComponent: ",self._moveService
		return RTC.RTC_OK
	
	#	##
	#	#
	#	# The aborting action when main logic error occurred.
	#	# former rtc_aborting_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onAborting(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The error action in ERROR state
	#	# former rtc_error_do()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onError(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The reset action that is invoked resetting
	#	# This is same but different the former rtc_init_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onReset(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The state update action that is invoked after onExecute() action
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#

	#	#
	#def onStateUpdate(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The action that is invoked when execution context's rate is changed
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onRateChanged(self, ec_id):
	#
	#	return RTC.RTC_OK
	



def MyFirstComponentInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=myfirstcomponent_spec)
    manager.registerFactory(profile,
                            MyFirstComponent,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    MyFirstComponentInit(manager)

    # Create a component
    comp = manager.createComponent("MyFirstComponent")
    

def main():
	
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	#InPortTestConsumer.InPortTestConsumerInit()
	#InPortTestProvider.InPortTestProviderInit()
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()


if __name__ == "__main__":
	main()

