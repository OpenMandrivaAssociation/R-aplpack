%define modulename aplpack
%define realver 1.2.2
%define r_library %{_libdir}/R/library

Summary:	Another plot package for R
Name:		R-cran-%{modulename}
Version:	%realver
Release:	%mkrel 1
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://cran.r-project.org/web/packages/%{modulename}/index.html
Source0:	http://cran.r-project.org/src/contrib/%{modulename}_%{realver}.tar.gz
BuildRequires:	R-base
BuildRequires:	texinfo
BuildRequires:	tetex-latex 
Requires:	R-base
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A set of functions for drawing some special plots: stem.leaf 
plots a stem and leaf plot bagplot plots a bagplot faces plots 
chernoff faces spin3R for an inspection of a 3-dim point cloud.

%prep
%setup -q -c

%build

R CMD build %{modulename}

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{r_library}

# (tpg) install
R CMD INSTALL %{modulename} --library=%{buildroot}/%{r_library}

# (tpg) provided by R-base
rm -rf %{buildroot}/%{r_library}/R.css

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{r_library}/%{modulename}
