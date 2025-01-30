import pyxel

pyxel.init(160, 120, title="Pyxel Drawing 2")

# 0 黒, 7 白
pyxel.pset(10, 10, 7)
pyxel.line(10, 20, 80, 20, 8)
pyxel.circ(20, 50, 10, 11)
pyxel.circb(50, 50, 10, 11)
pyxel.rect(10, 80, 20, 10, 13)
pyxel.rectb(40, 80, 20, 10, 13)

pyxel.show()
