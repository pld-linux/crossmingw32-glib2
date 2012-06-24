%define		realname		glib
Summary:	Useful routines for 'C' programming
Summary(cs):	�ikovn� knihovna s funkcemi pro pomocn� programy
Summary(da):	Nyttige biblioteksfunktioner
Summary(de):	Eine n�tzliche Library von Dienstprogramm-Funktionen
Summary(es):	Conjunto de funciones gr�ficas utilitarias
Summary(fi):	Kirjasto, jossa on ty�kalufunktioita
Summary(fr):	Biblioth�que de fonctions utilitaires
Summary(ja):	�����ʥ桼�ƥ���ƥ��ؿ��Υ饤�֥��
Summary(pl):	Biblioteka zawieraj�ca wiele u�ytecznych funkcji C
Summary(pt_BR):	Conjunto de fun��es gr�ficas utilit�rias
Summary(tr):	Yararl� ufak yordamlar kitapl���
Summary(zh_CN):	ʵ�ù��ߺ�����
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
�����Ĥ���������褹��褦�߷פ���Ƥ��ꡢ¿���Υץ���फ���׵ᤵ���Ȥ��䤹��
�ؿ����󶡤��ޤ���

GLib��GDK,
GTK+¾¿���Υ��ץꥱ�����������Ѥ���롣���Υ饤�֥��˰�¸���륢�ץꥱ�������
���Τ���ˤ���glib�ѥå������򥤥󥹥ȡ��뤷�Ƥ���������

%description -l pl
Glib jest zestawem bibliotek zawieraj�cych funkcje do obs�ugi list i
drzew, funkcje mieszaj�ce, funkcje do alokacji pami�ci i du�o innych
podstawowych funkcji i r�nych struktur danych u�ywanych przez program
GIMP i wiele innych.

%description -l pt_BR
Conjunto de fun��es utilit�rias. Bibliotecas de desenvolvimento e
arquivos de inclus�o est�o em glib-devel.

%description -l tr
Yararl� yordamlar kitapl���. Geli�tirme kitapl�klar� ve ba�l�k
dosyalar� glib-devel paketinde yer almaktad�r.

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
