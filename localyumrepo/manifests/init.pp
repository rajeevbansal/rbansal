class localyumrepo {
Package { ensure => "installed" }

package { "vsftpd": } 
package { "deltarpm": }
package { "python-deltarpm": }
package { "createrepo": }

service { "named":
  enable => true,
}

service { "vsftpd":
  enable => "true",
}

file { "/var/ftp/pub/localyumserver":
    ensure => "directory",
}

file { "/etc/yum.repos.d/localyumserver.repo":
  content => template("${module_name}/localyumserver.repo.erb"),
}

exec { "copy_files":
    path    => "/usr/local/bin/:/bin:/usr/sbin",
    command => "cp -ar *.* /var/ftp/pub/localyumserver",
}

exec { "create_repo":
    path    => "/usr/local/bin/:/bin:/usr/sbin",
    command => "createrepo -v /var/ftp/pub/localyumserver/",
}

exec { "yum":
    path    => "/usr/local/bin/:/bin:/usr/sbin",
    command => "yum clean all",
    }

exec { "yum":
    path    => "/usr/local/bin/:/bin:/usr/sbin",
    command => "yum update",
    }

file { "/usr/sbin/chgipad":
ensure => 'file',
content => template("${modules_name}/chgipad"),
owner  => 'root',
group  => 'root',
mode   => '0755',
}

exec { "script":
path    => "/usr/local/bin/:/bin:/usr/sbin",    
command => "./chgipad",
    }
}