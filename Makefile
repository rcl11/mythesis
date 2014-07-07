.PHONY: clean

EXTRASTYS = abhepexpt.sty abhep.sty  abmath.sty lineno.sty SIunits.sty varwidth.sty

mythesis.pdf: mythesis.tex mythesis.cls chap1.tex chap2.tex chap3.tex frontmatter.tex appendices.tex
	@rm -f $(EXTRASTYS)
	unzip extrastyles.zip
	@rm -f mythesis.{aux,toc,lof,lot}
	(pdflatex mythesis && bibtex mythesis && pdflatex mythesis && pdflatex mythesis) || rm -f $(EXTRASTYS) mythesis.pdf
	@rm -f mythesis.{aux,toc,lof,lot}
	@rm -f $(EXTRASTYS)

clean:
	@rm -f $(EXTRASTYS)
	@rm -f mythesis.pdf mythesis.log mythesis.aux
	@rm -f *.bbl *.blg *.lof *.cut
	@rm -f *.lot *.out *.toc
