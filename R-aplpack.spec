%global packname  aplpack
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.2.3
Release:          1
Summary:          Another Plot PACKage: stem.leaf, bagplot, faces, spin3R, and some slider functions
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/Archive/%{packname}/%{packname}_%{version}.tar.gz
Requires:         R-tcltk 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-tcltk
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

%check
%{_bindir}/R CMD check %{packname}

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
