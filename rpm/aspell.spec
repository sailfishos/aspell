Summary: A spelling checker
Name: aspell
Version: 0.60.8.1
Release: 1
License: LGPLv2 and MIT
URL: https://github.com/sailfishos/aspell
Source0: aspell-%{version}.tar.gz
Patch0: aspell-0.60.5-pspell_conf.patch
Patch1: aspell-0.60.8-gcc15.patch
BuildRequires: gettext, ncurses-devel, pkgconfig, texinfo
Provides: pspell < 0.13
Obsoletes: pspell < 0.13
Conflicts: ispell < 3.1.21, aspell-pt_BR < 2.5, aspell-config < 0.27
Conflicts: aspell-de < 0.50, aspell-fr < 0.50, aspell-ca < 0.50, aspell-da < 0.50, aspell-es < 0.50, aspell-it < 0.50, aspell-nl < 0.50, aspell-no < 0.50, aspell-sv < 0.50

%description
GNU Aspell is a spell checker designed to eventually replace Ispell. It can
either be used as a library or as an independent spell checker. Its main
feature is that it does a much better job of coming up with possible
suggestions than just about any other spell checker out there for the
English language, including Ispell and Microsoft Word. It also has many
other technical enhancements over Ispell such as using shared memory for
dictionaries and intelligently handling personal dictionaries when more
than one Aspell process is open at once.

%package devel
Summary: Static libraries and header files for Aspell development
Requires: aspell = %{version}-%{release}
Requires: pkgconfig
Provides: pspell-devel < 0.13
Obsoletes: pspell-devel < 0.13

%description devel
Aspell is a spelling checker. The aspell-devel package includes the
static libraries and header files needed for Aspell development.

%prep
%autosetup -p1 -n aspell-%{version}/aspell

%build
./autogen
%configure
%make_build

%install
%make_install

mkdir -p ${RPM_BUILD_ROOT}%{_libdir}/aspell-0.60

mv ${RPM_BUILD_ROOT}%{_libdir}/aspell-0.60/ispell ${RPM_BUILD_ROOT}%{_bindir}
mv ${RPM_BUILD_ROOT}%{_libdir}/aspell-0.60/spell ${RPM_BUILD_ROOT}%{_bindir}

rm -f ${RPM_BUILD_ROOT}%{_libdir}/libaspell.la
rm -f ${RPM_BUILD_ROOT}%{_libdir}/libpspell.la
rm -f ${RPM_BUILD_ROOT}%{_libdir}/aspell-0.60/*-filter.la
chmod 644 ${RPM_BUILD_ROOT}%{_bindir}/aspell-import
rm -f ${RPM_BUILD_ROOT}%{_infodir}/dir

%find_lang %{name}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%license COPYING
%doc README.md TODO
%dir %{_libdir}/aspell-0.60
%{_bindir}/a*
%{_bindir}/ispell
%{_bindir}/pr*
%{_bindir}/run-with-aspell
%{_bindir}/spell
%{_bindir}/word-list-compress
%{_libdir}/lib*.so.*
%{_libdir}/aspell-0.60/*
%{_datadir}/locale/*/LC_MESSAGES/aspell.mo
%{_infodir}/aspell.*
%{_mandir}/man1/aspell*
%{_mandir}/man1/run-with-aspell.1*
%{_mandir}/man1/word-list-compress.1*
%{_mandir}/man1/prezip-bin.1.*

%files devel
%dir %{_includedir}/pspell
%{_bindir}/pspell-config
%{_includedir}/aspell.h
%{_includedir}/pspell/pspell.h
%{_libdir}/lib*spell.so
%{_libdir}/pkgconfig/*
%{_infodir}/aspell-dev.*
%{_mandir}/man1/pspell-config.1*

