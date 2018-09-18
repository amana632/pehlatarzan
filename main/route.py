from flask import request, jsonify
from main import app
from main.model import User, user_schema, users_schema, UserSchema, serviceprovider_schema, serviceproviders_schema, ServiceProvider, ServiceProviderSchema
from flask_marshmallow import Marshmallow
from main import db


# @app.route("/order/<id>", methods=["PUT"])
# def order_update(id):
#     order = Order.query.get(id)

#     order_id = request.form['order_id']
#     item_id = request.form['item_id']
#     quantity = request.form['quantity']	
#     price = request.form['price']
#     user_id = request.form['user_id']
#     hotel_id = request.form['hotel_id']
#     waiter_id = request.form['waiter_id']


#     order.order_id = order_id
#     order.item_id = item_id
#     order.quantity = quantity
#     order.price = price
#     order.user_id = user_id
#     order.hotel_id = hotel_id
#     order.waiter_id = waiter_id
 

#     db.session.commit()
#     return order_schema.jsonify(order)


@app.route("/register_serviceprovider", methods=["POST"])
def register_serviceprovider():
    email = request.form['email']
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

    
    
    new_service_provider = ServiceProvider(email, service_advisor_name, service_advisor_no, workshop_no, latitude, longitude, user_pic, workshop_pic, gst, service_category, pickup_facility, twentyfourhour_facility, general_service, roadside_assistance, maintenence_repair, dent_repairing, car_wash, disc_general_service, disc_roadside_assistance, disc_maintenence_repair, disc_dent_repairing, disc_car_wash, bank_name, branch_name, ifsc_code, account_number, hb_twotosix, hb_sixtoten, hb_tenabove, sedan_sixtoten, sedan_tentotwentyfive, sedan_twentyfiveabove, suv_twelvetotwenty, suv_twentytoforty, suv_fortyabove, muv_fifteentoforty, muv_fortyabove)

    db.session.add(new_service_provider)
    db.session.commit()
    return jsonify(new_service_provider)


# endpoint to show all users
@app.route("/service_provider", methods=["GET"])
def get_service_provider():
    all_serviceproviders = ServiceProvider.query.all()
    result = serviceproviders_schema.dump(all_serviceproviders)
    return jsonify(result.data)

@app.route('/service_provider/<email>')
def show_service_provider(email):
    serviceprovider = ServiceProvider.query.filter_by(email=email).first_or_404()
    return jsonify(serviceprovider.data)

@app.route("/user", methods=["POST"])
def add_user():
    user_id = request.form['userid']
    password = request.form['password']
    email = request.form['email']
    user_type = request.form['user_type']
    
    
    new_user = User(user_id, password, email, user_type)

    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user)



# @app.route("/user", methods=["POST"])
# def add_user():
#     user_name = request.form['username']
#     password = request.form['password']
#     name = request.form['name']
#     phone = request.form['phone']
#     email = request.form['email']
#     user_type = request.form['user_type']
    
    
#     new_user = User(user_name, password, name, phone, email, user_type)

#     db.session.add(new_user)
#     db.session.commit()
#     return jsonify(new_user)


# @app.route("/order", methods=["POST"])
# def add_order():
#     order_id = request.form['order_id']
#     item_id = request.form['item_id']
#     quantity = request.form['quantity']	
#     price = request.form['price']
#     user_id = request.form['user_id']
#     hotel_id = request.form['hotel_id']
#     waiter_id = request.form['waiter_id']

#     new_order = Order(order_id, item_id, quantity, price, user_id, hotel_id, waiter_id)

#     db.session.add(new_order)
#     db.session.commit()
#     return jsonify(new_order)



# # endpoint to show all users
# @app.route("/order", methods=["GET"])
# def get_order():
#     all_orders = Order.query.all()
#     result = orders_schema.dump(all_orders)
#     return jsonify(result.data)


# # endpoint to get user detail by id
# @app.route("/order/<id>", methods=["GET"])
# def order_detail(id):
#     order = Order.query.get(id)
#     return order_schema.jsonify(order)


# # endpoint to update user
# @app.route("/order/<id>", methods=["PUT"])
# def order_update(id):
#     order = Order.query.get(id)

#     order_id = request.form['order_id']
#     item_id = request.form['item_id']
#     quantity = request.form['quantity']	
#     price = request.form['price']
#     user_id = request.form['user_id']
#     hotel_id = request.form['hotel_id']
#     waiter_id = request.form['waiter_id']


#     order.order_id = order_id
#     order.item_id = item_id
#     order.quantity = quantity
#     order.price = price
#     order.user_id = user_id
#     order.hotel_id = hotel_id
#     order.waiter_id = waiter_id
 

