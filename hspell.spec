%define lib_name %mklibname %{name} %{lib_major}
%define lib_major 0

Summary:     	Hspell project is a free Hebrew linguistic project. 
Name:          hspell
Version:       1.0
Release:       %mkrel 1
Group:         Text tools
Source0:       %{name}-%{version}.tar.bz2
URL:           http://www.ivrix.org.il/projects/spell-checker/
BuildRoot:     %{_tmppath}/%{name}-%{version}-root
License:       LGPL
BuildRequires: automake1.8
Requires:		%{lib_name} = %{version}-%{release}	

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

%package -n %{lib_name}
Group:          Text tools
Summary:        Shared library files for hspell

%description -n %{lib_name}
Shared library files for the hspell package.

%package -n %{lib_name}-devel
Group:          Development/Other
Summary:        Development files for aspell
Requires:       %{name} = %{version}-%{release}
Requires:       %{lib_name} = %{version}-%{release}
Provides:       libhspell-devel = %{version}-%{release}
Provides:       hspell-devel = %{version}-%{release}

%description -n %{lib_name}-devel
Development headers, and files for development from the hspell package.

%prep
%setup -q

%build
CFLAGS="%optflags -fPIC" CPPFLAGS="%optflags -fPIC" FFLAGS="optflags -fPIC" \
%configure2_5x --enable-fatverb --enable-fatverb 
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std


%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{lib_name} -p /sbin/ldconfig
%postun -n %{lib_name} -p /sbin/ldconfig

%files 
%defattr(-,root,root)
%_bindir/*
%_datadir/hspell/*.wgz*   
%_mandir/man*/*

%files -n %{lib_name}-devel
%defattr(-, root, root)
%_includedir/hspell.h
%_includedir/linginfo.h

%files -n %{lib_name}
%defattr(-, root, root)
%_libdir/libhspell.a


