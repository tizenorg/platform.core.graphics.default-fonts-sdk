Name:       default-fonts-sdk
Summary:    free fonts for SLP SDK
Version:    0.0.1
Release:    0
Group:      TO_BE/FILLED_IN
License:    Apache-2.0
Source0:    %{name}-%{version}.tar.gz
Source1001: packaging/default-fonts-sdk.manifest 

%description
free fonts for SLP SDK
This package is maintained by SDK team

%prep
%setup -q

%build
cp %{SOURCE1001} .

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_datadir}/fonts && cp -a fonts %{buildroot}%{_datadir}

%files
%manifest default-fonts-sdk.manifest
%defattr(0644,root,root,-)
%{_datadir}/fonts/SLPSansBold_1119.ttf
%{_datadir}/fonts/SLPSansRegular_1119.ttf
%{_datadir}/fonts/SLPSansFallbackMedium.ttf
%{_datadir}/fonts/SLPSansFallbackRegular.ttf
%{_datadir}/fonts/SLPSansFallbackBold.ttf
%{_datadir}/fonts/SLPSansLight_1119.ttf
%{_datadir}/fonts/SLPSansMedium_1119.ttf
