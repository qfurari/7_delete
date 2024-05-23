#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file deleteObject.py
 @brief ModuleDescription
 @date $Date$


"""
# </rtc-template>

import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist


# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
deleteobject_spec = ["implementation_id", "deleteObject", 
         "type_name",         "deleteObject", 
         "description",       "ModuleDescription", 
         "version",           "1.0.0", 
         "vendor",            "VenderName", 
         "category",          "Category", 
         "activity_type",     "STATIC", 
         "max_instance",      "1", 
         "language",          "Python", 
         "lang_type",         "SCRIPT",
         ""]
# </rtc-template>

# <rtc-template block="component_description">
##
# @class deleteObject
# @brief ModuleDescription
# 
# 
# </rtc-template>
class deleteObject(OpenRTM_aist.DataFlowComponentBase):
	
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_inCoordinate = OpenRTM_aist.instantiateDataType(RTC.TimedShortSeq)
        """
        """
        self._inCoordinateIn = OpenRTM_aist.InPort("inCoordinate", self._d_inCoordinate)
        self._d_id = OpenRTM_aist.instantiateDataType(RTC.TimedShort)
        """
        """
        self._idIn = OpenRTM_aist.InPort("id", self._d_id)
        self._d_inVoice = OpenRTM_aist.instantiateDataType(RTC.TimedOctetSeq)
        """
        """
        self._inVoiceIn = OpenRTM_aist.InPort("inVoice", self._d_inVoice)
        self._d_inImage = OpenRTM_aist.instantiateDataType(RTC.TimedOctetSeq)
        """
        """
        self._inImageIn = OpenRTM_aist.InPort("inImage", self._d_inImage)
        self._d_outVoice = OpenRTM_aist.instantiateDataType(RTC.TimedOctetSeq)
        """
        """
        self._outVoiceOut = OpenRTM_aist.OutPort("outVoice", self._d_outVoice)
        self._d_outImage = OpenRTM_aist.instantiateDataType(RTC.TimedOctetSeq)
        """
        """
        self._outImageOut = OpenRTM_aist.OutPort("outImage", self._d_outImage)
        self._d_outCoordinate = OpenRTM_aist.instantiateDataType(RTC.TimedShortSeq)
        """
        """
        self._outCoordinateOut = OpenRTM_aist.OutPort("outCoordinate", self._d_outCoordinate)


		


        # initialize of configuration-data.
        # <rtc-template block="init_conf_param">
		
        # </rtc-template>


		 
    ##
    #
    # The initialize action (on CREATED->ALIVE transition)
    # 
    # @return RTC::ReturnCode_t
    # 
    #
    def onInitialize(self):
        # Bind variables and configuration variable
		
        # Set InPort buffers
        self.addInPort("inCoordinate",self._inCoordinateIn)
        self.addInPort("id",self._idIn)
        self.addInPort("inVoice",self._inVoiceIn)
        self.addInPort("inImage",self._inImageIn)
		
        # Set OutPort buffers
        self.addOutPort("outVoice",self._outVoiceOut)
        self.addOutPort("outImage",self._outImageOut)
        self.addOutPort("outCoordinate",self._outCoordinateOut)
		
        # Set service provider to Ports
		
        # Set service consumers to Ports
		
        # Set CORBA Service Ports
		
        return RTC.RTC_OK
	
    ###
    ## 
    ## The finalize action (on ALIVE->END transition)
    ## 
    ## @return RTC::ReturnCode_t
    #
    ## 
    #def onFinalize(self):
    #

    #    return RTC.RTC_OK
	
    ###
    ##
    ## The startup action when ExecutionContext startup
    ## 
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onStartup(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The shutdown action when ExecutionContext stop
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onShutdown(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ##
    #
    # The activated action (Active state entry action)
    #
    # @param ec_id target ExecutionContext Id
    # 
    # @return RTC::ReturnCode_t
    #
    #
    def onActivated(self, ec_id):
    
        return RTC.RTC_OK
	
    ##
    #
    # The deactivated action (Active state exit action)
    #
    # @param ec_id target ExecutionContext Id
    #
    # @return RTC::ReturnCode_t
    #
    #
    def onDeactivated(self, ec_id):
    
        return RTC.RTC_OK
	
    ##
    #
    # The execution action that is invoked periodically
    #
    # @param ec_id target ExecutionContext Id
    #
    # @return RTC::ReturnCode_t
    #
    #
    def onExecute(self, ec_id):
              # idポートからデータを読み込む
        # 入力ポートからデータを受け取り、変数に代入する処理
        if self._inVoiceIn.isNew():
            print("#####オブジェクトデリート######")
            #追加音声の読み込み
            print("音声読み込み開始")
            voiceIn_data_list = []
            while self._inVoiceIn.isNew():
                voiceIn_data = self._inVoiceIn.read().data
                #voiceIn_data_list += voiceIn_data
                voiceIn_data_list.append(voiceIn_data)
            print("現在の音声配列の長さ："+ str(len(voiceIn_data_list)))

        if self._inImageIn.isNew():
            #追加画像の読み込み
            print("画像読み込み開始")
            imageIn_data_list = []
            while self._inImageIn.isNew():
                imageIn_data = self._inImageIn.read().data
                #imageIn_data_list += imageIn_data
                imageIn_data_list.append(imageIn_data)
            print("現在の画像配列の長さ："+ str(len(imageIn_data_list)))

        if self._inCoordinateIn.isNew():
            #追加座標の読み込み
            print("座標読み込み開始")
            coordinateIn_data_list = []
            while self._inCoordinateIn.isNew():
                coordinateIn_data = self._inCoordinateIn.read().data
                coordinateIn_data_list.append(coordinateIn_data)
            print("現在の座標配列の長さ："+ str(len(coordinateIn_data_list)))
        # 入力データのチェック
        
        if self._idIn.isNew():
            id_data = self._idIn.read()
            id_number = id_data.data
            
                # ここで各配列とidの値を使った処理を行う
            del voiceIn_data_list[id_number]
            del imageIn_data_list[id_number]
            del coordinateIn_data[id_number]
            print("現在の音声配列の長さ："+ str(len(voiceIn_data_list)))
            print("現在の画像配列の長さ："+ str(len(imageIn_data_list)))
            print("現在の座標配列の長さ："+ str(len(coordinateIn_data_list)))
           #Voice出力
            for data in voiceIn_data_list:
                Outvoice = RTC.TimedOctetSeq(RTC.Time(0,0),data)
            self._outVoiceOut.write(Outvoice)
            #imageの出力
            for data in imageIn_data_list:
                Outimage = RTC.TimedOctetSeq(RTC.Time(0,0),data)
            self._outImageOut.write(Outimage)
            #座標の出力
            for data in coordinateIn_data_list:
                OutCoordinate = RTC.TimedShortSeq(RTC.Time(0,0),data)
                self._outCoordinateOut.write(OutCoordinate)
            # 入力データが揃っていない場合は処理を中断
            
        return RTC.RTC_OK
        
    
      
	
    ###
    ##
    ## The aborting action when main logic error occurred.
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onAborting(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The error action in ERROR state
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onError(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The reset action that is invoked resetting
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onReset(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The state update action that is invoked after onExecute() action
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##

    ##
    #def onStateUpdate(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The action that is invoked when execution context's rate is changed
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onRateChanged(self, ec_id):
    #
    #    return RTC.RTC_OK
	



def deleteObjectInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=deleteobject_spec)
    manager.registerFactory(profile,
                            deleteObject,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    deleteObjectInit(manager)

    # create instance_name option for createComponent()
    instance_name = [i for i in sys.argv if "--instance_name=" in i]
    if instance_name:
        args = instance_name[0].replace("--", "?")
    else:
        args = ""
  
    # Create a component
    comp = manager.createComponent("deleteObject" + args)

def main():
    # remove --instance_name= option
    argv = [i for i in sys.argv if not "--instance_name=" in i]
    # Initialize manager
    mgr = OpenRTM_aist.Manager.init(sys.argv)
    mgr.setModuleInitProc(MyModuleInit)
    mgr.activateManager()
    mgr.runManager()

if __name__ == "__main__":
    main()

