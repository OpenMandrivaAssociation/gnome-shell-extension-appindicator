%global uuid appindicatorsupport@rgcjonas.gmail.com

Name:		gnome-shell-extension-appindicator
Summary:	AppIndicator/KStatusNotifierItem support for GNOME Shell
Version:	46
Release:	%mkrel 2
License:	GPLv2
Group:		Graphical desktop/GNOME
URL:		https://github.com/ubuntu/gnome-shell-extension-appindicator
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	jq
BuildRequires:	meson
# /usr/bin/glib-compile-schemas
BuildRequires:	glib2.0-common
Requires:	gnome-shell >= 3.14.0
Requires:	libappindicator-gtk3

# gnome-shell-extension-appindicator version >= 40 now also includes
# support for legacy X11 tray icons and the topicons(-plus) extensions
# are no longer maintained upstream
Provides:	gnome-shell-extension-topicons-plus = %{version}-%{release}
Provides:	gnome-shell-extension-topicons = %{version}-%{release}
Obsoletes:	gnome-shell-extension-topicons < 27-3

%description
This extension integrates Ubuntu AppIndicators and KStatusNotifierItems (KDE's
blessed successor of the systray) into GNOME Shell.

You can use gnome-tweaks (additional package) or run in terminal:

  gnome-extensions enable %uuid

%prep
%autosetup -p1

%build
%meson \
    -Dlocal_install=disabled
%meson_build

%install
%meson_install

%find_lang AppIndicatorExtension

rm %{buildroot}%{_datadir}/glib-2.0/schemas/gschemas.compiled

%files -f AppIndicatorExtension.lang
%license LICENSE
%doc README.md AUTHORS.md
%{_datadir}/gnome-shell/extensions/%{uuid}/
%{_datadir}/glib-2.0/schemas/*.gschema.xml
