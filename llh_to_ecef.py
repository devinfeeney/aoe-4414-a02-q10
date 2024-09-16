# llh_to_ecef.py

# Usage: python3 llh_to_ecef.py lat_deg lon_deg hae_km
# Description: Converts latitude, longitude, and altitude in LLH coordinates to ECEF coordinates.

# Parameters:
#  lat_deg: Latitude given in degrees
#  lon_deg: Longitude given in degrees
#  hae_km: Altitude given in kilometers

# Output:
#  Coordinates in the ecef reference frame (x, y, z), answer in degrees

# Written by Devin Feeney
# Other contributors: None

# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import math
import sys

# "constants"
R_E_KM = 6378.137
e_E = 0.081819221456
r_E_km = 6378.1363

# helper functions - Denominator calculation
def calc_denom(ecc, lat_rad):
    return math.sqrt(1.0-ecc*ecc*math.pow(math.sin(lat_rad),2.0))

# Check and parse script arguments
if len(sys.argv) == 4:
    try:
        lat_deg = float(sys.argv[1])
        lon_deg = float(sys.argv[2])
        hae_km = float(sys.argv[3])
    except ValueError:
        print('Error: Latitude, longitude, and altitude must be numbers.')
        sys.exit()
else:
    print('Usage: python3 llh_to_ecef.py lat_deg lon_deg hae_km')
    sys.exit()

# Calculate ECEF coordinates
lat_rad = lat_deg * math.pi / 180.0 #lat in radians
lon_rad = lon_deg * math.pi / 180.0 #lonng in radians
denom = calc_denom(e_E, lat_rad)
C_E = r_E_km / denom
S_E = (r_E_km * (1 - e_E * e_E)) / denom
r_x_km = (C_E + hae_km) * math.cos(lat_rad) * math.cos(lon_rad)
r_y_km = (C_E + hae_km) * math.cos(lat_rad) * math.sin(lon_rad)
r_z_km = (S_E +hae_km) * math.sin(lat_rad)

# Display final answers
print(f'{r_x_km}')
print(f'{r_y_km}')
print(f'{r_z_km}')

