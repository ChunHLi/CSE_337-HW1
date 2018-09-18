import time;
from collections import defaultdict


def main():
    f = open("prices_sample.csv","r")
    f_contents = f.read()
    f_list = f_contents.splitlines()
    time_f_list = []
    for x in range(0,len(f_list)):
        tmp = f_list[x][:10]
        tmp = time.strftime("%Y-%m-%d %H:%M:S", time.localtime(int(tmp)))
        time_f_list.append(tmp.split())
    time_f_dict = defaultdict(list)
    for x in range(0,len(time_f_list)):
        time_f_dict[time_f_list[x][0]].append(time_f_list[x][1])
    nf = open("prices_sample_by_date","w+")
    for x in time_f_dict:
        nf_line = x + ": "
        for y in range(0,len(time_f_dict[x])):
            nf_line = nf_line + time_f_dict[x][y] + ", "
        nf_line = nf_line[:-2] + "\n"
        nf.write(nf_line)


if __name__ == "__main__":
    main()