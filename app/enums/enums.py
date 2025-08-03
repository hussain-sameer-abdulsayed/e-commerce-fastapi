from enum import Enum

class Province(Enum):
    baghdad = "Baghdad"
    basrah = "Basrah"
    ninawa = "Ninewa"
    erbil = "Erbil"
    kirkuk = "Kirkuk"
    sulaymaniyah = "Sulaymaniyah"
    duhok = "Duhok"
    anbar = "Anbar"
    babil = "Babil"
    najaf = "Najaf"
    karbala = "Karbala"
    maysan = "Maysan"
    diyala = "Diyala"
    wasit = "Wasit"
    salahaddin = "Salahaddin"
    muthanna = "Muthanna"
    thiqar = "Thiqar"


class Order_Status(Enum):
   pending = "Pending"
   accepted = "Accepted"
   shipped = "Shipped"
   delivered = "Delivered"
   cancelled = "Cancelled"

class Discount_Model_Type(Enum):
    category = "Category"
    product = "Product"
    shipment = "Shipment"

class Gender(Enum):
   male = "Male"
   female = "Female"
