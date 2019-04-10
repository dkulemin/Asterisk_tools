with open('contacts.txt') as fin:
    with open('output.txt', 'w') as fout:
        for line in fin:
            tmp = line.split('@')
            #print('Export-CsUserData -PoolFqdn "lyncpool02-17.utmn.ru" -FileName "C:\\1\\{0}.zip" -UserFilter {1}'.format(tmp[0], line.strip()), file=fout)
            print('Update-CsUserData -Filename "C:\\1\\{0}.zip" -UserFilter {1} -Force'.format(tmp[0], line.strip()), file=fout)
            #print('\t\t\t\t\t<Contact Buddy="{0}" SubscribePresence="1" Groups="1 3" />'.format(line.strip()), file=fout)
