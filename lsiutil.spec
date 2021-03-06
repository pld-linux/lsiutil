Summary:	LSIUtil Configuration Utility
Name:		lsiutil
Version:	1.56
Release:	1
License:	GPL
URL:		ftp://ftp.lsi.com/HostAdapterDrivers/linux/lsiutil/
Source0:	ftp://ftp.lsi.com/HostAdapterDrivers/linux/%{name}/lsiutil.tar.gz
# Source0-md5:	ceaf1104943ee1384b136ee0aaab4fba
Source1:	ftp://ftp.lsi.com/HostAdapterDrivers/linux/lsiutil/LSIUtil_UG.pdf
# Source1-md5:	4fc70658ffda877719ef3a0690f1f5e3
Group:		Base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LSIUtil is a powerful configuration utility that you can use with all
LSI Logic Fibre Channel, SAS, and SCSI host board adapters. LSIUtil
enables you to perform tasks such as updating board firmware, scanning
for connected devices, viewing configuration page information, running
diagnostic tests, and displaying current system events and statistics.
You can run LSIUtil in text-based, menu-driven mode or in
full-featured command line mode.


%prep
%setup -q -n %{name}
install %{SOURCE1} .

%build
rm -f lsiutil

%{__cc} -Wall %{rpmcppflags} %{rpmcflags} %{rpmldflags} -O lsiutil.c -o lsiutil

%install
rm -rf $RPM_BUILD_ROOT

install -D lsiutil $RPM_BUILD_ROOT%{_sbindir}/lsiutil

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.pdf
%attr(755,root,root) %{_sbindir}/lsiutil
