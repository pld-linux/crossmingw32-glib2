%define		realname		glib
Summary:	Useful routines for 'C' programming
Summary(cs):	©ikovná knihovna s funkcemi pro pomocné programy
Summary(da):	Nyttige biblioteksfunktioner
Summary(de):	Eine nützliche Library von Dienstprogramm-Funktionen
Summary(es):	Conjunto de funciones gráficas utilitarias
Summary(fi):	Kirjasto, jossa on työkalufunktioita
Summary(fr):	Bibliothèque de fonctions utilitaires
Summary(ja):	ÊØÍø¤Ê¥æ¡¼¥Æ¥£¥ê¥Æ¥£´Ø¿ô¤Î¥é¥¤¥Ö¥é¥ê
Summary(pl):	Biblioteka zawieraj±ca wiele u¿ytecznych funkcji C
Summary(pt_BR):	Conjunto de funções gráficas utilitárias
Summary(tr):	Yararlý ufak yordamlar kitaplýðý
Summary(zh_CN):	ÊµÓÃ¹¤¾ßº¯Êý¿â
Name:		crossmingw32-%{realname}
Version:	2.2.2
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.gimp.org/~tml/gimp/win32/glib-dev-2.2.2.zip
URL:		http://www.gtk.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{realname}-%{version}-root-%(id -u -n)

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

%description -l cs
©ikovná knihovna s funkcemi pro pomocné programy. Vývojové knihovny a
hlavièky jsou v balíèku glib-devel.

%description -l da
Nyttigt bibliotek med forskellige funktioner. Udviklings- biblioteker
og headerfiler er i glib-devel pakken.

%description -l de
Eine nützliche Library von Dienstprogramm-Funktionen.
Entwicklungs-Libraries und Header befinden sich in glib-devel.

%description -l es
Conjunto de funciones utilitarias. Bibliotecas de desarrollo y
archivos de inclusión están en glib-devel.

%description -l fi
Kirjasto, jossa on työkalufunktioita. Kehitysversiot ja
header-tiedostot ovat glib-devel-paketissa.

%description -l ja

GLib¤Ï¥æ¡¼¥Æ¥£¥ê¥Æ¥£´Ø¿ô¤ò½¸¤á¤¿ÊØÍø¤Ê¥é¥¤¥Ö¥é¥ê¤Ç¤¹¡£¤³¤Î£Ã¸À¸ìÍÑ¥é¥¤¥Ö¥é¥ê¤Ï¡¢
¤¤¤¯¤Ä¤«¤ÎÌäÂê¤ò²ò·è¤¹¤ë¤è¤¦Àß·×¤µ¤ì¤Æ¤ª¤ê¡¢Â¿¤¯¤Î¥×¥í¥°¥é¥à¤«¤éÍ×µá¤µ¤ì¤ë»È¤¤¤ä¤¹¤¤
´Ø¿ô¤òÄó¶¡¤·¤Þ¤¹¡£

GLib¤ÏGDK,
GTK+Â¾Â¿¤¯¤Î¥¢¥×¥ê¥±¡¼¥·¥ç¥ó¤ÇÍøÍÑ¤µ¤ì¤ë¡£¤³¤Î¥é¥¤¥Ö¥é¥ê¤Ë°ÍÂ¸¤¹¤ë¥¢¥×¥ê¥±¡¼¥·¥ç¥ó
Åù¤Î¤¿¤á¤Ë¤³¤Îglib¥Ñ¥Ã¥±¡¼¥¸¤ò¥¤¥ó¥¹¥È¡¼¥ë¤·¤Æ¤¯¤À¤µ¤¤¡£

%description -l pl
Glib jest zestawem bibliotek zawieraj±cych funkcje do obs³ugi list i
drzew, funkcje mieszaj±ce, funkcje do alokacji pamiêci i du¿o innych
podstawowych funkcji i ró¿nych struktur danych u¿ywanych przez program
GIMP i wiele innych.

%description -l pt_BR
Conjunto de funções utilitárias. Bibliotecas de desenvolvimento e
arquivos de inclusão estão em glib-devel.

%description -l tr
Yararlý yordamlar kitaplýðý. Geliþtirme kitaplýklarý ve baþlýk
dosyalarý glib-devel paketinde yer almaktadýr.

%prep
install -d glib2
#%setup -q -n %{realname}-%{version}
cd glib2 && rm * -rf ; unzip %{SOURCE0} && cd ..

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{arch}
cp glib2/* $RPM_BUILD_ROOT%{arch} -rf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{arch}
