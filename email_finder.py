# Email Hunter program developed with Hunter API Wrapper
# Requirement(package needs to be installed): pip install punter
# Supported versions: Python 2.7.x versions


from punter import search     # A Python wrapper for the Email Hunter API.

domain=raw_input("Enter the domain name: ")     # Target Domain name to search

print "Please...Wait. Process is running........\n"

# Exception hadling
try:
      email_search=search("78b2223fda0a178e2ef1f596916104a88e346cd3",domain,type='personal')        # Trying to retrieve Personal Email IDs
      email_list=email_search["emails"]
      personal_emails=[]
      for email in email_list:
           personal_emails.append(email['value'])
except:
      personal_emails=[]
      print "No Email IDs were found...\n"                                                # If no records retrieved
try:
      email_search=search("78b2223fda0a178e2ef1f596916104a88e346cd3",domain,type='generic')         # Trying to retrieve Generic Email IDs
      email_list=email_search["emails"]
      generic_emails=[]
      for email in email_list:
           generic_emails.append(email['value'])
except:
      generic_emails=[]
      print "No Email IDs were found...\n"                                                # If no records retrieved

# Printing the results
print "Personal Email IDs....\n============================="

for ids in personal_emails:
      print ids


print "\nGeneric Email IDs....\n============================"

for ids in generic_emails:
      print ids


