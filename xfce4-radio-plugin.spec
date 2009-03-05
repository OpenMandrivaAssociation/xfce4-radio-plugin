Summary:	Radio plugin for the Xfce panel
Name:		xfce4-radio-plugin
Version:	0.4.1
Release:	%mkrel 2
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-radio-plugin
Source0:	http://goodies.xfce.org/releases/xfce4-radio-plugin/%{name}-%{version}.tar.gz
Requires:	xfce4-panel >= 4.4.2
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	perl(XML::Parser)
Obsoletes:	xfce-radio-plugin
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This is an Xfce panel plugin which allows you to control your V4l radio device.
You can turn your radio on/off, tune it to some frequency and manage station
presets.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std 
 
%find_lang %{name}

%if %mdkversion < 200900
%post
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%clean_icon_cache hicolor
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_iconsdir}/hicolor/*/apps/*.png
%{_datadir}/xfce4/panel-plugins/*.desktop 
%{_libdir}/xfce4/panel-plugins/*
