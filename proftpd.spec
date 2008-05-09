# TODO
# - mod_caps uses uname -r for detection
# - don't use internal libltdl
#
# Conditional build:
%bcond_without	pam		# disable PAM support
%bcond_without	ipv6		# disable IPv6 and TCPD support
%bcond_without	ssl		# disbale TLS/SSL support
%bcond_without	ldap		# disable LDAP support
%bcond_without	mysql		# disable MySQL support
%bcond_without	pgsql		# disable PostgreSQL support
%bcond_without	quotafile	# disable quota file support
%bcond_without	quotaldap	# disable quota ldap support
%bcond_without	quotamysql	# disable quota mysql support
%bcond_without	quotapgsql	# disable quota pgsql support
#
Summary:	PROfessional FTP Daemon with apache-like configuration syntax
Summary(es.UTF-8):	Servidor FTP profesional, con sintaxis de configuración semejante a la del apache
Summary(pl.UTF-8):	PROfesionalny serwer FTP
Summary(pt_BR.UTF-8):	Servidor FTP profissional, com sintaxe de configuração semelhante à do apache
Summary(zh_CN.UTF-8):	易于管理的,安全的 FTP 服务器
Name:		proftpd
Version:	1.3.1
Release:	4
Epoch:		2
License:	GPL v2+
Group:		Daemons
Source0:	ftp://ftp.proftpd.org/distrib/source/%{name}-%{version}.tar.bz2
# Source0-md5:	175958df8de92d5209b7b1e2e23a5a28
Source1:	%{name}.conf
Source3:	ftp.pamd
Source4:	%{name}.inetd
Source5:	%{name}.sysconfig
Source6:	%{name}.init
Source7:	ftpusers.tar.bz2
# Source7-md5:	76c80b6ec9f4d079a1e27316edddbe16
Source9:	%{name}-mod_pam.conf
Source10:	%{name}-mod_tls.conf
Source11:	%{name}-anonftp.conf
Patch0:		%{name}-umode_t.patch
Patch1:		%{name}-paths.patch
Patch2:		%{name}-noautopriv.patch
Patch3:		%{name}-wtmp.patch
Patch4:		%{name}-configure.patch
Patch5:		%{name}-pool.patch
URL:		http://www.proftpd.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libwrap-devel
%if %{with mysql} || %{with quotamysql}
BuildRequires:	mysql-devel
%endif
BuildRequires:	ncurses-devel
%if %{with ldap} || %{with quotaldap}
BuildRequires:	openldap-devel
%endif
%{?with_ssl:BuildRequires:	openssl-devel >= 0.9.7d}
%{?with_pam:BuildRequires:		pam-devel}
%if %{with pgsql} || %{with quotapgsql}
BuildRequires:	postgresql-devel
%endif
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir		/etc/ftpd
%define		_localstatedir	/var/run
%define		_libexecdir		%{_prefix}/%{_lib}/%{name}

%description
ProFTPD is a highly configurable FTP daemon for Unix and Unix-like
operating systems. ProFTPD is designed to be somewhat of a "drop-in"
replacement for wu-ftpd. Full online documentation is available at
<http://www.proftpd.org/>, including a server configuration directive
reference manual.

%description -l es.UTF-8
ProFTPD es un servidor FTP altamente configurable para sistemas
operativos Unix. Está proyectado para ser un substituto directo al
wu-ftpd. La documentación completa está disponible en
<http://www.proftpd.org/>, incluido el manual de referencia para las
directivas de configuración del servidor.

%description -l pl.UTF-8
ProFTPD jest wysoce konfigurowalnym serwerem FTP dla systemów Unix.
ProFTPD jest robiony jako bezpośredni zamiennik wu-ftpd. Pełna
dokumentacja jest dostępna on-line pod <http://www.proftpd.org/>
włącznie z dokumentacją dotyczącą konfigurowania.

%description -l pt_BR.UTF-8
O ProFTPD é um servidor FTP altamente configurável para sistemas
operacionais Unix.

