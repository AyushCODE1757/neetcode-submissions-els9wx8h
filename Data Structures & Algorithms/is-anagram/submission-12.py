class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) < len(t):
            return self.isAnagram(t, s)
        sfreq = Counter(s)
        tfreq = Counter(t)
        for s in sfreq:
            if s not in tfreq:
                return False
            if sfreq[s] != tfreq[s]:
                return False
        return True