from pyfeyn.user import *

processOptions()
fd = FeynDiagram()

in1 = Vertex(-3,  1.2).addLabel(r"\Pgluon", displace=-0.3)
in2 = Vertex(-3, -1.2).addLabel(r"\Pgluon", displace=-0.3)
out1 = Vertex(3, 0).addLabel(r"\Pphi", displace=0.3)
top_vtx = Vertex(-0.7, 1.2)
btm_vtx = Vertex(-0.7, -1.2)
mid_vtx = Vertex(1.3, 0.0)

fa1 = Gluon(in1, top_vtx)
fa2 = Gluon(btm_vtx, in2)
higgs = Higgs(mid_vtx, out1)
fc = Fermion(top_vtx, mid_vtx).addArrow()
fc = Fermion(mid_vtx, btm_vtx).addArrow()
fc = Fermion(btm_vtx, top_vtx).addArrow()
fd.draw("feynman_mssm_ggH.pdf")
