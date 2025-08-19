provinsi = {'Nanggroe Aceh Darussalam': 'Aceh','Sumatera Selatan': 'Palembang','Kalimantan Barat': 'Pontianak','Jawa Timur': 'Madiun','Sulawesi Selatan': 'Makassar','Maluku': 'Ambon'}
ListOfKeys = list(provinsi.keys())
print("Daftar Provinsi:", ListOfKeys)
print("Jumlah Provinsi:", len(ListOfKeys))
provinsi['Jawa Timur'] = 'Surabaya'
print("Provinsi Jawa Timur:", provinsi['Jawa Timur'])