É projetado para ser um substituto direto para o wu-ftpd. A
documentação completa está disponível em <http://www.proftpd.org/>,
incluindo o manual de referência para as diretivas de configuração do
servidor.

%package common
Summary:	PROfessional FTP Daemon with apache-like configuration syntax - common files
Summary(pl.UTF-8):	PROfesionalny serwer FTP  - wspólne pliki
Group:		Daemons
Requires(post):	awk
Requires(post):	fileutils
Obsoletes:	proftpd < 0:1.2.2rc1-3

%description common
ProFTPD is a highly configurable FTP daemon for Unix and Unix-like
operating systems. ProFTPD is designed to be somewhat of a "drop-in"
replacement for wu-ftpd. Full online documentation is available at
<http://www.proftpd.org/>, including a server configuration directive
reference manual.

%description common -l es.UTF-8
ProFTPD es un servidor FTP altamente configurable para sistemas
operativos Unix. Está proyectado para ser un substituto directo al
wu-ftpd. La documentación completa está disponible en
<http://www.proftpd.org/>, incluido el manual de referencia para las
directivas de configuración del servidor.

%description common -l pl.UTF-8
ProFTPD jest wysoce konfigurowalnym serwerem FTP dla systemów Unix.
ProFTPD jest robiony jako bezpośredni zamiennik wu-ftpd. Pełna
dokumentacja jest dostępna on-line pod <http://www.proftpd.org/>
włącznie z dokumentacją dotyczącą konfigurowania.

%description common -l pt_BR.UTF-8
O ProFTPD é um servidor FTP altamente configurável para sistemas
operacionais Unix.

É projetado para ser um substituto direto para o wu-ftpd. A
documentação completa está disponível em <http://www.proftpd.org/>,
incluindo o manual de referência para as diretivas de configuração do
servidor.

%package inetd
Summary:	inetd configs for proftpd
Summary(pl.UTF-8):	Pliki konfiguracyjne do użycia proftpd poprzez inetd
Group:		Daemons
Requires(post):	fileutils
Requires(post):	grep
Requires(post):	sed >= 4.0
Requires(triggerpostun):	sed >= 4.0
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	rc-inetd
Provides:	ftpserver
Provides:	proftpd = %{epoch}:%{version}-%{release}
Obsoletes:	anonftp
Obsoletes:	bftpd
Obsoletes:	ftpd-BSD
Obsoletes:	ftpserver
Obsoletes:	glftpd
Obsoletes:	heimdal-ftpd
Obsoletes:	krb5-ftpd
Obsoletes:	linux-ftpd
Obsoletes:	muddleftpd
Obsoletes:	proftpd-standalone
Obsoletes:	pure-ftpd
Obsoletes:	troll-ftpd
Obsoletes:	vsftpd
Obsoletes:	wu-ftpd
Conflicts:	man-pages < 1.51
Conflicts:	rpm < 4.4.2-0.2

%description inetd
ProFTPD configs for running from inetd.

%description inetd -l pl.UTF-8
Pliki konfiguracyjna ProFTPD do startowania demona poprzez inetd.

%package standalone
Summary:	Standalone daemon configs for proftpd
Summary(pl.UTF-8):	Pliki konfiguracyjne do startowania proftpd w trybie standalone
Group:		Daemons
Requires(post):	fileutils
Requires(post):	grep
Requires(post):	sed >= 4.0
Requires(post,preun):	/sbin/chkconfig
Requires(triggerpostun):	sed >= 4.0
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	rc-scripts
Provides:	ftpserver
Provides:	proftpd = %{epoch}:%{version}-%{release}
Obsoletes:	anonftp
Obsoletes:	bftpd
Obsoletes:	ftpd-BSD
Obsoletes:	ftpserver
Obsoletes:	glftpd
Obsoletes:	heimdal-ftpd
Obsoletes:	krb5-ftpd
Obsoletes:	linux-ftpd
Obsoletes:	muddleftpd
Obsoletes:	proftpd-inetd
Obsoletes:	pure-ftpd
Obsoletes:	troll-ftpd
Obsoletes:	vsftpd
Obsoletes:	wu-ftpd
Conflicts:	man-pages < 1.51
Conflicts:	rpm < 4.4.2-0.2

