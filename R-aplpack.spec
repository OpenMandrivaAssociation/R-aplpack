%global packname  aplpack
%global rlibdir  %{_libdir}/R/library

%define debug_package %{nil}

Name:             R-%{packname}
Version:          1.2.9
Release:          1
Summary:          Another Plot PACKage: stem.leaf, bagplot, faces, spin3R, slider functions
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/aplpack_1.2.9.tar.gz
Requires:         R-tcltk 
Requires:         R-tkrplot 
BuildRequires:    R-devel
BuildRequires:    Rmath-devel
BuildRequires:    texlive-collection-latex
BuildRequires:    R-tcltk
BuildRequires:    R-tkrplot 
%rename R-cran-aplpack

%description
set of functions for drawing some special plots: stem.leaf plots a stem
and leaf plot bagplot plots a bagplot faces plots chernoff faces spin3R
for an inspection of a 3-dim point cloud slider functions for interactive

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

#%check
#%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/pdf
%{rlibdir}/%{packname}/src


%changelog
* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2.4-1
+ Revision: 775030
- Update to latest version

* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2.3-1
+ Revision: 774834
- Update and rebuild with R2spec
- Update and rebuild with R2spec

* Sat Dec 26 2009 Jérôme Brenier <incubusss@mandriva.org> 1.2.2-1mdv2010.1
+ Revision: 482345
- buildrequires texinfo and tetex-latex
- new version 1.2.2

* Tue Sep 08 2009 Thierry Vignaud <tv@mandriva.org> 1.1.1-5mdv2010.0
+ Revision: 433074
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 1.1.1-4mdv2009.0
+ Revision: 260123
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 1.1.1-3mdv2009.0
+ Revision: 248145
- rebuild

* Thu Feb 28 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.1.1-1mdv2008.1
+ Revision: 176462
- complete spec file
- fix Url
- add source and spec file
- Created package structure for R-cran-aplpack.



