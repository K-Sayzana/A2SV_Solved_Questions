class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        count_dom=defaultdict(int)
       
        for domainCount in cpdomains:
            count, domain=domainCount.split()
            domains=domain.split('.')
            domains.reverse()

            for i in range(1, len(domains)+1):
                line=".".join(reversed(domains[:i]))
                count_dom[line]+=int(count)
        
        res=[]

        for k, v in count_dom.items():
            res.append(str(v) + " "+ k)
        

        return res

      
        




