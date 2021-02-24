
import argparse
import math
import struct

zoomLevel = 17

def deg2num(lat_deg, lon_deg, zoom):
    lat_rad = math.radians(lat_deg)
    n = 2.0 ** zoom
    xtile = ((lon_deg + 180.0) / 360.0 * n)
    ytile = ((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
    return (xtile, ytile)


def getShadow(path,lat,lon):

    tile = deg2num(lat,lon,zoomLevel)
    tilePix = (256 * (tile[0] - int(tile[0])), 256 * (tile[1] - int(tile[1])))
    pos = int(int(tilePix[1]) * 256 + tilePix[0])

    filePath = '%s/%d/%d/%d.bin'%(path,zoomLevel,tile[0],tile[1])
    f = open(filePath,'rb')
    f.seek(2 * pos)
    value = struct.unpack('h', f.read(2))[0]
    f.close()

    return value

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get shadow information.')
    parser.add_argument('--lat', action="store", dest="lat", help='Latitude', type=float, required=True)
    parser.add_argument('--lon', action="store", dest="lon", help='Longitude', type=float, required=True)
    parser.add_argument('--path', action="store", dest="path", help='Slippy tiles path', required=True)

    args = parser.parse_args()
    print(getShadow(args.path,args.lat,args.lon))
