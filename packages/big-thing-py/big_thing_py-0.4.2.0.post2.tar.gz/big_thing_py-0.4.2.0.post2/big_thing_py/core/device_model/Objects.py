from big_thing_py.core.service_model import Objects as Skill
from big_thing_py.core.device_model.DeviceObjects import MXDeviceCategory
from typing import Set, Dict, List, Union, Any


class AirConditioner(MXDeviceCategory, device_type=0x0000):
    skills = {
        Skill.switch,
        Skill.airConditionerMode,
    }


class AirPurifier(MXDeviceCategory, device_type=0x0001):
    skills = {
        Skill.switch,
        Skill.airPurifierFanMode,
    }


class AirQualityDetector(MXDeviceCategory, device_type=0x0002):
    skills = {
        Skill.dustSensor,
        Skill.carbonDioxideMeasurement,
        Skill.temperatureMeasurement,
        Skill.relativeHumidityMeasurement,
        Skill.tvocMeasurement,
    }


class Blind(MXDeviceCategory, device_type=0x0003):
    skills = {
        Skill.blind,
        Skill.blindLevel,
    }


class Button(MXDeviceCategory, device_type=0x0004):
    skills = {
        Skill.button,
    }


class Calculator(MXDeviceCategory, device_type=0x0005):
    skills = {
        Skill.calculator,
    }


class Camera(MXDeviceCategory, device_type=0x0006):
    skills = {
        Skill.switch,
        Skill.camera,
    }


class Charger(MXDeviceCategory, device_type=0x0007):
    skills = {
        Skill.chargingState,
        Skill.currentMeasurement,
        Skill.voltageMeasurement,
    }


class Clock(MXDeviceCategory, device_type=0x0008):
    skills = {
        Skill.clock,
    }


class ContactSensor(MXDeviceCategory, device_type=0x0009):
    skills = {
        Skill.contactSensor,
    }


class Curtain(MXDeviceCategory, device_type=0x000A):
    skills = {
        Skill.curtain,
    }


class Dehumidifier(MXDeviceCategory, device_type=0x0010):
    skills = {
        Skill.switch,
        Skill.dehumidifierMode,
    }


class Dishwasher(MXDeviceCategory, device_type=0x0011):
    skills = {
        Skill.switch,
        Skill.dishwasherMode,
    }


class DoorLock(MXDeviceCategory, device_type=0x0012):
    skills = {
        Skill.doorControl,
    }


class EmailProvider(MXDeviceCategory, device_type=0x0013):
    skills = {
        Skill.emailProvider,
    }


class Fan(MXDeviceCategory, device_type=0x0014):
    skills = {
        Skill.switch,
        Skill.fanControl,
    }


class Feeder(MXDeviceCategory, device_type=0x0015):
    skills = {
        Skill.switch,
        Skill.feederOperatingState,
        Skill.feederPortion,
    }


class GasMeter(MXDeviceCategory, device_type=0x0016):
    skills = {
        Skill.gasMeter,
    }


class GasValve(MXDeviceCategory, device_type=0x0017):
    skills = {
        Skill.gasMeter,
        Skill.valve,
    }


class Humidifier(MXDeviceCategory, device_type=0x0018):
    skills = {
        Skill.switch,
        Skill.humidifierMode,
    }


class HumiditySensor(MXDeviceCategory, device_type=0x0019):
    skills = {
        Skill.relativeHumidityMeasurement,
    }


class Irrigator(MXDeviceCategory, device_type=0x001A):
    skills = {
        Skill.switch,
        Skill.irrigatorOperatingState,
        Skill.irrigatorPortion,
    }


class LeakSensor(MXDeviceCategory, device_type=0x001B):
    skills = {
        Skill.leakSensor,
    }


class Light(MXDeviceCategory, device_type=0x001C):
    skills = {
        Skill.switch,
        Skill.switchLevel,
        Skill.colorControl,
    }


class LightSensor(MXDeviceCategory, device_type=0x001D):
    skills = {
        Skill.lightLevel,
    }


class MenuProvider(MXDeviceCategory, device_type=0x001E):
    skills = {
        Skill.menuProvider,
    }


class MotionSensor(MXDeviceCategory, device_type=0x001F):
    skills = {
        Skill.motionSensor,
    }


class PresenceSensor(MXDeviceCategory, device_type=0x0020):
    skills = {
        Skill.presenceSensor,
    }


class Pump(MXDeviceCategory, device_type=0x0021):
    skills = {
        Skill.switch,
        Skill.pump,
        Skill.pumpOperationMode,
    }


class Refrigerator(MXDeviceCategory, device_type=0x0022):
    skills = {
        Skill.switch,
        Skill.refrigeration,
    }


class RobotCleaner(MXDeviceCategory, device_type=0x0023):
    skills = {
        Skill.switch,
        Skill.robotCleanerCleaningMode,
    }


class Shade(MXDeviceCategory, device_type=0x0024):
    skills = {
        Skill.windowShade,
        Skill.windowShadeLevel,
    }


class Siren(MXDeviceCategory, device_type=0x0025):
    skills = {
        Skill.switch,
        Skill.sirenMode,
    }


class SmartPlug(MXDeviceCategory, device_type=0x0026):
    skills = {
        Skill.switch,
        Skill.powerMeter,
        Skill.voltageMeasurement,
        Skill.currentMeasurement,
    }


class SmokeDetector(MXDeviceCategory, device_type=0x0027):
    skills = {
        Skill.smokeDetector,
    }


class SoundSensor(MXDeviceCategory, device_type=0x0028):
    skills = {
        Skill.soundSensor,
        Skill.soundPressureLevel,
    }


class Speaker(MXDeviceCategory, device_type=0x0029):
    skills = {
        Skill.switch,
        Skill.mediaPlayback,
    }


class Switch(MXDeviceCategory, device_type=0x002A):
    skills = {
        Skill.switch,
    }


class Television(MXDeviceCategory, device_type=0x002C):
    skills = {
        Skill.switch,
        Skill.tvChannel,
        Skill.audioMute,
        Skill.audioVolume,
    }


class TemperatureSensor(MXDeviceCategory, device_type=0x002D):
    skills = {
        Skill.temperatureMeasurement,
    }


class TestDevice(MXDeviceCategory, device_type=0x002B):
    skills = {
        Skill.testSkill,
    }


class Valve(MXDeviceCategory, device_type=0x002E):
    skills = {
        Skill.valve,
    }


class WeatherProvider(MXDeviceCategory, device_type=0x002F):
    skills = {
        Skill.weatherProvider,
    }


class Window(MXDeviceCategory, device_type=0x0030):
    skills = {
        Skill.windowControl,
    }


class FaceRecognizer(MXDeviceCategory, device_type=0x0031):
    skills = {}


class CloudServiceProvider(MXDeviceCategory, device_type=0x0032):
    skills = {}
    
class FallDetector(MXDeviceCategory, device_type=0x0033):
    skills = {}
    
class NewsProvider(MXDeviceCategory, device_type=0x0034):
    skills = {}


####


class ManagerThing(MXDeviceCategory, device_type=0xF000):
    skills = {
        Skill.manager,
    }


class Undefined(MXDeviceCategory, device_type=0xFFFF):
    skills = {}


if __name__ == '__main__':
    print(Window.skills)
