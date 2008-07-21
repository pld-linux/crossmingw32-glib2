Summary:	Useful routines for 'C' programming - Ming32 cross version
Summary(cs.UTF-8):	Šikovná knihovna s funkcemi pro pomocné programy
Summary(da.UTF-8):	Nyttige biblioteksfunktioner
Summary(de.UTF-8):	Eine nützliche Library von Dienstprogramm-Funktionen
Summary(es.UTF-8):	Conjunto de funciones gráficas utilitarias
Summary(fi.UTF-8):	Kirjasto, jossa on työkalufunktioita
Summary(fr.UTF-8):	Bibliothèque de fonctions utilitaires
Summary(ja.UTF-8):	便利なユーティリティ関数のライブラリ
Summary(pl.UTF-8):	Biblioteka zawierająca wiele użytecznych funkcji C - wersja skrośna dla Ming32
Summary(pt_BR.UTF-8):	Conjunto de funções gráficas utilitárias
Summary(tr.UTF-8):	Yararlı ufak yordamlar kitaplığı
Summary(zh_CN.UTF-8):	实用工具函数库
%define		realname   glib
Name:		crossmingw32-%{realname}2
Version:	2.16.5
Release:	1
License:	LGPL v2+
Group:		Development/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/glib/2.16/glib-%{version}.tar.bz2
# Source0-md5:	039f02d47d4071322a3f00abf031e5d9
Patch0:		%{name}-stacktest.patch
Patch1:		%{realname}2-lt.patch
URL:		http://www.gtk.org/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.7
BuildRequires:	crossmingw32-gcc
BuildRequires:	crossmingw32-gettext
BuildRequires:	crossmingw32-libiconv
BuildRequires:	crossmingw32-pcre >= 7.6
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.16.0
Requires:	crossmingw32-gettext
Requires:	crossmingw32-pcre >= 7.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_strip	1

%define		target			i386-mingw32
%define		host			%{target}
%define		target_platform 	%{target}

%define		_sysprefix		/usr
%define		_prefix			%{_sysprefix}/%{target}
%define		_libdir			%{_prefix}/lib
%define		_pkgconfigdir		%{_prefix}/lib/pkgconfig
%define		_dlldir			/usr/share/wine/windows/system
%define		__cc			%{target}-gcc
%define		__cxx			%{target}-g++

%description
GLib, is a library which includes support routines for C such as
lists, trees, hashes, memory allocation, and many other things. GLIB
includes also generally useful data structures used by GIMP and many
other.

This package contains the cross version for Win32.

%description -l cs.UTF-8
Šikovná knihovna s funkcemi pro pomocné programy. Vývojové knihovny a
hlavičky jsou v balíčku glib-devel.

%description -l da.UTF-8
Nyttigt bibliotek med forskellige funktioner. Udviklings- biblioteker
og headerfiler er i glib-devel pakken.

%description -l de.UTF-8
Eine nützliche Library von Dienstprogramm-Funktionen.
Entwicklungs-Libraries und Header befinden sich in glib-devel.

%description -l es.UTF-8
Conjunto de funciones utilitarias. Bibliotecas de desarrollo y
archivos de inclusión están en glib-devel.

%description -l fi.UTF-8
Kirjasto, jossa on työkalufunktioita. Kehitysversiot ja
header-tiedostot ovat glib-devel-paketissa.

%description -l ja.UTF-8
GLibはユーティリティ関数を集めた便利なライブラリです。このＣ言語用ライブラリは、
いくつかの問題を解決するよう設計されており、多くのプログラムから要求される使いやすい
関数を提供します。

GLibはGDK,
GTK+他多くのアプリケーションで利用される。このライブラリに依存するアプリケーション
等のためにこのglibパッケージをインストールしてください。

%description -l pl.UTF-8
Glib jest zestawem bibliotek zawierających funkcje do obsługi list i
drzew, funkcje mieszające, funkcje do alokacji pamięci i dużo innych
podstawowych funkcji i różnych struktur danych używanych przez program
GIMP i wiele innych.

Ten pakiet zawiera wersję skrośną dla Win32.

%description -l pt_BR.UTF-8
Conjunto de funções utilitárias. Bibliotecas de desenvolvimento e
arquivos de inclusão estão em glib-devel.

%description -l tr.UTF-8
Yararlı yordamlar kitaplığı. Geliştirme kitaplıkları ve başlık
dosyaları glib-devel paketinde yer almaktadır.

%package dll
Summary:	DLL glib2 libraries for Windows
Summary(pl.UTF-8):	Biblioteki DLL glib2 dla Windows
Group:		Applications/Emulators
Requires:	crossmingw32-gettext-dll
Requires:	crossmingw32-pcre-dll >= 7.6
Requires:	wine

%description dll
DLL glib2 libraries for Windows.

%description dll -l pl.UTF-8
Biblioteki DLL glib2 dla Windows.

%prep
%setup -q -n %{realname}-%{version}
%patch0 -p1
%patch1 -p1

%build
export PKG_CONFIG_LIBDIR=%{_prefix}/lib/pkgconfig
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--target=%{target} \
	--host=%{target} \
	--disable-gtk-doc \
	--enable-shared \
	--with-pcre=system

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_dlldir}
mv -f $RPM_BUILD_ROOT%{_prefix}/bin/*.dll $RPM_BUILD_ROOT%{_dlldir}

%if 0%{!?debug:1}
%{target}-strip --strip-unneeded -R.comment -R.note $RPM_BUILD_ROOT%{_dlldir}/*.dll
%{target}-strip -g -R.comment -R.note $RPM_BUILD_ROOT%{_libdir}/*.a
%endif

rm -f $RPM_BUILD_ROOT%{_libdir}/charset.alias
# use system glib2-devel instead
rm -rf $RPM_BUILD_ROOT%{_datadir}/{aclocal,glib-2.0,gtk-doc,man}
# runtime
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/libgio-2.0.dll.a
%{_libdir}/libglib-2.0.dll.a
%{_libdir}/libgmodule-2.0.dll.a
%{_libdir}/libgobject-2.0.dll.a
%{_libdir}/libgthread-2.0.dll.a
%{_libdir}/libgio-2.0.la
%{_libdir}/libglib-2.0.la
%{_libdir}/libgmodule-2.0.la
%{_libdir}/libgobject-2.0.la
%{_libdir}/libgthread-2.0.la
%{_libdir}/gio-2.0.def
%{_libdir}/glib-2.0.def
%{_libdir}/gmodule-2.0.def
%{_libdir}/gobject-2.0.def
%{_libdir}/gthread-2.0.def
%{_includedir}/glib-2.0
%dir %{_libdir}/glib-2.0
%dir %{_libdir}/glib-2.0/include
%{_libdir}/glib-2.0/include/glibconfig.h
%{_pkgconfigdir}/gio-2.0.pc
%{_pkgconfigdir}/glib-2.0.pc
%{_pkgconfigdir}/gmodule-2.0.pc
%{_pkgconfigdir}/gmodule-export-2.0.pc
%{_pkgconfigdir}/gmodule-no-export-2.0.pc
%{_pkgconfigdir}/gobject-2.0.pc
%{_pkgconfigdir}/gthread-2.0.pc

%files dll
%defattr(644,root,root,755)
%{_dlldir}/libgio-2.0-*.dll
%{_dlldir}/libglib-2.0-*.dll
%{_dlldir}/libgmodule-2.0-*.dll
%{_dlldir}/libgobject-2.0-*.dll
%{_dlldir}/libgthread-2.0-*.dll
