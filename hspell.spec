%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Free Hebrew linguistic project
Name:		hspell
Version:	1.1
Release:	%mkrel 4
Group:		Text tools
License:	LGPL
URL:		http://www.ivrix.org.il/projects/spell-checker/
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	automake1.8
Requires:	%{libname} = %{version}-%{release}	
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The Hspell project is a free Hebrew linguistic project. 
Its primary goal is to create a free Hebrew spell-checker. 
 In addition to a spell-checker, the project also produced a Hebrew 
morphological analyzer, which for every valid Hebrew word lists all of its 
possible readings (valid combinations of prefix and inflected base word). 
 The secondary goal of the project is to make the algorithms and dictionaries, 
created initially for the spell-checker, freely available. These could be used 
in more sophisticated research or applications that require Hebrew word lists 
or a Hebrew morphology engine. 
 Such potential application areas might include search engines, speech 
synthesis, and much much more. The availability of a free basis will hopefully 
encourage free development on top of it, to the benefit of the general 
Hebrew-speaking population.

%package -n	%{libname}
Summary:	Shared library files for hspell
Group:		Text tools

%description -n	%{libname}
Shared library files for the hspell package.

%package -n	%{develname}
Summary:	Development files for hspell
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Provides:	libhspell-devel = %{version}-%{release}
Provides:	hspell-devel = %{version}-%{release}
Obsoletes:	%{mklibname hspell 0 -d}

%description -n	%{develname}
Development headers, and files for development from the hspell package.

%prep

%setup -q

%build
CFLAGS="%optflags -fPIC" CPPFLAGS="%optflags -fPIC" FFLAGS="optflags -fPIC" \
%configure2_5x --enable-fatverb --enable-fatverb 
%make

%install
rm -rf %{buildroot}

%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%_bindir/*
%_datadir/hspell/*.wgz*   
%_mandir/man*/*

%files -n %{libname}
%defattr(-, root, root)
%_libdir/libhspell.a

%files -n %{develname}
%defattr(-, root, root)
%_includedir/hspell.h
%_includedir/linginfo.h


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1-3mdv2011.0
+ Revision: 665464
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1-2mdv2011.0
+ Revision: 605879
- rebuild

* Sat Jan 02 2010 Frederik Himpe <fhimpe@mandriva.org> 1.1-1mdv2010.1
+ Revision: 485100
- update to new version 1.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0-6mdv2010.0
+ Revision: 425152
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0-5mdv2009.1
+ Revision: 351236
- rebuild

* Sun Jul 06 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0-4mdv2009.0
+ Revision: 232202
- fix summary-ended-with-dot
- fix devel package naming

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.0-1mdv2008.1
+ Revision: 126847
- kill re-definition of %%buildroot on Pixel's request
- do not hardcode bz2 extension
- replace %%_datadir/man by %%_mandir!


* Thu Nov 16 2006 Laurent Montel <lmontel@mandriva.com> 1.0-1mdv2007.0
+ Revision: 85054
- 1.0
- Import hspell

* Thu Feb 02 2006 Laurent MONTEL <lmontel@mandriva.com> 0.9-3
- Fix flags

* Thu Feb 02 2006 Laurent MONTEL <lmontel@mandriva.com> 0.9-2
- Fix compile under x86_64

* Mon Dec 12 2005 Laurent MONTEL <lmontel@mandriva.com> 0.9-1
- initial spec