#     db.session.commit()
#     return order_schema.jsonify(order)


# # endpoint to delete user
# @app.route("/order/<id>", methods=["DELETE"])
# def order_delete(id):
#     order = Order.query.get(id)
#     db.session.delete(order)
#     db.session.commit()

#     return order_schema.jsonify(order)


# # endpoint to create new user
# @app.route("/cook", methods=["POST"])
# def add_cook():
#     cook_id = request.form['cook_id']
#     hotel_id = request.form['hotel_id']
#     cook_name = request.form['cook_name']
#     order_id = request.form['order_id']
#     db.session.add(new_cook)
#     db.session.commit()

#     return jsonify(new_cook)


# # endpoint to show all users
# @app.route("/cook", methods=["GET"])
# def get_cook():
#     all_cook = Cook.query.all()
#     result = cook_schema.dump(all_cook)
#     return jsonify(result.data)


# # endpoint to get user detail by id
# @app.route("/cook/<id>", methods=["GET"])
# def cook_detail(id):
#     cook = Cook.query.get(id)
#     return cook_schema.jsonify(cook)


# # endpoint to update user
# @app.route("/cook/<id>", methods=["PUT"])
# def cook_update(id):
#     cook_id= request.form['cook_id']
#     hotel_id = request.form['hotel_id']
#     cook_name = request.form['cook_name']
#     order_id = request.form['order_id']

#     cook.hotel_id = hotel_id
#     cook.cook_name = cook_name
#     cook.order_id = order_id
#     cook.cook_id = cook_id
    
#     db.session.commit()
#     return cook_schema.jsonify(cook)


# # endpoint to delete user
# @app.route("/cook/<id>", methods=["DELETE"])
# def cook_delete(id):
#     cook = Cook.query.get(id)
#     db.session.delete(cook)
#     db.session.commit()

#     return user_schema.jsonify(cook)


# @app.route("/waiter", methods=["POST"])
# def add_waiter():
#     hotel_id = request.form['hotel_id']
#     waiter_name = request.form['waiter_name']
#     waiter_contact = request.form['waiter_contact']
#     waiter_free = request.form['waiter_free']
#     order_id = request.form['order_id']
#     waiter_id = request.form['waiter_id']
#     db.session.add(new_waiter)
#     db.session.commit()

#     return jsonify(new_waiter)


# # endpoint to show all users
# @app.route("/waiter", methods=["GET"])
# def get_waiter():
#     all_waiters = Waiter.query.all()
#     result = waiters_schema.dump(all_waiters)
#     return jsonify(result.data)


# # endpoint to get user detail by id
# @app.route("/waiter/<id>", methods=["GET"])
# def waiter_detail(id):
#     waiter = Waiter.query.get(id)
#     return user_schema.jsonify(waiter)


# # endpoint to update user
# @app.route("/waiter/<id>", methods=["PUT"])
# def waiter_update(id):
#     hotel_id = request.form['hotel_id']
#     waiter_name = request.form['waiter_name']
#     waiter_contact = request.form['waiter_contact']
#     waiter_free = request.form['waiter_free']
#     order_id = request.form['order_id']
#     waiter_id = request.form['waiter_id']

#     waiter.hotel_id = hotel_id
#     waiter.waiter_name = waiter_name
#     waiter.waiter_contact = waiter_contact
#     waiter.waiter_free = waiter_free
#     waiter.order_id = order_id
#     waiter.waiter_id= waiter_id
    

#     db.session.commit()
#     return waiter_schema.jsonify(waiter)


# # endpoint to delete user
# @app.route("/waiter/<id>", methods=["DELETE"])
# def waiter_delete(id):
#     waiter = Waiter.query.get(id)
#     db.session.delete(waiter)
#     db.session.commit()

#     return user_schema.jsonify(waiter)

# # endpoint to create new hotels
# @app.route("/hotels", methods=["POST"])
# def add_hotels():
#     hotel_id = request.form['hotel_id']
#     hotel_name = request.form['hotel_name']
#     hotel_address = request.form['hotel_address']
#     hotel_open = request.form['hotel_open']
#     hotel_moreinfo = request.form['hotel_moreinfo']
#     hotel_phone = request.form['hotel_phone']
#     hotel_email = request.form['hotel_email']
#     hotel_lat = request.form['hotel_lat']
#     hotel_long = request.form['hotel_long']
#     hotel_capacity = request.form['hotel_capacity']
#     hotel_desc = request.form['hotel_desc']
#     hotel_stars = request.form['hotel_stars']
#     hotel_menupic = request.form['hotel_menupic']
#     hotel_close = request.form['hotel_close']
#     hotel_hotelpic = request.form['hotel_hotelpic']
#     hotel_avgcost = request.form['hotel_avgcost']
    
    
    
    
#     new_hotels = Hotels(hotel_id, hotel_name,hotel_address,hotel_open,hotel_close,hotel_desc,hotel_stars,hotel_menupic,      hotel_hotelpic,hotel_avgcost,hotel_moreinfo,hotel_phone, hotel_email,hotel_lat, hotel_long,hotel_capacity)

