#default-fonts-sdk
Name:       default-fonts-sdk
Summary:    fonts for Tizen SDK
Version:    1.3.0
Release:    1
Group:      TO_BE/FILLED_IN
License:    Apache License, Version 2.0
Source0:    %{name}-%{version}.tar.gz
Source1001: packaging/default-fonts-sdk.manifest
Requires(post): fontconfig

%description
fonts for Tizen SDK
This package is maintained by SDK team

%prep
%setup -q

%build
cp %{SOURCE1001} .

%install
rm -rf %{buildroot}
%if 0%{?sec_product_feature_profile_wearable}
    export TARGET=wearable
%else
    export TARGET=mobile
%endif

mkdir -p %{buildroot}/usr/share/license && cp LICENSE %{buildroot}/usr/share/license/%{name}
mkdir -p %{buildroot}%{_datadir}/fonts && cp -a common/fonts %{buildroot}%{_datadir}
#cp -a $TARGET/fonts %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_datadir}/fallback_fonts && cp -a common/fallback_fonts %{buildroot}%{_datadir}
#cp -a $TARGET/fallback_fonts %{buildroot}%{_datadir}

%post
/usr/bin/fc-cache -f

%files
%manifest default-fonts-sdk.manifest
%defattr(-,root,root,-)
%{_datadir}/fonts/*
%{_datadir}/fallback_fonts/*
/usr/share/license/%{name}

