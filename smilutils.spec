%define name	smilutils
%define version	0.3.2
%define release %mkrel 4.7

%define major	0
%define libname %mklibname kinoextensions %major

%define _disable_ld_no_undefined 1
%define _disable_ld_as_needed 1

Name: 	 	%{name}
Summary: 	Command line tools for Kino's SMIL video format
Version: 	%{version}
Release: 	%{release}
Source:		%{name}-20070731.tar.bz2
Patch0:		smilutils-gcc4.3.patch
Patch1:		smilutils-gcc4.4.patch
URL:		http://sf.net/projects/kino
License:	GPL
Group:		Video
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	autoconf
BuildRequires:	libdv-devel quicktime-devel libxml2-devel
BuildRequires:	SDL-devel libgdk_pixbuf2.0-devel 

%description
SMIL is the file format kino uses to save projects. Here are a collection of
command line tools for SMIL manipulation.

%package -n 	%{libname}
Summary:        Dynamic libraries from %name
Group:          System/Libraries
Obsoletes:	%{libname}-devel

%description -n %{libname}
Dynamic libraries from %name.

%prep
%setup -q -n %name
%patch0 -p1
%patch1 -p1

%build
./autogen.sh
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%if "%{_lib}" != "lib"
	mv -f %buildroot%_prefix/lib %buildroot%_libdir
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%doc README COPYING
%{_bindir}/*
%{_mandir}/man1/*

%files -n %libname
%defattr(-,root,root)
%{_libdir}/kino/*
