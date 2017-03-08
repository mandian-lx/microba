%{?_javapackages_macros:%_javapackages_macros}

Summary:	A set of JFC (Swing) components
Name:		microba
Version:	0.4.4.3
Release:	1
License:	BSD
Group:		Development/Java
URL:		https://github.com/tdbear/%{name}/
Source0:	https://github.com/tdbear/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:  maven-local
BuildRequires:  mvn(jgraph:jgraph)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)

%description
Microba controls is a set of JFC (Swing) components.

%files -f .mfiles
%doc readme.txt
%doc README.md
%doc change.log.txt
%doc LICENSE

#----------------------------------------------------------------------------

%package javadoc
Summary:	Javadoc for %{name}
Group:		Documentation

%description javadoc
API documentation for %{name}.

%files javadoc -f .mfiles-javadoc
%doc LICENSE

#----------------------------------------------------------------------------

%prep
%setup -q

# Delete all pre-built binaries
find . -name "*.jar" -delete
find . -name "*.class" -delete

# fix jar-not-indexed warning
%pom_add_plugin :maven-jar-plugin . "<configuration>
	<archive>
		<index>true</index>
	</archive>
</configuration>"

# Fix Jar name
%mvn_file :%{name} %{name}-%{version} %{name}

%build
%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

