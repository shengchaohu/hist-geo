import db


class AddressLoader:
    def __init__(self, query):
        self.query = query

    def get_address(self):
        """
        return format: {year:{id:{admin_type, chinese_name, x, y, ...}}}
        """
        db_loader = db.DBLoader()
        res = db_loader.extract(self.query)
        address = {}
        for r in res:
            addr_id = r[0]
            name_chn = r[3]
            admin_type = r[4]
            start_year = r[5]
            end_year = r[6]
            x_co = r[7]
            y_co = r[8]
            belongs1_name = r[10]
            belongs2_name = r[12]
            belongs3_name = r[14]
            belongs4_name = r[16]
            belongs5_name = r[18]
            # ignore those without coordinates
            if not x_co or not y_co:
                continue
            for year in range(start_year, end_year + 1):
                if year not in address:
                    address[year] = {}
                if addr_id in address[year]:
                    continue
                else:
                    address[year][addr_id] = (
                        admin_type,
                        name_chn,
                        x_co,
                        y_co,
                        belongs1_name,
                        belongs2_name,
                        belongs3_name,
                        belongs4_name,
                        belongs5_name,
                    )
        return address
