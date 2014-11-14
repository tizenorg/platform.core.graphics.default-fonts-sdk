Name:       default-fonts-sdk
Summary:    Free fonts for Tizen SDK
Version:    1.2.1.0
Release:    12
Group:      Graphics & UI Framework/Fonts
License:    Apache-2.0
Source0:    %{name}-%{version}.tar.gz
Source1001: default-fonts-sdk.manifest
BuildArch:  noarch

%description
free fonts for Tizen SDK
This package is maintained by SDK team

%prep
%setup -q

%build
cp %{SOURCE1001} .

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_datadir}/fonts && cp -a fonts %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_datadir}/fallback_fonts && cp -a fallback_fonts %{buildroot}%{_datadir}

%files
%manifest %{name}.manifest
%defattr(0644,root,root,-)
%{_datadir}/fonts/*
%{_datadir}/fallback_fonts/*
