def romanToInt(self, s: str) -> int:
        sum = 0
        i = len(s) -1
        while i >= 0:
            curr_sum = 0
            char = s[i]
            
            if char == "I":
                curr_sum += 1
                if (i-1) >= 0 and s[i-1] == "I":
                    curr_sum += 1
                    if (i-2) >= 0 and s[i-2] == "I":
                        curr_sum += 1
                        i -= 3
                    else:
                        i -= 2
                else:
                    i -= 1
            
            elif char == "X":
                curr_sum += 10
                if (i-1) >= 0 and s[i-1] == "I":
                    curr_sum -= 1
                    i -= 2
                else:
                    i -= 1
                
            elif char == "V":
                curr_sum += 5
                if (i-1) >= 0 and s[i-1] == "I":
                    curr_sum -= 1
                    i -= 2
                else:
                    i -= 1
                    
            elif char == "L":
                curr_sum += 50
                if (i-1) >= 0 and s[i-1] == "X":
                    curr_sum -= 10
                    i -= 2
                else:
                    i -= 1
                
            elif char == "C":
                curr_sum += 100
                if (i-1) >= 0 and s[i-1] == "X":
                    curr_sum -= 10
                    i -= 2
                else:
                    i -= 1
                    
            elif char == "D":
                curr_sum += 500
                if (i-1) >= 0 and s[i-1] == "C":
                    curr_sum -= 100
                    i -= 2
                else:
                    i -= 1
                
            elif char == "M":
                curr_sum += 1000
                if (i-1) >= 0 and s[i-1] == "C":
                    curr_sum -= 100
                    i -= 2
                else:
                    i -= 1
                    
            sum += curr_sum
        return sum
