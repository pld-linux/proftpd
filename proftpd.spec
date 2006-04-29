# TODO
# - mod_caps uses uname -r for detection
# Conditional build:
%bcond_without	pam		# disable PAM support
%bcond_without	ipv6		# disable IPv6 and TCPD support
%bcond_without	ssl		# disbale TLS/SSL support
%bcond_without	ldap		# enable LDAP support
%bcond_without	mysql		# enable MySQL support
%bcond_without	pgsql		# enable PostgreSQL support
%bcond_without	quotafile	# enable quota file support
%bcond_without	quotaldap	# enable quota ldap support
%bcond_without	quotamysql	# enable quota mysql support
%bcond_without	quotapgsql	# enable quota pgsql support
#
Summary:	PROfessional FTP Daemon with apache-like configuration syntax
Summary(es):	Servidor FTP profesional, con sintaxis de configuración semejante a la del apache
Summary(pl):	PROfesionalny serwer FTP
Summary(pt_BR):	Servidor FTP profissional, com sintaxe de configuração semelhante à do apache
Summary(zh_CN):	Ò×ÓÚ¹ÜÀíµÄ,°²È«µÄ FTP ·þÎñÆ÷
Name:		proftpd
Version:	1.3.0
Release:	0.24
Epoch:		1
License:	GPL v2+
Group:		Daemons
Source0:	ftp://ftp.proftpd.org/distrib/source/%{name}-%{version}.tar.bz2
# Source0-md5:	fae47d01b52e035eb6b7190e74c17722
Source1:	%{name}.conf
Source3:	ftp.pamd
Source4:	%{name}.inetd
Source5:	%{name}.sysconfig
Source6:	%{name}.init
Source7:	ftpusers.tar.bz2
# Source7-md5:	76c80b6ec9f4d079a1e27316edddbe16
Source9:	%{name}-mod_pam.conf
Source10:	%{name}-mod_tls.conf
Patch0:		%{name}-umode_t.patch
Patch1:		%{name}-glibc.patch
Patch2:		%{name}-paths.patch
Patch3:		%{name}-noautopriv.patch
Patch4:		%{name}-wtmp.patch
Patch5:		%{name}-sendfile64.patch
Patch6:		%{name}-configure.patch
URL:		http://www.proftpd.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libwrap-devel
%{?with_quotamysql:BuildRequires:	mysql-devel}
BuildRequires:	ncurses-devel
%{?with_quotaldap:BuildRequires:	openldap-devel}
%{?with_ssl:BuildRequires:	openssl-devel >= 0.9.7d}
%{?with_pam:BuildRequires:		pam-devel}
%{?with_quotapgsql:BuildRequires:	postgresql-devel}
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir		/etc/ftpd
%define		_localstatedir	/var/run
%define		_libexecdir		%{_prefix}/%{_lib}/%{name}

%description
ProFTPD is a highly configurable FTP daemon for unix and unix-like
operating systems. ProFTPD is designed to be somewhat of a "drop-in"
replacement for wu-ftpd. Full online documentation is available at
<http://www.proftpd.org/>, including a server configuration directive
reference manual.

%description -l es
ProFTPD es un servidor FTP altamente configurable para sistemas
operativos unix. Está proyectado para ser un substituto directo al
wu-ftpd. La documentación completa está disponible en
<http://www.proftpd.org/>, incluido el manual de referencia para las
directivas de configuración del servidor.

%description -l pl
ProFTPD jest wysoce konfigurowalnym serwerem FTP dla systemów Unix.
ProFTPD jest robiony jako bezpo¶redni zamiennik wu-ftpd. Pe³na
dokumentacja jest dostêpna on-line pod <http://www.proftpd.org/>
w³±cznie z dokumentacj± dotycz±c± konfigurowania.

%description -l pt_BR
O ProFTPD é um servidor FTP altamente configurável para sistemas
operacionais unix.

É projetado para ser um substituto direto para o wu-ftpd. A
documentação completa está disponível em <http://www.proftpd.org/>,
incluindo o manual de referência para as diretivas de configuração do
servidor.

