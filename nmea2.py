import pynmea2

def sentence(self):

    try:
        nmeaobj = pynmea2.parse(self)

        if(nmeaobj.sentence_type == 'GGA'):

            lat = nmeaobj.latitude
            lon = nmeaobj.longitude
            lat_dir = nmeaobj.lat_dir
            lon_dir = nmeaobj.lon_dir
            gps_qual = nmeaobj.gps_qual
            num_sats = nmeaobj.num_sats
            horizontal_dil = nmeaobj.horizontal_dil
            alt = nmeaobj.altitude
            altitude_units = nmeaobj.altitude_units
            timestamp = nmeaobj.timestamp

            return 'latitude: ' + str(lat), 'lat_dir: ' + str(lat_dir), 'longitude: ' + str(lon), 'lon_dir: ' + str(lon_dir), \
                   'gps_qual: ' + str(gps_qual), 'num_sats: ' + str(num_sats), 'horizontal_dil: ' + str(horizontal_dil), \
                   'altitude: ' + str(alt), 'altitude_unidade: ' + str(altitude_units), 'timestamp: ' + str(timestamp)

        elif(nmeaobj.sentence_type == 'RMC'):

            data = self.split(",")

            time = data[1]
            lat = nmeaobj.latitude
            lat_dir = nmeaobj.lat_dir
            lon = nmeaobj.longitude
            lon_dir = nmeaobj.lon_dir
            speed = data[7]
            course = data[8]
            utc = data[9]

            return 'latitude: ' + str(lat), 'lat_dir: ' + str(lat_dir), 'lon: ' + str(lon), 'lon_dir: ' + str(lon_dir), \
                   'speed: ' + str(speed), 'course: ' + str(course), 'data: ' + str(utc), 'hora: ' + str(time)

    except:
        pass