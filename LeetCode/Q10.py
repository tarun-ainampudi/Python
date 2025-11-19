class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p=='.*':
            print(1)
            return True
        elif '.*' in p:
            print(20)
            sp = 0
            pp = 0
            news = ''
            newp = ''
            if p[0] == '.' and p[1] == '*':
                print(201)
                while(p[2]!=s[sp] and sp<len(s)-1):
                    sp+=1
                print(s[sp:],p[2:])
                return self.isMatch(s[sp:],p[2:])
            else:
                print(202)
                return self.isMatch(s,p.replace('.*',''))


        if "*" in p:
            print(2)
            if p[-1]  == '*':
                print(3)
                i = len(s)-1
                while(p[-2] == s[i] and i>0):
                    i-=1
                if(p[-2] in s):
                    print(4)
                    return self.isMatch(s[:i+1],p[:-1])
                else:
                    print(5)
                    return True
            else:
                print(6)
                sp = 0
                pp = 0
                news = ''
                newp = ''
                while(pp<len(p) and sp<len(s)):
                    print(news,newp)
                    print(pp,sp)
                    if(pp+1<len(p) and p[pp+1] =='*'):
                        if pp == 0 :
                            pp+=2
                        else:
                            pp+=1
                        continue
                    elif s[sp] == p[pp]:
                        news += s[sp]
                        newp += p[pp]
                        sp+=1
                    elif p[pp] == '*':
                        print(p[pp-1])
                        while(p[pp-1]==s[sp] and sp<len(s)-1):
                            sp+=1 
                    elif s[sp] != p[pp] and p[pp] == '.' :
                        newp += p[pp]
                    pp+=1
                while(pp<len(p)):
                    if(pp+1<len(p) and p[pp+1] =='*'):
                        pp+=2
                        continue
                    newp += p[pp]
                    pp+=1
                while(sp<len(s)):
                    news += s[sp]
                    sp+=1
                print(news,newp)
                print(self.isMatch(news,newp))
                return self.isMatch(news,newp)
                # print(6)
                # cmli = p.split('*')
                # sli = []
                # pli = []
                # sp = 0
                # ep = 0
                # print(cmli,"cmli")
                # if cmli[-1] == '':
                #     print(7)
                #     for j in range(len(cmli)-1):
                #         ep+=len(j)
                #         sli.append(s[sp:ep])
                #         pli.append(j+"*")
                #         sp = ep
                # else:
                #     print(8)
                #     for j in range(len(cmli)-1):
                #         ep+=len(cmli[j])
                #         sli.append(s[sp:ep])
                #         pli.append(cmli[j]+"*")
                #         sp = ep
                #     ep+=len(cmli[-1])
                #     sli.append(s[sp:ep])
                #     pli.append(cmli[-1])
                # print(sli,pli)
                # for i in range(len(sli)):
                #     if not self.isMatch(sli[i],pli[i]):
                #         return False
                # return True
        elif "." in p:
            print(9)
            if p=='.':
                return len(s)==1
            elif p[-1]  == '.':
                print(13)
                if p[-2] == s[-2]:
                    print(14)
                    return self.isMatch(s[:-1],p[:-1])
                else:
                    print(15)
                    return False
            else:
                print(16)
                sp = 0
                pp = 0
                news = ''
                newp = ''
                while(pp<len(p) and sp<len(s)):
                    print(news,newp)
                    if s[sp] == p[pp]:
                        news += s[sp]
                        newp += p[pp]
                        sp+=1
                    elif p[pp] == '.':
                        sp+=1 
                    elif s[sp] != p[pp]:
                        newp += p[pp]
                    pp+=1
                while(pp<len(p)):
                    newp += p[pp]
                    pp+=1
                while(sp<len(s)):
                    news += s[sp]
                    sp+=1
                print(news,newp)
                print(self.isMatch(news,newp))
                return self.isMatch(news,newp)
            

        else:
            print(17)
            if s==p:
                return True
            else:
                return False

                     

                    
        
        
        
sol = Solution()
print(sol.isMatch("aab","c*a*b")) # True
# print(sol.isMatch("mississippi","mis*is*p*.")) # False  # False
# print(sol.isMatch("ab",".*")) # True                                                                                                    
# print(sol.isMatch("ab",".*c")) # False
# print(sol.isMatch("mississippi","mis*is*ip*.")) # True