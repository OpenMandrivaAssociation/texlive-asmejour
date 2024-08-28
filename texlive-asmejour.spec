Name:		texlive-asmejour
Version:	71903
Release:	1
Summary:	A template for ASME journal papers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/asmejour
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/asmejour.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/asmejour.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The asmejour class provides a template to format preprints
submitted to ASME journals. The layout and reference formats
closely follow the style that is currently being used for
published papers. The class is intended to be used with the
asmejour.bst BibTeX style, which is part of this distribution.
Unlike older ASME LaTeX templates, asmejour pdfs will contain
hyperlinks, bookmarks, and metadata, and references can include
the DOI and URL fields. Options include line numbering, final
column balancing, various math options, government copyright,
and archivability (PDF/A). The class is compatible with
pdfLaTeX or LuaLaTeX. This package is not a publication of
ASME.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/asmejour
%{_texmfdistdir}/bibtex/bst/asmejour
%doc %{_texmfdistdir}/doc/latex/asmejour

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
