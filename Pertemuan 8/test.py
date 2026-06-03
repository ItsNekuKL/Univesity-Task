class UniversalHashing:
  def __init__(self, m : int, p: int, a: int, b : int):
    """ Initialisasi paramter Universal Hasing : Rumus H(x) = ((ax + b) mod p) mod m """
    self.m = m #ukuran table hash
    self.p = p #bilangan prima
    self.a = a #nilai acak a (1 <= a <= p-1)
    self.b = b #nilai acak b (1 <= b <= p-1)

    """Initialisasi table hash kosong sepanjang m"""
    self.hash_table = [None] * self.m

  def perhitungan_hash(self, key: int) -> int:
    """Menghitung indeks hash menggunakan formula universal hasing"""
    inner_operation = (self.a * key) + self.b
    mod_p = inner_operation % self.p
    mod_m = mod_p % self.m
    return mod_m

  def insert(self, key: int):
    """Memasukan kunci ke dalam table hash berdasarkan indeksnya"""
    index = self.perhitungan_hash(key)
    self.hash_table[index] = key
    print(f"Key {key:2} -> Langkah: (({self.a}*{key} + {self.b}) mod {self.p}) mod {self.m} = {index}")

  def display_table(self):
    """Menampilkan isi table hash"""
    print("\n=== Hasil table hash ===")
    print(f"{'Indeks':<10} | {'Kunci (key)': <10}")
    print("="*25)
    for index, key in enumerate(self.hash_table):
      display_value = key if key is not None else "*Kosong"
      print(f"{index:<10} | {display_value:<10}")

if __name__ == "__main__":

  ukuran_table = 7
  bilangan_prima = 11
  nilai_a = 3
  nilai_b = 4

  uh = UniversalHashing(ukuran_table, bilangan_prima, nilai_a, nilai_b)

  print("=== Proses Perhitungan ===")
  key_to_insert = [5,12,25]

  for k in key_to_insert:
    uh.insert(k)

  uh.display_table()