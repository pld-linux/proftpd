Summary:     PROfessional FTP Daemon with apache-like configuration syntax
Summary(pl): PROfesionalny FTP Demon z podobnym do apache sposobem konfigurowania
Name:        proftpd
Version:     1.2.0pre1
Release:     1
Copyright:   GPL
Group:       Networking/Daemons
Source0:     ftp://ftp.proftpd.org/distrib/%{name}-%{version}.tar.gz
Source1:     configuration.html
Source2:     reference.html
Source3:     proftpd.conf
Patch0:      proftpd-mdtm-localtime.patch
Patch1:      proftpd.patch
URL:         http://www.proftpd.org/
Provides:    ftpserver
Obsoletes:   wu-ftpd ncftpd beroftpd anonftp
BuildRoot:   /tmp/%{name}-%{version}-root

%description
ProFTPD is a highly configurable ftp daemon for unix and unix-like
operating systems.

ProFTPD is designed to be somewhat of a "drop-in" replacement for wu-ftpd.
Full online documentation is available at http://www.proftpd.org,
including a server configuration directive reference manual.

%description -l pl
ProFTPD jest wysoce konfigurowalnym demonem ftp dla U*nixów.

ProFTPD jest robiony jako bezpo¶redni zamiennik wu-ftpd.
Pe³na dokunentacja jest dostêpna on-line pod http://www.proftpd.org w³±cznie
z dokumentacj± dotycz±c± konfigurowania.

%prep
%setup -q
%patch0 -p1
#%patch1 -p1

install %{SOURCE1} %{SOURCE2} .

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s \
./configure \
	--prefix=/usr \
	--sysconfdir=/etc/ftpd \
	--enable-autoshadow
make rundir=/var/run

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/ftpd,home/ftp/pub/Incoming}
install -d $RPM_BUILD_ROOT/{var/run,usr/{bin,sbin,man/{man1,man8}}}

make install \
	INSTALL_USER=`id -u` \
	INSTALL_GROUP=`id -g` \
	prefix=$RPM_BUILD_ROOT/usr \
	rundir=$RPM_BUILD_ROOT/var/run \
	sysconfdir=$RPM_BUILD_ROOT/etc/ftpd

mv $RPM_BUILD_ROOT/usr/sbin/in.proftpd $RPM_BUILD_ROOT/usr/sbin/in.ftpd
install %{SOURCE3} $RPM_BUILD_ROOT/etc/ftpd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc changelog README
%doc sample-configurations/{virtual,anonymous}.conf *.html
%attr(600, root, root) %dir /etc/ftpd
%attr(600, root, root) %config(noreplace) %verify(not md5 mtime size) /etc/ftpd/proftpd.conf
%attr(755, root, root) /usr/bin/*
%attr(755, root, root) /usr/sbin/*
%attr(644, root,  man) /usr/man/man[158]/*
%attr(755,  ftp,  ftp) %dir /home/ftp
%attr(755,  ftp,  ftp) %dir /home/ftp/pub
%attr(711,  ftp,  ftp) %dir /home/ftp/pub/Incoming

%changelog
* Sun Nov 15 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.2.0pre1-1]
- added default configuration file with hashed configuration for
  anonymous ftp,
- config file moved to /etc/ftpd (with 700 permission),
- added %verify rule for /etc/etc/proftpd,
- added /home/ftp hierarhy for anonymous ftp resources,
- rundir must point to /var/run,
- added level 1 man pages,
- rewrited %install,
- removed patch for wu-ftpd compat.

* Sat Aug 22 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.1.6pre4-2]
- added proftpd-1.1.6pre4-compat_wu-ftpd.patch (null handling some wu-ftpd
  cmdl options).

* Thu Aug  6 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.1.6pre4-1]
- added pl translation,
- removed INSTALL from %doc (install procedure is in spec ;),
- addded permissions in %files instead setting them in %build (lets make 
  %buil only build procedure - more logical),
- renamed /usr/sbin/in.proftpd to /usr/sbin/in.ftpd (now updating inetd.conf
  is not neccesary) also removed %post[un] - this is simpler and now proftpd
  is "real" drop-in wu-ftpd replacement ;>,
- fiew simplifications in %install and %files,
- Conflicts: replaced by Obsoletes: in headre (more automated replacing
  other ftpserver) also added to list anonftp as not neccesary under proftpd,
- added noreplace %config parameter for /etc/proftpd.conf.

* Sat Aug 01 1998 Arne Coucheron <arneco@online.no>
  [1.1.6pre2-1]

* Thu Jul 23 1998 Arne Coucheron <arneco@online.no>
  [1.1.5pl4-1]
- making use of shadow libraries
  (Thanks to Mike McHendry <mmchen@ally.minn.net> for the hint)
- added beroftpd to Conflicts:
- added configuration and reference docs to the package

* Sun Jun 28 1998 Arne Coucheron <arneco@online.no>
  [1.0.3pl1-2]
- using $RPM_OPT_FLAGS
- using %%{name} and %%{version} macros
- using %defattr macro in filelist, ordinary users can build now 
- using install -d instead of mkdir -p
- made proftpd.conf chmod 600 for security
- added -q parameter to %setup
- added %config to /etc/proftpd.conf in filelist
- added Conflicts: wu-ftpd ncftpd
- installing util programs in /usr/bin instead of /usr/sbin
- changed name of spec file to proftpd.spec

* Wed May 6 1998 Vladimir Ivanov <vlad@elis.tasur.edu.ru>
- Fixed bug in mod_auth.c
- Initial RPM release
