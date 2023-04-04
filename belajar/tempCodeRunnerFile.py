from enum import Enum


class State(Enum):
    INACTIVE = 0
    ACTIVE = 1


print(State.ACTIVE)
# Perintah diatas akan menampilkan State.ACTIVE
# Sementara perintah dibawah akan menampilkan isi dari State.ACTIVE
# print(State.ACTIVE.value)
