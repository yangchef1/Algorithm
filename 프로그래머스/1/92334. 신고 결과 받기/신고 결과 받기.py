def solution(id_list, report, k):
    report_dict = {}
    report_cnt = {}
    
    for r in report:
        a, b = r.split()
        rs = report_dict.get(a, set())
        if b not in rs:
            report_cnt[b] = report_cnt.get(b, 0) + 1
        rs.add(b)
        report_dict[a] = rs
    
    answer = [0] * len(id_list)
    for ru, v in report_cnt.items():
        if v >= k:
            for u, r in report_dict.items():
                if ru in r:
                    answer[id_list.index(u)] += 1
    return answer