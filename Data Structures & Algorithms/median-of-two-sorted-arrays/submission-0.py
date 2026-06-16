class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1

        while True:
            m = (l + r) // 2 #A
            j = half - m - 2 #B

            Aleft = A[m] if m >= 0 else float("-infinity")
            Aright = A[m + 1] if (m + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # correct case
            if Aleft <= Bright and Bleft <= Aright:
                #odd
                if total % 2:
                    return min(Aright, Bright)
                
                return (max(Aleft, Bleft) + min(Aright, Bright))/2

            elif Aleft > Bright:
                r = m - 1
            else:
                l = m + 1



        