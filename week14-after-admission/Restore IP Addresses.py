class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.ips = []
        self.generate([], s)
        return self.ips

    
    def generate(self, partial_ip, remaining):
        if len(partial_ip) > 4:
            return 
        elif remaining=="" and len(partial_ip) < 4:
            return
        elif remaining == "":
            valid_ip = ".".join(partial_ip)
            self.ips.append(valid_ip)
            return

        for i in range(1, len(remaining)+1):
            chunk = remaining[:i]
            leading_zeros = chunk[0] == "0" and len(chunk)>1
            in_range = 0<= int(chunk) <= 255

            if not leading_zeros and in_range:
                partial_ip.append(chunk)
                self.generate(partial_ip, remaining[i:])
                partial_ip.pop()
            
