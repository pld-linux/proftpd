# 
# Conditional builds:
# bcond_off_pam - disable PAM support
# bcond_on_ldap - enable LDAP suppoer
# bcond_on_mysql - enable MySQL suppoer
# bcond_on_quota - enable quota support
# bcond_on_linuxprivs - enable libcap support
# bcond_off_ipv6 - disable IPv6 and TCPD support
# bcond_off_ssl - disbale TLS/SSL support
# --without pam --with ldap --with mysql --with quota --with linuxprivs
Summary:	PROfessional FTP Daemon with apache-like configuration syntax
Summary(pl):	PROfesionalny serwer FTP  
Name:		proftpd
Version:	1.2.2rc1
Release:	3
License:	GPL
Group:		Daemons
Group(de):	Server
Group(pl):	Serwery
Source0:	ftp://ftp.proftpd.org/distrib/source/%{name}-%{version}.tar.bz2
Source1:	%{name}.conf
Source2:	%{name}.logrotate
Source3:	ftp.pamd
Source4:	%{name}.inetd
Source5:	%{name}.sysconfig
Source6:	%{name}.init
Source7:	%{name}-mod_tcpd.c
Patch0:		%{name}-1.2.2rc1-v6-20010406.patch.gz
# ftp://ftp.runestig.com/pub/proftpd-tls/
Patch1:		%{name}-1.2.2rc1+v6-tls.20010401.patch.gz
Patch2:		%{name}-umode_t.patch
Patch3:		%{name}-glibc.patch
Patch4:		%{name}-paths.patch
Patch5:		%{name}-release.patch
Patch6:		%{name}-noautopriv.patch
Patch7:		%{name}-DESTDIR.patch
Patch8:		%{name}-wtmp.patch
Patch9:		%{name}-link.patch
URL:		http://www.proftpd.org/
%{?!bcond_off_pam:BuildRequires:	pam-devel}
%{?bcond_on_ldap:BuildRequires:		openldap-devel}
%{?bcond_on_mysql:BuildRequires:	mysql-devel}
%{?!bcond_off_ssl:BuildRequires:	openssl-devel}
BuildRequires:	libwrap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/ftpd
%define		_localstatedir	/var/run

%description
ProFTPD is a highly configurable ftp daemon for unix and unix-like
operating systems. ProFTPD is designed to be somewhat of a "drop-in"
replacement for wu-ftpd. Full online documentation is available at
http://www.proftpd.org/, including a server configuration directive
reference manual.

%description -l pl
ProFTPD jest wysoce konfigurowalnym serwerem ftp dla systemów Unix.
ProFTPD jest robiony jako bezpo¶redni zamiennik wu-ftpd. Pe³na
dokunentacja jest dostêpna on-line pod http://www.proftpd.org/
w³±cznie z dokumentacj± dotycz±c± konfigurowania.

%package common
Summary:	PROfessional FTP Daemon with apache-like configuration syntax - common files
Summary(pl):	PROfesionalny serwer FTP  - wspólne pliki
Group:		Daemons
Prereq:		awk
Prereq:		fileutils
Requires:	logrotate
%{?!bcond_off_pam:Requires:	pam >= 0.67}
Obsoletes:	proftpd < 0:1.2.2rc1-3

%description  common
ProFTPD is a highly configurable ftp daemon for unix and unix-like
operating systems. ProFTPD is designed to be somewhat of a "drop-in"
replacement for wu-ftpd. Full online documentation is available at
http://www.proftpd.org/, including a server configuration directive
reference manual.

%description -l pl common
ProFTPD jest wysoce konfigurowalnym serwerem ftp dla systemów Unix.
ProFTPD jest robiony jako bezpo¶redni zamiennik wu-ftpd. Pe³na
dokunentacja jest dostêpna on-line pod http://www.proftpd.org/
w³±cznie z dokumentacj± dotycz±c± konfigurowania.


