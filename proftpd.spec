# TODO
# - why main and -common package descriptions are same?
#
# Conditional build:
%bcond_without	pam		# disable PAM support
%bcond_without	ipv6		# disable IPv6 and TCPD support
%bcond_without	ssl		# disbale TLS/SSL support
%bcond_with	ldap		# enable LDAP support
%bcond_with	mysql		# enable MySQL support
%bcond_with	pgsql		# enable PostgreSQL support
%bcond_with	quotafile	# enable quota file support
%bcond_with	quotaldap	# enable quota ldap support
%bcond_with	quotamysql	# enable quota mysql support
%bcond_with	quotapgsql	# enable quota pgsql support
%bcond_with	linuxprivs	# enable libcap support
#
Summary:	PROfessional FTP Daemon with apache-like configuration syntax
Summary(es):	Servidor FTP profesional, con sintaxis de configuración semejante a la del apache
Summary(pl):	PROfesionalny serwer FTP
Summary(pt_BR):	Servidor FTP profissional, com sintaxe de configuração semelhante à do apache
Summary(zh_CN):	Ò×ÓÚ¹ÜÀíµÄ,°²È«µÄ FTP ·þÎñÆ÷
Name:		proftpd
Version:	1.2.10
Release:	5
Epoch:		1
License:	GPL v2+
Group:		Daemons
Source0:	ftp://ftp.proftpd.org/distrib/source/%{name}-%{version}.tar.bz2
# Source0-md5:	5feb4a7348e12faefc25e34fd92efdd6
Source1:	%{name}.conf
Source2:	%{name}.logrotate
Source3:	ftp.pamd
Source4:	%{name}.inetd
Source5:	%{name}.sysconfig
Source6:	%{name}.init
Source7:	ftpusers.tar.bz2
# Source7-md5:	76c80b6ec9f4d079a1e27316edddbe16
Source8:	http://www.castaglia.org/proftpd/modules/proftpd-mod-shaper-0.5.5.tar.gz
# Source8-md5:	ca3d63ffbc6ad5b6a9063f79b36d1b55
Patch0:		%{name}-umode_t.patch
Patch1:		%{name}-glibc.patch
Patch2:		%{name}-paths.patch
Patch3:		%{name}-noautopriv.patch
Patch4:		%{name}-wtmp.patch
Patch5:		%{name}-sendfile64.patch
URL:		http://www.proftpd.org/
%{?with_pam:Requires:		pam >= 0.79.0}
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libwrap-devel
%{?with_mysql:BuildRequires:		mysql-devel}
%{?with_quotamysql:BuildRequires:	mysql-devel}
BuildRequires:	ncurses-devel
%{?with_ldap:BuildRequires:		openldap-devel}
%{?with_quotaldap:BuildRequires:	openldap-devel}
%{?with_ssl:BuildRequires:		openssl-devel >= 0.9.7d}
%{?with_pam:BuildRequires:		pam-devel}
%{?with_pgsql:BuildRequires:		postgresql-devel}
%{?with_quotapgsql:BuildRequires:	postgresql-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/ftpd
%define		_localstatedir	/var/run

%description
ProFTPD is a highly configurable FTP daemon for unix and unix-like
operating systems. ProFTPD is designed to be somewhat of a "drop-in"
replacement for wu-ftpd. Full online documentation is available at
<http://www.proftpd.org/>, including a server configuration directive
reference manual.

This package also includes mod_shaper module from
<http://www.castaglia.org/proftpd/>

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
Requires:	logrotate
%{?with_pam:Requires:	pam >= 0.77.3}
Obsoletes:	proftpd < 0:1.2.2rc1-3

%description common
ProFTPD is a highly configurable FTP daemon for unix and unix-like
operating systems. ProFTPD is designed to be somewhat of a "drop-in"
replacement for wu-ftpd. Full online documentation is available at
<http://www.proftpd.org/>, including a server configuration directive
reference manual.

%description common -l pl
ProFTPD jest wysoce konfigurowalnym serwerem FTP dla systemów Unix.
ProFTPD jest robiony jako bezpo¶redni zamiennik wu-ftpd. Pe³na
dokunentacja jest dostêpna on-line pod http://www.proftpd.org/
w³±cznie z dokumentacj± dotycz±c± konfigurowania.

%package inetd
Summary:	inetd configs for proftpd
Summary(pl):	Pliki konfiguracyjne do u¿ycia proftpd poprzez inetd
Group:		Daemons
PreReq:		%{name}-common = %{epoch}:%{version}-%{release}
PreReq:		rc-inetd
Requires(post):	fileutils
Requires(post):	grep
Requires(post):	sed
Provides:	proftpd = %{epoch}:%{version}-%{release}
Provides:	ftpserver
Obsoletes:	proftpd-standalone
Obsoletes:	ftpserver
Obsoletes:	anonftp
Obsoletes:	bftpd
Obsoletes:	ftpd-BSD
Obsoletes:	glftpd
Obsoletes:	heimdal-ftpd
Obsoletes:	linux-ftpd
Obsoletes:	muddleftpd
Obsoletes:	pure-ftpd
Obsoletes:	troll-ftpd
Obsoletes:	vsftpd
Obsoletes:	wu-ftpd
Conflicts:	man-pages < 1.51

%description inetd
ProFTPD configs for running from inetd.

%description inetd -l pl
Pliki konfiguracyjna ProFTPD do startowania demona poprzez inetd.

%package standalone
Summary:	Standalone daemon configs for proftpd
Summary(pl):	Pliki konfiguracyjne do startowania proftpd w trybie standalone
Group:		Daemons
PreReq:		%{name}-common = %{epoch}:%{version}-%{release}
PreReq:		rc-scripts
Requires(post,preun):	/sbin/chkconfig
Requires(post):	fileutils
Requires(post):	grep
Requires(post):	sed
Provides:	proftpd = %{epoch}:%{version}-%{release}
Provides:	ftpserver
Obsoletes:	proftpd-inetd
Obsoletes:	ftpserver
Obsoletes:	anonftp
Obsoletes:	bftpd
Obsoletes:	ftpd-BSD
Obsoletes:	glftpd
Obsoletes:	heimdal-ftpd
Obsoletes:	linux-ftpd
Obsoletes:	muddleftpd
Obsoletes:	pure-ftpd
Obsoletes:	troll-ftpd
Obsoletes:	vsftpd
Obsoletes:	wu-ftpd
Conflicts:	man-pages < 1.51

%description standalone
ProFTPD configs for running as a standalone daemon.

%description standalone -l pl
Pliki konfiguracyjne ProFTPD do startowania demona w trybie
standalone.

%prep
%if %{with mysql} && %{with pgsql}
echo "Error: You can't build at once --with mysql and --with pgsql"
exit 1
%endif

%setup -q -a 8
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
# move mod_shaper code on to the source tree
mv mod_shaper/mod_shaper.c contrib/

%build
cp -f /usr/share/automake/config.sub .
%{__autoconf}
RUN_DIR=%{_localstatedir} ; export RUN_DIR
CFLAGS="%{rpmcflags} -I/usr/include/ncurses %{?with_mysql:-I/usr/include/mysql}"
CPPFLAGS="%{rpmcflags} -I/usr/include/ncurses %{?with_mysql:-I/usr/include/mysql}"

MODULES="
mod_ratio
mod_readme
mod_shaper
%{?with_ssl:mod_tls}
%{?with_ipv6:mod_wrap}
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

%configure \
	--enable-autoshadow \
	--with-modules=$(echo $MODULES | tr ' ' ':') \
	%{?with_ipv6:--enable-ipv6} \
	%{!?with_ssl:--disable-tls} \
	--enable-ctrls \
	--enable-sendfile

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{logrotate.d,pam.d,security,sysconfig/rc-inetd,rc.d/init.d} \
	$RPM_BUILD_ROOT/var/{lib/ftp/pub/Incoming,log}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL_USER=%(id -u) \
	INSTALL_GROUP=%(id -g)

rm -f $RPM_BUILD_ROOT%{_sbindir}/in.proftpd

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}
install %{SOURCE2} $RPM_BUILD_ROOT/etc/logrotate.d/ftpd
%{?with_pam:install %{SOURCE3} $RPM_BUILD_ROOT/etc/pam.d/ftp}
install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/ftpd
install %{SOURCE5} $RPM_BUILD_ROOT/etc/sysconfig/proftpd
install %{SOURCE6} $RPM_BUILD_ROOT/etc/rc.d/init.d/proftpd
install contrib/xferstats.holger-preiss $RPM_BUILD_ROOT%{_bindir}/xferstat

