from pyfeyn.user import *

fd = FeynDiagram()

in1  = Point(-3, 0)
out1 = Point( 3, 0)
vtx1 = Vertex(0, 0, mark=CIRCLE)
vtx2 = Vertex(0, 0)

higgs1 = Higgs(in1, vtx1).addLabel(r"\PHiggs")
higgs2 = Higgs(vtx2, out1)
loop1 = Higgs(vtx1, vtx1).arcThru(x=0, y=2.0).addLabel(r"S")
#loop1 = Fermion(vtx2, vtx1).bend(-1).addArrow()

fd.draw("HiggsMass_bosonLoop.pdf")
