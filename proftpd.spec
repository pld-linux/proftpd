#
# Conditional build:
# _without_pam		- disable PAM support
# _with_ldap		- enable LDAP support
# _with_mysql		- enable MySQL support
# _with_quota		- enable quota support
# _with_linuxprivs	- enable libcap support
# _without_ipv6		- disable IPv6 and TCPD support
# _without_ssl		- disbale TLS/SSL support
#
Summary:	PROfessional FTP Daemon with apache-like configuration syntax
Summary(es):	Servidor FTP profesional, con sintaxis de configuración semejante a la del apache
Summary(pl):	PROfesionalny serwer FTP
Summary(pt_BR):	Servidor FTP profissional, com sintaxe de configuração semelhante à do apache
Summary(zh_CN):	Ò×ÓÚ¹ÜÀíµÄ,°²È«µÄ FTP ·þÎñÆ÷
Name:		proftpd
Version:	1.2.5
Release:	5
Epoch:		1
License:	GPL
Group:		Daemons
Source0:	ftp://ftp.proftpd.org/distrib/source/%{name}-%{version}.tar.bz2
# Source0-md5: 100a374dfcaa4852cb767dc6afeb4277
Source1:	%{name}.conf
Source2:	%{name}.logrotate
Source3:	ftp.pamd
Source4:	%{name}.inetd
Source5:	%{name}.sysconfig
Source6:	%{name}.init
Source7:	%{name}-mod_tcpd.c
Source8:	ftpusers.tar.bz2
# Source8-md5: 76c80b6ec9f4d079a1e27316edddbe16
Patch0:		%{name}-1.2.5-v6-20020808.patch.gz
# ftp://ftp.runestig.com/pub/proftpd-tls/
Patch1:		%{name}-1.2.2rc3+v6-tls.20010505.patch.gz
Patch2:		%{name}-umode_t.patch
Patch3:		%{name}-glibc.patch
Patch4:		%{name}-paths.patch
Patch5:		%{name}-release.patch
Patch6:		%{name}-noautopriv.patch
Patch7:		%{name}-DESTDIR.patch
Patch8:		%{name}-wtmp.patch
Patch9:		%{name}-link.patch
Patch10:	%{name}-port-65535.patch
Patch11:	%{name}-vmail_crypt.patch
URL:		http://www.proftpd.org/
BuildRequires:	autoconf
BuildRequires:	libwrap-devel
%{?_with_mysql:BuildRequires:	mysql-devel}
%{?_with_ldap:BuildRequires:	openldap-devel}
%{?!_without_ssl:BuildRequires:	openssl-devel >= 0.9.7}
%{?!_without_pam:BuildRequires:	pam-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/ftpd
%define		_localstatedir	/var/run

%description
ProFTPD is a highly configurable ftp daemon for unix and unix-like
operating systems. ProFTPD is designed to be somewhat of a "drop-in"
replacement for wu-ftpd. Full online documentation is available at
http://www.proftpd.org/, including a server configuration directive
reference manual.

%description -l es
ProFTPD es un servidor ftp altamente configurable para sistemas
operativos unix. Está proyectado para ser un substituto directo al
wu-ftpd. La documentación completa está disponible en
http://www.proftpd.org, incluido el manual de referencia para las
directivas de configuración del servidor.

%description -l pl
ProFTPD jest wysoce konfigurowalnym serwerem ftp dla systemów Unix.
ProFTPD jest robiony jako bezpo¶redni zamiennik wu-ftpd. Pe³na
dokunentacja jest dostêpna on-line pod http://www.proftpd.org/
w³±cznie z dokumentacj± dotycz±c± konfigurowania.

%description -l pt_BR
O ProFTPD é um servidor ftp altamente configurável para sistemas
operacionais unix.

É projetado para ser um substituto direto para o wu-ftpd. A
documentação completa está disponível em http://www.proftpd.org,
incluindo o manual de referência para as diretivas de configuração do
servidor.

%package common
Summary:	PROfessional FTP Daemon with apache-like configuration syntax - common files
Summary(pl):	PROfesionalny serwer FTP  - wspólne pliki
Group:		Daemons
Requires(post):	awk
Requires(post):	fileutils
Requires:	logrotate
%{?!_without_pam:Requires:	pam >= 0.67}
Obsoletes:	proftpd < 0:1.2.2rc1-3

%description  common
ProFTPD is a highly configurable ftp daemon for unix and unix-like
operating systems. ProFTPD is designed to be somewhat of a "drop-in"
replacement for wu-ftpd. Full online documentation is available at
http://www.proftpd.org/, including a server configuration directive
reference manual.

%description common -l pl
ProFTPD jest wysoce konfigurowalnym serwerem ftp dla systemów Unix.
ProFTPD jest robiony jako bezpo¶redni zamiennik wu-ftpd. Pe³na
dokunentacja jest dostêpna on-line pod http://www.proftpd.org/
w³±cznie z dokumentacj± dotycz±c± konfigurowania.

%package inetd
Summary:	inetd configs for proftpd
Summary(pl):	Pliki konfiguracyjne do u¿ycia proftpd poprzez inetd
Group:		Daemons
PreReq:		%{name}-common = %{epoch}:%{version}
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
Summary:	standalone daemon configs for proftpd
Summary(pl):	Pliki konfiguracyjne do startowania proftpd w trybie standalone
Group:		Daemons
PreReq:		%{name}-common = %{version}
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
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p0
%patch11 -p1
install -m644 %{SOURCE7} contrib/mod_tcpd.c

%build
%{__autoconf}
RUN_DIR=%{_localstatedir} ; export RUN_DIR
%configure \
	--enable-autoshadow \
	--with-modules=mod_ratio:mod_readme%{?!_without_ipv6::mod_tcpd}%{?!_without_pam::mod_pam}%{?_with_ldap::mod_ldap}%{?_with_quota::mod_quota}%{?_with_linuxprivs::mod_linuxprivs}%{?_with_mysql::mod_sql:mod_sql_mysql} \
	%{?!_without_ipv6:--enable-ipv6} \
	%{?_without_ssl:--disable-tls} \
	--enable-sendfile

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/{logrotate.d,pam.d,security,sysconfig/rc-inetd,rc.d/init.d} \
	$RPM_BUILD_ROOT/{home/services/ftp/pub/Incoming,var/log}

%{__make} install DESTDIR=$RPM_BUILD_ROOT \
	INSTALL_USER=`id -u` \
	INSTALL_GROUP=`id -g`

rm -f $RPM_BUILD_ROOT%{_sbindir}/in.proftpd

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}
install %{SOURCE2} $RPM_BUILD_ROOT/etc/logrotate.d/ftpd
%{?!_without_pam:install %{SOURCE3} $RPM_BUILD_ROOT/etc/pam.d/ftp}
install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/ftpd
install %{SOURCE5} $RPM_BUILD_ROOT/etc/sysconfig/proftpd
install %{SOURCE6} $RPM_BUILD_ROOT/etc/rc.d/init.d/proftpd
install contrib/xferstats.holger-preiss $RPM_BUILD_ROOT%{_bindir}/xferstat

bzip2 -dc %{SOURCE8} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

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

%files common
%defattr(644,root,root,755)
%doc sample-configurations/{virtual,anonymous}.conf ChangeLog README
%doc README.linux-* contrib/README.modules README.IPv6 README.PAM
%doc README.TLS README.mod_sql README.LDAP doc/*html

%attr(750,root,ftp) %dir %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %ghost %{_sysconfdir}/ftpusers
%attr(640,root,root) %{_sysconfdir}/ftpusers.default
%attr(640,root,root) /etc/logrotate.d/*
%attr(640,root,root) %ghost /var/log/*
%{?!_without_pam:%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/*}

%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/blacklist.ftp

%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*

%{_mandir}/man[18]/*

%dir /home/services/ftp
%dir /home/services/ftp/pub
%attr(711,root,root) %dir /home/services/ftp/pub/Incoming

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