%package common
Summary:	PROfessional FTP Daemon with apache-like configuration syntax - common files
Summary(pl):	PROfesionalny serwer FTP  - wspólne pliki
Group:		Daemons
Requires(post):	awk
Requires(post):	fileutils
Obsoletes:	proftpd < 0:1.2.2rc1-3

%description common
ProFTPD is a highly configurable FTP daemon for unix and unix-like
operating systems. ProFTPD is designed to be somewhat of a "drop-in"
replacement for wu-ftpd. Full online documentation is available at
<http://www.proftpd.org/>, including a server configuration directive
reference manual.

%description common -l es
ProFTPD es un servidor FTP altamente configurable para sistemas
operativos unix. Está proyectado para ser un substituto directo al
wu-ftpd. La documentación completa está disponible en
<http://www.proftpd.org/>, incluido el manual de referencia para las
directivas de configuración del servidor.

%description common -l pl
ProFTPD jest wysoce konfigurowalnym serwerem FTP dla systemów Unix.
ProFTPD jest robiony jako bezpo¶redni zamiennik wu-ftpd. Pe³na
dokumentacja jest dostêpna on-line pod <http://www.proftpd.org/>
w³±cznie z dokumentacj± dotycz±c± konfigurowania.

%description common -l pt_BR
O ProFTPD é um servidor FTP altamente configurável para sistemas
operacionais unix.

É projetado para ser um substituto direto para o wu-ftpd. A
documentação completa está disponível em <http://www.proftpd.org/>,
incluindo o manual de referência para as diretivas de configuração do
servidor.

%package inetd
Summary:	inetd configs for proftpd
Summary(pl):	Pliki konfiguracyjne do u¿ycia proftpd poprzez inetd
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

%description inetd -l pl
Pliki konfiguracyjna ProFTPD do startowania demona poprzez inetd.

%package standalone
Summary:	Standalone daemon configs for proftpd
Summary(pl):	Pliki konfiguracyjne do startowania proftpd w trybie standalone
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

%description standalone -l pl
Pliki konfiguracyjne ProFTPD do startowania demona w trybie
standalone.

%package devel
Summary:	Header files ProFTPD
Group:		Development/Libraries

%description devel
This is the package containing the header files for ProFTPD.

%package mod_auth_pam
Summary:	ProFTPD PAM auth module
Group:		Daemons
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	pam >= 0.79.0

%description mod_auth_pam
PAM authentication method for ProFTPD.

%package mod_ldap
Summary:	ProFTPD OpenLDAP module
Group:		Daemons
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description mod_ldap
LDAP authentication support.

mod_ldap provides LDAP authentication support for ProFTPD. It supports
many features useful in "toaster" environments such as default UID/GID
and autocreation/autogeneration of home directories.

%package mod_quotatab
Summary:	ProFTPD quotatab module
Group:		Daemons
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description mod_quotatab
A module for managing FTP byte/file quotas via centralized tables.

%package mod_quotatab_file
Summary:	ProFTPD quotatab file module
Group:		Daemons
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-mod_quotatab = %{epoch}:%{version}-%{release}

%description mod_quotatab_file
A mod_quotatab sub-module for managing quota data via file-based
tables.

%package mod_quotatab_ldap
Summary:	ProFTPD quotatab ldap module
Group:		Daemons
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-mod_ldap = %{epoch}:%{version}-%{release}
Requires:	%{name}-mod_quotatab = %{epoch}:%{version}-%{release}

%description mod_quotatab_ldap
A mod_quotatab sub-module for obtaining quota information from an LDAP
directory.

%package mod_quotatab_sql
Summary:	ProFTPD quotatab sql module
Group:		Daemons
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-mod_quotatab = %{epoch}:%{version}-%{release}
Requires:	%{name}-mod_sql = %{epoch}:%{version}-%{release}

%description mod_quotatab_sql
A mod_quotatab sub-module for managing quota data via SQL-based
tables.

