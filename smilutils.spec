%define _disable_ld_no_undefined 1
%define _disable_ld_as_needed 1

%define major	0
%define libname %mklibname kinoextensions %{major}
%define liblegacy %mklibname kinolegacy %{major}
%define devname %mklibname kinoextensions -d

Summary:	Command line tools for Kino's SMIL video format
Name:		smilutils
Version:	0.3.2
Release:	20070731.13
License:	GPLv2
Group:		Video
Url:		http://sf.net/projects/kino
Source0:	%{name}-20070731.tar.bz2
Patch0:		smilutils-gcc4.3.patch
Patch1:		smilutils-gcc4.4.patch
Patch2:		smilutils-automake-1.13.patch
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libdv)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libquicktime)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(sdl)

%description
SMIL is the file format kino uses to save projects. Here are a collection of
command line tools for SMIL manipulation.

%package -n 	%{libname}
Summary:	Dynamic library from %{name}
Group:		System/Libraries

%description -n %{libname}
Dynamic library from %{name}.

%package -n 	%{liblegacy}
Summary:	Dynamic library from %{name}
Group:		System/Libraries
Conflicts:	%{_lib}kinoextensions0 < 0.3.2-20070731.7

%description -n %{liblegacy}
Dynamic library from %{name}.

%package -n     %{devname}
Summary:	Development libraries for %{name}
Group:		Development/C
Conflicts:	%{_lib}kinoextensions0 < 0.3.2-20070731.7

%description -n %{devname}
This package contains the development library for %{name}.

%prep
%setup -qn %{name}
%apply_patches
./autogen.sh

%build
%configure2_5x --disable-static
%make
										
%install
%makeinstall_std

%if "%{_lib}" != "lib"
	mv -f %{buildroot}%{_prefix}/lib %{buildroot}%{_libdir}
%endif

%files
%doc README COPYING
%{_bindir}/*
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/kino/libkinoextensions.so.%{major}*

%files -n %{liblegacy}
%{_libdir}/kino/libkinolegacy.so.%{major}*

%files -n %{devname}
%{_libdir}/kino/lib*.so


