Name:           lxc-templates
Version:        3.0.0
Release:        0.1%{?dist}
Summary:        Old style template scripts for LXC

License:        LGPLv2+
URL:            https://linuxcontainers.org
Source0:        https://linuxcontainers.org/downloads/lxc/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  autoconf automake

Requires:       lxc-libs%{?_isa} >= %{version}
# Note: Requirements for the template scripts (busybox, dpkg,                       
# debootstrap, rsync, openssh-server, dhclient, apt, pacman, zypper,
# ubuntu-cloudimg-query etc...) are not explicitly mentioned here:
# their presence varies wildly on supported Fedora/EPEL releases and
# archs, and they are in most cases needed for a single template
# only. Also, the templates normally fail graciously when such a tool
# is missing. Moving each template to its own subpackage on the other
# hand would be overkill.

%global debug_package   %{nil}

%description
%{summary}.
The modern approach to build container images is distrobuilder.

%prep
%autosetup -n %{name}-%{version}
./autogen.sh
%configure

%build
%{make_build} %{?_smp_mflags}

%install
%{make_install} %{?_smp_mflags}

%files
%defattr(-,root,root)
%doc CONTRIBUTING MAINTAINERS
%license COPYING
%{_datadir}/lxc/config/* 
%{_datadir}/lxc/templates/lxc-*      

%changelog
* Sun Apr 01 2018 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 3.0.0-0.1
- Update to 3.0.0

* Mon Mar 26 2018 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 3.0.0.beta1-0.1
- Initial package