%package mod_ratio
Summary:	ProFTPD quotatab ratio module
Group:		Daemons
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description mod_ratio
Support upload/download ratios.

%package mod_readme
Summary:	ProFTPD readme module
Group:		Daemons
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description mod_readme
"README" file support.

%package mod_sql
Summary:	ProFTPD SQL support module
Group:		Daemons
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description mod_sql
This module provides the necessary support for SQL based
authentication, logging and other features as required.

%package mod_sql_mysql
Summary:	ProFTPD sql mysql module
Group:		Daemons
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-mod_sql = %{epoch}:%{version}-%{release}

%description mod_sql_mysql
Support for connecting to MySQL databases.

%package mod_sql_postgres
Summary:	ProFTPD sql postgres module
Group:		Daemons
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-mod_sql = %{epoch}:%{version}-%{release}

%description mod_sql_postgres
Support for connecting to Postgres databases.

%package mod_tls
Summary:	ProFTPD TLS support
Group:		Daemons
Requires:	%{name}-common = %{epoch}:%{version}-%{release}

%description mod_tls
An RFC2228 SSL/TLS module for ProFTPD.

%package mod_wrap
Summary:	ProFTPD Interface to libwrap
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

%prep
%setup -q -n %{name}-%{version}%{?_rc}
%patch0 -p1
#%patch1 -p1 CONFUSES mod_ls.c
%patch2 -p1
%patch3 -p1
%patch4 -p1
#%patch5 -p1 NEEDS UPDATE
%patch6 -p1

%build
cp -f /usr/share/automake/config.sub .
%{__autoconf}

MODULES="
mod_ratio
mod_readme
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
	%{?with_mysql:--with-includes=%{_includedir}/mysql} \
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
echo 'LoadModule        mod_ldap.c' > $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/mod_ldap.conf
echo 'LoadModule        mod_quotatab.c' > $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/mod_quotatab.conf
echo 'LoadModule        mod_quotatab_file.c' > $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/mod_quotatab_file.conf
echo 'LoadModule        mod_quotatab_ldap.c' > $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/mod_quotatab_ldap.conf
echo 'LoadModule        mod_quotatab_sql.c' > $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/mod_quotatab_sql.conf
echo 'LoadModule        mod_ratio.c' > $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/mod_ratio.conf
echo 'LoadModule        mod_readme.c' > $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/mod_readme.conf
echo 'LoadModule        mod_sql.c' > $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/mod_sql.conf
echo 'LoadModule        mod_sql_mysql.c' > $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/mod_sql_mysql.conf
echo 'LoadModule        mod_sql_postgres.c' > $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/mod_sql_postgres.conf
install %{SOURCE10} $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/mod_tls.conf
echo 'LoadModule        mod_wrap.c' > $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/mod_wrap.conf

%{?with_pam:install %{SOURCE3} $RPM_BUILD_ROOT/etc/pam.d/ftp}
install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/ftpd
install %{SOURCE5} $RPM_BUILD_ROOT/etc/sysconfig/proftpd
install %{SOURCE6} $RPM_BUILD_ROOT/etc/rc.d/init.d/proftpd
install contrib/xferstats.holger-preiss $RPM_BUILD_ROOT%{_bindir}/xferstat

bzip2 -dc %{SOURCE7} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

:> $RPM_BUILD_ROOT%{_sysconfdir}/ftpusers.default
:> $RPM_BUILD_ROOT%{_sysconfdir}/ftpusers
:> $RPM_BUILD_ROOT/var/log/xferlog

# only for -inetd package?
ln -sf proftpd $RPM_BUILD_ROOT%{_sbindir}/ftpd

:> $RPM_BUILD_ROOT/etc/security/blacklist.ftp