#     db.session.add(new_hotels)
#     db.session.commit()

#     return jsonify(new_hotels)


# # endpoint to show all hotelss
# @app.route("/hotels", methods=["GET"])
# def get_hotels():
#     all_hotelss = Hotels.query.all()
#     result = hotelss_schema.dump(all_hotelss)
#     return jsonify(result.data)


# # endpoint to get hotels detail by id
# @app.route("/hotels/<id>", methods=["GET"])
# def hotels_detail(id):
#     hotels = Hotels.query.get(id)
#     return hotels_schema.jsonify(hotels)


# # endpoint to update hotels
# @app.route("/hotels/<id>", methods=["PUT"])
# def hotels_update(id):
#     hotelsname = request.form['hotelsname']
#     email = request.form['email']
#     hotelsfirstname = request.form['hotelsfirstname']
#     hotelslastname = request.form['hotelslastname']
#     hotelsphone = request.form['hotelsphone']
#     hotelspass = request.form['hotelspass']

#     hotels.hotel_id= hotel_id
#     hotels.hotel_name = hotel_name
#     hotels.hotel_address  = hotel_address
#     hotels.hotel_open= hotel_open
#     hotels.hotel_close= hotel_close
#     hotels.hotel_desc= hotel_desc
#     hotels.hotel_stars= hotel_stars
#     hotels.hotel_menupic= hotel_menupic
#     hotels.hotel_hotelpic = hotel_hotelpic
#     hotels.hotel_avgcost  = hotel_avgcost
#     hotels.hotel_moreinfo= hotel_moreinfo
#     hotels.hotel_phone= hotel_phone
#     hotels.hotel_email= hotel_email
#     hotels.hotel_lat= hotel_lat
#     hotels.hotel_long= hotel_long
#     hotels.hotel_capacity= hotel_capacity

#     db.session.commit()
#     return hotels_schema.jsonify(hotels)


# # endpoint to delete hotels
# @app.route("/hotels/<id>", methods=["DELETE"])
# def hotels_delete(id):
#     hotels = Hotels.query.get(id)
#     db.session.delete(hotels)
#     db.session.commit()

#     return hotels_schema.jsonify(hotels)

# # endpoint to create new user
# @app.route("/products", methods=["POST"])
# def add_trans():
#     trans_id = request.form['trans_id']
#     user_id = request.form['user_id']
#     hotel_id = request.form['hotel_id']	
#     total = request.form['total']
#     coupon_disc = request.form['coupon_disc']
#     trans_date = request.form['trans_date']

#     new_transaction = Trans(trans_id, user_id, hotel_id, total, coupon_disc, trans_date)

#     db.session.add(new_transaction)
#     db.session.commit()
#     return jsonify(new_transaction)



# # endpoint to show all users
# @app.route("/trans", methods=["GET"])
# def get_trans():
#     all_transs = Trans.query.all()
#     result = transs_schema.dump(all_transs)
#     return jsonify(result.data)


# # endpoint to get user detail by id
# @app.route("/trans/<id>", methods=["GET"])
# def trans_detail(id):
#     trans = Trans.query.get(id)
#     return trans_schema.jsonify(trans)


# # endpoint to update user
# @app.route("/trans/<id>", methods=["PUT"])
# def trans_update(id):
#     trans = Trans.query.get(id)
#     trans_ids = request.form['trans_id']
#     user_ids = request.form['user_id']
#     hotel_ids = request.form['hotel_id']	
#     totals = request.form['total']
#     coupon_discs = request.form['coupon_disc']
#     trans_dates = request.form['trans_date']

#     trans.trans_id = trans_id
#     trans.user_id = user_id
#     trans.hotel_id = hotel_id
#     trans.total = total
#     trans.coupon_disc = coupon_disc
#     trans.trans_date = trans_date
 

#     db.session.commit()
#     return trans_schema.jsonify(trans)


# # endpoint to delete user
# @app.route("/trans/<id>", methods=["DELETE"])
# def trans_delete(id):
#     trans = Trans.query.get(id)
#     db.session.delete(trans)
#     db.session.commit()

