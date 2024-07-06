import dns.resolver

domain = 'sinegy.com' #'google.com'

#answers = dns.resolver.resolve(domain,'A')
#for server in answers:
    #print(server.target)

resolver = dns.resolver.Resolver()
answers = resolver.query(domain, 'A')
_ = [ print(answer.to_text()) for answer in answers]

wawa = [ answer.to_text() for answer in answers]
print(wawa)
