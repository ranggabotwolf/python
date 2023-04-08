"""Annotations"""

# Python sangat dinamis dalam  penulisannya
# Kita tidak harus menspesifikasikan type dari variable atau function parameter atau function return value


# def increment(n):
#    return n + 1
# Code diatas adalah code tanpa annotations
# Dan code dibawah adalah code dengan annotations


def increment(n: int) -> int:
    # Kita telah menspesifikasikan fungsi diatas dengan n yang menerima int, dan akan mengembalikan / return int
    return n + 1


# Kita juga bisa melakukannya pada variable, seperti berikut:
count: int = 0
# Variable count diatas sudah menggunakan annotations, yaitu menjadikan variable count menerima type data int
# pendeklarasian annotations adalah dengan menggunakan tanda : sebelum annotations

# Python akan mengabaikan annotations ini
# Tool terpisah yang disebut mypy bisa dijalankan standalone
# atau terintegrasi dengan IDE untuk mengecek secara otomatis type error ketika kita sedang mengoding
# itu juga membantu menangkap bug yang salah bahkan ketika menjalankan code
# Kita akan sangat terbantu ketika software kita sudah menjadi besar
# dan kita harus merefactor code kita