%description standalone
ProFTPD configs for running as a standalone daemon.

%description standalone -l pl.UTF-8
Pliki konfiguracyjne ProFTPD do startowania demona w trybie
standalone.

%package devel
Summary:	Header files ProFTPD
Summary(pl.UTF-8):	Pliki nagłówkowe ProFTPD
Group:		Development/Libraries
Requires:	acl-devel

%description devel
This is the package containing the header files for ProFTPD.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe ProFTPD

%package anonftp
Summary:	Anonymous FTP config for ProFTPD
Summary(pl.UTF-8):	Konfiguracja anonimowego FTP dla ProFTPD
Group:		Daemons
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description anonftp
Anonymous FTP config for ProFTPD.

%description anonftp -l pl.UTF-8
Konfiguracja anonimowego FTP dla ProFTPD.

%package mod_auth_pam
Summary:	ProFTPD PAM auth module
Summary(pl.UTF-8):	Moduł uwierzytelnienia PAM dla ProFTPD
Group:		Daemons
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	pam >= 0.79.0

%description mod_auth_pam
PAM authentication method for ProFTPD.

%description mod_auth_pam -l pl.UTF-8
Metoda uwierzytelnienia PAM dla ProFTPD.

%package mod_ldap
Summary:	ProFTPD OpenLDAP module
Summary(pl.UTF-8):	Moduł OpenLDAP dla ProFTPD
Group:		Daemons
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description mod_ldap
mod_ldap provides LDAP authentication support for ProFTPD. It supports
many features useful in "toaster" environments such as default UID/GID
and autocreation/autogeneration of home directories.

%description mod_ldap -l pl.UTF-8
mod_ldap dodaje obsługę uwierzytelnienia LDAP do ProFTPD. Obsługuje
wiele cech przydatnych w środowiskach "tosterowych", takich jak
domyślny UID/GID i automatyczne tworzenie/generowanie katalogów
domowych.

%package mod_quotatab
Summary:	ProFTPD quotatab module
Summary(pl.UTF-8):	Moduł quotatab dla ProFTPD
Group:		Daemons
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description mod_quotatab
A module for managing FTP byte/file quotas via centralized tables.

%description mod_quotatab -l pl.UTF-8
Moduł do zarządzania ograniczeniami bajtów/plików FTP poprzez
scentralizowane tabele.

%package mod_quotatab_file
Summary:	ProFTPD quotatab file module
Summary(pl.UTF-8):	Moduł quotatab_file dla ProFTPD
Group:		Daemons
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-mod_quotatab = %{epoch}:%{version}-%{release}

%description mod_quotatab_file
A mod_quotatab sub-module for managing quota data via file-based
tables.

%description mod_quotatab_file -l pl.UTF-8
Podmoduł mod_quotatab do zarządzania danymi o ograniczeniach poprzez
tabele zapisane w pliku.

%package mod_quotatab_ldap
Summary:	ProFTPD quotatab ldap module
Summary(pl.UTF-8):	Moduł quotatab_ldap dla ProFTPD
Group:		Daemons
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-mod_ldap = %{epoch}:%{version}-%{release}
Requires:	%{name}-mod_quotatab = %{epoch}:%{version}-%{release}

%description mod_quotatab_ldap
A mod_quotatab sub-module for obtaining quota information from an LDAP
directory.

%description mod_quotatab_ldap -l pl.UTF-8
Podmoduł mod_quotatab do pobierania informacji o ograniczeniach z
katalogu LDAP.

