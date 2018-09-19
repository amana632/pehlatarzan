from main import db
from flask_marshmallow import Marshmallow

from main import ma

class User(db.Model):
    __tablename__ = 'User'
    password = db.Column(db.String(255))
    email = db.Column(db.String(255),primary_key=True)
    user_type = db.Column(db.String(255))

    def __init__(self, password, email, user_type):
        self.password = password
        self.email = email
        self.user_type = user_type

class UserSchema(ma.Schema):
    class Meta:
        fields = ('password', 'email', 'user_type')

user_schema = UserSchema()
users_schema = UserSchema(many=True)



class ServiceProvider(db.Model):
    __tablename__ = 'ServiceProvider'
    emailid = db.Column(db.String(255), primary_key = True)
    service_advisor_name = db.Column(db.String(255))
    service_advisor_no = db.Column(db.Integer)
    workshop_no = db.Column(db.Integer)
    latitude = db.Column(db.String(255))
    longitude = db.Column(db.String(255))
    user_pic = db.Column(db.String)
    workshop_pic = db.Column(db.String)
    gst = db.Column(db.String(255))
    service_category = db.Column(db.String)
    pickup_facility = db.Column(db.String(255))
    twentyfourhour_facility = db.Column(db.String(255))
    general_service = db.Column(db.String)
    roadside_assistance = db.Column(db.String)
    maintenence_repair = db.Column(db.String)
    dent_repairing = db.Column(db.String)
    car_wash = db.Column(db.String)
    disc_general_service = db.Column(db.String(255))
    disc_roadside_assistance = db.Column(db.String(255))
    disc_maintenence_repair = db.Column(db.String(255))
    disc_dent_repairing = db.Column(db.String(255))
    disc_car_wash = db.Column(db.String(255))
    bank_name = db.Column(db.String(255))
    branch_name = db.Column(db.String(255))
    ifsc_code = db.Column(db.String(255))
    account_number = db.Column(db.String(255))
    hb_twotosix = db.Column(db.Integer)
    hb_sixtoten = db.Column(db.Integer)
    hb_tenabove = db.Column(db.Integer)
    sedan_sixtoten = db.Column(db.Integer)
    sedan_tentotwentyfive = db.Column(db.Integer)
    sedan_twentyfiveabove = db.Column(db.Integer)
    suv_twelvetotwenty = db.Column(db.Integer)
    suv_twentytoforty = db.Column(db.Integer)
    suv_fortyabove = db.Column(db.Integer)
    muv_fifteentoforty = db.Column(db.Integer)
    muv_fortyabove = db.Column(db.Integer)


    def __init__(self, emailid, service_advisor_name, service_advisor_no, workshop_no, latitude, longitude, user_pic, workshop_pic, gst, service_category, pickup_facility, twentyfourhour_facility, general_service, roadside_assistance, maintenence_repair, dent_repairing, car_wash, disc_general_service, disc_roadside_assistance, disc_maintenence_repair, disc_dent_repairing, disc_car_wash, bank_name, branch_name, ifsc_code, account_number, hb_twotosix, hb_sixtoten, hb_tenabove, sedan_sixtoten, sedan_tentotwentyfive, sedan_twentyfiveabove, suv_twelvetotwenty, suv_twentytoforty, suv_fortyabove, muv_fifteentoforty, muv_fortyabove ):
        self.emailid = emailid
        self.service_advisor_name = service_advisor_name
        self.service_advisor_no = service_advisor_no
        self.workshop_no = workshop_no
        self.latitude = latitude
        self.longitude = longitude
        self.user_pic = user_pic
        self.workshop_pic = workshop_pic
        self.gst = gst
        self.service_category = service_category
        self.pickup_facility = pickup_facility
        self.twentyfourhour_facility = twentyfourhour_facility
        self.general_service = general_service
        self.roadside_assistance = roadside_assistance
        self.maintenence_repair = maintenence_repair
        self.dent_repairing = dent_repairing
        self.car_wash = car_wash
        self.disc_general_service = disc_general_service
        self.disc_roadside_assistance = disc_roadside_assistance
        self.disc_maintenence_repair = disc_maintenence_repair
        self.disc_dent_repairing = disc_dent_repairing
        self.disc_car_wash = disc_car_wash
        self.bank_name = bank_name
        self.branch_name = branch_name
        self.ifsc_code = ifsc_code
        self.account_number = account_number
        self.hb_twotosix = hb_twotosix
        self.hb_sixtoten = hb_sixtoten
        self.hb_tenabove = hb_tenabove
        self.sedan_sixtoten = sedan_sixtoten
        self.sedan_tentotwentyfive = sedan_tentotwentyfive
        self.sedan_twentyfiveabove = sedan_twentyfiveabove
        self.suv_twelvetotwenty = suv_twelvetotwenty
        self.suv_twentytoforty = suv_twentytoforty
        self.suv_fortyabove = suv_fortyabove
        self.muv_fifteentoforty = muv_fifteentoforty
        self.muv_fortyabove = muv_fortyabove
            
class ServiceProviderSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('emailid', 'service_advisor_name', 'service_advisor_no', 'workshop_no', 'latitude', 'longitude', 'user_pic', 'workshop_pic', 'gst', 'service_category', 'pickup_facility', 'twentyfourhour_facility', 'general_service', 'roadside_assistance', 'maintenence_repair', 'dent_repairing', 'car_wash', 'disc_general_service', 'disc_roadside_assistance', 'disc_maintenence_repair', 'disc_dent_repairing', 'disc_car_wash', 'bank_name', 'branch_name', 'ifsc_code', 'account_number', 'hb_twotosix', 'hb_sixtoten', 'hb_tenabove', 'sedan_sixtoten', 'sedan_tentotwentyfive', 'sedan_twentyfiveabove', 'suv_twelvetotwenty', 'suv_twentytoforty', 'suv_fortyabove', 'muv_fifteentoforty', 'muv_fortyabove')

serviceprovider_schema = ServiceProviderSchema()
serviceproviders_schema = ServiceProviderSchema(many=True)


