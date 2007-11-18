%define oname xfce4-radio-plugin

Summary:	Radio plugin for the Xfce panel
Name:		xfce-radio-plugin
Version:	0.2.1
Release:	%mkrel 1
License:	GPL
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-radio-plugin
Source0:	%{oname}-%{version}.tar.bz2
Requires:	xfce-panel >= 4.3.22
BuildRequires:	xfce-panel-devel >= 4.3.22
BuildRequires:	perl(XML::Parser)
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This is an Xfce panel plugin which allows you to control your V4l radio device.
You can turn your radio on/off, tune it to some frequency and manage station
presets.

%prep
%setup -qn %{oname}-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std 
 
%find_lang %{oname}

%post
%update_icon_cache hicolor

%postun
%clean_icon_cache hicolor

%clean
rm -rf %{buildroot}

%files -f %{oname}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL NEWS README
%{_iconsdir}/hicolor/*/apps/*.png
%{_datadir}/xfce4/panel-plugins/*.desktop 
%{_libdir}/xfce4/panel-plugins/*