rm $RPM_BUILD_ROOT%{_libdir}/%{name}/*.a
rm $RPM_BUILD_ROOT%{_libdir}/%{name}/*.la

rm -f $RPM_BUILD_ROOT%{_mandir}/ftpusers-path.diff*
cp -a include/* config.h $RPM_BUILD_ROOT%{_includedir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post common
umask 027
touch /var/log/xferlog
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
%module_scripts mod_sql
%module_scripts mod_sql_mysql
%module_scripts mod_sql_postgres
%module_scripts mod_tls
%module_scripts mod_wrap

%triggerpostun inetd -- %{name}-inetd <= 1:1.2.10
echo "Changing deprecated config options"
cp -f %{_sysconfdir}/proftpd.conf{,.rpmorig}
sed -i -e '
	s/AuthPAMAuthoritative\b/AuthPAM/
	s/TCPDServiceName/TCPServiceName/
	s/TlsRsaCertFile/TLSRSACertificateFile/
	s/TlsRsaKeyFile/TLSRSACertificateKeyFile/
	s/TlsDsaCertFile/TLSDSACertificateFile/
	s/TlsDsaKeyFile/TLSDSACertificateKeyFile/
	s/TlsCrlFile/TLSCARevocationFile/
	s/TlsDhParamFile/TLSDHParamFile/
	s/TlsCipherList/TLSCipherSuite/
	s/TlsCertsOk/TLSVerifyClient/
	/UseTCPD/d
' %{_sysconfdir}/proftpd.conf

%triggerpostun standalone -- %{name}-standalone <= 1:1.2.10
echo "Changing deprecated config options"
cp -f %{_sysconfdir}/proftpd.conf{,.rpmorig}
sed -i -e '
	s/AuthPAMAuthoritative\b/AuthPAM/
	s/TCPDServiceName/TCPServiceName/
	s/TlsRsaCertFile/TLSRSACertificateFile/
	s/TlsRsaKeyFile/TLSRSACertificateKeyFile/
	s/TlsDsaCertFile/TLSDSACertificateFile/
	s/TlsDsaKeyFile/TLSDSACertificateKeyFile/
	s/TlsCrlFile/TLSCARevocationFile/
	s/TlsDhParamFile/TLSDHParamFile/
	s/TlsCipherList/TLSCipherSuite/
	s/TlsCertsOk/TLSVerifyClient/
	/UseTCPD/d
' %{_sysconfdir}/proftpd.conf

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
%attr(640,root,root) %ghost /var/log/*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/blacklist.ftp
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

%files mod_auth_pam
%defattr(644,root,root,755)
%doc README.PAM
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mod_auth_pam.conf
%attr(755,root,root) %{_libexecdir}/mod_auth_pam.so

%files mod_ldap
%defattr(644,root,root,755)
%doc README.LDAP
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mod_ldap.conf
%attr(755,root,root) %{_libexecdir}/mod_ldap.so

%files mod_quotatab
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mod_quotatab.conf
%attr(755,root,root) %{_libexecdir}/mod_quotatab.so

%files mod_quotatab_file
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mod_quotatab_file.conf
%attr(755,root,root) %{_libexecdir}/mod_quotatab_file.so

%files mod_quotatab_ldap
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mod_quotatab_ldap.conf
%attr(755,root,root) %{_libexecdir}/mod_quotatab_ldap.so

%files mod_quotatab_sql
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mod_quotatab_sql.conf
%attr(755,root,root) %{_libexecdir}/mod_quotatab_sql.so

%files mod_ratio
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mod_ratio.conf
%attr(755,root,root) %{_libexecdir}/mod_ratio.so

%files mod_readme
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mod_readme.conf
%attr(755,root,root) %{_libexecdir}/mod_readme.so

%files mod_sql
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mod_sql.conf
%attr(755,root,root) %{_libexecdir}/mod_sql.so

%files mod_sql_mysql
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mod_sql_mysql.conf
%attr(755,root,root) %{_libexecdir}/mod_sql_mysql.so

%files mod_sql_postgres
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mod_sql_postgres.conf
%attr(755,root,root) %{_libexecdir}/mod_sql_postgres.so

%files mod_tls
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mod_tls.conf
%attr(755,root,root) %{_libexecdir}/mod_tls.so

%files mod_wrap
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mod_wrap.conf
%attr(755,root,root) %{_libexecdir}/mod_wrap.so
