#!/bin/bash
source ~/.bash_profile

red=`tput setaf 1`
green=`tput setaf 2`
yellow=`tput setaf 3`
reset=`tput sgr0`





domain=$1

echo "${red}Recon started on $domain ${reset}"

echo "${red}Listing subdomains using subfinder..."




subfinder -d $domain -o domains

echo "${red}Probing for live hosts...  "

cat domains | httprobe | tee https-subs.txt



       

echo "${green}Spider and search for  vulnerability...  "
python3 zspider.py

