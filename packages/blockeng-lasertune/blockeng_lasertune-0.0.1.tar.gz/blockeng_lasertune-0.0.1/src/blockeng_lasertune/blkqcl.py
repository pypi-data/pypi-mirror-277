import http.client
import urllib.error
import urllib.request
import base64
import socket
from urllib.parse import urlparse
import xml.etree.ElementTree as ET

_SOAPENV_NS = "http://schemas.xmlsoap.org/soap/envelope/"

_kNS_Automatic = "automatic"

"""
DOCS
"""


class BLKQCL_Proxy:
    __url = ""

    __namespaces = {}

    """
    DOCS
    """
    kMESSAGE_TIMESTAMP = "timestamp"

    """
        April release of BLK15-Controller WSDL
    """
    kNS_2014_04 = "http://www.blockeng.com/Schemas/2014-04/BLK-15/"

    """
        July 2014 release
    """
    kNS_2014_07 = "http://www.blockeng.com/Schemas/2014-07/BLKQCL/"

    """
        May 2015 release (System Release 0.02)
    """
    kNS_2015_05 = "http://www.blockeng.com/Schemas/2015-05/BLKQCL/"

    """
        May 2016 (System Release 3)
    """
    kNS_2016_05 = "http://www.blockeng.com/Schemas/2016-05/BLKQCL/"

    """
        April 2017
    """
    kNS_2017_04 = "http://www.blockeng.com/Schemas/2017-04/BLKQCL/"

    """
        Use this if you have a mix of devices with different software versions, to make your code independent of
        BLK15 software version (within limits)
    """
    kNS_Automatic = _kNS_Automatic

    __ns = None

    __authorization_credentials = None

    """
    SensorDataKind
    """
    kAllSensors = {}

    """
    SensorDataKind - enumeration of different kinds of sensors.
    """
    class SensorDataKind:
        Accelerometer = "Accelerometer"
        ActiveLaser = "ActiveLaser"
        DetectorTemperature = "DetectorTemperature"
        ElectricalBoardTemperature = "ElectricalBoardTemperature"
        ExternalPressure1 = "ExternalPressure1"
        ExternalPressure2 = "ExternalPressure2"
        ExternalPressure3 = "ExternalPressure3"
        ExternalPressure4 = "ExternalPressure4"
        ExternalTemperature1 = "ExternalTemperature1"
        ExternalTemperature2 = "ExternalTemperature2"
        ExternalTemperature3 = "ExternalTemperature3"
        ExternalTemperature4 = "ExternalTemperature4"
        LaserCurrent = "LaserCurrent"
        LaserTemperature = "LaserTemperature"
        LaserVoltage = "LaserVoltage"
        MirrorTemperature = "MirrorTemperature"
        RangeFinder = "RangeFinder"
        SystemHumidity = "SystemHumidity"
        SystemTemperature = "SystemTemperature"

    """
    AlarmKind
    """
    kAllAlarms: dict = {}

    """
    AlarmType - enumeration of different alarms.
    """
    class AlarmType:
        Critical_CannotTalkToFPGA = "Critical_CannotTalkToFPGA"
        Critical_LaserOverDriving = "Critical_LaserOverDriving"
        Critical_LaserOverheating = "Critical_LaserOverheating"
        Critical_MirrorOverCurrent = "Critical_MirrorOverCurrent"
        Critical_MirrorNoCurrent = "Critical_MirrorNoCurrent"
        Critical_SystemOverTemperature = "Critical_SystemOverTemperature"
        Critical_LowVoltageFromPowerBoard = "Critical_LowVoltageFromPowerBoard"
        Error_LaserTemperatureNotSettled = "Error_LaserTemperatureNotSettled"
        Error_SystemTemperatureNotSettled = "Error_SystemTemperatureNotSettled"
        Error_DetectorTemperatureNotLocked = "Error_DetectorTemperatureNotLocked"
        Error_ThermalControlFault = "Error_ThermalControlFault"
        Error_PulseParameterFault = "Error_PulseParameterFault"
        Warning_AmbientTemperatureTooHigh = "Warning_AmbientTemperatureTooHigh"
        Warning_VibrationTooHigh = "Warning_VibrationTooHigh"
        Warning_DetectorSignalTooCloseToSaturationLevel = "Warning_DetectorSignalTooCloseToSaturationLevel"
        Warning_LaserImpedenceTooHigh = "Warning_LaserImpedenceTooHigh"
        Warning_MirrorImpedenceTooHigh = "Warning_MirrorImpedenceTooHigh"
        Warning_CalibrationTooHigh = "Warning_CalibrationTooHigh"
        Warning_UserDiskspaceLow = "Warning_UserDiskspaceLow"

    """
    ToggleSwitchType
    """

    class ToggleSwitchType:
        FanA = "FanA"
        FanB = "FanB"
        SolenoidA = "SolenoidA"
        SolenoidB = "SolenoidB"

    """
    ToggleStateType - TBD.
    """
    class ToggleStateType:
        Off = "Off"
        On = "On"

    """
    SOAPFault
    """
    class SOAPFault(BaseException):
        OriginalException = None
        FaultString = ""

        def __init__(self, origE, faultStr):
            self.OriginalException = origE
            self.FaultString = faultStr

    """
    TBD.
    Very primitive http connection facility, but enough to do simple http pipelining...
    Quite surprised I couldnt find an existing python implementation
    """

    class HomogeneousPipeline:
        __numberOfPrefetches = 2
        __buffer = []
        __sock = None
        __closeOnNextCall = False
        __useMsg = None

        def __init__(self, numberOfPrefetches=2):
            # print("***HomogeneousPipeline::CTOR")
            self.__numberOfPrefetches = numberOfPrefetches
            self.__buffer = []
            self.__sock = None

        def doSend(self, proxy, httpHeaders, soapEnvelope):
            # print ("***ENTER doSend")
            if self.__closeOnNextCall:
                # print ("***got self.__closeOnNextCall")
                self.__closeOnNextCall = False
                self.doClose()
            openingConnection = (self.__sock is None)
            self.__mkConnIfNeeded(proxy)

            # only compute once and re-use
            if self.__useMsg is None:
                method = "POST"
                url = "/"
                http_vsn_str = "HTTP/1.1"
                hdr = "%s %s %s" % (method, url, http_vsn_str)
                self.__buffer.append(hdr)

                httpHeaders["Content-Length"] = str(len(soapEnvelope))
                for hdr, value in httpHeaders.iteritems():
                    self.__putheader(hdr, value)
                self.__buffer.extend(("", ""))
                msg = "\r\n".join(self.__buffer)
                del self.__buffer[:]
                msg += soapEnvelope
                self.__useMsg = msg
            # print "***indoSend: msg=", self.__useMsg
            self.__sock.sendall(self.__useMsg)
            if openingConnection:
                for i in range(1, self.__numberOfPrefetches):
                    self.__sock.sendall(self.__useMsg)

        def doReceiveNext(self):
            # print ("***ENTER doReceiveNext")
            kwds: dict = {"method": "POST"}
            kwds["buffering"] = True
            response = http.client.HTTPResponse(self.__sock, **kwds)
            try:
                response.begin()
                if response.will_close:
                    # print ("***response.will_close =", response.will_close)
                    # print ("***AND response.status =", response.status)
                    self.__closeOnNextCall = True
            except:
                # print ("***doReceiveNext exception caught - setting __closeOnNextCall")
                self.__closeOnNextCall = True
                raise

            return response

        def __putheader(self, header, *values):
            """Send a request header line to the server.
            For example: h.putheader('Accept', 'text/html')
            """
            hdr = "%s: %s" % (header, "\r\n\t".join([str(v) for v in values]))
            self.__buffer.append(hdr)

        def __mkConnIfNeeded(self, proxy):
            if self.__sock is None:
                # print ("***opening new sock")
                timeout = 12
                source_address = None
                host = urlparse(proxy.GetEffectiveURL()).hostname
                port = urlparse(proxy.GetEffectiveURL()).port
                if port is None:
                    port = 8080
                self.__sock = socket.create_connection((host, port), timeout, source_address)

        def doClose(self):
            if self.__sock:
                self.__sock.close()
                self.__sock = None

    __pipeline = None

    # PRIVATE
    def __make_base_auth(self, user, password):
        tok = user + ":" + password
        hash = base64.b64encode(tok)
        return "Basic " + hash

    """
    DOCS
        If pipelined is False (default) this is a normal proxy
        If pipelined is True (or an unsinged # >= 1 - but only >=2 is useful) - then only the parameters from the first
        proxy call are captured and re-used for each subsequent call. Its illegal to call a 'pipedlined' proxy with diffeent
        arguments or differnt methods after its been started
    """

    def __init__(
            self,
            url,
            ns=_kNS_Automatic,
            authorization_credentials=None,
            authentication_username=None,
            authentication_password=None,
            pipelined=False
    ):
        # do (so far primitive) job of looking for leading http://, and default port#
        if url.find("http://") == -1:
            url = "http://" + url
        if url.find(":", 7) == -1:
            url = url + ":8080"
        self.__url = url

        # try each protocol version if automatic
        if ns == self.kNS_Automatic:
            try:
                ns = self.kNS_2017_04
                self.__ns = ns
                self.__namespaces = {"blk": self.__ns, "soapenv": _SOAPENV_NS}
                # ignore result - just for side-effect of failure or success
                self.GetDeviceName()
            except BLKQCL_Proxy.SOAPFault:
                ns = self.kNS_Automatic
        if ns == self.kNS_Automatic:
            try:
                ns = self.kNS_2016_05
                self.__ns = ns
                self.__namespaces = {"blk": self.__ns, "soapenv": _SOAPENV_NS}
                # ignore result - just for side-effect of failure or success
                self.GetDeviceName()
            except BLKQCL_Proxy.SOAPFault:
                ns = self.kNS_Automatic
        if ns == self.kNS_Automatic:
            try:
                ns = self.kNS_2015_05
                self.__ns = ns
                self.__namespaces = {"blk": self.__ns, "soapenv": _SOAPENV_NS}
                # ignore result - just for side-effect of failure or success
                self.GetDeviceName()
            except BLKQCL_Proxy.SOAPFault:
                ns = self.kNS_Automatic
        if ns == self.kNS_Automatic:
            try:
                ns = self.kNS_2014_07
                self.__ns = ns
                self.__namespaces = {"blk": self.__ns, "soapenv": _SOAPENV_NS}
                # ignore result - just for side-effect of failure or success
                self.GetDeviceName()
            except BLKQCL_Proxy.SOAPFault:
                ns = self.kNS_Automatic
        if ns == self.kNS_Automatic:
            try:
                ns = self.kNS_2014_04
                self.__ns = ns
                self.__namespaces = {"blk": self.__ns, "soapenv": _SOAPENV_NS}
                # ignore result - just for side-effect of failure or success
                self.GetDeviceName()
            except BLKQCL_Proxy.SOAPFault:
                ns = self.kNS_Automatic

        if ns == self.kNS_Automatic:
            raise BLKQCL_Proxy.SOAPFault(None, "Cannot automatically identify the protocol version")

        self.__ns = ns
        self.__namespaces = {"blk": self.__ns, "soapenv": _SOAPENV_NS}

        # AUTH
        if authorization_credentials is not None:
            if (authentication_username is not None) or (authentication_password is not None):
                raise Exception(
                    "authorization_credentials and authentication_username/authentication_password are "
                    "mutually exclusive"
                )
        if (authentication_username is None) is not (authentication_password is None):
            raise Exception(
                "authentication_username and authentication_password must either be both specified, or neither"
            )
        self.__authorization_credentials = authorization_credentials
        if self.__authorization_credentials is None and authentication_username is not None:
            self.__authorization_credentials = (
                self.__make_base_auth(authentication_username, authentication_password)
            )

        if pipelined is True:
            pipelined = 2
        if pipelined is not False:
            self.__pipeline = self.HomogeneousPipeline(numberOfPrefetches=pipelined)

    def GetEffectiveURL(self):
        return self.__url

    def GetFactorySettings(self, envelopeArgs=None, resultEnvelope=None) -> dict:
        """
        [public]    IConfiguration.GetFactorySettings () -> FactorySettingsType;
        [python]	dictionary GetFactorySettings (envelopeArgs = None, resultEnvelope = None)

        :param envelopeArgs:
        :param resultEnvelope:
        :return:
        """
        response = self.__doSendInnerCommandText_("<blk:GetFactorySettings/>")
        resp = response.read()
        # print ("raw response=", resp, "\n")
        root = ET.fromstring(resp)
        responseRoot = root.find(".//blk:GetFactorySettingsResponse", self.__namespaces)

        result = {}

        self.__Add2DictIf(
            result,
            "BiasDAC",
            responseRoot.find(".//blk:BiasDAC", self.__namespaces),
            (lambda elt: int(elt.text))
        )

        defaultUserSettingsNode = responseRoot.find(".//blk:DefaultUserSettings", self.__namespaces)
        if defaultUserSettingsNode is not None:
            result["DefaultUserSettings"] = self.__extractUserSettings(defaultUserSettingsNode)

        if self.__ns == self.kNS_2014_04:
            tmp = responseRoot.find(".//blk:CCUTemperatureSetPointRange", self.__namespaces)
            if tmp is not None:
                result["DetectorTemperatureSetPointRange"] = self.__extractRange_Float(tmp)
        else:
            tmp = responseRoot.find(".//blk:DetectorTemperatureSetPointRange", self.__namespaces)
            if tmp is not None:
                result["DetectorTemperatureSetPointRange"] = self.__extractRange_Float(tmp)

        if self.__ns == self.kNS_2014_04:
            tmp = responseRoot.find(".//blk:CCUTECPIDParameters", self.__namespaces)
            if tmp is not None:
                result["DetectorTECPIDParameters"] = self.__extractPID(tmp)
        else:
            tmp = responseRoot.find(".//blk:DetectorTECPIDParameters", self.__namespaces)
            if tmp is not None:
                result["DetectorTECPIDParameters"] = self.__extractPID(tmp)

        self.__Add2DictIf(
            result,
            "DetectorDarkMode",
            responseRoot.find(".//blk:DetectorDarkMode", self.__namespaces),
            (lambda elt: elt.text)
        )

        tmp = responseRoot.find(".//blk:LaserStitchPoints", self.__namespaces)
        if tmp is not None:
            explicit = []
            for exp in tmp.findall("./blk:Explicit", self.__namespaces):
                LowerTuner = int(exp.find("./blk:LowerTuner", self.__namespaces).text)
                UpperTuner = int(exp.find("./blk:UpperTuner", self.__namespaces).text)
                wn = float(exp.find("./blk:WaveNumber", self.__namespaces).text)
                explicit.append({"LowerTuner": LowerTuner, "UpperTuner": UpperTuner, "WaveNumber": wn})
            result["LaserStitchPoints"] = explicit

        tmp = responseRoot.find(".//blk:LaserPulseDurationLimit", self.__namespaces)
        if tmp is not None:
            result["LaserPulseDurationLimit"] = self.__extractRange(tmp)
        self.__Add2DictIf(
            result,
            "LaserDutyCycleLimit",
            responseRoot.find(".//blk:LaserDutyCycleLimit", self.__namespaces),
            (lambda elt: float(elt.text))
        )
        self.__Add2DictIf(
            result,
            "LightToPostDark",
            responseRoot.find(".//blk:LightToPostDark", self.__namespaces),
            (lambda elt: elt.text)
        )
        self.__Add2DictIf(
            result,
            "MirrorMoveSmoothingDuration",
            responseRoot.find(".//blk:MirrorMoveSmoothingDuration", self.__namespaces),
            (lambda elt: elt.text)
        )
        tmp = responseRoot.find(".//blk:OpticsTemperatureRange", self.__namespaces)
        if tmp is not None:
            result["OpticsTemperatureRange"] = self.__extractRange_Float(tmp)

        self.__Add2DictIf(
            result,
            "PreDarkToLight",
            responseRoot.find(".//blk:PreDarkToLight", self.__namespaces),
            (lambda elt: elt.text)
        )

        tmp = responseRoot.find(".//blk:SampleDelayRange", self.__namespaces)
        if tmp is not None:
            result["SampleDelayRange"] = self.__extractRange(tmp)

        if self.__ns == self.kNS_2014_04:
            tmp = responseRoot.find(".//blk:EnvironmentalOperationTemperatures", self.__namespaces)
            if tmp is not None:
                result["SystemTemperatureRange"] = self.__extractRange_Float(tmp)
        else:
            tmp = responseRoot.find(".//blk:SystemTemperatureRange", self.__namespaces)
            if tmp is not None:
                result["SystemTemperatureRange"] = self.__extractRange_Float(tmp)

        tmp = responseRoot.find(".//blk:SupportedFeatures", self.__namespaces)
        if tmp is not None:
            supportedFeatures = []
            for sf in tmp.findall(".//blk:SupportedFeature", self.__namespaces):
                supportedFeatures.append(sf.text)
            result["SupportedFeatures"] = supportedFeatures

        tmp = responseRoot.find(".//blk:ToggleSwitchInitialValues", self.__namespaces)
        if tmp is not None:
            toggleSwitchInitialValues = {}
            for sv in tmp.findall(".//blk:SwitchAndValue", self.__namespaces):
                toggleSwitchInitialValues[sv.attrib["Switch"]] = sv.attrib["InitialValue"]
            result["ToggleSwitchInitialValues"] = toggleSwitchInitialValues

        tuners = {}
        for tunerNode in root.findall(".//blk:Tuners/blk:Tuner", self.__namespaces):
            tunerN = {}
            tunerID = tunerNode.attrib["Tuner"]

            self.__Add2DictIf(
                tunerN,
                "ReferenceLaserVoltage",
                tunerNode.find(".//blk:ReferenceLaserVoltage", self.__namespaces),
                (lambda elt: float(elt.text))
            )
            tmp = tunerNode.find(".//blk:LaserWaveNumberRanges", self.__namespaces)
            if tmp is not None:
                tunerN["LaserWaveNumberRanges"] = self.__extractRange_Float(tmp)
            tmp = tunerNode.find(".//blk:TunerTECControlParameters", self.__namespaces)
            if tmp is not None:
                tunerN["TunerTECControlParameters"] = self.__extractPID(tmp)
            self.__Add2DictIf(
                tunerN,
                "TECCurrentUpperBound",
                tunerNode.find(".//blk:TECCurrentUpperBound", self.__namespaces),
                (lambda elt: float(elt.text))
            )
            tmp = tunerNode.find(".//blk:MirrorCurrentToDriveVoltageRelation", self.__namespaces)
            if tmp is not None:
                xxx = {}
                if tmp.find(".//blk:Slope", self.__namespaces) is not None:
                    xxx["Slope"] = float(tmp.find(".//blk:Slope", self.__namespaces).text)
                if tmp.find(".//blk:YIntercept", self.__namespaces) is not None:
                    xxx["YIntercept"] = float(tmp.find(".//blk:YIntercept", self.__namespaces).text)
                tunerN["MirrorCurrentToDriveVoltageRelation"] = xxx
            tmp = tunerNode.find(".//blk:LaserOperationTemperatures", self.__namespaces)
            if tmp is not None:
                tunerN["LaserOperationTemperatures"] = self.__extractRange_Float(tmp)
            tmp = tunerNode.find(".//blk:LaserPumpingVoltageBounds", self.__namespaces)
            if tmp is not None:
                tunerN["LaserPumpingVoltageBounds"] = self.__extractRange_Float(tmp)
            self.__Add2DictIf(
                tunerN,
                "LaserFixedPumpingVoltage",
                tunerNode.find(".//blk:LaserFixedPumpingVoltage", self.__namespaces),
                (lambda elt: float(elt.text))
            )
            self.__Add2DictIf(
                tunerN,
                "LaserMaximumPumpingCurrent",
                tunerNode.find(".//blk:LaserMaximumPumpingCurrent", self.__namespaces),
                (lambda elt: float(elt.text))
            )
            self.__Add2DictIf(
                tunerN,
                "ReferenceMirrorPosition",
                tunerNode.find(".//blk:ReferenceMirrorPosition", self.__namespaces),
                (lambda elt: float(elt.text))
            )
            tmp = tunerNode.find(".//blk:MirrorMovementRange", self.__namespaces)
            if tmp is not None:
                tunerN["MirrorMovementRange"] = self.__extractRange_int(tmp)
            self.__Add2DictIf(
                tunerN, "MirrorOperationFrequency",
                tunerNode.find(".//blk:MirrorOperationFrequency", self.__namespaces),
                (lambda elt: float(elt.text))
            )
            lvpv = {}
            for lpv in tunerNode.findall(".//blk:LaserVariablePumpingVoltage/blk:PumpingVoltage", self.__namespaces):
                lvpv[float(lpv.attrib["waveNumber"])] = float(lpv.text)
            tunerN["LaserVariablePumpingVoltage"] = lvpv
            wntdvct = {}
            for lpv in tunerNode.findall(".//blk:WaveNumberToDriveVoltageCalibrationTable/blk:Map", self.__namespaces):
                wntdvct[float(lpv.attrib["waveNumber"])] = int(lpv.attrib["drivingVoltage"])
            tunerN["WaveNumberToDriveVoltageCalibrationTable"] = wntdvct
            cur2wnTbl = {}
            for lpv in tunerNode.findall(".//blk:CurrentToWaveNumberCalibrationTable/blk:Map", self.__namespaces):
                cur2wnTbl[int(lpv.attrib["ADC"])] = float(lpv.attrib["waveNumber"])
            tunerN["CurrentToWaveNumberCalibrationTable"] = cur2wnTbl
            referenceNormalizationParametersNode = tunerNode.find(".//blk:ReferenceNormalizationParameters",
                                                                  self.__namespaces)
            if referenceNormalizationParametersNode is not None:
                rmp = {}
                self.__Add2DictIf(
                    rmp,
                    "ScanningSpeed",
                    referenceNormalizationParametersNode.find(".//blk:ScanningSpeed", self.__namespaces),
                    (lambda elt: float(elt.text))
                )
                self.__Add2DictIf(
                    rmp,
                    "NumberOfSamples",
                    referenceNormalizationParametersNode.find(".//blk:NumberOfSamples", self.__namespaces),
                    (lambda elt: float(elt.text))
                )
                self.__Add2DictIf(
                    rmp,
                    "LaserTemperature",
                    referenceNormalizationParametersNode.find(".//blk:LaserTemperature", self.__namespaces),
                    (lambda elt: float(elt.text))
                )
                self.__Add2DictIf(
                    rmp,
                    "StartPosition",
                    referenceNormalizationParametersNode.find(".//blk:StartPosition", self.__namespaces),
                    (lambda elt: float(elt.text))
                )
                self.__Add2DictIf(
                    rmp,
                    "StopPosition",
                    referenceNormalizationParametersNode.find(".//blk:StopPosition", self.__namespaces),
                    (lambda elt: float(elt.text))
                )
                tunerN["ReferenceNormalizationParameters"] = rmp

            tuners[tunerID] = tunerN
        result["Tuners"] = tuners

        if resultEnvelope is not None:
            self.__Add2DictIf(
                resultEnvelope,
                self.kMESSAGE_TIMESTAMP,
                root.find(".//blk:timestamp", self.__namespaces),
                (lambda elt: float(elt.text))
            )
        return result

    def GetUserSettings(self, envelopeArgs=None, resultEnvelope=None) -> dict:
        """
        [public]	IConfiguration.GetUserSettings () -> UserSettingsType
        [python]	dictionary	GetUserSettings (envelopeArgs = None, resultEnvelope = None)

        This retrieves all the user-settable, persistent options which control your BLK-15.

        :param envelopeArgs:
        :param resultEnvelope:
        :return:
        """
        response = self.__doSendInnerCommandText_("<blk:GetUserSettings/>")
        resp = response.read()
        # print ("raw response=", resp, "\n")
        root = ET.fromstring(resp)
        result = self.__extractUserSettings(root.find(".//blk:GetUserSettingsResponse", self.__namespaces))
        if resultEnvelope is not None:
            self.__Add2DictIf(
                resultEnvelope,
                self.kMESSAGE_TIMESTAMP,
                root.find(".//blk:timestamp", self.__namespaces),
                (lambda elt: float(elt.text))
            )
        return result

    def SetUserSettings(self, settings, envelopeArgs=None, resultEnvelope=None):
        """
        DOCS

        [public]    IConfiguration.SetUserSettings (UserSettingsType settings) -> void;
        [python]	void SetUserSettings (settings, envelopeArgs = None, resultEnvelope = None)

        This sets any (or all) of the user-settable, persistent options which control your BLK-15.
        This allows setting any single (or collection of) persistent options.

        EXAMPLE:

        proxy.SetUserSettings ({'LaserControlMode': 'InternallyControlled'});

        :param settings:
        :param envelopeArgs:
        :param resultEnvelope:
        :return:
        """
        innerCmdText = self.__serializeUserSettings(settings)
        response = self.__doSendInnerCommandText_("<blk:SetUserSettings>" + innerCmdText + "</blk:SetUserSettings>")
        resp = response.read()
        # print ("raw response=", resp, "\n")
        root = ET.fromstring(resp)
        if resultEnvelope is not None:
            self.__Add2DictIf(
                resultEnvelope,
                self.kMESSAGE_TIMESTAMP,
                root.find(".//blk:timestamp", self.__namespaces),
                (lambda elt: float(elt.text))
            )

    def ResetToFactoryDefaults(self, envelopeArgs=None, resultEnvelope=None):
        """
        [public]    IConfiguration.ResetToFactoryDefaults () -> void;
        [python]	ResetToFactoryDefaults (envelopeArgs = None, resultEnvelope = None)

        :param envelopeArgs:
        :param resultEnvelope:
        :return:
        """
        response = self.__doSendInnerCommandText_("<blk:ResetToFactoryDefaults/>")
        resp = response.read()
        # print ("raw response=", resp, "\n")
        root = ET.fromstring(resp)
        if resultEnvelope is not None:
            self.__Add2DictIf(
                resultEnvelope,
                self.kMESSAGE_TIMESTAMP,
                root.find(".//blk:timestamp", self.__namespaces),
                (lambda elt: float(elt.text))
            )

    def GetAlarms(self, envelopeArgs=None, resultEnvelope=None) -> list:
        """
        [public]    IDeviceManagement.GetAlarms () -> AlarmType[]
        [public]	GetAlarms () -> array
        [python]	array	GetAlarms (envelopeArgs = None, resultEnvelope = None)

        :param envelopeArgs:
        :param resultEnvelope:
        :return:
        :rtype: list
        """
        response = self.__doSendInnerCommandText_("<blk:GetAlarms/>")
        resp = response.read()
        # print ("raw response=", resp, "\n")
        root = ET.fromstring(resp)
        if resultEnvelope is not None:
            self.__Add2DictIf(
                resultEnvelope,
                self.kMESSAGE_TIMESTAMP,
                root.find(".//blk:timestamp", self.__namespaces),
                (lambda elt: float(elt.text))
            )
        alarms = []
        for a in root.findall(".//blk:Alarm", self.__namespaces):
            alarms.append(a.text)
        return alarms

    def ClearAlarms(self, alarms, envelopeArgs=None, resultEnvelope=None):
        """
        [public]    IDeviceManagement.ClearAlarms (All) -> AlarmType[]
        [public]    IDeviceManagement.ClearAlarms (AlarmType[]) -> AlarmType[]
        [python]	array	ClearAlarms (kAll, envelopeArgs = None, resultEnvelope = None)
        [python]	array	ClearAlarms (alarms, envelopeArgs = None, resultEnvelope = None)

        :param alarms:
        :param envelopeArgs:
        :param resultEnvelope:
        :return:
        """
        innerText = "<blk:ClearAlarms>"
        if alarms == self.kAllAlarms:
            innerText += "<blk:All/>"
        else:
            innerText += "<blk:Alarms>"
            for a in alarms:
                innerText += "<blk:Alarm>" + a + "</blk:Alarm>"
            innerText += "</blk:Alarms>"
        innerText += "</blk:ClearAlarms>"

        response = self.__doSendInnerCommandText_(innerText)
        resp = response.read()
        # print ("raw response=", resp, "\n")
        root = ET.fromstring(resp)
        if resultEnvelope is not None:
            self.__Add2DictIf(
                resultEnvelope,
                self.kMESSAGE_TIMESTAMP,
                root.find(".//blk:timestamp", self.__namespaces),
                (lambda elt: float(elt.text))
            )
        alarms = []
        for a in root.findall(".//blk:Alarm", self.__namespaces):
            alarms.append(a.text)
        return alarms

    def GetBatteryStatus(self, envelopeArgs=None, resultEnvelope=None):
        """
        [public]    GetBatteryStatus () -> BatteryStatusType;
        [python]	dictionary	GetBatteryStatus (envelopeArgs = None, resultEnvelope = None)

        :param envelopeArgs:
        :param resultEnvelope:
        :return:
        """
        response = self.__doSendInnerCommandText_("<blk:GetBatteryStatus/>")
        resp = response.read()
        # print ("raw response=", resp, "\n")
        root = ET.fromstring(resp)
        if resultEnvelope is not None:
            self.__Add2DictIf(
                resultEnvelope,
                self.kMESSAGE_TIMESTAMP,
                root.find(".//blk:timestamp", self.__namespaces),
                (lambda elt: float(elt.text))
            )
        result = {}
        self.__Add2DictIf(
            result,
            "BatteryCapable",
            root.find(".//blk:BatteryCapable", self.__namespaces),
            (lambda elt: elt.text == "true")
        )
        self.__Add2DictIf(
            result,
            "BatteryPresent",
            root.find(".//blk:BatteryPresent", self.__namespaces),
            (lambda elt: elt.text == "true")
        )
        self.__Add2DictIf(
            result, "BatteryPercentCharged",
            root.find(".//blk:BatteryPercentCharged", self.__namespaces),
            (lambda elt: float(elt.text))
        )
        self.__Add2DictIf(
            result, "ExternalPowerPresent",
            root.find(".//blk:ExternalPowerPresent", self.__namespaces),
            (lambda elt: elt.text == "true")
        )
        self.__Add2DictIf(
            result,
            "Charging",
            root.find(".//blk:Charging", self.__namespaces),
            (lambda elt: elt.text == "true")
        )
        # todo - NYI - StatusStates
        return result

    def GetDeviceName(self, envelopeArgs=None, resultEnvelope=None) -> str:
        """
        [public]    IDeviceManagement.GetDeviceName () -> String;
        [python]	dictionary	GetDeviceName (envelopeArgs = None, resultEnvelope = None)

        :param envelopeArgs:
        :param resultEnvelope:
        :return:
        """
        response = self.__doSendInnerCommandText_("<blk:GetDeviceName/>")
        resp = response.read()
        # print ("raw response=", resp, "\n")
        root = ET.fromstring(resp)
        if resultEnvelope is not None:
            self.__Add2DictIf(
                resultEnvelope,
                self.kMESSAGE_TIMESTAMP,
                root.find(".//blk:timestamp", self.__namespaces),
                (lambda elt: float(elt.text))
            )
        return root.find(".//blk:GetDeviceNameResponse", self.__namespaces).text

    def SetDeviceName(self, deviceName, envelopeArgs=None, resultEnvelope=None):
        """
        [public]    IDeviceManagement.SetDeviceName (deviceName) -> void;
        [python]	void	SetDeviceName (deviceName, envelopeArgs = None, resultEnvelope = None)

        :param deviceName:
        :param envelopeArgs:
        :param resultEnvelope:
        :return:
        """
        response = self.__doSendInnerCommandText_("<blk:SetDeviceName>" + deviceName + "</blk:SetDeviceName>")
        resp = response.read()
        # print ("raw response=", resp, "\n")
        root = ET.fromstring(resp)
        if resultEnvelope is not None:
            self.__Add2DictIf(
                resultEnvelope,
                self.kMESSAGE_TIMESTAMP,
                root.find(".//blk:timestamp", self.__namespaces),
                (lambda elt: float(elt.text))
            )

    def GetPowerState(self, envelopeArgs=None, resultEnvelope=None) -> str:
        """
        [public]    IDeviceManagement.GetPowerState () -> PowerStateType;
        [python]	dictionary	GetPowerState (envelopeArgs = None, resultEnvelope = None)

        :param envelopeArgs:
        :param resultEnvelope:
        :return:
        """
        response = self.__doSendInnerCommandText_("<blk:GetPowerState/>")
        resp = response.read()
        # print ("raw response=", resp, "\n")
        root = ET.fromstring(resp)
        if resultEnvelope is not None:
            self.__Add2DictIf(
                resultEnvelope,
                self.kMESSAGE_TIMESTAMP,
                root.find(".//blk:timestamp", self.__namespaces),
                (lambda elt: float(elt.text))
            )
        return root.find(".//blk:GetPowerStateResponse", self.__namespaces).text

    def SetPowerState(self, powerState, envelopeArgs=None, resultEnvelope=None):
        """
        [public]    IDeviceManagement.SetPowerState (PowerStateType powerState) -> void;
        [python]	void	SetPowerState (powerState, envelopeArgs = None, resultEnvelope = None)

        :param powerState:
        :param envelopeArgs:
        :param resultEnvelope:
        :return:
        """
        response = self.__doSendInnerCommandText_("<blk:SetPowerState>" + powerState + "</blk:SetPowerState>")
        resp = response.read()
        # print ("raw response=", resp, "\n")
        root = ET.fromstring(resp)
        if resultEnvelope is not None:
            self.__Add2DictIf(
                resultEnvelope,
                self.kMESSAGE_TIMESTAMP,
                root.find(".//blk:timestamp", self.__namespaces),
                (lambda elt: float(elt.text))
            )

    def GetVersionDetails(self, envelopeArgs=None, resultEnvelope=None) -> dict:
        """
        [public]    IDeviceManagement.GetVersionDetails () -> VersionInfoType;
        [python]	dictionary	GetVersionDetails (envelopeArgs = None, resultEnvelope = None)

        :param envelopeArgs:
        :param resultEnvelope:
        :return:
        """
        response = self.__doSendInnerCommandText_("<blk:GetVersionDetails/>")
        resp = response.read()
        # print ("raw response=", resp, "\n")
        root = ET.fromstring(resp)
        if resultEnvelope is not None:
            self.__Add2DictIf(
                resultEnvelope,
                self.kMESSAGE_TIMESTAMP,
                root.find(".//blk:timestamp", self.__namespaces),
                (lambda elt: float(elt.text))
            )
        result = {}
        self.__Add2DictIf(
            result,
            "ModelName",
            root.find(".//blk:ModelName", self.__namespaces),
            (lambda elt: elt.text)
        )
        self.__Add2DictIf(
            result,
            "ModelNumber",
            root.find(".//blk:ModelNumber", self.__namespaces),
            (lambda elt: elt.text)
        )
        self.__Add2DictIf(
            result,
            "FactorySerialNumber",
            root.find(".//blk:FactorySerialNumber", self.__namespaces),
            (lambda elt: elt.text)
        )
        self.__Add2DictIf(
            result,
            "ACU-FPGA-SoftwareVersion",
            root.find(".//blk:ACU-FPGA-SoftwareVersion", self.__namespaces),
            (lambda elt: elt.text)
        )
        self.__Add2DictIf(
            result, "CCU-FPGA-SoftwareVersion",
            root.find(".//blk:CCU-FPGA-SoftwareVersion", self.__namespaces),
            (lambda elt: elt.text)
        )
        self.__Add2DictIf(
            result, "BLK-Controller-SoftwareVersion",
            root.find(".//blk:BLK-Controller-SoftwareVersion", self.__namespaces),
            (lambda elt: elt.text)
        )
        self.__Add2DictIf(
            result, "OS-SoftwareVersion",
            root.find(".//blk:OS-SoftwareVersion", self.__namespaces),
            (lambda elt: elt.text)
        )
        return result

    def GetLaserPointerOn(self, envelopeArgs=None, resultEnvelope=None) -> bool:
        """
        [public]    ILaserOperation.GetLaserPointerOn () -> bool;
        [python]	bool	GetLaserPointerOn (envelopeArgs = None, resultEnvelope = None)

        :param envelopeArgs:
        :param resultEnvelope:
        :return:
        """
        response = self.__doSendInnerCommandText_("<blk:GetLaserPointerOn/>")
        resp = response.read()
        # print ("raw response=", resp, "\n")
        root = ET.fromstring(resp)
        if resultEnvelope is not None:
            self.__Add2DictIf(
                resultEnvelope,
                self.kMESSAGE_TIMESTAMP,
                root.find(".//blk:timestamp", self.__namespaces),
                (lambda elt: float(elt.text))
            )
        return root.find(".//blk:GetLaserPointerOnResponse", self.__namespaces).text == "true"

    def SetLaserPointerOn(self, laserPointerOn, envelopeArgs=None, resultEnvelope=None):
        """
        [public]    ILaserOperation.SetLaserPointerOn (bool laserPointerOn) -> void;
        [python]	void	SetLaserPointerOn (laserPointerOn, envelopeArgs = None, resultEnvelope = None)

        :param laserPointerOn:
        :param envelopeArgs:
        :param resultEnvelope:
        :return:
        """
        response = self.__doSendInnerCommandText_(
            "<blk:SetLaserPointerOn>" + str(laserPointerOn) + "</blk:SetLaserPointerOn>"
        )
        resp = response.read()
        # print ("raw response=", resp, "\n")
        root = ET.fromstring(resp)
        if resultEnvelope is not None:
            self.__Add2DictIf(
                resultEnvelope,
                self.kMESSAGE_TIMESTAMP,
                root.find(".//blk:timestamp", self.__namespaces),
                (lambda elt: float(elt.text))
            )

    def GetToggleSwitchState(self, which, envelopeArgs=None, resultEnvelope=None) -> str:
        """
        [public]	ILaserOperation.GetToggleSwitchState (ToggleSwitchType: which) -> ToggleStateType
        [python]	GetToggleSwitchState (which, envelopeArgs = None, resultEnvelope = None)

        :param which:
        :param envelopeArgs:
        :param resultEnvelope:
        :return:
        """
        if (
                which is not self.ToggleSwitchType.FanA
                and which is not self.ToggleSwitchType.FanB
                and which is not self.ToggleSwitchType.SolenoidA
                and which is not self.ToggleSwitchType.SolenoidB
        ):
            raise Exception("invalid which")
        response = self.__doSendInnerCommandText_(
            "<blk:GetToggleSwitchState><blk:Which>" + which + "</blk:Which></blk:GetToggleSwitchState>")
        resp = response.read()
        # print ("raw response=", resp, "\n")
        root = ET.fromstring(resp)
        if resultEnvelope is not None:
            self.__Add2DictIf(
                resultEnvelope,
                self.kMESSAGE_TIMESTAMP,
                root.find(".//blk:timestamp", self.__namespaces),
                (lambda elt: float(elt.text))
            )
        return root.find(".//blk:GetToggleSwitchStateResponse", self.__namespaces).text

    def SetToggleSwitchState(self, which, state, envelopeArgs=None, resultEnvelope=None):
        """
        [public]	ILaserOperation.SetToggleSwitchState (ToggleSwitchType: which, ToggleStateType: state) -> void
        [python]  SetToggleSwitchState (ToggleSwitchType: which, ToggleStateType: state) -> void

        :param which:
        :param state:
        :param envelopeArgs:
        :param resultEnvelope:
        :return:
        """
        if (
                which is not self.ToggleSwitchType.FanA
                and which is not self.ToggleSwitchType.FanB
                and which is not self.ToggleSwitchType.SolenoidA
                and which is not self.ToggleSwitchType.SolenoidB
        ):
            raise Exception("invalid which")
        if (state is not self.ToggleStateType.Off) and (state is not self.ToggleStateType.On):
            raise Exception("invalid ToggleStateType")
        response = self.__doSendInnerCommandText_(
            "<blk:SetToggleSwitchState><blk:Which>"
            + which
            + "</blk:Which><blk:State>"
            + state
            + "</blk:State></blk:SetToggleSwitchState>"
        )
        resp = response.read()
        # print ("raw response=", resp, "\n")
        root = ET.fromstring(resp)
        if resultEnvelope is not None:
            self.__Add2DictIf(
                resultEnvelope,
                self.kMESSAGE_TIMESTAMP,
                root.find(".//blk:timestamp", self.__namespaces),
                (lambda elt: float(elt.text))
            )

    def ReadSensors(self, sensorsToRead, envelopeArgs=None, resultEnvelope=None) -> dict:
        """
        [public]	ILaserOperation.ReadSensors (All) -> SensorDataType;
        [public]	ILaserOperation.ReadSensors (SensorDataKind[] whichSensors) -> SensorDataType;
        [python]	SENSOR-READINGS	ReadSensors (kAllSensors)
        [python]	SENSOR-READINGS	ReadSensors ([SensorDataKind]*)

        Note - if you pass an empty set of sensors to ReadSensors() - you will get back no readings.
        Pass kAllSensors to read all available sensors or better yet, a specific set (array)
        of sensors of type SensorDataKind

        :param sensorsToRead:
        :type sensorsToRead: dict
        :param envelopeArgs:
        :param resultEnvelope:
        :return:
        """
        args = ""
        if sensorsToRead == self.kAllSensors:
            args = "<blk:All/>"
        else:
            if type(sensorsToRead) is not str:
                for sensori in sensorsToRead:
                    args += "<blk:Sensor>" + sensori + "</blk:Sensor>"
            else:
                args += "<blk:Sensor>" + sensorsToRead + "</blk:Sensor>"
        msg = "<blk:ReadSensors>" + args + "</blk:ReadSensors>"
        response = self.__doSendInnerCommandText_(msg)
        resp = response.read()
        # print ("raw response=", resp, "\n")
        root = ET.fromstring(resp)
        result = {}

        self.__Add2DictIf(
            result,
            "DetectorTemperature",
            root.find(".//blk:DetectorTemperature", self.__namespaces),
            (lambda elt: float(elt.text))
        )
        self.__Add2DictIf(
            result, "SystemTemperature",
            root.find(".//blk:SystemTemperature", self.__namespaces),
            (lambda elt: float(elt.text))
        )
        self.__Add2DictIf(
            result, "OpticsTemperature",
            root.find(".//blk:OpticsTemperature", self.__namespaces),
            (lambda elt: float(elt.text))
        )
        self.__Add2DictIf(
            result, "ExternalPressure1",
            root.find(".//blk:ExternalPressure1", self.__namespaces),
            (lambda elt: float(elt.text))
        )
        self.__Add2DictIf(
            result, "ExternalPressure2",
            root.find(".//blk:ExternalPressure2", self.__namespaces),
            (lambda elt: float(elt.text))
        )
        self.__Add2DictIf(
            result, "ExternalPressure3",
            root.find(".//blk:ExternalPressure3", self.__namespaces),
            (lambda elt: float(elt.text))
        )
        self.__Add2DictIf(
            result, "ExternalPressure4",
            root.find(".//blk:ExternalPressure4", self.__namespaces),
            (lambda elt: float(elt.text))
        )
        self.__Add2DictIf(
            result, "ExternalTemperature1",
            root.find(".//blk:ExternalTemperature1", self.__namespaces),
            (lambda elt: float(elt.text))
        )
        self.__Add2DictIf(
            result, "ExternalTemperature2",
            root.find(".//blk:ExternalTemperature2", self.__namespaces),
            (lambda elt: float(elt.text))
        )
        self.__Add2DictIf(
            result, "ExternalTemperature3",
            root.find(".//blk:ExternalTemperature3", self.__namespaces),
            (lambda elt: float(elt.text))
        )
        self.__Add2DictIf(
            result, "ExternalTemperature4",
            root.find(".//blk:ExternalTemperature4", self.__namespaces),
            (lambda elt: float(elt.text))
        )
        self.__Add2DictIf(
            result, "ElectricalBoardTemperature",
            root.find(".//blk:ElectricalBoardTemperature", self.__namespaces),
            (lambda elt: float(elt.text))
        )
        self.__Add2DictIf(
            result, "SystemHumidity",
            root.find(".//blk:SystemHumidity", self.__namespaces),
            (lambda elt: float(elt.text))
        )

        tmp = root.find(".//blk:LaserTemperature", self.__namespaces)
        if tmp is not None:
            t = {}
            self.__Add2DictIf(
                t,
                "1",
                tmp.find(".//blk:Temperature[@Tuner='1']", self.__namespaces),
                (lambda elt: float(elt.text))
            )
            self.__Add2DictIf(
                t,
                "2",
                tmp.find(".//blk:Temperature[@Tuner='2']", self.__namespaces),
                (lambda elt: float(elt.text))
            )
            self.__Add2DictIf(
                t,
                "3",
                tmp.find(".//blk:Temperature[@Tuner='3']", self.__namespaces),
                (lambda elt: float(elt.text))
            )
            self.__Add2DictIf(
                t,
                "4",
                tmp.find(".//blk:Temperature[@Tuner='4']", self.__namespaces),
                (lambda elt: float(elt.text))
            )
            result["LaserTemperature"] = t

        tmp = root.find(".//blk:LaserCurrent", self.__namespaces)
        if tmp is not None:
            t = {}
            self.__Add2DictIf(
                t,
                "1",
                tmp.find(".//blk:Current[@Tuner='1']", self.__namespaces),
                (lambda elt: float(elt.text))
            )
            self.__Add2DictIf(
                t,
                "2",
                tmp.find(".//blk:Current[@Tuner='2']", self.__namespaces),
                (lambda elt: float(elt.text))
            )
            self.__Add2DictIf(
                t,
                "3",
                tmp.find(".//blk:Current[@Tuner='3']", self.__namespaces),
                (lambda elt: float(elt.text))
            )
            self.__Add2DictIf(
                t,
                "4",
                tmp.find(".//blk:Current[@Tuner='4']", self.__namespaces),
                (lambda elt: float(elt.text))
            )
            result["LaserCurrent"] = t

        tmp = root.find(".//blk:LaserVoltage", self.__namespaces)
        if tmp is not None:
            t = {}
            self.__Add2DictIf(
                t,
                "1",
                tmp.find(".//blk:Voltage[@Tuner='1']", self.__namespaces),
                (lambda elt: float(elt.text))
            )
            self.__Add2DictIf(
                t,
                "2",
                tmp.find(".//blk:Voltage[@Tuner='2']", self.__namespaces),
                (lambda elt: float(elt.text))
            )
            self.__Add2DictIf(
                t,
                "3",
                tmp.find(".//blk:Voltage[@Tuner='3']", self.__namespaces),
                (lambda elt: float(elt.text))
            )
            self.__Add2DictIf(
                t,
                "4",
                tmp.find(".//blk:Voltage[@Tuner='4']", self.__namespaces),
                (lambda elt: float(elt.text))
            )
            result["LaserVoltage"] = t

        tmp = root.find(".//blk:Accelerometer", self.__namespaces)
        if tmp is not None:
            t = {}
            t["AngularVelocityX"] = float(tmp.find(".//blk:AngularVelocityX", self.__namespaces).text)
            t["AngularVelocityY"] = float(tmp.find(".//blk:AngularVelocityY", self.__namespaces).text)
            t["AngularVelocityZ"] = float(tmp.find(".//blk:AngularVelocityZ", self.__namespaces).text)
            t["AccelerationX"] = float(tmp.find(".//blk:AccelerationX", self.__namespaces).text)
            t["AccelerationY"] = float(tmp.find(".//blk:AccelerationY", self.__namespaces).text)
            t["AccelerationZ"] = float(tmp.find(".//blk:AccelerationZ", self.__namespaces).text)
            result["Accelerometer"] = t
        self.__Add2DictIf(
            result,
            "ActiveLaser",
            root.find(".//blk:ActiveLaser", self.__namespaces),
            (lambda elt: int(elt.text))
        )
        self.__Add2DictIf(
            result,
            "ActiveLaserWaveNumber",
            root.find(".//blk:ActiveLaserWaveNumber", self.__namespaces),
            (lambda elt: float(elt.text))
        )
        self.__Add2DictIf(
            result,
            "RangeFinder",
            root.find(".//blk:RangeFinder", self.__namespaces),
            (lambda elt: float(elt.text))
        )
        if resultEnvelope is not None:
            self.__Add2DictIf(
                resultEnvelope,
                self.kMESSAGE_TIMESTAMP,
                root.find(".//blk:timestamp", self.__namespaces),
                (lambda elt: float(elt.text))
            )
        return result

    def StopLasers(self, envelopeArgs=None, resultEnvelope=None):
        """
        [public]    ILaserOperation.StopLasers () -> void;
        [python]	void	StopLasers (envelopeArgs = None, resultEnvelope = None)

        :param envelopeArgs:
        :param resultEnvelope:
        :return:
        """
        msg = "<blk:StopLasers>" + "" + "</blk:StopLasers>"
        response = self.__doSendInnerCommandText_(msg)
        resp = response.read()
        # print ("raw response=", resp, "\n")
        root = ET.fromstring(resp)
        if resultEnvelope is not None:
            self.__Add2DictIf(
                resultEnvelope,
                self.kMESSAGE_TIMESTAMP,
                root.find(".//blk:timestamp", self.__namespaces),
                (lambda elt: float(elt.text))
            )

    def MoveTune(
            self, waveNumber, duringTransition="LaserOn", envelopeArgs=None, resultEnvelope=None
    ) -> float:
        """
        [public]	ILaserOperations.MoveTune (
                        WaveNumberType waveNumber,
                        LaserOnOffTransitionType duringTransition = LaserOn
                    ) -> WaveNumberType;

        [python]	MoveTune (
                        WaveNumberType waveNumber,
                        duringTransition = 'LaserOn',
                        envelopeArgs = None,
                        resultEnvelope = None
                    )

        The Move operation simply turns the laser on, and on a particular waveNumber.

        :param waveNumber:
        :param duringTransition:
        :param envelopeArgs:
        :param resultEnvelope:
        :return:
        :rtype: float
        """
        innerCmdText = ""
        if (self.__ns == self.kNS_2014_04) or (self.__ns == self.kNS_2014_07):
            innerCmdText += (
                    "<blk:MoveTune waveNumber=\""
                    + str(waveNumber)
                    + "\"duringTransition=\""
                    + duringTransition
                    + "\"/>"
            )
        else:
            innerCmdText += "<blk:MoveTune duringTransition=\"" + duringTransition + "\">"
            if isinstance(waveNumber, list):
                for i in waveNumber:
                    innerCmdText += "<blk:WaveNumber>" + str(i) + "</blk:WaveNumber>"
            else:
                innerCmdText += "<blk:WaveNumber>" + str(waveNumber) + "</blk:WaveNumber>"
            innerCmdText += "</blk:MoveTune>"

        response = self.__doSendInnerCommandText_(innerCmdText)
        resp = response.read()
        # print ("raw response=", resp, "\n")
        root = ET.fromstring(resp)
        if resultEnvelope is not None:
            self.__Add2DictIf(
                resultEnvelope,
                self.kMESSAGE_TIMESTAMP,
                root.find(".//blk:timestamp", self.__namespaces),
                (lambda elt: float(elt.text))
            )
        return float(root.find(".//blk:WaveNumber", self.__namespaces).text)

    def StepTune(
            self,
            start,
            end,
            delta,
            dwellTime="PT0S",
            duringTransition="LaserOn",
            envelopeArgs=None,
            resultEnvelope=None
    ):
        """
        [public]  ILaserOperation.StepTune (
                        WaveNumberType start,
                        WaveNumberType end,
                        WaveNumberDistanceType delta,
                        duration dwellTime = PT0S,
                        LaserOnOffTransitionType duringTransition = LaserOn
                    ) -> WaveNumberType[];

        [python]	array StepTune (
                        start,
                        end,
                        delta,
                        dwellTime = "PT0S",
                        duringTransition = "LaserOn",
                        envelopeArgs = None,
                        resultEnvelope = None
                    )

        :param start:
        :param end:
        :param delta:
        :param dwellTime:
        :param duringTransition:
        :param envelopeArgs:
        :param resultEnvelope:
        :return:
        """
        innerCmdText = ""
        innerCmdText += "<blk:StepTune"
        if self.__ns == self.kNS_2014_04:
            innerCmdText += " startWaveNumber=\"" + str(start) + "\""
            innerCmdText += " stopWaveNumber=\"" + str(end) + "\""
            innerCmdText += " stepSize=\"" + str(delta) + "\""
        else:
            innerCmdText += " start=\"" + str(start) + "\""
            innerCmdText += " end=\"" + str(end) + "\""
            innerCmdText += " delta=\"" + str(delta) + "\""
        innerCmdText += " dwellTime=\"" + dwellTime + "\""
        innerCmdText += " duringTransition=\"" + duringTransition + "\""
        innerCmdText += "/>"
        response = self.__doSendInnerCommandText_(innerCmdText)
        resp = response.read()
        # print ("raw response=", resp, "\n")
        root = ET.fromstring(resp)
        measurements = []
        for measurement in root.findall(".//blk:WaveNumber", self.__namespaces):
            measurements.append(float(measurement.text))
        if resultEnvelope is not None:
            self.__Add2DictIf(
                resultEnvelope,
                self.kMESSAGE_TIMESTAMP,
                root.find(".//blk:timestamp", self.__namespaces),
                (lambda elt: float(elt.text))
            )
        return measurements

    def SweepTune(
            self,
            start,
            end,
            sweepRate,
            repeatCount=1,
            interRepeatDelay="PTOS",
            envelopeArgs=None,
            resultEnvelope=None
    ):
        """
        [public]	ILaserOperation.SweepTune (
                        WaveNumberType start,
                        WaveNumberType end,
                        SweepRateType sweepRate,
                        repeatCount = 1,
                        interRepeatDelay = PT0S
                    ) -> void;

        [python]	void	SweepTune (
                        start,
                        end,
                        sweepRate,
                        repeatCount = 1,
                        interRepeatDelay = "PTOS",
                        envelopeArgs = None,
                        resultEnvelope = None
                    )

        :param start:
        :param end:
        :param sweepRate:
        :param repeatCount:
        :param interRepeatDelay:
        :param envelopeArgs:
        :param resultEnvelope:
        :return:
        """
        innerCmdText = ""
        innerCmdText += "<blk:SweepTune"
        if self.__ns == self.kNS_2014_04:
            innerCmdText += " startWaveNumber=\"" + str(start) + "\""
            innerCmdText += " stopWaveNumber=\"" + str(end) + "\""
            innerCmdText += " sweepSpeed=\"" + str(sweepRate) + "\""
        else:
            innerCmdText += " start=\"" + str(start) + "\""
            innerCmdText += " end=\"" + str(end) + "\""
            innerCmdText += " sweepRate=\"" + str(sweepRate) + "\""
        if self.__ns == self.kNS_2014_04:
            innerCmdText += " repeatCount=\"" + str(repeatCount) + "\""
            innerCmdText += " interRepeatDelay=\"" + interRepeatDelay + "\""
        innerCmdText += "/>"
        if self.__ns == self.kNS_2014_04 or self.__ns == self.kNS_2014_07:
            for i in range(1, repeatCount):
                response = self.__doSendInnerCommandText_(innerCmdText)
        else:
            response = self.__doSendInnerCommandText_(innerCmdText)
        resp = response.read()
        # print ("raw response=", resp, "\n")
        root = ET.fromstring(resp)
        if resultEnvelope is not None:
            self.__Add2DictIf(
                resultEnvelope,
                self.kMESSAGE_TIMESTAMP,
                root.find(".//blk:timestamp", self.__namespaces),
                (lambda elt: float(elt.text))
            )

    def ExternallyControlledTune(self, envelopeArgs=None, resultEnvelope=None):
        """
        [public]    ILaserOperations.ExternallyControlledTune ();
        [python]	void ExternallyControlledTune (envelopeArgs = None, resultEnvelope = None)

        :param envelopeArgs:
        :param resultEnvelope:
        :return:
        """
        response = self.__doSendInnerCommandText_("<blk:ExternallyControlledTune/>")
        resp = response.read()
        # print ("raw response=", resp, "\n")
        root = ET.fromstring(resp)
        if resultEnvelope is not None:
            self.__Add2DictIf(
                resultEnvelope,
                self.kMESSAGE_TIMESTAMP,
                root.find(".//blk:timestamp", self.__namespaces),
                (lambda elt: float(elt.text))
            )

    def Delay(self, delay, envelopeArgs=None, resultEnvelope=None):
        """
        [public]    ILaserOperations.Delay (delay);
        [python]	void Delay (duration delay, envelopeArgs = None, resultEnvelope = None)

        :param delay:
        :param envelopeArgs:
        :param resultEnvelope:
        :return:
        """
        response = self.__doSendInnerCommandText_("<blk:Delay>" + delay + "</blk:Delay>")
        resp = response.read()
        # print ("raw response=", resp, "\n")
        root = ET.fromstring(resp)
        if resultEnvelope is not None:
            self.__Add2DictIf(
                resultEnvelope,
                self.kMESSAGE_TIMESTAMP,
                root.find(".//blk:timestamp", self.__namespaces),
                (lambda elt: float(elt.text))
            )

    def StepScan(
            self,
            start,
            end,
            delta,
            dwellTime,
            duringTransition="LaserOn",
            scansPerSpectrum=1,
            delayBetweenCoAdds="PT0S",
            envelopeArgs=None,
            resultEnvelope=None
    ):
        """
        [public]    ILaserOperations.StepScan (
                        WaveNumberType start,
                        WaveNumberType end,
                        WaveNumberDistanceType delta,
                        duration dwellTime,
                        LaserOnOffTransitionType duringTransition = LaserOn,
                        unsigned int scansPerSpectrum= 1,
                        duration delayBetweenCoAdds = PT0S
                    ) -> SpectrumType;

        [python]	dictionary StepScan (
                        start,
                        end,
                        delta,
                        dwellTime,
                        duringTransition = "LaserOn",
                        scansPerSpectrum= 1,
                        delayBetweenCoAdds = "PT0S",
                        envelopeArgs = None,
                        resultEnvelope = None
                    )

        :param start:
        :param end:
        :param delta:
        :param dwellTime:
        :param duringTransition:
        :param scansPerSpectrum:
        :param delayBetweenCoAdds:
        :param envelopeArgs:
        :param resultEnvelope:
        :return:
        """
        innerCmdText = ""
        innerCmdText += "<blk:StepScan>"
        innerCmdText += "  <blk:Start>" + str(start) + "</blk:Start>"
        innerCmdText += "  <blk:End>" + str(end) + "</blk:End>"
        innerCmdText += "  <blk:Delta>" + str(delta) + "</blk:Delta>"
        if self.__ns == self.kNS_2014_04:
            innerCmdText += "  <blk:DuringTransition>" + duringTransition + "</blk:DuringTransition>"
            innerCmdText += "  <blk:StepDwellTime>" + dwellTime + "</blk:StepDwellTime>"
        else:
            innerCmdText += "  <blk:DwellTime>" + dwellTime + "</blk:DwellTime>"
            innerCmdText += "  <blk:DuringTransition>" + duringTransition + "</blk:DuringTransition>"
        innerCmdText += "  <blk:ScansPerSpectrum>" + str(scansPerSpectrum) + "</blk:ScansPerSpectrum>"
        innerCmdText += "  <blk:DelayBetweenCoAdds>" + str(delayBetweenCoAdds) + "</blk:DelayBetweenCoAdds>"
        innerCmdText += "</blk:StepScan>"

        response = self.__doSendInnerCommandText_(innerCmdText)
        resp = response.read()
        # print ("raw response=", resp, "\n")
        measurements = self.__ParseMeasurementsFromResult(resp)
        if resultEnvelope is not None:
            self.__Add2DictIf(
                resultEnvelope,
                self.kMESSAGE_TIMESTAMP,
                self.__ParseSOAPTimestampFromSOAPResult(resp)
            )
        return measurements

    """

    """

    def SweepScan(
            self,
            start,
            end,
            sweepRate,
            scanResolution=10.0,
            scansPerSpectrum=1,
            delayBetweenCoAdds="PT0S",
            envelopeArgs=None,
            resultEnvelope=None
    ):
        """
        [public]    ILaserOperations.SweepScan (
                        WaveNumberType start,
                        WaveNumberType end,
                        SweepRateType sweepRate,
                        WaveNumberDistanceType scanResolution = 10.0,
                        unsigned int scansPerSpectrum= 1,
                        duration delayBetweenCoAdds = PT0S
                    ) -> SpectrumType;

        [python]	dictionary	SweepScan (
                        start,
                        end,
                        sweepRate,
                        scanResolution = 10.0,
                        scansPerSpectrum= 1,
                        delayBetweenCoAdds = "PT0S",
                        envelopeArgs = None,
                        resultEnvelope = None
                    )

        :param start:
        :param end:
        :param sweepRate:
        :param scanResolution:
        :param scansPerSpectrum:
        :param delayBetweenCoAdds:
        :param envelopeArgs:
        :param resultEnvelope:
        :return:
        """
        innerCmdText = ""
        innerCmdText += "<blk:SweepScan>"
        innerCmdText += "  <blk:Start>" + str(start) + "</blk:Start>"
        innerCmdText += "  <blk:End>" + str(end) + "</blk:End>"
        innerCmdText += "  <blk:SweepRate>" + str(sweepRate) + "</blk:SweepRate>"
        innerCmdText += "  <blk:ScanResolution>" + str(scanResolution) + "</blk:ScanResolution>"
        innerCmdText += "  <blk:ScansPerSpectrum>" + str(scansPerSpectrum) + "</blk:ScansPerSpectrum>"
        innerCmdText += "  <blk:DelayBetweenCoAdds>" + str(delayBetweenCoAdds) + "</blk:DelayBetweenCoAdds>"
        innerCmdText += "</blk:SweepScan>"
        response = self.__doSendInnerCommandText_(innerCmdText)
        resp = response.read()
        # print ("raw response=", resp, "\n")
        measurements = self.__ParseMeasurementsFromResult(resp)
        if resultEnvelope is not None:
            self.__Add2DictIf(
                resultEnvelope,
                self.kMESSAGE_TIMESTAMP,
                self.__ParseSOAPTimestampFromSOAPResult(resp)
            )
        return measurements

    kScanResolution_NaturalBinning = "NaturalBinning"

    """
        
    """

    def InterleavedScan(
            self, singleSpectrumMeasurementTime, scanResolution=10.0, scansPerSpectrum=1,
            delayBetweenCoAdds="PT0S", envelopeArgs=None, resultEnvelope=None
    ):
        """
        [public]    ILaserOperations.InterleavedScan (
                            duration singleSpectrumMeasurementTime,
                            WaveNumberDistanceType scanResolution = 10.0,
                            unsigned int scansPerSpectrum = 1,
                            duration delayBetweenCoAdds = PT0S
                    ) -> SpectrumType;

        [python]	dictionary	InterleavedScan (
                            singleSpectrumMeasurementTime,
                            scanResolution = 10.0,
                            scansPerSpectrum = 1,
                            delayBetweenCoAdds = "PT0S",
                            envelopeArgs = None,
                            resultEnvelope = None
                    )

        :param singleSpectrumMeasurementTime:
        :param scanResolution:
        :param scansPerSpectrum:
        :param delayBetweenCoAdds:
        :param envelopeArgs:
        :param resultEnvelope:
        :return:
        """
        innerCmdText = ""
        innerCmdText += "<blk:InterleavedScan>"
        if self.__ns == self.kNS_2014_04:
            innerCmdText += "  <blk:DeltaResolution>" + str(scanResolution) + "</blk:DeltaResolution>"
            innerCmdText += "  <blk:SingleSpectrumMeasurementTime>" + str(
                singleSpectrumMeasurementTime) + "</blk:SingleSpectrumMeasurementTime>"
        else:
            innerCmdText += "  <blk:SingleSpectrumMeasurementTime>" + str(
                singleSpectrumMeasurementTime) + "</blk:SingleSpectrumMeasurementTime>"
            innerCmdText += "  <blk:ScanResolution>" + str(scanResolution) + "</blk:ScanResolution>"
        innerCmdText += "  <blk:ScansPerSpectrum>" + str(scansPerSpectrum) + "</blk:ScansPerSpectrum>"
        innerCmdText += "  <blk:DelayBetweenCoAdds>" + delayBetweenCoAdds + "</blk:DelayBetweenCoAdds>"
        innerCmdText += "</blk:InterleavedScan>"
        response = self.__doSendInnerCommandText_(innerCmdText)
        resp = response.read()
        # print ("raw response=", resp, "\n")
        measurements = self.__ParseMeasurementsFromResult(resp)
        if resultEnvelope is not None:
            self.__Add2DictIf(
                resultEnvelope,
                self.kMESSAGE_TIMESTAMP,
                self.__ParseSOAPTimestampFromSOAPResult(resp)
            )
        return measurements

    # REMAINING TO ORGANIZE - BUT ALL PRIVATE OR MANUFACTURING OR LOW LEVEL DEBUGGING

    def SetFactorySettings(self, factorySettings, envelopeArgs=None, resultEnvelope=None):
        """
        void SetFactorySettings (factorySettings, envelopeArgs = None, resultEnvelope = None)

        @todo ADD ToggleSwitchInitialValues/SystemDServices support

        :param factorySettings:
        :param envelopeArgs:
        :param resultEnvelope:
        :return:
        """
        innerCmdText = ""
        innerCmdText += self.__writeRangeIfNeeded("SystemTemperatureRange", factorySettings)
        innerCmdText += self.__writeRangeIfNeeded("OpticsTemperatureRange", factorySettings)

        if "LaserStitchPoints" in factorySettings:
            innerCmdText += "<blk:LaserStitchPoints>"
            for i in factorySettings["LaserStitchPoints"]:
                innerCmdText += "<blk:Explicit>"
                innerCmdText += "<blk:LowerTuner>" + str(i['LowerTuner']) + "</blk:LowerTuner>"
                innerCmdText += "<blk:UpperTuner>" + str(i['UpperTuner']) + "</blk:UpperTuner>"
                innerCmdText += "<blk:WaveNumber>" + str(i['WaveNumber']) + "</blk:WaveNumber>"
                innerCmdText += "</blk:Explicit>"
            innerCmdText += "</blk:LaserStitchPoints>"

        innerCmdText += self.__writeRangeIfNeeded("LaserPulseDurationLimit", factorySettings)
        innerCmdText += self.__writePIDIfNeeded("DetectorTECPIDParameters", factorySettings)
        innerCmdText += self.__writeRangeIfNeeded("DetectorTemperatureSetPointRange", factorySettings)
        innerCmdText += self.__writeRangeIfNeeded("SampleDelayRange", factorySettings)
        innerCmdText += self.__writeValueIfNeeded("BiasDAC", factorySettings)
        innerCmdText += self.__writeValueIfNeeded("PreDarkToLight", factorySettings)
        innerCmdText += self.__writeValueIfNeeded("LightToPostDark", factorySettings)
        innerCmdText += self.__writeRangeIfNeeded("LaserPulseDurationLimit", factorySettings)
        innerCmdText += self.__writeValueIfNeeded("LaserDutyCycleLimit", factorySettings)
        innerCmdText += self.__writeValueIfNeeded("MirrorMoveSmoothingDuration", factorySettings)

        if "Tuners" in factorySettings:
            innerCmdText += "<blk:Tuners>"
            for ti in factorySettings["Tuners"]:
                innerCmdText += "<blk:Tuner Tuner=\"" + ti + "\">"
                tunerN = factorySettings["Tuners"][ti]
                if "LaserWaveNumberRanges" in tunerN:
                    lb = tunerN["LaserWaveNumberRanges"]["lowerBound"]
                    ub = tunerN["LaserWaveNumberRanges"]["upperBound"]
                    innerCmdText += "<blk:LaserWaveNumberRanges upperBound=\"" + str(ub) + "\" lowerBound=\"" + str(
                        lb) + "\"/>"
                if "ReferenceLaserVoltage" in tunerN:
                    innerCmdText += "<blk:ReferenceLaserVoltage>" + str(
                        tunerN["ReferenceLaserVoltage"]) + "</blk:ReferenceLaserVoltage>"
                if "WaveNumberToDriveVoltageCalibrationTable" in tunerN:
                    innerCmdText += "<blk:WaveNumberToDriveVoltageCalibrationTable>"
                    for ci in tunerN["WaveNumberToDriveVoltageCalibrationTable"]:
                        innerCmdText += "<blk:Map waveNumber=\"" + str(ci) + "\" drivingVoltage=\"" + str(
                            tunerN["WaveNumberToDriveVoltageCalibrationTable"][ci]) + "\"/>"
                    innerCmdText += "</blk:WaveNumberToDriveVoltageCalibrationTable>"
                if "CurrentToWaveNumberCalibrationTable" in tunerN:
                    innerCmdText += "<blk:CurrentToWaveNumberCalibrationTable>"
                    for ci in tunerN["CurrentToWaveNumberCalibrationTable"]:
                        innerCmdText += "<blk:Map waveNumber=\"" + str(
                            tunerN["CurrentToWaveNumberCalibrationTable"][ci]) + "\" ADC=\"" + str(ci) + "\"/>"
                    innerCmdText += "</blk:CurrentToWaveNumberCalibrationTable>"
                ####
                #### @todo NOTE - INCOMPLETE - NOT ALL FIELDS HANDLED HERE!!!
                innerCmdText += "</blk:Tuner>"
            innerCmdText += "</blk:Tuners>"

        if "DefaultUserSettings" in factorySettings:
            innerCmdText += "<blk:DefaultUserSettings>"
            innerCmdText += self.__serializeUserSettings(factorySettings["DefaultUserSettings"])
            innerCmdText += "</blk:DefaultUserSettings>"

        if "SupportedFeatures" in factorySettings:
            innerCmdText += "<blk:SupportedFeatures>"
            for sfi in factorySettings["SupportedFeatures"]:
                innerCmdText += "<blk:SupportedFeature>" + sfi + "</blk:SupportedFeature>"
            innerCmdText += "</blk:SupportedFeatures>"

        # print "<blk:SetFactorySettings>"  + innerCmdText + "</blk:SetFactorySettings>"
        response = self.__doSendInnerCommandText_(
            "<blk:SetFactorySettings>" + innerCmdText + "</blk:SetFactorySettings>"
        )
        resp = response.read()
        # print ("raw response=", resp, "\n")
        root = ET.fromstring(resp)
        if resultEnvelope is not None:
            self.__Add2DictIf(
                resultEnvelope,
                self.kMESSAGE_TIMESTAMP,
                root.find(".//timestamp", self.__namespaces),
                (lambda elt: float(elt.text))
            )

    """
    PROTECTED-INTERFACE
    """

    def ACUPeek(self, registerName, repeatCount=1, envelopeArgs=None, resultEnvelope=None):
        innerCmdText = ""
        innerCmdText += "<blk:ACUPeek>"
        innerCmdText += "<blk:RegisterName>" + registerName + "</blk:RegisterName>"
        if self.__ns != self.kNS_2014_04 and self.__ns != self.kNS_2014_07:
            innerCmdText += "<blk:RepeatCount>" + str(repeatCount) + "</blk:RepeatCount>"
        innerCmdText += "</blk:ACUPeek>"
        response = self.__doSendInnerCommandText_(innerCmdText)
        resp = response.read()
        # print ("raw response=", resp, "\n")
        root = ET.fromstring(resp)
        if resultEnvelope is not None:
            self.__Add2DictIf(
                resultEnvelope,
                self.kMESSAGE_TIMESTAMP,
                root.find(".//timestamp", self.__namespaces),
                (lambda elt: float(elt.text))
            )
        if repeatCount == 1:
            return int(root.find(".//blk:Value", self.__namespaces).text)
        else:
            values = []
            for v in root.findall(".//blk:Value", self.__namespaces):
                values.append(int(v.text))
            return values

    """
    PROTECTED-INTERFACE
    """

    def ACUPoke(self, registerName, value, envelopeArgs=None, resultEnvelope=None):
        innerCmdText = ""
        innerCmdText += (
                "<blk:ACUPoke><blk:RegisterName>"
                + registerName
                + "</blk:RegisterName><blk:Value>"
                + str(value)
                + "</blk:Value></blk:ACUPoke>"
        )
        response = self.__doSendInnerCommandText_(innerCmdText)
        resp = response.read()
        # print ("raw response=", resp, "\n")
        root = ET.fromstring(resp)
        if resultEnvelope is not None:
            self.__Add2DictIf(
                resultEnvelope,
                self.kMESSAGE_TIMESTAMP,
                root.find(".//timestamp", self.__namespaces),
                (lambda elt: float(elt.text))
            )

    """
    PROTECTED-INTERFACE
    """

    def CCUPeek(self, registerName, repeatCount=1, envelopeArgs=None, resultEnvelope=None):
        innerCmdText = ""
        innerCmdText += "<blk:CCUPeek>"
        innerCmdText += "<blk:RegisterName>" + registerName + "</blk:RegisterName>"
        if (self.__ns != self.kNS_2014_04) and (self.__ns != self.kNS_2014_07):
            innerCmdText += "<blk:RepeatCount>" + str(repeatCount) + "</blk:RepeatCount>"
        innerCmdText += "</blk:CCUPeek>"
        response = self.__doSendInnerCommandText_(innerCmdText)
        resp = response.read()
        # print ("raw response=", resp, "\n")
        root = ET.fromstring(resp)
        if resultEnvelope is not None:
            self.__Add2DictIf(
                resultEnvelope,
                self.kMESSAGE_TIMESTAMP,
                root.find(".//timestamp", self.__namespaces),
                (lambda elt: float(elt.text))
            )
        if repeatCount == 1:
            return int(root.find(".//blk:Value", self.__namespaces).text)
        else:
            values = []
            for v in root.findall(".//blk:Value", self.__namespaces):
                values.append(int(v.text))
            return values

    """
    PROTECTED-INTERFACE
    """

    def CCUPoke(self, registerName, value, envelopeArgs=None, resultEnvelope=None):
        innerCmdText = ""
        innerCmdText += (
                "<blk:CCUPoke><blk:RegisterName>"
                + registerName
                + "</blk:RegisterName><blk:Value>"
                + str(value)
                + "</blk:Value></blk:CCUPoke>"
        )
        response = self.__doSendInnerCommandText_(innerCmdText)
        resp = response.read()
        # print ("raw response=", resp, "\n")
        root = ET.fromstring(resp)
        if resultEnvelope is not None:
            self.__Add2DictIf(
                resultEnvelope,
                self.kMESSAGE_TIMESTAMP,
                root.find(".//timestamp", self.__namespaces),
                (lambda elt: float(elt.text))
            )

    # Helper to formulate a SOAP request
    def __WrapRequestInEnvelope(self, r):
        result = ""
        result += (
                "<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:blk=\""
                + self.__ns
                + "\">"
        )
        result += "	<soapenv:Header/>"
        result += "	<soapenv:Body>"
        result += r
        result += "</soapenv:Body>"
        result += "</soapenv:Envelope>"
        return result

    # Helper to optionally update a dictionary result if the given element is present
    def __Add2DictIf(self, d, index, elt, f=None):
        if elt is not None:
            if f is None:
                d[index] = elt
            else:
                d[index] = f(elt)

    __savedConn = None

    # Exception handling helper
    def __doSendInnerCommandText_(self, innerCmdText):
        msgBody = self.__WrapRequestInEnvelope(innerCmdText)
        useHttpLibToRead: bool = True  # experimental - not clearly faster but means no leak of 'TIME_WAIT' sockets which should make more long-term robust
        # and should help even more on REMOTE calls/access
        try:
            if self.__pipeline is not None:
                headers = {"Content-type": "text/xml", "Accept": "text/xml", "Connection": " keep-alive"}
                if self.__authorization_credentials is not None:
                    headers["Authorization"] = self.__authorization_credentials
                self.__pipeline.doSend(self, headers, msgBody)
                response = self.__pipeline.doReceiveNext()
                # if (500 <= response.status) and (response.status <= 599):
                if 500 <= response.status <= 599:
                    self.__ThrowCorrectHTTPException(response)
                return response
            elif useHttpLibToRead:
                headers: dict = {"Content-type": "text/xml", "Accept": "text/xml", "Connection": " keep-alive"}
                if self.__authorization_credentials is not None:
                    headers["Authorization"] = self.__authorization_credentials
                if self.__savedConn is None:
                    conn = http.client.HTTPConnection(urlparse(self.__url).netloc)
                    # conn.set_debuglevel(10)
                    conn.connect()
                    self.__savedConn = conn
                else:
                    conn = self.__savedConn
                # conn.debuglevel = 1
                # print(innerCmdText,'\n\n\n', msgBody)
                conn.request("POST", "/", msgBody, headers)
                response = conn.getresponse()
                if 500 <= response.status <= 599:
                    self.__ThrowCorrectHTTPException(response)
                return response
            else:
                opener = urllib.request.build_opener()
                if self.__authorization_credentials is not None:
                    opener.addheaders = [("Authorization", self.__authorization_credentials)]
                return opener.open(self.__url, msgBody)
        except urllib.error.HTTPError as e:
            self.__ThrowCorrectHTTPException(e)

    # Exception handling helper
    def __ThrowCorrectHTTPException(self, origHTTPError):
        str = origHTTPError.read()
        root = ET.fromstring(str)
        n = root.find(".//faultstring", self.__namespaces)
        if n is None:
            raise origHTTPError
        else:
            raise BLKQCL_Proxy.SOAPFault(origHTTPError, n.text)

    # Shared code to extract user settings from an XML blob returned from WS
    def __extractUserSettings(self, userSettingsNode):
        result = {}

        tmp = userSettingsNode.find(".//blk:LaserTemperature", self.__namespaces)
        if tmp is not None:
            t = {}
            self.__Add2DictIf(
                t,
                "1",
                tmp.find(".//blk:Tuner[@Tuner='1']", self.__namespaces),
                (lambda elt: float(elt.text))
            )
            self.__Add2DictIf(
                t,
                "2",
                tmp.find(".//blk:Tuner[@Tuner='2']", self.__namespaces),
                (lambda elt: float(elt.text))
            )
            self.__Add2DictIf(
                t,
                "3",
                tmp.find(".//blk:Tuner[@Tuner='3']", self.__namespaces),
                (lambda elt: float(elt.text))
            )
            self.__Add2DictIf(
                t,
                "4",
                tmp.find(".//blk:Tuner[@Tuner='4']", self.__namespaces),
                (lambda elt: float(elt.text))
            )
            result["LaserTemperature"] = t

        tmp = userSettingsNode.find(".//blk:LaserPumpingVoltage", self.__namespaces)
        if tmp is not None:
            lpv = {}
            if self.__ns == self.kNS_2014_04:
                tmpFixedData = tmp.find(".//blk:Fixed", self.__namespaces)
                if tmpFixedData is None:
                    lpv["Variable"] = True
                else:
                    t = {}
                    self.__Add2DictIf(
                        t,
                        "1",
                        tmpFixedData.find(".//blk:Tuner[@Tuner='1']", self.__namespaces),
                        (lambda elt: float(elt.text))
                    )
                    self.__Add2DictIf(
                        t,
                        "2",
                        tmpFixedData.find(".//blk:Tuner[@Tuner='2']", self.__namespaces),
                        (lambda elt: float(elt.text))
                    )
                    self.__Add2DictIf(
                        t,
                        "3",
                        tmpFixedData.find(".//blk:Tuner[@Tuner='3']", self.__namespaces),
                        (lambda elt: float(elt.text))
                    )
                    self.__Add2DictIf(
                        t,
                        "4",
                        tmpFixedData.find(".//blk:Tuner[@Tuner='4']", self.__namespaces),
                        (lambda elt: float(elt.text))
                    )
                    lpv["Fixed"] = t
            else:
                for i in range(1, 4 + 1):
                    self.__Add2DictIf(
                        lpv, str(i),
                        tmp.find(".//blk:Tuner[@Tuner='" + str(i) + "']/blk:Variable", self.__namespaces),
                        (lambda elt: "Variable")
                    )
                    self.__Add2DictIf(
                        lpv, str(i),
                        tmp.find(".//blk:Tuner[@Tuner='" + str(i) + "']/blk:Fixed", self.__namespaces),
                        (lambda elt: {"Fixed": float(elt.attrib["Voltage"])})
                    )
            result["LaserPumpingVoltage"] = lpv

        self.__Add2DictIf(
            result,
            "SystemTemperature",
            userSettingsNode.find(".//blk:SystemTemperature", self.__namespaces),
            (lambda elt: float(elt.text))
        )
        self.__Add2DictIf(
            result,
            "PulsePeriod",
            userSettingsNode.find(".//blk:PulsePeriod", self.__namespaces),
            (lambda elt: elt.text)
        )
        self.__Add2DictIf(
            result,
            "PulseDuration",
            userSettingsNode.find(".//blk:PulseDuration", self.__namespaces),
            (lambda elt: elt.text)
        )
        self.__Add2DictIf(
            result,
            "LaserControlMode",
            userSettingsNode.find(".//blk:LaserControlMode", self.__namespaces), (lambda elt: elt.text)
        )
        self.__Add2DictIf(
            result,
            "ContinueFiringAfterInterleavedScans",
            userSettingsNode.find(".//blk:ContinueFiringAfterInterleavedScans", self.__namespaces),
            (lambda elt: elt.text == "true")
        )
        self.__Add2DictIf(
            result,
            "AutomaticallyAdjustInterleavedScanLag",
            userSettingsNode.find(".//blk:AutomaticallyAdjustInterleavedScanLag", self.__namespaces),
            (lambda elt: elt.text == "true")
        )
        self.__Add2DictIf(
            result,
            "TRIG_OUTDelayTime",
            userSettingsNode.find(".//blk:TRIG_OUTDelayTime", self.__namespaces),
            (lambda elt: elt.text)
        )

        idleAutoPowerStateChanges = (
            userSettingsNode.find(".//blk:IdleAutoPowerStateChanges", self.__namespaces)
        )
        if idleAutoPowerStateChanges is not None:
            iapsc = {}
            self.__Add2DictIf(
                iapsc,
                "Off",
                idleAutoPowerStateChanges.find(".//blk:Off", self.__namespaces),
                (lambda elt: elt.text)
            )
            self.__Add2DictIf(
                iapsc,
                "Hibernate",
                idleAutoPowerStateChanges.find(".//blk:Hibernate", self.__namespaces),
                (lambda elt: elt.text)
            )
            self.__Add2DictIf(
                iapsc,
                "Sleep",
                idleAutoPowerStateChanges.find(".//blk:Sleep", self.__namespaces),
                (lambda elt: elt.text)
            )
            self.__Add2DictIf(
                iapsc,
                "LaserNotReady",
                idleAutoPowerStateChanges.find(".//blk:LaserNotReady", self.__namespaces),
                (lambda elt: elt.text)
            )
            result["IdleAutoPowerStateChanges"] = iapsc

        self.__Add2DictIf(
            result,
            "MonitorDACEnable",
            userSettingsNode.find(".//blk:MonitorDACEnable", self.__namespaces),
            (lambda elt: elt.text == "true")
        )
        self.__Add2DictIf(
            result,
            "GainDAC",
            userSettingsNode.find(".//blk:GainDAC", self.__namespaces),
            (lambda elt: int(elt.text))
        )
        self.__Add2DictIf(
            result,
            "SampleDelay",
            userSettingsNode.find(".//blk:SampleDelay", self.__namespaces),
            (lambda elt: elt.text)
        )
        self.__Add2DictIf(
            result,
            "SampleWidth",
            userSettingsNode.find(".//blk:SampleWidth", self.__namespaces),
            (lambda elt: elt.text)
        )
        self.__Add2DictIf(
            result,
            "DetectorTemperatureSetPoint",
            userSettingsNode.find(".//blk:CCUTemperatureSetPoint", self.__namespaces),
            (lambda elt: float(elt.text))
        )
        self.__Add2DictIf(
            result,
            "OnDiskspaceLow",
            userSettingsNode.find(".//blk:OnDiskspaceLow", self.__namespaces),
            (lambda elt: elt.text)
        )
        self.__Add2DictIf(
            result, "DeleteScansOlderThan",
            userSettingsNode.find(".//blk:DeleteScansOlderThan", self.__namespaces),
            (lambda elt: elt.text)
        )

        return result

    # [private]
    def __serializeUserSettings(self, settings):
        innerCmdText = ""
        if "LaserTemperature" in settings:
            innerCmdText += "<blk:LaserTemperature>"
            lt = settings["LaserTemperature"]
            if 1 in lt:
                innerCmdText += "<blk:Tuner Tuner=\"1\">" + str(lt[1]) + "</blk:Tuner>"
            if 2 in lt:
                innerCmdText += "<blk:Tuner Tuner=\"2\">" + str(lt[2]) + "</blk:Tuner>"
            if 3 in lt:
                innerCmdText += "<blk:Tuner Tuner=\"3\">" + str(lt[3]) + "</blk:Tuner>"
            if 4 in lt:
                innerCmdText += "<blk:Tuner Tuner=\"4\">" + str(lt[4]) + "</blk:Tuner>"
            innerCmdText += "</blk:LaserTemperature>"
        if "LaserPumpingVoltage" in settings:
            innerCmdText += "<blk:LaserPumpingVoltage>"
            if self.__ns == self.kNS_2014_04:
                if "Variable" in settings["LaserPumpingVoltage"]:
                    innerCmdText += "<blk:Variable/>"
                else:
                    innerCmdText += "<blk:Fixed>"
                    lt = settings["Fixed"]
                    if 1 in lt:
                        innerCmdText += "<blk:Tuner Tuner=\"1\">" + str(lt[1]) + "</blk:Tuner>"
                    if 2 in lt:
                        innerCmdText += "<blk:Tuner Tuner=\"2\">" + str(lt[2]) + "</blk:Tuner>"
                    if 3 in lt:
                        innerCmdText += "<blk:Tuner Tuner=\"3\">" + str(lt[3]) + "</blk:Tuner>"
                    if 4 in lt:
                        innerCmdText += "<blk:Tuner Tuner=\"4\">" + str(lt[4]) + "</blk:Tuner>"
                    innerCmdText += "</blk:Fixed>"
            else:
                lt = settings["LaserPumpingVoltage"]
                for i in range(1, 4 + 1):
                    if str(i) in lt:
                        txt = ""
                        if lt[str(i)] == "Variable":
                            txt = "<blk:Variable/>"
                        elif "Fixed" in lt[str(i)]:
                            txt = (
                                    "<blk:Fixed Voltage=\""
                                    + str(lt[str(i)]["Fixed"])
                                    + "\"/>"
                            )
                        innerCmdText += (
                                "<blk:Tuner Tuner=\""
                                + str(i)
                                + "\">"
                                + txt
                                + "</blk:Tuner>"
                        )
            innerCmdText += "</blk:LaserPumpingVoltage>"
        innerCmdText += self.__writeValueIfNeeded("PulseDuration", settings)
        innerCmdText += self.__writeValueIfNeeded("PulsePeriod", settings)
        innerCmdText += self.__writeValueIfNeeded("LaserControlMode", settings)
        innerCmdText += self.__writeValueIfNeeded("ContinueFiringAfterInterleavedScans", settings)
        innerCmdText += self.__writeValueIfNeeded("AutomaticallyAdjustInterleavedScanLag", settings)
        innerCmdText += self.__writeValueIfNeeded("TRIG_OUTDelayTime", settings)
        if "IdleAutoPowerStateChanges" in settings:
            innerCmdText += "<blk:IdleAutoPowerStateChanges>"
            autoPowerStateChanges = settings["IdleAutoPowerStateChanges"]
            innerCmdText += self.__writeValueIfNeeded("Off", autoPowerStateChanges)
            innerCmdText += self.__writeValueIfNeeded("Hibernate", autoPowerStateChanges)
            innerCmdText += self.__writeValueIfNeeded("Sleep", autoPowerStateChanges)
            innerCmdText += self.__writeValueIfNeeded("LaserNotReady", autoPowerStateChanges)
            innerCmdText += "</blk:IdleAutoPowerStateChanges>"
        innerCmdText += self.__writeValueIfNeeded("MonitorDACEnable", settings)
        innerCmdText += self.__writeValueIfNeeded("GainDAC", settings)
        innerCmdText += self.__writeValueIfNeeded("SampleDelay", settings)
        innerCmdText += self.__writeValueIfNeeded("SampleWidth", settings)
        innerCmdText += self.__writeValueIfNeeded("DetectorTemperatureSetPoint", settings)
        innerCmdText += self.__writeValueIfNeeded("OnDiskspaceLow", settings)
        innerCmdText += self.__writeValueIfNeeded("DeleteScansOlderThan", settings)
        return innerCmdText

    # [private]
    def __writeValueIfNeeded(self, eltName, settings):
        accumCmdText = ""
        if eltName in settings:
            asStr = None
            if isinstance(settings[eltName], str):
                asStr = settings[eltName]
            if isinstance(settings[eltName], int) or isinstance(settings[eltName], float):
                asStr = str(settings[eltName])
            if isinstance(settings[eltName], bool):
                asStr = "true" if settings[eltName] else "false"
            accumCmdText += "<blk:" + eltName + ">" + asStr + "</blk:" + eltName + ">"
        return accumCmdText

    # [private]
    def __writePIDIfNeeded(self, eltName, settings):
        accumCmdText = ""
        if eltName in settings:
            P = settings[eltName]["P"]
            I = settings[eltName]["I"]
            D = settings[eltName]["D"]
            accumCmdText += "<blk:" + eltName + ">"
            accumCmdText += "<blk:P>" + str(P) + "</blk:P>"
            accumCmdText += "<blk:I>" + str(I) + "</blk:I>"
            accumCmdText += "<blk:D>" + str(D) + "</blk:D>"
            accumCmdText += "</blk:" + eltName + ">"
        return accumCmdText

    # [private]
    def __writeRangeIfNeeded(self, eltName, settings):
        accumCmdText = ""
        if eltName in settings:
            lb = settings[eltName]["lowerBound"]
            ub = settings[eltName]["upperBound"]
            accumCmdText += (
                    "<blk:"
                    + eltName
                    + " upperBound=\""
                    + str(ub)
                    + "\" lowerBound=\""
                    + str(lb)
                    + "\"/>"
            )
        return accumCmdText

    # [private]
    def __extractRange(self, domNode):
        result = {}
        result["lowerBound"] = domNode.attrib["lowerBound"]
        result["upperBound"] = domNode.attrib["upperBound"]
        return result

    # [private]
    def __extractRange_Float(self, domNode):
        result = self.__extractRange(domNode)
        result["lowerBound"] = float(result["lowerBound"])
        result["upperBound"] = float(result["upperBound"])
        return result

    # [private]
    def __extractRange_int(self, domNode):
        result = self.__extractRange(domNode)
        result["lowerBound"] = int(result["lowerBound"])
        result["upperBound"] = int(result["upperBound"])
        return result

    # [private]
    def __extractPID(self, domNode):
        result = {}
        result["P"] = int(domNode.find("blk:P", self.__namespaces).text)
        result["I"] = int(domNode.find("blk:I", self.__namespaces).text)
        result["D"] = int(domNode.find("blk:D", self.__namespaces).text)
        return result

    # [private]
    def __ParseSOAPTimestampFromSOAPResult(self, soapResponseString):
        doWithStringManip = True
        doWithXPath = False
        if doWithXPath:
            root = ET.fromstring(soapResponseString)
            xPathTS = root.find(".//blk:timestamp", self.__namespaces), (lambda elt: float(elt.text))
        if doWithStringManip:
            i = 0
            kTS_TAG_ = "<timestamp>"
            kTS_TAG_LEN = len(kTS_TAG_)
            nextI = soapResponseString.find(kTS_TAG_, i)
            if nextI < 0:
                if doWithXPath:
                    if xPathTS is not None:
                        print("OOPS")
                return None
            # print ("thiselt = ", soapResponseString[nextI:nextI + 70])
            i = nextI + kTS_TAG_LEN
            endOfElt = soapResponseString.find("<", i)
            if endOfElt < 0:
                if doWithXPath:
                    if xPathTS is not None:
                        print("OOPS")
                return None
            if doWithXPath:
                if xPathTS != float(soapResponseString[i:endOfElt]):
                    print("OOPS")
            return float(soapResponseString[i:endOfElt])

    # [private]
    def __ParseMeasurementsFromResult(self, soapResponseString):
        doWithStringManip = True
        doWithXPath = False
        if doWithXPath:
            root = ET.fromstring(soapResponseString)
            xpMeasurements = {}
            for measurement in root.findall(".//blk:Measurement", self.__namespaces):
                xpMeasurements[float(measurement.attrib["waveNumber"])] = float(measurement.attrib["intensity"])
        if doWithStringManip:
            stringManipMeasurements = {}
            respLen = len(soapResponseString)
            i = 0
            kMEASUREMENT_TAG = "Measurement "
            kMEASUREMENT_TAG_LEN = len(kMEASUREMENT_TAG)
            kINTENSITY_ATTR = "intensity"
            kWAVENUMBER_ATTR = "waveNumber"
            while i < respLen:
                nextI = soapResponseString.find(kMEASUREMENT_TAG, i)
                if nextI < 0:
                    break
                # print ("thiselt = ", soapResponseString[nextI:nextI + 70])
                i = nextI + kMEASUREMENT_TAG_LEN

                intensityStartQuote = soapResponseString.find(kINTENSITY_ATTR, i)
                if intensityStartQuote < 0:
                    break
                intensityStartQuote = soapResponseString.find('\"', intensityStartQuote) + 1
                intensityEndQuote = soapResponseString.find('\"', intensityStartQuote)
                intensityStr = soapResponseString[intensityStartQuote:intensityEndQuote]
                # print ("intensityStr=", intensityStr)

                waveNumberStartQuote = soapResponseString.find(kWAVENUMBER_ATTR, i)
                if waveNumberStartQuote < 0:
                    break
                waveNumberStartQuote = soapResponseString.find('\"', waveNumberStartQuote) + 1
                waveNumberEndQuote = soapResponseString.find('\"', waveNumberStartQuote)
                waveNumberStr = soapResponseString[waveNumberStartQuote:waveNumberEndQuote]
                # print("waveNumberStr=", waveNumberStr)
                stringManipMeasurements[float(waveNumberStr)] = float(intensityStr)
        if doWithStringManip and doWithXPath:
            if set(stringManipMeasurements.items()) != set(xpMeasurements.items()):
                print("****OOPS")
        if doWithStringManip:
            return stringManipMeasurements
        if doWithXPath:
            return xpMeasurements
