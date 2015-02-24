from pyfeyn.user import *

processOptions()
fd = FeynDiagram()

in1 = Vertex(-3,  1.2).addLabel(r"\Pgluon", displace=-0.3)
in2 = Vertex(-3, -1.2).addLabel(r"\Pgluon", displace=-0.3)
out1 = Vertex(2.0, 1.2).addLabel(r"\Pqb", displace=0.3)
out2 = Vertex(2.0, 0).addLabel(r"\Pphi", displace=0.3)
out3 = Vertex(2.0, -1.2).addLabel(r"\Paqb", displace=0.3)
top_vtx = Vertex(-0.5, 1.2)
btm_vtx = Vertex(-0.5, -1.2)
mid_vtx = Vertex(-0.5, 0.0)

fa1 = Gluon(in1, top_vtx)
fa2 = Gluon(in2, btm_vtx)
higgs = Higgs(mid_vtx, out2)
fc = Fermion(mid_vtx, top_vtx).addLabel(r"\Paqb", displace=0.3).addArrow()
fc = Fermion(btm_vtx, mid_vtx).addLabel(r"\Pqb", displace=0.3).addArrow()
fb1 = Fermion(top_vtx, out1).addArrow()
fb2 = Fermion(out3, btm_vtx).addArrow()

fd.draw("feynman_mssm_bbH.pdf")
