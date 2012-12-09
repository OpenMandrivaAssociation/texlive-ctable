# revision 23834
# category Package
# catalog-ctan /macros/latex/contrib/ctable
# catalog-date 2011-09-05 13:58:41 +0200
# catalog-license lppl
# catalog-version 1.21
Name:		texlive-ctable
Version:	1.21
Release:	2
Summary:	Easily typeset centered tables
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ctable
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ctable.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ctable.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ctable.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides commands to easily typeset centered, left- or right-
aligned table and (multiple-)figure floats, with footnotes.
Instead of an environment, a command with 4 arguments is used;
the first is optional and is used for key,value pairs
generating variations on the defaults and offering a route for
future extensions.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ctable/ctable.sty
%doc %{_texmfdistdir}/doc/latex/ctable/01a
%doc %{_texmfdistdir}/doc/latex/ctable/01b
%doc %{_texmfdistdir}/doc/latex/ctable/02k
%doc %{_texmfdistdir}/doc/latex/ctable/02l
%doc %{_texmfdistdir}/doc/latex/ctable/02m
%doc %{_texmfdistdir}/doc/latex/ctable/03a
%doc %{_texmfdistdir}/doc/latex/ctable/03b
%doc %{_texmfdistdir}/doc/latex/ctable/04a
%doc %{_texmfdistdir}/doc/latex/ctable/04b
%doc %{_texmfdistdir}/doc/latex/ctable/05a
%doc %{_texmfdistdir}/doc/latex/ctable/05b
%doc %{_texmfdistdir}/doc/latex/ctable/06a
%doc %{_texmfdistdir}/doc/latex/ctable/06b
%doc %{_texmfdistdir}/doc/latex/ctable/07a
%doc %{_texmfdistdir}/doc/latex/ctable/07b
%doc %{_texmfdistdir}/doc/latex/ctable/08a
%doc %{_texmfdistdir}/doc/latex/ctable/08b
%doc %{_texmfdistdir}/doc/latex/ctable/09b
%doc %{_texmfdistdir}/doc/latex/ctable/10a
%doc %{_texmfdistdir}/doc/latex/ctable/10b
%doc %{_texmfdistdir}/doc/latex/ctable/12a
%doc %{_texmfdistdir}/doc/latex/ctable/12b
%doc %{_texmfdistdir}/doc/latex/ctable/13a
%doc %{_texmfdistdir}/doc/latex/ctable/13b
%doc %{_texmfdistdir}/doc/latex/ctable/13c
%doc %{_texmfdistdir}/doc/latex/ctable/14a
%doc %{_texmfdistdir}/doc/latex/ctable/README
%doc %{_texmfdistdir}/doc/latex/ctable/ctable.pdf
%doc %{_texmfdistdir}/doc/latex/ctable/doit
%doc %{_texmfdistdir}/doc/latex/ctable/inst
%doc %{_texmfdistdir}/doc/latex/ctable/lion.png
%doc %{_texmfdistdir}/doc/latex/ctable/penguin.jpg
#- source
%doc %{_texmfdistdir}/source/latex/ctable/ctable.dtx
%doc %{_texmfdistdir}/source/latex/ctable/ctable.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.21-2
+ Revision: 750662
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.21-1
+ Revision: 718177
- texlive-ctable
- texlive-ctable
- texlive-ctable
- texlive-ctable

