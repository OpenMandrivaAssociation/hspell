%define devname %mklibname %{name} -d

Summary:	Free Hebrew linguistic project
Name:		hspell
Version:	1.1
Release:	6
Group:		Text tools
License:	LGPL
URL:		http://www.ivrix.org.il/projects/spell-checker/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		hspell-1.1-no-strip.patch
BuildRequires:	automake1.8

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

%package -n	%{devname}
Summary:	Development files for hspell
Group:		Development/Other
Provides:	hspell-devel = %{version}-%{release}
Obsoletes:	%{_lib}hspell0 < 1.1-6
Conflicts:	%{_lib}hspell0 < 1.1-6

%description -n	%{devname}
Development headers, and files for development from the hspell package.

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="%{optflags} -fPIC" CPPFLAGS="%{optflags} -fPIC" FFLAGS="optflags -fPIC" \
%configure2_5x --enable-fatverb --enable-fatverb --enable-shared --disable-static
%make

%install
%makeinstall_std

%files
%{_bindir}/*
%{_datadir}/hspell/*.wgz*
%{_mandir}/man*/*

%files -n %{devname}
%{_libdir}/libhspell.a
%{_includedir}/hspell.h
%{_includedir}/linginfo.h

