Summary:	PROfessional FTP Daemon with apache-like configuration syntax
Summary(pl):	PROfesionalny serwer FTP  
Name:		proftpd
Version:	1.2.0pre10
Release:	2
License:	GPL
Group:		Daemons
Group(pl):	Serwery
Source0:	ftp://ftp.proftpd.org/distrib/%{name}-%{version}.tar.gz
#Source1:	configuration.html
#Source2:	reference.html
Source1:	proftpd.conf
Source2:	proftpd.logrotate
Source3:	ftp.pamd
Source4:	%{name}.inetd
Patch0:		proftpd-mdtm-localtime.patch
Patch1:		proftpd.patch
Patch2:		proftpd-glibc.patch
Patch3:		proftpd-paths.patch
Patch4:		proftpd-libcap.patch
Patch5:		proftpd-release.patch
Patch6:		proftpd-noautopriv.patch
Patch7:		proftpd-betterlog.patch
Patch8:		proftpd-DESTDIR.patch
URL:		http://www.proftpd.org/
BuildRequires:	pam-devel
Prereq:		rc-inetd
Requires:	rc-inetd
Requires:	logrotate
Requires:	pam >= 0.67
Requires:	inetdaemon
Provides:	ftpserver
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	ftpserver
Obsoletes:	wu-ftpd
Obsoletes:	anonftp
Obsoletes:	ftpd-BSD

%define		_sysconfdir	/etc/ftpd
%define		_localstatedir	/var/run

%description
ProFTPD is a highly configurable ftp daemon for unix and unix-like
operating systems.  ProFTPD is designed to be somewhat of a "drop-in"
replacement for wu-ftpd. Full online documentation is available at
http://www.proftpd.org/, including a server configuration directive
reference manual.

%description -l pl
ProFTPD jest wysoce konfigurowalnym serwerem ftp dla systemów Unix.
ProFTPD jest robiony jako bezpo¶redni zamiennik wu-ftpd. Pe³na dokunentacja
jest dostêpna on-line pod http://www.proftpd.org/ w³±cznie z dokumentacj±
dotycz±c± konfigurowania.

%prep
%setup -q 
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4	-p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
autoconf
LDFLAGS="-ldl -s"; export LDFLAGS
%configure \
	--enable-autoshadow \
	--with-modules=mod_ratio:mod_pam:mod_readme

make rundir=/var/run

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{etc/{logrotate.d,pam.d,sysconfig/rc-inetd},home/ftp/pub/Incoming}
install -d $RPM_BUILD_ROOT/var/log

make install DESTDIR=$RPM_BUILD_ROOT \
	INSTALL_USER=`id -u` \
	INSTALL_GROUP=`id -g`

rm -f $RPM_BUILD_ROOT%{_sbindir}/in.proftpd

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}
install %{SOURCE2} $RPM_BUILD_ROOT/etc/logrotate.d/ftpd
install %{SOURCE3} $RPM_BUILD_ROOT/etc/pam.d/ftp
install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/ftpd
install contrib/xferstats.* $RPM_BUILD_ROOT%{_bindir}/xferstat

mv contrib/README contrib/README.modules

:> $RPM_BUILD_ROOT%{_sysconfdir}/ftpusers.default
:> $RPM_BUILD_ROOT%{_sysconfdir}/ftpusers
:> $RPM_BUILD_ROOT/var/log/xferlog

ln -s proftpd $RPM_BUILD_ROOT%{_sbindir}/ftpd

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man[158]/* \
	sample-configurations/{virtual,anonymous}.conf ChangeLog README \
	README.linux-* contrib/README.modules

%post 
touch /var/log/xferlog
awk 'BEGIN { FS = ":" }; { if($3 < 100) print $1; }' < /etc/passwd >> %{_sysconfdir}/ftpusers.default
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
	/etc/rc.d/init.d/rc-inetd restart
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README*}.gz contrib/README.modules.gz
%doc sample-configurations/{virtual,anonymous}.conf.gz 

%attr(750,root,root) %dir %{_sysconfdir}
%attr(640,root,root) /etc/logrotate.d/*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.conf
%attr(640,root,root) %ghost /var/log/*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/*
%attr(640,root,root) /etc/sysconfig/rc-inetd/ftpd

%attr(640,root,root) %{_sysconfdir}/ftpusers.default
%attr(640,root,root) %ghost %{_sysconfdir}/ftpusers

%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*

%{_mandir}/man[158]/*

%dir /home/ftp/pub
%attr(711,root,root) %dir /home/ftp/pub/Incoming
