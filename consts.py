INTERVAL_IN_S = 60 * 60 * 24 * 15  # 15 days

LIFETIME = dict()

TIMING_BELT = "Timing_belt"  # تسمه تایم
LIFETIME[TIMING_BELT] = 80000  # should change it every 80,000km(if its not original: 50,000km)

ENGINE_OIL = "Engine_oil"  # روغن موتور
LIFETIME[ENGINE_OIL] = 5000  # should change it every 5000km

TIRE_ROTATION = "Tire_rotation"  # تعویض ضربدری لاستیک ها
LIFETIME[TIRE_ROTATION] = 20000  # should change it every 20,000km

TIRE = "Tire"  # تعویض کلی لاستیک ها
LIFETIME[TIRE] = 40000  # should change it every 40,000km

BATTERY_WATER = "Battery_water"  # بررسی آب باتری
LIFETIME[BATTERY_WATER] = 5000  # should change it every 5000km

ENGINE_CHECK = "Engine_check"  # تنظیم موتور(تعویض شمع)
LIFETIME[ENGINE_CHECK] = 25000  # should change it every 25,000km

GEAR_OIL = "Gear_oil"  # روغن گیربکس(واسکازین)
LIFETIME[GEAR_OIL] = 100000  # should change it every 100,000km

CLUTCH_PLATE = "Clutch_plate"  # صفحه کلاج
LIFETIME[CLUTCH_PLATE] = 100000  # should change it every 100,000km

AIR_FILTER = "Air_filter"  # فیلتر هوا
LIFETIME[AIR_FILTER] = 10000  # should change it every 10,000km

OIL_FILTER = "Oil_filter"  # فیلتر روغن
LIFETIME[OIL_FILTER] = 10000  # should change it every 10,000km

ROOM_FILTER = "Room_filter"  # فیلتر اتاق
LIFETIME[ROOM_FILTER] = 20000  # should change it every 20,000km

BENZINE_FILTER = "Benzine_filter"  # صافی بنزین
LIFETIME[BENZINE_FILTER] = 20000  # should change it every 20,000km

BRAKE_FLUID = "Brake_fluid"  # روغن ترمز
LIFETIME[BRAKE_FLUID] = 30000  # should change it every min(60,000km or 2 years)~=30,000km
