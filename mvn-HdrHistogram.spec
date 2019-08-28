#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-HdrHistogram
Version  : 2.1.9
Release  : 1
URL      : https://github.com/HdrHistogram/HdrHistogram/archive/HdrHistogram-2.1.9.tar.gz
Source0  : https://github.com/HdrHistogram/HdrHistogram/archive/HdrHistogram-2.1.9.tar.gz
Source1  : https://repo1.maven.org/maven2/org/hdrhistogram/HdrHistogram/2.1.9/HdrHistogram-2.1.9.jar
Source2  : https://repo1.maven.org/maven2/org/hdrhistogram/HdrHistogram/2.1.9/HdrHistogram-2.1.9.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0
Requires: mvn-HdrHistogram-data = %{version}-%{release}
Requires: mvn-HdrHistogram-license = %{version}-%{release}
BuildRequires : apache-ant
BuildRequires : buildreq-mvn

%description
HdrHistogram
----------------------------------------------
[![Gitter](https://badges.gitter.im/Join Chat.svg)](https://gitter.im/HdrHistogram/HdrHistogram?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Javadoc](http://javadoc-emblem.rhcloud.com/doc/org.hdrhistogram/HdrHistogram/badge.svg)]
(http://www.javadoc.io/doc/org.hdrhistogram/HdrHistogram)

%package data
Summary: data components for the mvn-HdrHistogram package.
Group: Data

%description data
data components for the mvn-HdrHistogram package.


%package license
Summary: license components for the mvn-HdrHistogram package.
Group: Default

%description license
license components for the mvn-HdrHistogram package.


%prep
%setup -q -n HdrHistogram-HdrHistogram-2.1.9

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-HdrHistogram
cp COPYING.txt %{buildroot}/usr/share/package-licenses/mvn-HdrHistogram/COPYING.txt
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/hdrhistogram/HdrHistogram/2.1.9
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/hdrhistogram/HdrHistogram/2.1.9/HdrHistogram-2.1.9.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/hdrhistogram/HdrHistogram/2.1.9
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/hdrhistogram/HdrHistogram/2.1.9/HdrHistogram-2.1.9.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/hdrhistogram/HdrHistogram/2.1.9/HdrHistogram-2.1.9.jar
/usr/share/java/.m2/repository/org/hdrhistogram/HdrHistogram/2.1.9/HdrHistogram-2.1.9.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-HdrHistogram/COPYING.txt