%package mod_quotatab_sql
Summary:	ProFTPD quotatab sql module
Summary(pl.UTF-8):	Moduł quotatab_sql dla ProFTPD
Group:		Daemons
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-mod_quotatab = %{epoch}:%{version}-%{release}
Requires:	%{name}-mod_sql = %{epoch}:%{version}-%{release}

%description mod_quotatab_sql
A mod_quotatab sub-module for managing quota data via SQL-based
tables.

%description mod_quotatab_sql -l pl.UTF-8
Podmoduł mod_quotatab do zarządzania danymi o ograniczeniach poprzez
tabele SQL.

%package mod_ratio
Summary:	ProFTPD ratio module
Summary(pl.UTF-8):	Moduł ratio dla ProFTPD
Group:		Daemons
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description mod_ratio
Support upload/download ratios.

%description mod_ratio -l pl.UTF-8
Obsługa współczynników upload/download.

%package mod_readme
Summary:	ProFTPD readme module
Summary(pl.UTF-8):	Moduł readme dla ProFTPD
Group:		Daemons
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description mod_readme
"README" file support.

%description mod_readme -l pl.UTF-8
Obsługa pliku "README".

%package mod_rewrite
Summary:	ProFTPD rewrite module
Summary(pl.UTF-8):	Moduł rewrite dla ProFTPD
Group:		Daemons
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description mod_rewrite
Runtime rewrite engine.

%package mod_sql
Summary:	ProFTPD SQL support module
Summary(pl.UTF-8):	Moduł obsługi SQL dla ProFTPD
Group:		Daemons
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description mod_sql
This module provides the necessary support for SQL based
authentication, logging and other features as required.

%description mod_sql -l pl.UTF-8
Ten moduł dodaje obsługę SQL potrzebną do uwierzytelniania, logowania
i innych możliwości opartych o SQL.

%package mod_sql_mysql
Summary:	ProFTPD sql mysql module
Summary(pl.UTF-8):	Moduł sql_mysql dla ProFTPD
Group:		Daemons
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-mod_sql = %{epoch}:%{version}-%{release}

%description mod_sql_mysql
Support for connecting to MySQL databases.

%description mod_sql_mysql -l pl.UTF-8
Obsługa łączenia się z bazami danych MySQL.

%package mod_sql_postgres
Summary:	ProFTPD sql postgres module
Summary(pl.UTF-8):	Moduł sql_postgres dla ProFTPD
Group:		Daemons
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-mod_sql = %{epoch}:%{version}-%{release}

%description mod_sql_postgres
Support for connecting to PostgreSQL databases.

%description mod_sql_postgres -l pl.UTF-8
Obsługa łączenia się z bazami danych PostgreSQL.

%package mod_tls
Summary:	ProFTPD TLS support
Summary(pl.UTF-8):	Obsługa TLS dla ProFTPD
Group:		Daemons
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description mod_tls
An RFC2228 SSL/TLS module for ProFTPD.

%description mod_tls -l pl.UTF-8
Moduł SSL/TLS zgodny z RFC2228 dla ProFTPD.

%package mod_wrap
Summary:	ProFTPD interface to libwrap
Summary(pl.UTF-8):	Interfejs ProFTPD do libwrap
Group:		Daemons
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	libwrap

%description mod_wrap
It enables the daemon to use the common tcpwrappers access control
library while in standalone mode, and in a very configurable manner.

Many programs will automatically add entries in the common allow/deny
files, and use of this module will allow a ProFTPD daemon running in
standalone mode to adapt as these entries are added. The portsentry
program does this, for example: when illegal access is attempted, it
will add hosts to the /etc/hosts.deny file.

%description mod_wrap -l pl.UTF-8
Ten pakiet pozwala demonowi używać wspólnej biblioteki kontroli
dostępu tcpwrappers w trybie samodzielnym w bardzo wygodny sposób.

