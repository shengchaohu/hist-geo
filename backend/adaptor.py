import copy
from abc import abstractmethod


class GeoJsonAdaptor:
    @abstractmethod
    def dict_to_geo_json(self, data):
        pass


class AdministrativeDivionAdaptor(GeoJsonAdaptor):
    """
    https://en.wikipedia.org/wiki/GeoJSON
    https://datatracker.ietf.org/doc/html/rfc7946
    """

    template_geo_json = {"type": "FeatureCollection", "features": []}

    template_point = {
        "type": "Feature",
        "geometry": {"type": "Point", "coordinates": []},
        "properties": {"description": "", "ch_name": "", "admin_type": ""},
    }

    def dict_to_geo_json(self, data):
        """
        data of format {id: {admin_type, chinese_name, x, y, ...},}
        """


class MingAdaptor(AdministrativeDivionAdaptor):
    Name = {"安抚司": "ro", "府": "r^", "蛮夷长官司": "ko", "屯卫": "bo", "卫": "m^", "县": "k^", "长官司": "b^", "州": "mo", "其它": "co"}
    TYPE_DICT = {
        "Anfusi": 0,
        "Fu": 1,
        "Manyichangguansi": 2,
        "Tunwei": 3,
        "Wei": 4,
        "Xian": 5,
        "Zhangguansi": 6,
        "Zhou": 7,
    }
    MARKERS = ["ro", "r^", "ko", "bo", "m^", "k^", "b^", "mo", "wo"]

    def dict_to_geo_json(self, data):
        """
        data of format {id: {admin_type, chinese_name, x, y, ...},}
        """
        geo_json = copy.deepcopy(self.template_geo_json)
        for k, v in data.items():
            point = copy.deepcopy(self.template_point)
            point["properties"]["admin_type"] = v[0]
            point["properties"]["ch_name"] = v[1]
            point["geometry"]["coordinates"] = [v[2], v[3]]
            description = ""
            for i in range(4, 9):
                if v[i]:
                    description += f"{v[i]}-"
                else:
                    description = description[:-1]  # remove the last -
                    break
            point["properties"]["description"] = description
            geo_json["features"].append(point)
        return geo_json
