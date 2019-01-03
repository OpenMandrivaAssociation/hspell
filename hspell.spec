%define major	0
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Free Hebrew linguistic project
Name:		hspell
Version:	1.4
Release:	1
Group:		Text tools
License:	AGPLv3
Url:		http://www.ivrix.org.il/projects/spell-checker/
Source0:	http://hspell.ivrix.org.il/%{name}-%{version}.tar.gz
Patch1:		hspell-1.2-perl-5.26.patch
BuildRequires:  pkgconfig(zlib)
BuildRequires:  locales-he
BuildRequires:  hunspell
BuildRequires:  pkgconfig(hunspell)
Requires:	%{libname} = %{EVRD}

%description
The Hspell project is a free Hebrew linguistic project.

Its primary goal is to create a free Hebrew spell-checker.

In addition to a spell-checker, the project also produced a Hebrew
morphological analyzer, which for every valid Hebrew word lists all
of its possible readings (valid combinations of prefix and inflected
base word).

The secondary goal of the project is to make the algorithms and
dictionaries, created initially for the spell-checker, freely
available. These could be used in more sophisticated research or
applications that require Hebrew word lists or a Hebrew morphology
engine.

Such potential application areas might include search engines, speech
synthesis, and much much more. The availability of a free basis will
hopefully encourage free development on top of it, to the benefit of
the general Hebrew-speaking population.

%package -n %{libname}
Summary:	Shared library files for hspell
Group:		Text tools

%description -n %{libname}
Shared library files for the hspell package.

%package -n	%{devname}
Summary:	Development files for hspell
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Conflicts:	%{_lib}hspell0 < 1.1-6

%description -n	%{devname}
Development headers, and files for development from the hspell package.

%prep
%autosetup -p1

%build
CFLAGS="%{optflags} -fPIC" CPPFLAGS="%{optflags} -fPIC" FFLAGS="optflags -fPIC" \
%configure \
	--enable-fatverb \
	--enable-shared

%make_build

%install
%make_install

%files
%{_bindir}/*
%{_datadir}/hspell/*.wgz*
%{_mandir}/man1/*
%{_mandir}/man3/*

%files -n %{libname}
%{_libdir}/libhspell.so.%{major}*

%files -n %{devname}
%{_libdir}/libhspell.so
%{_libdir}/libhspell.a
%{_includedir}/hspell.h
%{_includedir}/linginfo.h

