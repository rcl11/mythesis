from pyfeyn.user import *

processOptions()
fd = FeynDiagram()

in1 = Vertex(-2.8,  0.8).addLabel(r"\Pq", displace=-0.3)
in2 = Vertex(-2.8, -0.8).addLabel(r"\Pq", displace=-0.3)
out1 = Vertex(2.5, 1.5).addLabel(r"\Pq", displace=0.3)
out2 = Vertex(2.5, 0).addLabel(r"\PH", displace=0.3)
out3 = Vertex(2.5, -1.5).addLabel(r"\Pq", displace=0.3)
top_vtx = Vertex(-0.5, 0.8)
btm_vtx = Vertex(-0.5, -0.8)
mid_vtx = Vertex(0.7, 0.0)

fa1 = Fermion(in1, top_vtx).addArrow()
fa2 = Fermion(in2, btm_vtx).addArrow()
higgs = Higgs(mid_vtx, out2)
fc = Vector(top_vtx,
mid_vtx).setAmplitude(0.10).setFrequency(1.1).addLabel(r"\PW/\PZ",
displace=-0.4, pos = 0.7)
fc = Vector(mid_vtx,
btm_vtx).setAmplitude(0.10).setFrequency(1.1).addLabel(r"\PW/\PZ",
displace=-0.4, pos = 0.3)
fb1 = Fermion(top_vtx, out1).addArrow()
fb2 = Fermion(btm_vtx, out3).addArrow()

fd.draw("feynman_qqH.pdf")