Wiele programów automatycznie dodaje wpisy we wspólnych plikach
allow/deny, a użycie tego modułu pozwala demonowi ProFTPD działającemu
w trybie samodzielnym adaptować te wpisy w miarę dodawania. Robi tak
na przykład program portsentry: przy próbie niedozwolonego dostępu
dodaje hosty do pliku /etc/hosts.deny.

%prep
%setup -q -n %{name}-%{version}%{?_rc}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

cp -f /usr/share/automake/config.sub .

# cleanup backups after patching
find . '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

%build
%{__autoconf}

MODULES="
mod_ratio
mod_readme
mod_rewrite
mod_wrap
%{?with_ssl:mod_tls}
%{?with_pam:mod_auth_pam}
%{?with_ldap:mod_ldap}
%{?with_quotafile:mod_quotatab mod_quotatab_file}
%{?with_quotaldap:mod_quotatab mod_quotatab_ldap}
%{?with_quotamysql:mod_quotatab mod_quotatab_sql}
%{?with_quotapgsql:mod_quotatab mod_quotatab_sql}
%{?with_linuxprivs:mod_linuxprivs}
%{?with_mysql:mod_sql mod_sql_mysql}
%{?with_pgsql:mod_sql mod_sql_postgres}
"

MODARG=$(echo $MODULES | tr ' ' '\n' | sort -u | xargs | tr ' ' ':')
%configure \
	--with-includes=/usr/include/ncurses%{?with_mysql::%{_includedir}/mysql} \
	--enable-autoshadow \
	--enable-ctrls \
	--enable-dso \
	--enable-facl \
	%{?with_ipv6:--enable-ipv6} \
	--enable-sendfile \
	%{!?with_ssl:--disable-tls} \
	--with-shared=$MODARG \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{pam.d,security,sysconfig/rc-inetd,rc.d/init.d} \
	$RPM_BUILD_ROOT/var/{lib/ftp/pub/Incoming,log} \
	$RPM_BUILD_ROOT%{_sysconfdir}/conf.d \
	$RPM_BUILD_ROOT%{_includedir}/%{name}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL_USER=%(id -u) \
	INSTALL_GROUP=%(id -g)

rm $RPM_BUILD_ROOT%{_sbindir}/in.proftpd

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}
install %{SOURCE9} $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/mod_auth_pam.conf
%{?with_ldap:echo 'LoadModule        mod_ldap.c' > $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/mod_ldap.conf}
echo 'LoadModule        mod_quotatab.c' > $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/mod_quotatab.conf
echo 'LoadModule        mod_quotatab_file.c' > $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/mod_quotatab_file.conf
%{?with_quotaldap:echo 'LoadModule        mod_quotatab_ldap.c' > $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/mod_quotatab_ldap.conf}
echo 'LoadModule        mod_ratio.c' > $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/mod_ratio.conf
echo 'LoadModule        mod_readme.c' > $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/mod_readme.conf
echo 'LoadModule        mod_rewrite.c' > $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/mod_rewrite.conf
%if %{with mysql} || %{with pgsql}
echo 'LoadModule        mod_quotatab_sql.c' > $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/mod_quotatab_sql.conf
echo 'LoadModule        mod_sql.c' > $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/mod_sql.conf
%endif
%{?with_mysql:echo 'LoadModule        mod_sql_mysql.c' > $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/mod_sql_mysql.conf}
%{?with_pgsql:echo 'LoadModule        mod_sql_postgres.c' > $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/mod_sql_postgres.conf}
install %{SOURCE10} $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/mod_tls.conf
echo 'LoadModule        mod_wrap.c' > $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/mod_wrap.conf
install %{SOURCE11} $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/anonftp.conf

%{?with_pam:install %{SOURCE3} $RPM_BUILD_ROOT/etc/pam.d/ftp}
install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/ftpd
install %{SOURCE5} $RPM_BUILD_ROOT/etc/sysconfig/proftpd
install %{SOURCE6} $RPM_BUILD_ROOT/etc/rc.d/init.d/proftpd
install contrib/xferstats.holger-preiss $RPM_BUILD_ROOT%{_bindir}/xferstat

