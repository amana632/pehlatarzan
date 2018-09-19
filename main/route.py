from flask import request, jsonify
from main import app
from main.model import User, user_schema, users_schema, UserSchema, serviceprovider_schema, serviceproviders_schema, ServiceProvider, ServiceProviderSchema
from flask_marshmallow import Marshmallow
from main import db


@app.route("/serviceproviderupdate/<emailid>", methods=["PUT"])
def serviceprovider_update(emailid):
    serviceprovider = ServiceProvider.query.filter_by(emailid=emailid).first_or_404()

    emailid = request.form['emailid']
    service_advisor_name = request.form['name']
    service_advisor_no = request.form['phone']
    workshop_no = request.form['workshop_no']
    latitude = request.form['lat']
    longitude = request.form['long']
    user_pic = request.form['userpic']
    workshop_pic = request.form['workshoppic']
    gst = request.form['gst']
    service_category = request.form['category']
    pickup_facility = request.form['pickup_facility']
    twentyfourhour_facility = request.form['24hr']
    general_service = request.form['general_service']
    roadside_assistance = request.form['roadside_assistance']
    maintenence_repair = request.form['maintenence_repair']
    dent_repairing = request.form['dent_repairing']
    car_wash = request.form['car_wash']
    disc_general_service = request.form['disc_general_service']
    disc_roadside_assistance = request.form['disc_roadside_assistance']
    disc_maintenence_repair = request.form['disc_maintenence_repair']
    disc_dent_repairing = request.form['disc_dent_repairing']
    disc_car_wash = request.form['disc_car_wash']
    bank_name = request.form['bank_name']
    branch_name = request.form['branch_name']
    ifsc_code = request.form['ifsc_code']
    account_number = request.form['account_number']
    hb_twotosix = request.form['hb_twotosix']
    hb_sixtoten = request.form['hb_sixtoten']
    hb_tenabove = request.form['hb_tenabove']
    sedan_sixtoten = request.form['sedan_sixtoten']
    sedan_tentotwentyfive = request.form['sedan_tentotwentyfive']
    sedan_twentyfiveabove = request.form['sedan_twentyfiveabove']
    suv_twelvetotwenty = request.form['suv_twelvetotwenty']
    suv_twentytoforty = request.form['suv_twentytoforty']
    suv_fortyabove = request.form['suv_fortyabove']
    muv_fifteentoforty = request.form['muv_fifteentoforty']
    muv_fortyabove = request.form['muv_fortyabove']


    serviceprovider.emailid = emailid
    serviceprovider.service_advisor_name = service_advisor_name
    serviceprovider.service_advisor_no = service_advisor_no
    serviceprovider.workshop_no = workshop_no
    serviceprovider.latitude = latitude
    serviceprovider.longitude = longitude
    serviceprovider.user_pic = user_pic
    serviceprovider.workshop_pic = workshop_pic
    serviceprovider.gst = gst
    serviceprovider.service_category = service_category
    serviceprovider.pickup_facility = pickup_facility
    serviceprovider.twentyfourhour_facility = twentyfourhour_facility
    serviceprovider.general_service = general_service
    serviceprovider.roadside_assistance = roadside_assistance
    serviceprovider.maintenence_repair = maintenence_repair
    serviceprovider.dent_repairing = dent_repairing
    serviceprovider.car_wash = car_wash
    serviceprovider.disc_general_service = disc_general_service
    serviceprovider.disc_roadside_assistance = disc_roadside_assistance
    serviceprovider.disc_maintenence_repair = disc_maintenence_repair
    serviceprovider.disc_dent_repairing = disc_dent_repairing
    serviceprovider.disc_car_wash = disc_car_wash
    serviceprovider.bank_name = bank_name
    serviceprovider.branch_name = branch_name
    serviceprovider.ifsc_code = ifsc_code
    serviceprovider.account_number = account_number
    serviceprovider.hb_twotosix = hb_twotosix
    serviceprovider.hb_sixtoten = hb_sixtoten
    serviceprovider.hb_tenabove = hb_tenabove
    serviceprovider.sedan_sixtoten = sedan_sixtoten
    serviceprovider.sedan_tentotwentyfive = sedan_tentotwentyfive
    serviceprovider.sedan_twentyfiveabove = sedan_twentyfiveabove
    serviceprovider.suv_twelvetotwenty = suv_twelvetotwenty
    serviceprovider.suv_twentytoforty = suv_twentytoforty
    serviceprovider.suv_fortyabove = suv_fortyabove
    serviceprovider.muv_fifteentoforty = muv_fifteentoforty
    serviceprovider.muv_fortyabove = muv_fortyabove
 

    db.session.commit()
    return serviceprovider_schema.jsonify(serviceprovider)


