%global tl_name asmejour
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.27
Release:	%{tl_revision}.1
Summary:	A template for ASME journal papers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/asmejour
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/asmejour.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/asmejour.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The asmejour class provides a template to format preprints submitted to
ASME journals. The layout and reference formats closely follow the style
that is currently being used for published papers. The class is intended
to be used with the asmejour.bst BibTeX style, which is part of this
distribution. Unlike older ASME LaTeX templates, asmejour pdfs will
contain hyperlinks, bookmarks, and metadata, and references can include
the DOI and URL fields. Options include line numbering, final column
balancing, various math options, government copyright, and accessibility
(PDF/A). The class is compatible with pdfLaTeX or LuaLaTeX. This package
is not a publication of ASME.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/bibtex
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/bibtex/bst
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/bibtex/bst/asmejour
%dir %{_datadir}/texmf-dist/doc/latex/asmejour
%dir %{_datadir}/texmf-dist/tex/latex/asmejour
%dir %{_datadir}/texmf-dist/doc/latex/asmejour/asmewide_example
%{_datadir}/texmf-dist/bibtex/bst/asmejour/asmejour.bst
%doc %{_datadir}/texmf-dist/doc/latex/asmejour/README.md
%doc %{_datadir}/texmf-dist/doc/latex/asmejour/asmejour-sample.bib
%doc %{_datadir}/texmf-dist/doc/latex/asmejour/asmejour-style.css
%doc %{_datadir}/texmf-dist/doc/latex/asmejour/asmejour-template.pdf
%doc %{_datadir}/texmf-dist/doc/latex/asmejour/asmejour-template.tex
%doc %{_datadir}/texmf-dist/doc/latex/asmejour/asmewide_example/asmejour-wide-equation-examples.pdf
%doc %{_datadir}/texmf-dist/doc/latex/asmejour/asmewide_example/asmejour-wide-equation-examples.tex
%doc %{_datadir}/texmf-dist/doc/latex/asmejour/asmewide_example/asmewide.sty
%doc %{_datadir}/texmf-dist/doc/latex/asmejour/asmewide_example/tesseral-harmonic.pdf
%doc %{_datadir}/texmf-dist/doc/latex/asmejour/asmewide_example/zonal-harmonic2.pdf
%doc %{_datadir}/texmf-dist/doc/latex/asmejour/sample-figure-1.pdf
%doc %{_datadir}/texmf-dist/doc/latex/asmejour/sample-figure-2a.pdf
%doc %{_datadir}/texmf-dist/doc/latex/asmejour/sample-figure-2b.pdf
%{_datadir}/texmf-dist/tex/latex/asmejour/asmejour.cls
