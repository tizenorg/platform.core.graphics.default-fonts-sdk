#sbs-git:slp/sdk/default-fonts-sdk default-fonts-sdk 0.0.1 cfc28893f4bd5cb9a28ffb97c4ca0ffcf30024b9
Name:       default-fonts-sdk
Summary:    free fonts for SLP SDK
Version:    0.0.1
Release:    1
Group:      TO_BE/FILLED_IN
License:    TO BE FILLED IN
Source0:    %{name}-%{version}.tar.gz

%description
free fonts for SLP SDK
This package is maintained by SDK team

%prep
%setup -q

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_datadir}/fonts && cp -a fonts %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_datadir}/fallback_fonts && cp -a fallback_fonts %{buildroot}%{_datadir}

%files
%defattr(0644,root,root,-)
%{_datadir}/fonts/SLPSansBold.ttf
%{_datadir}/fonts/SLPSansRegular.ttf
%{_datadir}/fonts/SLPSansLight.ttf
%{_datadir}/fonts/SLPSansMedium.ttf
%{_datadir}/fallback_fonts/SLPSansFallbackMedium.ttf
%{_datadir}/fallback_fonts/SLPSansFallbackRegular.ttf
%{_datadir}/fallback_fonts/SLPSansFallbackBold.ttf
