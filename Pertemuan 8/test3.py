class UniversalHashing:
  def __init__(self, m : int, p: int, a: int, b : int):
    """ Initialisasi paramter Universal Hasing : Rumus H(x) = ((ax + b) mod p) mod m """
    self.m = m #ukuran table hash
    self.p = p #bilangan prima
    self.a = a #nilai acak a (1 <= a <= p-1)
    self.b = b #nilai acak b (1 <= b <= p-1)

    """Initialisasi table hash kosong sepanjang m (menggunakan chaining untuk collision)"""
    self.hash_table = [[] for _ in range(self.m)]

  def perhitungan_hash(self, key: int) -> int:
    """Menghitung indeks hash menggunakan formula universal hasing"""
    inner_operation = (self.a * key) + self.b
    mod_p = inner_operation % self.p
    mod_m = mod_p % self.m
    return mod_m

  def insert(self, key: int):
    """Memasukan kunci ke dalam table hash berdasarkan indeksnya (dengan chaining)"""
    index = self.perhitungan_hash(key)
    self.hash_table[index].append(key)
    print(f"Key {key:2} -> Langkah: (({self.a}*{key} + {self.b}) mod {self.p}) mod {self.m} = {index}")

  def display_table(self):
    """Menampilkan isi table hash"""
    print("\n=== Hasil table hash ===")
    print(f"{'Indeks':<10} | {'Kunci (key)': <10}")
    print("="*60)
    for index, key in enumerate(self.hash_table):
      display_value = ', '.join(map(str, key)) if key else "*Kosong"
      print(f"{index:<10} | {display_value:<25}")

if __name__ == "__main__":

  while True:
    print(" MENU ".center(60, '='))
    print("1. Jalankan Sistem Hashing Universal")
    print("2. Keluar")
    choice = input("Pilih opsi (1/2): ")

    if choice == '1':
      try:
        ukuran_table = int(input("Masukkan ukuran tabel hash (m): "))
        bilangan_prima = int(input("Masukkan bilangan prima (p): "))
        nilai_a = int(input("Masukkan nilai a (1 <= a <= p-1): "))
        nilai_b = int(input("Masukkan nilai b (1 <= b <= p-1): "))

        uh = UniversalHashing(ukuran_table, bilangan_prima, nilai_a, nilai_b)

        print("\n=== Proses Perhitungan ===")
        keys_input = input("Masukkan kunci (key) yang ingin disisipkan (pisahkan dengan koma): ")
        key_to_insert = [int(k.strip()) for k in keys_input.split(',') if k.strip()]

        for k in key_to_insert:
          uh.insert(k)

        uh.display_table()
      except ValueError:
        print("Input tidak valid. Pastikan Anda memasukkan angka.")
      except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    elif choice == '2':
      print("Keluar dari sistem.")
      break
    else:
      print("Pilihan tidak valid. Silakan coba lagi.")
