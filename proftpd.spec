# 
# Conditional builds:
# bcond_off_pam - disable PAM support
# bcond_on_ldap - enable LDAP suppoer
# bcond_on_mysql - enable MySQL suppoer
# bcond_on_quota - enable quota support
# bcond_on_linuxprivs - enable libcap support
# bcond_off_ipv6 - disable IPv6 support
# --without pam --with ldap --with mysql --with quota --with linuxprivs
Summary:	PROfessional FTP Daemon with apache-like configuration syntax
Summary(pl):	PROfesionalny serwer FTP  
Name:		proftpd
Version:	1.2.0rc2
Release:	13
License:	GPL
Group:		Daemons
Group(de):	Server
Group(pl):	Serwery
Source0:	ftp://ftp.proftpd.net/pub/proftpd/%{name}-%{version}.tar.gz
Source1:	%{name}.conf
Source2:	%{name}.logrotate
Source3:	ftp.pamd
Source4:	%{name}.inetd
Patch0:		%{name}-CVS-20000901.patch.gz
Patch1:		%{name}-1.2.0rc2cvs-ipv6-20000920.patch.gz
Patch2:		%{name}-umode_t.patch
Patch3:		%{name}-glibc.patch
Patch4:		%{name}-paths.patch
Patch5:		%{name}-release.patch
Patch6:		%{name}-noautopriv.patch
Patch7:		%{name}-betterlog.patch
Patch8:		%{name}-DESTDIR.patch
Patch9:		%{name}-wtmp.patch
Patch10:	%{name}-pam.patch
Patch11:	%{name}-mysql.patch
Patch12:	%{name}-mod_sqlpw-v6.patch
URL:		http://www.proftpd.net/
%{?!bcond_off_pam:BuildRequires:	pam-devel}
%{?bcond_on_ldap:BuildRequires:	openldap-devel}
%{?bcond_on_mysql:BuildRequires: mysql-devel}
Prereq:		rc-inetd
Requires:	rc-inetd
Requires:	logrotate
%{?!bcond_off_pam:Requires:	pam >= 0.67}
Requires:	inetdaemon
Provides:	ftpserver
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	ftpserver
Obsoletes:	anonftp
Obsoletes:	bftpd
Obsoletes:	ftpd-BSD
Obsoletes:	heimdal-ftpd
Obsoletes:	linux-ftpd
Obsoletes:	pure-ftpd
Obsoletes:	wu-ftpd

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
%patch10 -p1
%patch11 -p1
%patch12 -p1

%build
autoconf
RUN_DIR=%{_localstatedir} ; export RUN_DIR
%configure \
	--enable-autoshadow \
	--with-modules=mod_ratio:mod_readme%{?!bcond_off_pam::mod_pam}%{?bcond_on_ldap::mod_ldap}%{?bcond_on_quota::mod_quota}%{?bcond_on_linuxprivs::mod_linuxprivs}%{?bcond_on_mysql::mod_sqlpw:mod_mysql} \
	%{?!bcond_off_ipv6:--enable-ipv6} \
	--disable-sendfile

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/{logrotate.d,pam.d,sysconfig/rc-inetd} \
	$RPM_BUILD_ROOT/{home/ftp/pub/Incoming,var/log}

%{__make} install DESTDIR=$RPM_BUILD_ROOT \
	INSTALL_USER=`id -u` \
	INSTALL_GROUP=`id -g`

rm -f $RPM_BUILD_ROOT%{_sbindir}/in.proftpd

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}
install %{SOURCE2} $RPM_BUILD_ROOT/etc/logrotate.d/ftpd
%{?!bcond_off_pam:install %{SOURCE3} $RPM_BUILD_ROOT/etc/pam.d/ftp}
install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/ftpd
install contrib/xferstats.* $RPM_BUILD_ROOT%{_bindir}/xferstat

mv -f contrib/README contrib/README.modules

:> $RPM_BUILD_ROOT%{_sysconfdir}/ftpusers.default
:> $RPM_BUILD_ROOT%{_sysconfdir}/ftpusers
:> $RPM_BUILD_ROOT/var/log/xferlog

ln -s proftpd $RPM_BUILD_ROOT%{_sbindir}/ftpd

gzip -9nf sample-configurations/{virtual,anonymous}.conf ChangeLog README \
	README.linux-* contrib/README.modules README.IPv6

%post 
touch /var/log/xferlog
awk 'BEGIN { FS = ":" }; { if(($3 < 1000)&&($1 != "ftp")) print $1; }' < /etc/passwd >> %{_sysconfdir}/ftpusers.default
if [ ! -f %{_sysconfdir}/ftpusers ]; then
	( cd %{_sysconfdir}; mv -f ftpusers.default ftpusers )
fi

if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd restart 1>&2
else
	echo "Type \"/etc/rc.d/init.d/rc-inetd start\" to start inet sever" 1>&2
fi

%postun
if [ "$1" = "0" -a -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload 1>&2
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README*}.gz contrib/README.modules.gz
%doc sample-configurations/{virtual,anonymous}.conf.gz 
%doc doc/*html

%attr(750,root,root) %dir %{_sysconfdir}
%attr(640,root,root) /etc/logrotate.d/*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.conf
%attr(640,root,root) %ghost /var/log/*
%{?!bcond_off_pam:%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/*}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd/ftpd

%attr(640,root,root) %{_sysconfdir}/ftpusers.default
%attr(640,root,root) %ghost %{_sysconfdir}/ftpusers

%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*

%{_mandir}/man[158]/*

%dir /home/ftp/pub
%attr(711,root,root) %dir /home/ftp/pub/Incoming