bzip2 -dc %{SOURCE7} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

mv -f contrib/README contrib/README.modules

:> $RPM_BUILD_ROOT%{_sysconfdir}/ftpusers.default
:> $RPM_BUILD_ROOT%{_sysconfdir}/ftpusers
:> $RPM_BUILD_ROOT/var/log/xferlog

ln -sf proftpd $RPM_BUILD_ROOT%{_sbindir}/ftpd

:> $RPM_BUILD_ROOT/etc/security/blacklist.ftp

%clean
rm -rf $RPM_BUILD_ROOT

%post common
umask 027
touch /var/log/xferlog
awk 'BEGIN { FS = ":" }; { if(($3 < 500)&&($1 != "ftp")) print $1; }' < /etc/passwd >> %{_sysconfdir}/ftpusers.default
if [ ! -f %{_sysconfdir}/ftpusers ]; then
	cp -f %{_sysconfdir}/ftpusers.default %{_sysconfdir}/ftpusers
fi

%post inetd
umask 027
if grep -iEqs "^ServerType[[:space:]]+standalone" %{_sysconfdir}/proftpd.conf ; then
	cp -a %{_sysconfdir}/proftpd.conf %{_sysconfdir}/proftpd.conf.rpmorig
	sed -e "s/^ServerType[[:space:]]\+standalone/ServerType			inetd/g" \
		%{_sysconfdir}/proftpd.conf.rpmorig >%{_sysconfdir}/proftpd.conf
