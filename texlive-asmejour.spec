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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
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