%package inetd
Summary:	inetd configs for proftpd
Group:		Daemons
Group(de):	Server
Group(pl):	Serwery
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
Obsoletes:	pure-ftpd
Obsoletes:	wu-ftpd

%description inetd
ProFTPD configs for running from inetd.

%package standalone
Summary:	standalone daemon configs for proftpd
Group:		Daemons
Group(de):	Server
Group(pl):	Serwery
Prereq:		%{name}-common = %{version}
Prereq:		rc-scripts
Provides:	proftpd = %{epoch}:%{version}-%{release}
Provides:	ftpserver
Obsoletes:	proftpd-inetd
Obsoletes:	ftpserver
Obsoletes:	anonftp
Obsoletes:	bftpd
Obsoletes:	ftpd-BSD
Obsoletes:	heimdal-ftpd
Obsoletes:	linux-ftpd
Obsoletes:	pure-ftpd
Obsoletes:	wu-ftpd

%description standalone
ProFTPD configs for running as a standalone daemon.

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
install -m644 %{SOURCE7} contrib/mod_tcpd.c

%build
autoconf
RUN_DIR=%{_localstatedir} ; export RUN_DIR
%configure \
	--enable-autoshadow \
	--with-modules=mod_ratio:mod_readme%{?!bcond_off_ipv6::mod_tcpd}%{?!bcond_off_pam::mod_pam}%{?bcond_on_ldap::mod_ldap}%{?bcond_on_quota::mod_quota}%{?bcond_on_linuxprivs::mod_linuxprivs}%{?bcond_on_mysql::mod_sql:mod_sql_mysql} \
	%{?!bcond_off_ipv6:--enable-ipv6} \
	%{?bcond_off_ssl:--disable-tls} \
	--enable-sendfile

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/{logrotate.d,pam.d,sysconfig/rc-inetd,rc.d/init.d} \
	$RPM_BUILD_ROOT/{home/ftp/pub/Incoming,var/log}

%{__make} install DESTDIR=$RPM_BUILD_ROOT \
	INSTALL_USER=`id -u` \
	INSTALL_GROUP=`id -g`

rm -f $RPM_BUILD_ROOT%{_sbindir}/in.proftpd

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}
install %{SOURCE2} $RPM_BUILD_ROOT/etc/logrotate.d/ftpd
%{?!bcond_off_pam:install %{SOURCE3} $RPM_BUILD_ROOT/etc/pam.d/ftp}
install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/ftpd
install %{SOURCE5} $RPM_BUILD_ROOT/etc/sysconfig/proftpd
install %{SOURCE6} $RPM_BUILD_ROOT/etc/rc.d/init.d/proftpd
install contrib/xferstats.* $RPM_BUILD_ROOT%{_bindir}/xferstat

mv -f contrib/README contrib/README.modules

:> $RPM_BUILD_ROOT%{_sysconfdir}/ftpusers.default
:> $RPM_BUILD_ROOT%{_sysconfdir}/ftpusers
:> $RPM_BUILD_ROOT/var/log/xferlog

ln -s proftpd $RPM_BUILD_ROOT%{_sbindir}/ftpd

gzip -9nf sample-configurations/{virtual,anonymous}.conf ChangeLog README \
	README.linux-* contrib/README.modules README.IPv6 README.PAM README.TLS
	 

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
	/etc/rc.d/init.d/rc-inetd restart 1>&2
else
	echo "Type \"/etc/rc.d/init.d/rc-inetd start\" to start inet sever" 1>&2
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README*}.gz contrib/README.modules.gz
%doc sample-configurations/{virtual,anonymous}.conf.gz 
%doc doc/*html

%attr(750,root,ftp) %dir %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.conf
%attr(640,root,root) /etc/logrotate.d/*
%attr(640,root,root) %ghost /var/log/*
%{?!bcond_off_pam:%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/*}

%attr(640,root,root) %{_sysconfdir}/ftpusers.default
%attr(640,root,root) %ghost %{_sysconfdir}/ftpusers

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
