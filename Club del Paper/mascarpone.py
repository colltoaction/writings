from discopy.frobenius import Box, Ty, Diagram, Spider, Id, Spider, Swap


e = Ty("egg")
w = Ty("white")
y = Ty("yolk")
s = Ty("sugar")
m = Ty("mascarpone")
c = Ty("crema di mascarpone")
ww = Ty("whisked whites")
yp = Ty("yolky paste")
tp = Ty("thick paste")
cr = Box("crack", e, w @ y)
wh = Box("whisk", w @ w, ww)
be = Box("beat", y @ y @ s, yp)
mi = Box("mix", w @ y, e)
st = Box("stir", yp @ m, tp)
fo = Box("fold", ww @ tp, c)
wsf = wh @ st >> fo
ccw = cr @ cr >> w @ Swap(y, w) @ y >> wh @ y @ y
best = be @ m >> st
cdm = cr @ cr @ s @ m >> w @ Swap(y, w) @ y @ s @ m >> wh @ be @ m >> ww @ st >> fo

cr.draw(fontsize=30, margins=(0.35, 0.2), figsize=(10, 5), path="sobocinski/crack.png")
wh.draw(fontsize=30, margins=(0.35, 0.2), figsize=(10, 5), path="sobocinski/whisk.png")
be.draw(fontsize=30, margins=(0.35, 0.2), figsize=(10, 5), path="sobocinski/beat.png")
mi.draw(fontsize=30, margins=(0.35, 0.2), figsize=(10, 5), path="sobocinski/mix.png")
st.draw(fontsize=30, margins=(0.35, 0.2), figsize=(10, 5), path="sobocinski/stir.png")
fo.draw(fontsize=30, margins=(0.35, 0.2), figsize=(10, 5), path="sobocinski/fold.png")
wsf.draw(fontsize=18, margins=(0.20, 0.05), figsize=(10, 5), path="sobocinski/whisk_stir_fold.png")
ccw.draw(fontsize=18, margins=(0.20, 0.05), figsize=(10, 5), path="sobocinski/crack_crack_whisk.png")
cdm.draw(fontsize=16, margins=(0.20, 0.05), figsize=(10, 5), path="sobocinski/crema di mascarpone.png")
best.draw(fontsize=16, margins=(0.20, 0.05), figsize=(10, 5), path="sobocinski/beat_stir.png")
