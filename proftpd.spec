# 
# Conditional builds:
# _without_pam - disable PAM support
# _with_ldap - enable LDAP suppoer
# _with_mysql - enable MySQL suppoer
# _with_quota - enable quota support
# _with_linuxprivs - enable libcap support
# _without_ipv6 - disable IPv6 and TCPD support
# _without_ssl - disbale TLS/SSL support
# --without pam --with ldap --with mysql --with quota --with linuxprivs
Summary:	PROfessional FTP Daemon with apache-like configuration syntax
Summary(es):	Servidor FTP profesional, con sintaxis de configuraci�n semejante a la del apache
Summary(pl):	PROfesionalny serwer FTP  
Summary(pt_BR):	Servidor FTP profissional, com sintaxe de configura��o semelhante � do apache
Name:		proftpd
Version:	1.2.5rc1
Release:	1
Epoch:		0
License:	GPL
Group:		Daemons
Source0:	ftp://ftp.proftpd.org/distrib/source/%{name}-%{version}.tar.bz2
Source1:	%{name}.conf
Source2:	%{name}.logrotate
Source3:	ftp.pamd
Source4:	%{name}.inetd
Source5:	%{name}.sysconfig
Source6:	%{name}.init
Source7:	%{name}-mod_tcpd.c
Patch0:		%{name}-1.2.2rc3-v6-20010814.patch.gz
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
Patch11:	%{name}-v6_fix.patch
URL:		http://www.proftpd.org/
%{?!_without_pam:BuildRequires:	pam-devel}
%{?_with_ldap:BuildRequires:		openldap-devel}
%{?_with_mysql:BuildRequires:	mysql-devel}
%{?!_without_ssl:BuildRequires:	openssl-devel >= 0.9.6a}
BuildRequires:	libwrap-devel
BuildRequires:	autoconf
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
operativos unix. Est� proyectado para ser un substituto directo al
wu-ftpd. La documentaci�n completa est� disponible en
http://www.proftpd.org, incluido el manual de referencia para las
directivas de configuraci�n del servidor.

%description -l pl
ProFTPD jest wysoce konfigurowalnym serwerem ftp dla system�w Unix.
ProFTPD jest robiony jako bezpo�redni zamiennik wu-ftpd. Pe�na
dokunentacja jest dost�pna on-line pod http://www.proftpd.org/
w��cznie z dokumentacj� dotycz�c� konfigurowania.

%description -l pt_BR
O ProFTPD � um servidor ftp altamente configur�vel para sistemas
operacionais unix.

� projetado para ser um substituto direto para o wu-ftpd. A
documenta��o completa est� dispon�vel em http://www.proftpd.org,
incluindo o manual de refer�ncia para as diretivas de configura��o do
servidor.

%package common
Summary:	PROfessional FTP Daemon with apache-like configuration syntax - common files
Summary(pl):	PROfesionalny serwer FTP  - wsp�lne pliki
Group:		Daemons
Prereq:		awk
Prereq:		fileutils
Requires:	logrotate
%{?!_without_pam:Requires:	pam >= 0.67}
Obsoletes:	proftpd < 0:1.2.2rc1-3

%description  common
ProFTPD is a highly configurable ftp daemon for unix and unix-like
operating systems. ProFTPD is designed to be somewhat of a "drop-in"
replacement for wu-ftpd. Full online documentation is available at
http://www.proftpd.org/, including a server configuration directive
reference manual.

%description -l pl common
ProFTPD jest wysoce konfigurowalnym serwerem ftp dla system�w Unix.
ProFTPD jest robiony jako bezpo�redni zamiennik wu-ftpd. Pe�na
dokunentacja jest dost�pna on-line pod http://www.proftpd.org/
w��cznie z dokumentacj� dotycz�c� konfigurowania.

%package inetd
Summary:	inetd configs for proftpd
Summary(pl):	Pliki konfiguracyjne do u�ycia proftpd poprzez inetd
Group:		Daemons
Prereq:		%{name}-common = %{epoch}:%{version}
Prereq:		rc-inetd
Provides:	proftpd = %{epoch}:%{version}-%{release}
Requires:	inetdaemon
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
Obsoletes:	wu-ftpd

%description inetd
ProFTPD configs for running from inetd.

%description -l pl inetd
Pliki konfiguracyjna ProFTPD do startowania demona poprzez inetd.

%package standalone
Summary:	standalone daemon configs for proftpd
Summary(pl):	Pliki konfiguracyjne do startowania proftpd w trybie standalone
Group:		Daemons
Prereq:		%{name}-common = %{version}
Prereq:		rc-scripts
Prereq:		/sbin/chkconfig
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
Obsoletes:	wu-ftpd

%description standalone
ProFTPD configs for running as a standalone daemon.

%description -l pl standalone
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
autoconf
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
	$RPM_BUILD_ROOT/{home/ftp/pub/Incoming,var/log}

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

mv -f contrib/README contrib/README.modules

:> $RPM_BUILD_ROOT%{_sysconfdir}/ftpusers.default
:> $RPM_BUILD_ROOT%{_sysconfdir}/ftpusers
:> $RPM_BUILD_ROOT/var/log/xferlog

ln -sf proftpd $RPM_BUILD_ROOT%{_sbindir}/ftpd

:> $RPM_BUILD_ROOT/etc/security/blacklist.ftp

gzip -9nf sample-configurations/{virtual,anonymous}.conf ChangeLog README \
	README.linux-* contrib/README.modules README.IPv6 README.PAM README.TLS
 
%clean
rm -rf $RPM_BUILD_ROOT

%post 
touch /var/log/xferlog
awk 'BEGIN { FS = ":" }; { if(($3 < 1000)&&($1 != "ftp")) print $1; }' < /etc/passwd >> %{_sysconfdir}/ftpusers.default
if [ ! -f %{_sysconfdir}/ftpusers ]; then
	( cd %{_sysconfdir}; mv -f ftpusers.default ftpusers )
fi

%post inetd
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
if [ "$1" = "0" -a -f /var/lock/subsys/proftpd ]; then
	/etc/rc.d/init.d/proftpd stop 1>&2
fi
/sbin/chkconfig --del proftpd

%files common
%defattr(644,root,root,755)
%doc {ChangeLog,README*}.gz contrib/README.modules.gz
%doc sample-configurations/{virtual,anonymous}.conf.gz 
%doc doc/*html

%attr(750,root,ftp) %dir %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.conf
%attr(640,root,root) /etc/logrotate.d/*
%attr(640,root,root) %ghost /var/log/*
%{?!_without_pam:%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/*}

%attr(640,root,root) %{_sysconfdir}/ftpusers.default
%attr(640,root,root) %ghost %{_sysconfdir}/ftpusers
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/blacklist.ftp

%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*

%{_mandir}/man[158]/*

%dir /home/ftp/pub
%attr(711,root,root) %dir /home/ftp/pub/Incoming

%files inetd
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd/ftpd

%files standalone
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/sysconfig/proftpd
%attr(754,root,root) /etc/rc.d/init.d/proftpd
