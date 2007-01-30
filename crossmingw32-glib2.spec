Summary:	Useful routines for 'C' programming - Ming32 cross version
Summary(cs):	�ikovn� knihovna s funkcemi pro pomocn� programy
Summary(da):	Nyttige biblioteksfunktioner
Summary(de):	Eine n�tzliche Library von Dienstprogramm-Funktionen
Summary(es):	Conjunto de funciones gr�ficas utilitarias
Summary(fi):	Kirjasto, jossa on ty�kalufunktioita
Summary(fr):	Biblioth�que de fonctions utilitaires
Summary(ja):	�����ʥ桼�ƥ���ƥ��ؿ��Υ饤�֥��
Summary(pl):	Biblioteka zawieraj�ca wiele u�ytecznych funkcji C - wersja skro�na dla Ming32
Summary(pt_BR):	Conjunto de fun��es gr�ficas utilit�rias
Summary(tr):	Yararl� ufak yordamlar kitapl���
Summary(zh_CN):	ʵ�ù��ߺ�����
Name:		crossmingw32-glib2
Version:	2.12.7
Release:	1
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.gtk.org/pub/glib/2.12/win32/glib-dev-%{version}.zip
# Source0-md5:	844f15b040854fc78bef0b4257742476
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

%description -l cs
�ikovn� knihovna s funkcemi pro pomocn� programy. V�vojov� knihovny a
hlavi�ky jsou v bal��ku glib-devel.

%description -l da
Nyttigt bibliotek med forskellige funktioner. Udviklings- biblioteker
og headerfiler er i glib-devel pakken.

%description -l de
Eine n�tzliche Library von Dienstprogramm-Funktionen.
Entwicklungs-Libraries und Header befinden sich in glib-devel.

%description -l es
Conjunto de funciones utilitarias. Bibliotecas de desarrollo y
archivos de inclusi�n est�n en glib-devel.

%description -l fi
Kirjasto, jossa on ty�kalufunktioita. Kehitysversiot ja
header-tiedostot ovat glib-devel-paketissa.

%description -l ja

GLib�ϥ桼�ƥ���ƥ��ؿ��򽸤᤿�����ʥ饤�֥��Ǥ������Σø����ѥ饤�֥��ϡ�
�����Ĥ���������褹��褦�߷פ���Ƥ��ꡢ¿���Υץ�����फ���׵ᤵ���Ȥ��䤹��
�ؿ����󶡤��ޤ���

GLib��GDK,
GTK+¾¿���Υ��ץꥱ�����������Ѥ���롣���Υ饤�֥��˰�¸���륢�ץꥱ�������
���Τ���ˤ���glib�ѥå������򥤥󥹥ȡ��뤷�Ƥ���������

%description -l pl
Glib jest zestawem bibliotek zawieraj�cych funkcje do obs�ugi list i
drzew, funkcje mieszaj�ce, funkcje do alokacji pami�ci i du�o innych
podstawowych funkcji i r�nych struktur danych u�ywanych przez program
GIMP i wiele innych.

Ten pakiet zawiera wersj� skro�n� dla Win32.

%description -l pt_BR
Conjunto de fun��es utilit�rias. Bibliotecas de desenvolvimento e
arquivos de inclus�o est�o em glib-devel.

%description -l tr
Yararl� yordamlar kitapl���. Geli�tirme kitapl�klar� ve ba�l�k
dosyalar� glib-devel paketinde yer almaktad�r.

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
