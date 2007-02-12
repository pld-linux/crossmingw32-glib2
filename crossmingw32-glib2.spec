Summary:	Useful routines for 'C' programming - Ming32 cross version
Summary(cs.UTF-8):   Šikovná knihovna s funkcemi pro pomocné programy
Summary(da.UTF-8):   Nyttige biblioteksfunktioner
Summary(de.UTF-8):   Eine nützliche Library von Dienstprogramm-Funktionen
Summary(es.UTF-8):   Conjunto de funciones gráficas utilitarias
Summary(fi.UTF-8):   Kirjasto, jossa on työkalufunktioita
Summary(fr.UTF-8):   Bibliothèque de fonctions utilitaires
Summary(ja.UTF-8):   便利なユーティリティ関数のライブラリ
Summary(pl.UTF-8):   Biblioteka zawierająca wiele użytecznych funkcji C - wersja skrośna dla Ming32
Summary(pt_BR.UTF-8):   Conjunto de funções gráficas utilitárias
Summary(tr.UTF-8):   Yararlı ufak yordamlar kitaplığı
Summary(zh_CN.UTF-8):   实用工具函数库
Name:		crossmingw32-glib2
Version:	2.12.9
Release:	1
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.gtk.org/pub/glib/2.12/win32/glib-dev-%{version}.zip
# Source0-md5:	7cf4be4e16727cfa8fbfd84de64f4b9c
URL:		http://www.gtk.org/
BuildRequires:	unzip
Requires:	crossmingw32-binutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_strip	1

%define		target			i386-mingw32
%define		target_platform 	i386-pc-mingw32
%define		arch			%{_prefix}/%{target}
%define		gccarch			%{_prefix}/lib/gcc-lib/%{target}
%define		gcclib			%{_prefix}/lib/gcc-lib/%{target}/%{version}

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

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{arch}/share

# omit man,share/aclocal,share/gtk-doc (they are system-wide)
cp -rf bin include lib $RPM_BUILD_ROOT%{arch}
cp -rf share/glib-2.0 $RPM_BUILD_ROOT%{arch}/share

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{arch}/bin/*
%{arch}/include/glib-2.0
%{arch}/lib/*.def
%{arch}/lib/*.lib
%{arch}/lib/*.dll.a
%{arch}/lib/glib-2.0
%{arch}/lib/pkgconfig/*.pc
# XXX: missing dir
%{arch}/share/glib-2.0
