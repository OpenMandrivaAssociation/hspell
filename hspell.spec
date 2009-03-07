%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Free Hebrew linguistic project
Name:		hspell
Version:	1.0
Release:	%mkrel 5
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
