#Sales report in Json

report = {}
report['Maulana'] = {
    'Nama': 'Maulana',
    'Barang': 'Kopi Semi',
    'Harga': 5000
}
report['Condro'] = {
    'Nama': 'Condro',
    'Barang': 'Kopi Agak Manis',
    'Harga': 5000
}
report['Dion'] = {
    'Nama': 'Dion',
    'Barang': 'Kopi Pahit',
    'Harga': 4000
}
report['Merkuri'] = {
    'Nama': 'Merkuri',
    'Barang': 'Kopi Biasa',
    'Harga': 4000
}

import json
k=json.dumps(report)
with open("/home/septiannurtrir/praxis-academy/novice/01-05/lat_Jsonprogram.xml","w") as f:
    f = json.load(f)
    print(f)