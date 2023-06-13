from shodan import Shodan
import time
from datetime import date
import sys

sys.stdout = open("scan_results.txt", "a")
api = Shodan('<your_API_key_here>')


def assets_globally():
    global api
    ics = api.count("tag:ics")
    iot = api.count("tag:iot")
    database = api.count("tag:database")
    rdp = api.count("product:'Remote Desktop Protocol'")
    ftp = api.count("port:21")
    ftp_anon = api.count("port:21 '230 anonymous login ok'")
    ipcam = api.count("product:'IP camera'")
    indexof = api.count("http.title:'Index of /' 'HTTP/1.1 200 OK'")

    print("\nIT and OT Infrastructure Elements in Worldwide Range\n")

    print('Industrial Control Systems exposed to the internet globally: {:,}'.format(ics['total']))
    print('Internet of Things devices exposed to the internet globally: {:,}'.format(iot['total']))
    print('Databases exposed to the internet globally: {:,}'.format(database['total']))
    print('RDP connections exposed to the internet globally: {:,}'.format(rdp['total']))
    print('FTP servers exposed to the internet globally: {:,}'.format(ftp['total']))
    print('FTP servers with anonymous login globally: {:,}'.format(ftp_anon['total']))
    print('IP cameras exposed to the internet globally: {:,}'.format(ipcam['total']))
    print('Webserver with possibly accessible content globally: {:,}'.format(indexof['total']))


assets_globally()

time.sleep(3)


def assets_hungary():
    global api
    ics_hu = api.count("tag:ics country:HU")
    iot_hu = api.count("tag:iot country:HU")
    database_hu = api.count("tag:database country:HU")
    rdp_hu = api.count("product:'Remote Desktop Protocol' country:HU")
    ftp_hu = api.count("port:21 country:HU")
    ftp_anon_hu = api.count("port:21 '230 anonymous login ok' country:HU")
    ipcam_hu = api.count("product:'IP camera' country:HU")
    indexof_hu = api.count("http.title:'Index of /' 'HTTP/1.1 200 OK' country:HU")

    print("\n\nIT and OT Infrastructure Elements Filtered for Hungary\n")

    print('Industrial Control Systems exposed to the internet in HU: {:,}'.format(ics_hu['total']))
    print('Internet of Things devices exposed to the internet in HU: {:,}'.format(iot_hu['total']))
    print('Databases exposed to the internet in HU: {:,}'.format(database_hu['total']))
    print('RDP connections exposed to the internet in HU: {:,}'.format(rdp_hu['total']))
    print('FTP servers exposed to the internet in HU: {:,}'.format(ftp_hu['total']))
    print('FTP servers with anonymous login in HU: {:,}'.format(ftp_anon_hu['total']))
    print('IP cameras exposed to the internet in HU: {:,}'.format(ipcam_hu['total']))
    print('Webserver with possibly accessible Content in HU: {:,}'.format(indexof_hu['total']))


assets_hungary()

time.sleep(3)


def compromised_databases():
    global api
    databases_all = api.count("tag:database tag:compromised")
    elastic_compromised = api.count("product:elastic tag:compromised")
    mongo_compromised = api.count("product:MongoDB tag:compromised")
    mysql_compromised = api.count("product:mysql tag:compromised")
    postgres_compromised = api.count("product:postgresql tag:compromised")
    mssql_compromised = api.count("product:ms-sql tag:compromised")

    print("\n\nCompromised Popular Databases Worldwide\n")

    print('Total compromised DBs globally: {:,}'.format(databases_all['total']))
    print('Compromised Elastic DBs globally: {:,}'.format(elastic_compromised['total']))
    print('Compromised MongoDBs globally: {:,}'.format(mongo_compromised['total']))
    print('Compromised MySQL DBs globally: {:,}'.format(mysql_compromised['total']))
    print('Compromised PostgreSQL DBs globally: {:,}'.format(postgres_compromised['total']))
    print('Compromised MS-SQL DBs globally: {:,}'.format(mssql_compromised['total']))


compromised_databases()

time.sleep(3)


def compromised_databases_hu():
    global api
    databases_all_hu = api.count("tag:database tag:compromised country:HU")
    elastic_compromised_hu = api.count("product:elastic tag:compromised country:HU")
    mongo_compromised_hu = api.count("product:MongoDB tag:compromised country:HU")
    mysql_compromised_hu = api.count("product:mysql tag:compromised country:HU")
    postgres_compromised_hu = api.count("product:postgresql tag:compromised country:HU")
    mssql_compromised_hu = api.count("product:ms-sql tag:compromised country:HU")

    print("\n\nCompromised Popular Databases Filtered for Hungary\n")

    print('Total compromised DBs in HU: {:,}'.format(databases_all_hu['total']))
    print('Compromised Elastic DBs in HU: {:,}'.format(elastic_compromised_hu['total']))
    print('Compromised MongoDBs in HU: {:,}'.format(mongo_compromised_hu['total']))
    print('Compromised MySQL DBs in HU: {:,}'.format(mysql_compromised_hu['total']))
    print('Compromised PostgreSQL DBs in HU: {:,}'.format(postgres_compromised_hu['total']))
    print('Compromised MS-SQL DBs in HU: {:,}'.format(mssql_compromised_hu['total']))


compromised_databases_hu()

print("\n\n")

today = date.today()
d2 = today.strftime("%B %d, %Y")
print("Date of Sample:", d2)
print("-"*80)
