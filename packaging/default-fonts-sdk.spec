#sbs-git:slp/sdk/default-fonts-sdk default-fonts-sdk 0.0.1 cfc28893f4bd5cb9a28ffb97c4ca0ffcf30024b9
Name:       default-fonts-sdk
Summary:    free fonts for SLP SDK
Version:    0.0.1
Release:    9
Group:      TO_BE/FILLED_IN
License:    TO BE FILLED IN
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
mkdir -p %{buildroot}%{_datadir}/fallback_fonts && cp -a fallback_fonts %{buildroot}%{_datadir}

%files
%manifest default-fonts-sdk.manifest
%defattr(0644,root,root,-)
%{_datadir}/fonts/TizenSansRegular.ttf
%{_datadir}/fonts/TizenSansBold.ttf
%{_datadir}/fallback_fonts/TizenSansFallbackRegular.ttf
%{_datadir}/fallback_fonts/TizenSansFallbackBold.ttf
