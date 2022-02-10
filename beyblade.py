# import pdb
# def main(T, N, P, P_o):
#     # T = input()
#     # N = input()
#     # P = input()
#     # P_o = input()
#     pdb.set_trace()
#     if T in range(1, 100000) and N in range(1, 100000) and int(P):
#         P_grev = [x for x in P.split()]
#         P_opp = [x for x in P_o.split()]
#         i == 0
#         for x in P_grev and y in P_opp:
#             if x > y:
#                 i += 1
#         print(i)
 # Write code here 
# import pdb
# def main(T, N, P, P_o):
    # T = input()
    # N = input()
    # P = input()
    # P_o = input()
    # pdb.set_trace()
    #if T in range(1, 100000) and N in range(1, 100000) and int(P):
    # pdb.set_trace()
    # P_grev = sorted([int(x) for x in P.split()])[::-1]
    # P_opp = sorted([int(x) for x in P_o.split()])[::-1]
    # j = 0
    # for i in P_grev:
    #     L = [i-x for x in P_opp]
        # for y in range(len(L)):
        #     if L[y] == 0:
        #         L.pop(y)
        #         L.append(0)
        # if L:
        #     if max(L) > 0:
                # print(f"min of L is {min([q for q in L if q > 0])}")
                # print(f"max L is {max(L)}")
                # print(f"G_rev : {P_grev}")
                # print(f"P_opp : {P_opp}")
                # print(f"L     : {L}")
                # print(f"i     : {i}")
                # print("==============================")
        #         P_opp.pop(L.index(min([q for q in L if q > 0])))
        #         L.pop(L.index(min([q for q in L if q > 0])))
        #         # P_grev.pop(L.index(min([q for q in L if q > 0])))
        #         j += 1
        # else: 
        #     print("i'll decide later")

    # i = 0
    # x = 0
    # j = 0
    # while i < len(P_opp):
    #     while P_grev[i] < P_opp[x]:
    #         x += 1
    #         i += 1
    #     else:
    #         j += 1
    #         P_opp.remove(P_opp[x])
    #         P_grev.remove(P_grev[i])
            
#     print(j)

# main("1", "10", "3 6 7 5 3 5 6 2 9 1", "2 7 0 9 3 6 0 6 2 6 ")


def main(T, N, P, P_o):
    T = int(input())
    r = 1
    while r <= T:
        # T = int(input())
        N = input()
        P = input()
        P_o = input()
        P_grev = sorted([int(x) for x in P.split()])[::-1]
        P_opp = sorted([int(x) for x in P_o.split()])[::-1]
        j = 0
        for i in P_grev:
            L = [i-x for x in P_opp]
            if max(L) > 0:
                P_opp.pop(L.index(min([q for q in L if q > 0])))
                L.pop(L.index(min([q for q in L if q > 0])))
                j += 1
        print(j)
        r += 1
main(1, "10", "3 6 7 5 3 5 6 2 9 1", "2 7 0 9 3 6 0 6 2 6 ")