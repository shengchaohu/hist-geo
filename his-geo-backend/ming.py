from address import AddressLoader

Name={'安抚司': 'ro', '府': 'r^', '蛮夷长官司': 'ko', '屯卫': 'bo', '卫': 'm^', '县': 'k^', '长官司': 'b^', '州': 'mo', '其它' : 'co'}
TYPE_DICT = {
    "Anfusi":0,
    "Fu":1,
    "Manyichangguansi":2,
    "Tunwei":3,
    "Wei":4,
    "Xian":5,
    "Zhangguansi":6,
    "Zhou":7,
}
MARKERS = ['ro','r^','ko','bo','m^','k^','b^','mo','wo']
EXTENT_MAT = (94.978752, 127.597982, 17.433220, 45.187445)

address_loader = AddressLoader(ADDRESSES_QUERY)
# {year:{id:{admin_type, x, y}}}
addresses = address_loader.get_address()