#     return trans_schema.jsonify(trans)







# # endpoint to get user detail by id
# @app.route("/user/<id>", methods=["GET"])
# def user_detail(id):
#     user = User.query.get(id)
#     return user_schema.jsonify(user)


# # endpoint to update user
# @app.route("/user/<id>", methods=["PUT"])
# def user_update(id):
#     username = request.form['username']
#     email = request.form['email']
#     userfirstname = request.form['userfirstname']
#     userlastname = request.form['userlastname']
#     userphone = request.form['userphone']
#     userpass = request.form['userpass']

#     user.email = email
#     user.username = username
#     user.userfirstname = userfirstname
#     user.userlastname = userlastname
#     user.userphone = userphone
#     user.userpass = userpass

#     db.session.commit()
#     return user_schema.jsonify(user)


# # endpoint to delete user
# @app.route("/user/<id>", methods=["DELETE"])
# def user_delete(id):
#     user = User.query.get(id)
#     db.session.delete(user)
#     db.session.commit()

#     return user_schema.jsonify(user)



#     # endpoint to create new user
# @app.route("/tables", methods=["POST"])
# def add_tables():
#     tables_id = request.form['tables_id']
#     hotel_id = request.form['hotel_id']
#     no_of_seats= request.form['no_of_seats']
#     reserved = request.form['reserved']
#     db.session.add(new_tables)
#     db.session.commit()

#     return jsonify(new_tables)


# # endpoint to show all users
# @app.route("/tables", methods=["GET"])
# def get_tables():
#     all_tables = Tables.query.all()
#     result = tables_schema.dump(all_tables)
#     return jsonify(result.data)


# # endpoint to get user detail by id
# @app.route("/tables/<id>", methods=["GET"])
# def tables_detail(id):
#     tables = Tables.query.get(id)
#     return tables_schema.jsonify(tables)


# # endpoint to update user
# @app.route("/tables/<id>", methods=["PUT"])
# def tables_update(id):
#     tables_id = request.form['tables_id']
#     hotel_id = request.form['hotel_id']
#     no_of_seats= request.form['no_of_seats']
#     reserved = request.form['reserved']

#     tables.hotel_id = hotel_id
#     tables.no_of_seats = no_of_seats
#     tables.reserved = reserved
#     tables.tables_id = tables_id
    
#     db.session.commit()
#     return tables_schema.jsonify(tables)


# # endpoint to delete user
# @app.route("/tables/<id>", methods=["DELETE"])
# def tables_delete(id):
#     tables = Tables.query.get(id)
#     db.session.delete(tables)
#     db.session.commit()

#     return user_schema.jsonify(tables)


# # endpoint to create new user
# @app.route("/products", methods=["POST"])
# def add_menu():
#     menu_id = request.form['menu_id']
#     name = request.form['name']
#     hotel_id = request.form['hotel_id']	
#     price = request.form['price']
#     available = request.form['available']
#     discounted = request.form['discounted']
#     bestseller = request.form['bestseller']

#     new_menu = Menu(menu_id, name, hotel_id, price, available, discounted, bestseller)

#     db.session.add(new_menu)
#     db.session.commit()
#     return jsonify(new_menu)



# # endpoint to show all users
# @app.route("/menu", methods=["GET"])
# def get_menu():
#     all_menus = Menu.query.all()
#     result = menus_schema.dump(all_menus)
#     return jsonify(result.data)


# # endpoint to get user detail by id
# @app.route("/menu/<id>", methods=["GET"])
# def menu_detail(id):
#     menu = Menu.query.get(id)
#     return menu_schema.jsonify(menu)


# # endpoint to update user
# @app.route("/menu/<id>", methods=["PUT"])
# def menu_update(id):
#     menu = Menu.query.get(id)

#     menu_id = request.form['menu_id']
#     name = request.form['name']
#     hotel_id = request.form['hotel_id']	
#     price = request.form['price']
#     available = request.form['available']
#     discounted = request.form['discounted']
#     bestseller = request.form['bestseller']

#     menu.menu_id = menu_id
#     menu.name = name
#     menu.hotel_id = hotel_id
#     menu.price = price
#     menu.available = available
#     menu.discounted = discounted
#     menu.bestseller = bestseller
 

#     db.session.commit()
#     return menu_schema.jsonify(menu)


# # endpoint to delete user
# @app.route("/menu/<id>", methods=["DELETE"])
# def menu_delete(id):
#     menu = Menu.query.get(id)
#     db.session.delete(menu)
#     db.session.commit()

#     return menu_schema.jsonify(menu)
