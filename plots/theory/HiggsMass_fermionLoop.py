from pyfeyn.user import *

fd = FeynDiagram()

in1  = Point(-3, 0)
out1 = Point( 3, 0)
vtx1 = Vertex(-1, 0, mark=CIRCLE)
vtx2 = Vertex( 1, 0, mark=CIRCLE)

higgs1 = Higgs(in1, vtx1).addLabel(r"\PHiggs")
higgs2 = Higgs(vtx2, out1)
loop1 = Fermion(vtx1, vtx2).bend(-1).addLabel(r"f").addArrow()
loop1 = Fermion(vtx2, vtx1).bend(-1).addArrow()

fd.draw("HiggsMass_fermionLoop.pdf")
