from datetime import timedelta, datetime
SECRET_KEY = "ewfrejugjrtgbjrtbtrhnbnrtbnttbtjgijitgejv nrjergegtgnrtrtjrirtjgrngrogorjgorhgrhr"

REMEMBER_COOKIE_DURATION = timedelta(days=30)

data_dict={"time_of_receipt": datetime.now().strftime("%H:%M"),
           "transmission_time": datetime.now().strftime("%H:%M"),
           "departure_time": None,
           "arrival_time" : None,
           "start_time_of_hospitalization" : None,
           "time_of_arrival_at_hospital": None,
           "call_end_time" : None,
           'doctor_id' : None,
           "patient_id": None}

