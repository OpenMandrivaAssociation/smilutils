%define name	smilutils
%define version	0.3.2
%define release %mkrel 20070731.1

%define major	0
%define libname %mklibname kinoextensions %major

Name: 	 	%{name}
Summary: 	Command line tools for Kino's SMIL video format
Version: 	%{version}
Release: 	%{release}
Source:		%{name}-20070731.tar.bz2
URL:		http://sf.net/projects/kino
License:	GPL
Group:		Video
BuildRequires:	autoconf2.5
BuildRequires:	libdv-devel quicktime-devel libxml2-devel
BuildRequires:	SDL-devel libgdk_pixbuf2.0-devel 

%description
SMIL is the file format kino uses to save projects. Here are a collection of
command line tools for SMIL manipulation.

%package -n 	%{libname}
Summary:        Dynamic libraries from %name
Group:          System/Libraries

%description -n %{libname}
Dynamic libraries from %name.

%package -n 	%{libname}-devel
Summary: 	Header files and static libraries from %name
Group: 		Development/C
Requires: 	%{libname} >= %{version}
Provides:	%{name}-devel = %{version}-%{release} 
Provides:	libkinoextensions-devel = %version-%release
Obsoletes: 	%{name}-devel

%description -n %{libname}-devel
Libraries and includes files for developing programs based on %name.

%prep
%setup -q -n %name

%build
./autogen.sh
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README COPYING
%{_bindir}/*
%{_mandir}/man1/*

%files -n %libname
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %libname-devel
%defattr(-,root,root)
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/*.so


