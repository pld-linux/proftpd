Summary:	PROfessional FTP Daemon with apache-like configuration syntax
Summary(pl):	PROfesionalny serwer FTP  
Name:		proftpd
Version:	1.2.0pre3
Release:	2
Copyright:	GPL
Group:		Daemons
Group(pl):	Serwery
Source0:	ftp://ftp.proftpd.org/distrib/%{name}-%{version}.tar.gz
#Source1:	configuration.html
#Source2:	reference.html
Source1:	%{name}.conf
Source2:	%{name}.logrotate
Patch0:		%{name}-mdtm-localtime.patch
Patch1:		%{name}.patch
Patch2:		%{name}-glibc.patch
Patch3:		%{name}-paths.patch
Patch4:		%{name}-libcap.patch
Patch5:		%{name}-release.patch
URL:		http://www.proftpd.org
BuildPrereq:	/lib/libcap.so
Requires:	logrotate
Provides:	ftpserver
Obsoletes:	wu-ftpd
Obsoletes:	ncftpd
Obsoletes:	beroftpd
Obsoletes:	anonftp
BuildRoot:	/tmp/%{name}-%{version}-root

%description
ProFTPD is a highly configurable ftp daemon for unix and unix-like
operating systems.

ProFTPD is designed to be somewhat of a "drop-in" replacement for wu-ftpd.
Full online documentation is available at http://www.proftpd.org,
including a server configuration directive reference manual.

%description -l pl
ProFTPD jest wysoce konfigurowalnym demonem ftp dla systemów Unix.

ProFTPD jest robiony jako bezpo¶redni zamiennik wu-ftpd.
Pe³na dokunentacja jest dostêpna on-line pod http://www.proftpd.org w³±cznie
z dokumentacj± dotycz±c± konfigurowania.

%prep
%setup -q 
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4	-p1
%patch5 -p1

%build
autoconf
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s \
    ./configure \
	--prefix=%{_prefix} \
	--sysconfdir=/etc/ftpd \
	--enable-autoshadow \
	--with-modules=mod_ratio:mod_pam:mod_linuxprivs:mod_readme \
	%{_target_platform}

make rundir=/var/run

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{etc/{ftpd,logrotate.d},home/ftp/pub/Incoming}
install -d $RPM_BUILD_ROOT/{var/run,usr/{bin,sbin,share/man/{man1,man8}}}
install -d $RPM_BUILD_ROOT/var/log

make install \
	INSTALL_USER=`id -u` \
	INSTALL_GROUP=`id -g` \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	rundir=$RPM_BUILD_ROOT/var/run \
	sysconfdir=$RPM_BUILD_ROOT/etc/ftpd

rm -f $RPM_BUILD_ROOT%{_sbindir}/in.proftpd

install %{SOURCE1} $RPM_BUILD_ROOT/etc/ftpd
install %{SOURCE2} $RPM_BUILD_ROOT/etc/logrotate.d/proftpd
install contrib/xferstats.* $RPM_BUILD_ROOT%{_bindir}/xferstat

mv contrib/README contrib/README.modules

:> $RPM_BUILD_ROOT/etc/ftpd/ftpusers
:> $RPM_BUILD_ROOT/var/log/xferlog

ln -s proftpd $RPM_BUILD_ROOT%{_sbindir}/ftpd

gzip -9fn $RPM_BUILD_ROOT%{_mandir}/man[158]/* 
gzip -9fn sample-configurations/{virtual,anonymous}.conf changelog README
gzip -9fn README.linux-* contrib/README.modules

%post 
cat /etc/passwd | cut -d: -f1 | grep -v ftp >> /etc/ftpd/ftpusers

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {changelog,README*}.gz contrib/README.modules.gz
%doc sample-configurations/{virtual,anonymous}.conf.gz 

%attr(750,root,root) %dir /etc/ftpd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/ftpd/*
%attr(640,root,root) /etc/logrotate.d/*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /var/log/*

%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*

%{_mandir}/man[158]/*

%dir /home/ftp/pub
%attr(711,root,root) %dir /home/ftp/pub/Incoming
