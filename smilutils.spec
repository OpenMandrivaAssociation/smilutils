%define major	0
%define libname %mklibname kinoextensions %major

%define _disable_ld_no_undefined 1
%define _disable_ld_as_needed 1

Name: 	 	smilutils
Summary: 	Command line tools for Kino's SMIL video format
Version: 	0.3.2
Release: 	20070731.6
Source:		%{name}-20070731.tar.bz2
Patch0:		smilutils-gcc4.3.patch
Patch1:		smilutils-gcc4.4.patch
Patch2:		smilutils-automake-1.13.patch
URL:		http://sf.net/projects/kino
License:	GPL
Group:		Video
BuildRequires:	autoconf
BuildRequires:	libdv-devel quicktime-devel libxml2-devel
BuildRequires:	SDL-devel libgdk_pixbuf2.0-devel 
BuildRequires:	png-devel
BuildRequires:	glib-2.0-devel
BuildRequires:	glib2-devel

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
%apply_patches

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

%files
%defattr(-,root,root)
%doc README COPYING
%{_bindir}/*
%{_mandir}/man1/*

%files -n %libname
%defattr(-,root,root)
%{_libdir}/kino/*


%changelog
* Sat Feb 11 2012 Oden Eriksson <oeriksson@mandriva.com> 0.3.2-20070731.5
+ Revision: 773075
- relink against libpcre.so.1

* Wed Apr 27 2011 Sergio Rafael Lemke <sergio@mandriva.com> 0.3.2-20070731.4
+ Revision: 659762
- bump release
- imported package smilutils

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - rebuild

  + Christophe Fergeau <cfergeau@mandriva.com>
    - rebuild
    - o fix gcc 4.4 build

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Jun 01 2008 Funda Wang <fwang@mandriva.org> 0.3.2-20070731.3mdv2009.0
+ Revision: 213977
- /usr/lib/kino is not a devel files location
- fix file list
- move .so files into /usr/lib64
- add debian patch for gcc 4.3

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.3.2-20070731.1mdv2008.1
+ Revision: 127381
- kill re-definition of %%buildroot on Pixel's request

* Wed Aug 22 2007 Austin Acton <austin@mandriva.org> 0.3.2-20070731.1mdv2008.0
+ Revision: 68816
- use debian sources to fix problems

* Fri Jun 08 2007 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 0.3.2-0.4mdv2008.0
+ Revision: 37529
- Rebuild with libslang2.

* Mon May 28 2007 Funda Wang <fwang@mandriva.org> 0.3.2-0.3mdv2008.0
+ Revision: 31897
- Rebuild against directfb 1.0


* Thu Mar 01 2007 Emmanuel Andry <eandry@mandriva.org> 0.3.2-0.2mdv2007.0
+ Revision: 130396
- rebuild for libgii
- Import smilutils

* Fri Jun 30 2006 Austin Acton <austin@mandriva.org> 0.3.2-1mdv2007.0
- from Cris B <cris AT beebgames DOT com> :
  - new version from CVS
  - requires gdk_pixbuf2
  - drop old patches

* Thu Sep 01 2005 Gwenole Beauchesne <gbeauchesne@mandriva.com> 0.3.0-4mdk
- fix for new libquicktime

* Thu Oct 28 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.3.0-3mdk
- C++ fixes

* Fri Jun 04 2004 Michael Scherer <misc@mandrake.org> 0.3.0-2mdk 
- rebuild for new libintl

* Sat Apr 03 2004 Austin Acton <austin@mandrake.org> 0.3.0-1mdk
- 0.3.0
- redo buildrequires
- rename library
- add man pages
- add devel files
- configure 2.5