bzip2 -dc %{SOURCE7} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

:> $RPM_BUILD_ROOT%{_sysconfdir}/ftpusers.default
:> $RPM_BUILD_ROOT%{_sysconfdir}/ftpusers

# only for -inetd package?
ln -sf proftpd $RPM_BUILD_ROOT%{_sbindir}/ftpd

:> $RPM_BUILD_ROOT/etc/security/blacklist.ftp

rm $RPM_BUILD_ROOT%{_libdir}/%{name}/*.a
rm $RPM_BUILD_ROOT%{_libdir}/%{name}/*.la

rm -f $RPM_BUILD_ROOT%{_mandir}/ftpusers-path.diff*
cp -aL include/* config.h $RPM_BUILD_ROOT%{_includedir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post common
umask 027
awk -F: '{ if (($3 < 500) && ($1 != "ftp")) print $1; }' < /etc/passwd >> %{_sysconfdir}/ftpusers.default
if [ ! -f %{_sysconfdir}/ftpusers ]; then
	cp -f %{_sysconfdir}/ftpusers.default %{_sysconfdir}/ftpusers
fi

%posttrans inetd
if grep -iEqs "^ServerType[[:space:]]+standalone" %{_sysconfdir}/proftpd.conf ; then
	cp -f %{_sysconfdir}/proftpd.conf{,.rpmorig}
	sed -i -e 's/^ServerType[[:space:]]\+standalone/ServerType			inetd/g' %{_sysconfdir}/proftpd.conf
fi
%service -q rc-inetd reload

%postun inetd
if [ "$1" = "0" ]; then
	%service -q rc-inetd reload
fi

%posttrans standalone
if grep -iEqs "^ServerType[[:space:]]+inetd" %{_sysconfdir}/proftpd.conf ; then
	cp -f %{_sysconfdir}/proftpd.conf{,.rpmorig}
	sed -i -e 's/^ServerType[[:space:]]\+inetd/ServerType			standalone/g' %{_sysconfdir}/proftpd.conf
fi
/sbin/chkconfig --add proftpd
%service proftpd restart "ProFTPD daemon"

%preun standalone
if [ "$1" = "0" ]; then
	%service proftpd stop
	/sbin/chkconfig --del proftpd
fi

# macro called at module post scriptlet
%define	module_post \
if [ "$1" = "1" ]; then \
	if grep -iEqs "^ServerType[[:space:]]+inetd" %{_sysconfdir}/proftpd.conf; then \
		%service -q rc-inetd reload \
	elif grep -iEqs "^ServerType[[:space:]]+standalone" %{_sysconfdir}/proftpd.conf; then \
		%service -q proftpd restart \
	fi \
fi

# macro called at module postun scriptlet
%define	module_postun \
if [ "$1" = "0" ]; then \
	if grep -iEqs "^ServerType[[:space:]]+inetd" %{_sysconfdir}/proftpd.conf; then \
		%service -q rc-inetd reload \
	elif grep -iEqs "^ServerType[[:space:]]+standalone" %{_sysconfdir}/proftpd.conf; then \
		%service -q proftpd restart \
	fi \
fi

# it's sooo annoying to write them
%define	module_scripts() \
%post %1 \
%module_post \
\
%postun %1 \
%module_postun

%module_scripts mod_auth_pam
%module_scripts mod_ldap
%module_scripts mod_quotatab
%module_scripts mod_quotatab_file
%module_scripts mod_quotatab_ldap
%module_scripts mod_quotatab_sql
%module_scripts mod_ratio
%module_scripts mod_readme
%module_scripts mod_rewrite
%module_scripts mod_sql
%module_scripts mod_sql_mysql
%module_scripts mod_sql_postgres
%module_scripts mod_tls
%module_scripts mod_wrap

%files common
%defattr(644,root,root,755)
%doc sample-configurations/*.conf CREDITS ChangeLog NEWS RELEASE_NOTES
%doc README README.capabilities README.classes README.controls README.IPv6
%doc README.modules
%doc doc/*html
%dir %attr(750,root,ftp) %dir %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %ghost %{_sysconfdir}/ftpusers
%attr(640,root,root) %{_sysconfdir}/ftpusers.default
%dir %attr(750,root,root) %{_sysconfdir}/conf.d
#%attr(640,root,root) %ghost /var/log/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%dir %{_libdir}/%{name}
%dir /var/run/proftpd
%{_mandir}/man[18]/*
%dir /var/lib/ftp
%dir /var/lib/ftp/pub
%attr(711,ftp,ftp) %dir /var/lib/ftp/pub/Incoming

%files inetd
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd/ftpd
%{_mandir}/man5/*
%lang(ja) %{_mandir}/ja/man5/ftpusers*
%lang(pl) %{_mandir}/pl/man5/ftpusers*
%lang(pt_BR) %{_mandir}/pt_BR/man5/ftpusers*
%lang(ru) %{_mandir}/ru/man5/ftpusers*

%files standalone
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/proftpd
%attr(754,root,root) /etc/rc.d/init.d/proftpd
%{_mandir}/man5/*
%lang(ja) %{_mandir}/ja/man5/ftpusers*
%lang(pl) %{_mandir}/pl/man5/ftpusers*
%lang(pt_BR) %{_mandir}/pt_BR/man5/ftpusers*
%lang(ru) %{_mandir}/ru/man5/ftpusers*

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}

%files anonftp
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/anonftp.conf

%if %{with pam}
%files mod_auth_pam
%defattr(644,root,root,755)
%doc README.PAM
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/blacklist.ftp
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mod_auth_pam.conf
%attr(755,root,root) %{_libexecdir}/mod_auth_pam.so
%endif

%if %{with ldap}
%files mod_ldap
%defattr(644,root,root,755)
%doc README.LDAP
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mod_ldap.conf
%attr(755,root,root) %{_libexecdir}/mod_ldap.so
%endif

%files mod_quotatab
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mod_quotatab.conf
%attr(755,root,root) %{_libexecdir}/mod_quotatab.so

%if %{with quotafile}
%files mod_quotatab_file
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mod_quotatab_file.conf
%attr(755,root,root) %{_libexecdir}/mod_quotatab_file.so
%endif

%if %{with quotaldap}
%files mod_quotatab_ldap
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mod_quotatab_ldap.conf
%attr(755,root,root) %{_libexecdir}/mod_quotatab_ldap.so
%endif

%if %{with quotamysql} || %{with quotapgsql}
%files mod_quotatab_sql
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mod_quotatab_sql.conf
%attr(755,root,root) %{_libexecdir}/mod_quotatab_sql.so
%endif

%files mod_ratio
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mod_ratio.conf
%attr(755,root,root) %{_libexecdir}/mod_ratio.so

%files mod_readme
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mod_readme.conf
%attr(755,root,root) %{_libexecdir}/mod_readme.so

%files mod_rewrite
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mod_rewrite.conf
%attr(755,root,root) %{_libexecdir}/mod_rewrite.so

%if %{with mysql} || %{with pgsql}
%files mod_sql
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mod_sql.conf
%attr(755,root,root) %{_libexecdir}/mod_sql.so
%endif

%if %{with mysql}
%files mod_sql_mysql
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mod_sql_mysql.conf
%attr(755,root,root) %{_libexecdir}/mod_sql_mysql.so
%endif

%if %{with pgsql}
%files mod_sql_postgres
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mod_sql_postgres.conf
%attr(755,root,root) %{_libexecdir}/mod_sql_postgres.so
%endif

%files mod_tls
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mod_tls.conf
%attr(755,root,root) %{_libexecdir}/mod_tls.so

%files mod_wrap
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mod_wrap.conf
%attr(755,root,root) %{_libexecdir}/mod_wrap.so
