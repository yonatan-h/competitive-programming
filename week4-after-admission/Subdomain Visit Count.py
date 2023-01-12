class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        sub_domain_count_map = get_sub_domain_count_map(cpdomains)
        return get_count_paired_array(sub_domain_count_map)
        
        

def get_count_paired_array(sub_domain_count_map):
    count_paired_array = []
    for sub_domain in sub_domain_count_map:
        count = sub_domain_count_map[sub_domain]
        
        count_paired_domain = str(count) + " "+ sub_domain
        count_paired_array.append(count_paired_domain)
    
    return count_paired_array
        
        

def get_sub_domain_count_map(count_paired_domains):
    sub_domain_count_map = defaultdict(int)
    
    for count_pair_domain in count_paired_domains:
        count, domain = count_pair_domain.split(" ")
        
        sub_domains = get_sub_domains(domain)
        count = int(count)
        
        for sub_domain in sub_domains:
            sub_domain_count_map[sub_domain] += count
    
    return sub_domain_count_map
        
#1sub
#40min

def get_sub_domains(domain):
    parts = deque(domain.split("."))
    
    sub_domains = []
    while parts:
        sub_domain = ".".join(parts)
        sub_domains.append(sub_domain)
        parts.popleft()
        
    
    return sub_domains
        