fi
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload 1>&2
else
	echo "Type \"/etc/rc.d/init.d/rc-inetd start\" to start inet server" 1>&2
fi

%postun inetd
if [ "$1" = "0" -a -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload 1>&2
fi

%post standalone
/sbin/chkconfig --add proftpd
if grep -iEqs "^ServerType[[:space:]]+inetd" %{_sysconfdir}/proftpd.conf ; then
	cp -a %{_sysconfdir}/proftpd.conf %{_sysconfdir}/proftpd.conf.rpmorig
	sed -e "s/^ServerType[[:space:]]\+inetd/ServerType			standalone/g" \
		%{_sysconfdir}/proftpd.conf.rpmorig >%{_sysconfdir}/proftpd.conf
fi
if [ -f /var/lock/subsys/proftpd ]; then
	/etc/rc.d/init.d/proftpd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/proftpd start\" to start ProFTPD daemon."
fi

%preun standalone
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/proftpd ]; then
		/etc/rc.d/init.d/proftpd stop 1>&2
	fi
	/sbin/chkconfig --del proftpd
fi

%triggerpostun -- %{name}-inetd <= 1.2.10-1
echo "Changing deprecated config uptions"
cp /etc/ftpd/proftpd.conf /etc/ftpd/proftpd.conf.backup
sed -i -e 's/AuthPAMAuthoritative\b/AuthPAM/' /etc/ftpd/proftpd.conf
sed -i -e 's/TCPDServiceName/TCPServiceName/' /etc/ftpd/proftpd.conf
grep -v UseTCPD /etc/ftpd/proftpd.conf > /etc/ftpd/proftpd.conf.tmp
mv -f /etc/ftpd/proftpd.conf.tmp /etc/ftpd/proftpd.conf
chmod 640 /etc/ftpd/proftpd.conf

%triggerpostun -- %{name}-standalone <= 1.2.10-1
echo "Changing deprecated config uptions"
cp /etc/ftpd/proftpd.conf /etc/ftpd/proftpd.conf.backup
sed -i -e 's/AuthPAMAuthoritative\b/AuthPAM/' /etc/ftpd/proftpd.conf
sed -i -e 's/TCPDServiceName/TCPServiceName/' /etc/ftpd/proftpd.conf
grep -v UseTCPD /etc/ftpd/proftpd.conf > /etc/ftpd/proftpd.conf.tmp
mv -f /etc/ftpd/proftpd.conf.tmp /etc/ftpd/proftpd.conf
chmod 640 /etc/ftpd/proftpd.conf

%files common
%defattr(644,root,root,755)
%doc sample-configurations/*.conf CREDITS ChangeLog NEWS RELEASE_NOTES
%doc README README.LDAP README.PAM README.capabilities README.classes README.controls README.IPv6
%doc README.modules
%doc doc/*html contrib/*.html

%attr(750,root,ftp) %dir %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %ghost %{_sysconfdir}/ftpusers
%attr(640,root,root) %{_sysconfdir}/ftpusers.default
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/logrotate.d/*
%attr(640,root,root) %ghost /var/log/*
%{?with_pam:%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/*}

%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/blacklist.ftp

%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*

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
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/sysconfig/proftpd
%attr(754,root,root) /etc/rc.d/init.d/proftpd
%{_mandir}/man5/*
%lang(ja) %{_mandir}/ja/man5/ftpusers*
%lang(pl) %{_mandir}/pl/man5/ftpusers*
%lang(pt_BR) %{_mandir}/pt_BR/man5/ftpusers*
%lang(ru) %{_mandir}/ru/man5/ftpusers*