@app.route("/register_serviceprovider", methods=["POST"])
def register_serviceprovider():
    emailid = request.form['emailid']
    service_advisor_name = request.form['name']
    service_advisor_no = request.form['phone']
    workshop_no = request.form['workshop_no']
    latitude = request.form['lat']
    longitude = request.form['long']
    user_pic = request.form['userpic']
    workshop_pic = request.form['workshoppic']
    gst = request.form['gst']
    service_category = request.form['category']
    pickup_facility = request.form['pickup_facility']
    twentyfourhour_facility = request.form['24hr']
    general_service = request.form['general_service']
    roadside_assistance = request.form['roadside_assistance']
    maintenence_repair = request.form['maintenence_repair']
    dent_repairing = request.form['dent_repairing']
    car_wash = request.form['car_wash']
    disc_general_service = request.form['disc_general_service']
    disc_roadside_assistance = request.form['disc_roadside_assistance']
    disc_maintenence_repair = request.form['disc_maintenence_repair']
    disc_dent_repairing = request.form['disc_dent_repairing']
    disc_car_wash = request.form['disc_car_wash']
    bank_name = request.form['bank_name']
    branch_name = request.form['branch_name']
    ifsc_code = request.form['ifsc_code']
    account_number = request.form['account_number']
    hb_twotosix = request.form['hb_twotosix']
    hb_sixtoten = request.form['hb_sixtoten']
    hb_tenabove = request.form['hb_tenabove']
    sedan_sixtoten = request.form['sedan_sixtoten']
    sedan_tentotwentyfive = request.form['sedan_tentotwentyfive']
    sedan_twentyfiveabove = request.form['sedan_twentyfiveabove']
    suv_twelvetotwenty = request.form['suv_twelvetotwenty']
    suv_twentytoforty = request.form['suv_twentytoforty']
    suv_fortyabove = request.form['suv_fortyabove']
    muv_fifteentoforty = request.form['muv_fifteentoforty']
    muv_fortyabove = request.form['muv_fortyabove']

    
    
    new_service_provider = ServiceProvider(emailid, service_advisor_name, service_advisor_no, workshop_no, latitude, longitude, user_pic, workshop_pic, gst, service_category, pickup_facility, twentyfourhour_facility, general_service, roadside_assistance, maintenence_repair, dent_repairing, car_wash, disc_general_service, disc_roadside_assistance, disc_maintenence_repair, disc_dent_repairing, disc_car_wash, bank_name, branch_name, ifsc_code, account_number, hb_twotosix, hb_sixtoten, hb_tenabove, sedan_sixtoten, sedan_tentotwentyfive, sedan_twentyfiveabove, suv_twelvetotwenty, suv_twentytoforty, suv_fortyabove, muv_fifteentoforty, muv_fortyabove)

    db.session.add(new_service_provider)
    db.session.commit()


# endpoint to show all users
@app.route("/service_provider", methods=["GET"])
def get_service_provider():
    all_serviceproviders = ServiceProvider.query.all()
    result = serviceproviders_schema.dump(all_serviceproviders)
    return jsonify(result.data)

@app.route('/service_provider/<emailid>')
def show_service_provider(emailid):
    serviceprovider = ServiceProvider.query.filter_by(emailid=emailid).first_or_404()
    return jsonify(serviceprovider.data)

@app.route("/user", methods=["POST"])
def add_user():
    password = request.form['password']
    email = request.form['emailid']
    user_type = request.form['user_type']
    
    
    new_user = User(password, email, user_type)

    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user)


@app.route("/user", methods=["GET"])
def get_user():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result.data)

@app.route('/user/<email>')
def show_user(emailid):
    user = User.query.filter_by(email=email).first_or_404()
    return jsonify(user.data)
















