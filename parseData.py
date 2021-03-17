import json

#getting data from json file
with open('./data.json') as f:
  data = json.load(f)

#creating new dictonary 
suppliers = {
    "supplier_price":[],
    "charges":[]
}

#parsing data for suppliers
for supplier in data["supplier_prices"]:
    supplier_pricelist = {}
    supplier_pricelist["identifier"] = supplier["Identifier"]
    supplier_pricelist["company_name"] = supplier["Company name"]
    supplier_pricelist["evse_id"] = supplier["EVSE ID"]
    supplier_pricelist["product_id"] = supplier["Product ID"]
    supplier_pricelist["currency"] = supplier["Currency"]

    #for fees
    supplier_pricelist["billing_threshold_flag"] = supplier["has minimum billing threshold"]
    supplier_pricelist["billing_amount_min"] = supplier["min billing amount"]
    supplier_pricelist["session_fee_flag"] = supplier["has session fee"]
    supplier_pricelist["max_session_fee_flag"] = supplier["has max session Fee"]
    supplier_pricelist["session_fee"] = float(supplier["session Fee"].replace("False","0.0").replace(",","."))
    supplier_pricelist["session_fee_max"] = float(supplier["max_session fee"].replace("False","0.0").replace(",","."))

    #for time price
    if "simple minute price" in supplier.keys():
        supplier_pricelist["simple_minute_price"] = float(supplier["simple minute price"].replace(",",".")) 
        supplier_pricelist["complex_minute_price_flag"] = supplier["has complex minute price"]
        supplier_pricelist["min_duration"] = float(supplier["min_duration"].replace(",",".")) 

    suppliers["supplier_price"].append(supplier_pricelist)


#parsing data for transaction
for charge in data["transactions"]:
    charges = {}
    charges["session_id"] = charge["Session ID"]
    charges["provider_id"] = charge["Proveider ID"]
    charges["evse_id"] = charge["EVSEID"]
    charges["uid"] = charge["UID"]
    charges["metering_signature"] = charge["Metering signature"]
    charges["charging_start"] = charge["Charging start"]
    charges["charging_end"] = charge["Charging end"]
    charges["session_start"] = charge["Session start"]
    charges["session_end"] = charge["Session end"]
    charges["meter_value_start"] = charge["Meter value start"]
    charges["meter_value_end"] = charge["Meter value end"]
    charges["country_code"] = charge["CountryCode"]
   
    suppliers["charges"].append(charges)



# Serializing json  
json_object = json.dumps(suppliers, indent = 1) 
  
# Writing to sample.json 
with open("parseddata.json", "w") as outfile: 
    outfile.write(json_object) 


