#!/bin/bash

# 		Author:	Harkamal Singh Dadwal Dated:	1-2-2012                                        	##############################################
# 		Following script is being written to control the various daemons in linux,              	##############################################
#		pl. be sure that systemctl  utility is available as the same is available on            	##############################################
#		RHEL 6 and ( fedora 15 / above) if not available then pl. use sevice command			##############################################
#		Note: Run this script as root user or using sudo and set x bit on using chmod +x <name of file>	##############################################
#		/dev/null is used to suppess the ouput of the service command,					##############################################

for serVar in crond cups ntpd smb autofs slapd vsftpd sshd httpd dovecot mysqld postfix cntlmd network
do
	service ${serVar} status &> /dev/null
	if [ $? -eq 0 ]; then
		echo -e "\e[00;31m${serVar} daemon is already running \e[00m" ;
	else
		echo -e "\e[00;31mPlease enter your choice y/n to run the (:${serVar}:) daemon\e[00m";
		read choice;
		choice="$(echo ${choice} | tr 'A-Z' 'a-z')";
		if [ "${choice}" == "y" ] ; then
			systemctl start ${serVar}.service
		else
			echo "Skipped";
		fi
	fi
done
echo -e "\e[00;32mScript finished please check ur services with service command \e[00m";
