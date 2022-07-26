from _datetime import datetime
import pytz


bogota_timezone = pytz.timezone("America/Bogota")
bogota_date = datetime.now(bogota_timezone)
print("Bogotá: ", bogota_date.strftime("%d/%m/%Y, %H:%M:%S"))


cdmx_timezone = pytz.timezone("America/Mexico_City")
cdmx_date = datetime.now(cdmx_timezone)
print("CDMX : ", cdmx_date.strftime("%d/%m/%Y, %H:%M:%S"))


caracas_timezone = pytz.timezone("America/Caracas")
caracas_date = datetime.now(caracas_timezone)
print("Caracas: ", caracas_date.strftime("%d/%m/%Y, %H:%M:%S"))

