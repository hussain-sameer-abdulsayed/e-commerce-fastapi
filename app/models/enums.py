from enum import Enum

class Province(str, Enum):
    baghdad = "بغداد"
    basrah = "البصرة"
    ninawa = "نينوى"
    erbil = "اربيل"
    kirkuk = "كركوك"
    sulaymaniyah = "السليمانية"
    duhok = "دهوك"
    anbar = "الانبار"
    babil = "بابل"
    najaf = "النجف"
    karbala = "كربلاء"
    maysan = "ميسان"
    diyala = "ديالى"
    wasit = "واسط"
    salahaddin = "صلاح_الدين"
    muthanna = "المثنى"
    thiqar = "ذي_قار"


class Order_Status(str, Enum):
   pending = "معلق"
   accepted = "مقبول"
   shipped = "جار التوصيل"
   dellivered = "تم التوصيل"
   cancelled = "ملغى"

class Discount_Model_Type(str, Enum):
    category = "فئة"
    product = "منتج"
    shipment = "توصيل"

class Gender(str, Enum):
   male = "ذكر"
   female = "انثى"



   