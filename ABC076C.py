import io
import sys


# input here
_INPUT = """\
?tc????
coder
"""
sys.stdin = io.StringIO(_INPUT)


def main():
    s2 = input()
    t = input()

    s2_r = s2[::-1]
    t_r = t[::-1]

    ans_flag = False
    # 全文字の組み合わせを試す
    for i in range(len(s2)):
        for j in range(i+1, len(s2)+1):
            # tと同じ文字数の時だけ部分一致するか判定する
            if (j-i) == len(t_r):
                flag = True
                # 一文字ごとに判定する
                for k, l in enumerate(range(i, j)):
                    if s2_r[l] != t_r[k] and s2_r[l] != '?':
                        flag = False
                if flag == True:
                    # 一致した位置を置換
                    ans = s2_r[:i] + t_r + s2_r[j:]
                    # 残りの?を辞書順最小のaに置換
                    ans = ans.replace('?', 'a')
                    # 元の順番に反転
                    ans = ans[::-1]
                    print(ans)
                    ans_flag = True

    # s2 = s2[::-1]
    # t = t[::-1]

    # for i in range(len(s2)):
    #     for j in range(i+1, len(s2)):
    #         if (j-i) == len(t):
    #             flag = True

    #             for k, l in enumerate(range(i, j)):
    #                 if s2[l] != t[k] and s2[l] != '?':
    #                     flag = False
    #             if flag:
    #                 res = s2[:i] + t + s2[j:]
    #                 res = res.replace("?", "a")
    #                 res = res[::-1]
    #                 print(res)
    #                 return

    print('UNRESTORABLE')


if __name__ == "__main__":
    main()
