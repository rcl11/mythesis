from pyfeyn.user import *

processOptions()
fd = FeynDiagram()

in1 = Vertex(-3,  1.2).addLabel(r"\Pq", displace=-0.3)
in2 = Vertex(-3, -1.2).addLabel(r"\Paq", displace=-0.3)
out1 = Vertex(3, 1.2).addLabel(r"\PW/\PZ", displace=0.4)
out2 = Vertex(3, -1.2).addLabel(r"\PH", displace=0.4)
lt_vtx = Vertex(-1.2, 0)
rt_vtx = Vertex(1.2, 0)

fa1 = Fermion(in1, lt_vtx).addArrow()
fa2 = Fermion(lt_vtx, in2).addArrow()
fa3 = Vector(rt_vtx, out1).setAmplitude(0.15).setFrequency(1.1)
higgs = Higgs(rt_vtx, out2)
fc = Vector(lt_vtx,
rt_vtx).setAmplitude(0.15).setFrequency(1.1).addLabel(r"\PW/\PZ")
fd.draw("feynman_VH.pdf")
