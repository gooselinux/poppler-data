
Summary: Encoding files 
Name:    poppler-data
Version: 0.4.0
Release: 1%{?dist}
# The cMap data files installed by the poppler-data package are
# under the COPYING.adobe license
# cidToUnicode, nameToUnicode and unicodeMap data files
# are under the COPYING.gpl2 license
License: BSD and GPLv2
Group:   Development/Libraries
URL:     http://poppler.freedesktop.org/
Source0: http://poppler.freedesktop.org/poppler-data-%{version}.tar.gz
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch

## first version to not include bundled poppler-data
#Conflicts: poppler < 0.11.0-5

%description
This package consists of encoding files for poppler.  When installed,
the encoding files enables poppler to correctly render CJK and Cyrillic 
properly.


%prep
%setup -q

%build
# intentionally left blank

%install
rm -rf $RPM_BUILD_ROOT
make install  DESTDIR=$RPM_BUILD_ROOT datadir=%{_datadir}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING COPYING.adobe COPYING.gpl2 README
%{_datadir}/poppler/


%changelog
* Thu Jan 14 2010 Marek Kasik <mkasik@redhat.com> - 0.4.0-1
- poppler-data-0.4.0
- Related: #543948

* Mon Nov 23 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.3.1-1
- poppler-data-0.3.1

* Tue Sep 22 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.3.0-1
- poppler-data-0.3.0
- License: BSD and GPLv2

* Mon Jun 22 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.2.1-1
- first try at separate poppler-data

