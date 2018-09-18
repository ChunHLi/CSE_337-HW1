import statistics
import time
from collections import defaultdict
from collections import OrderedDict


# q2.py


def main():
    f = open("prices_sample.csv","r")
    f_contents = f.read()
    f_list = f_contents.splitlines()
    date_price_f_dict = defaultdict(list)
    for x in range(0,len(f_list)):

        tmp_price = int(f_list[x][11:])
        tmp_date = f_list[x][:10]
        tmp_date = time.strftime("%Y-%m-%d %H:%M:S", time.localtime(int(tmp_date)))
        tmp_date = tmp_date[:10]
        date_price_f_dict[tmp_date].append(tmp_price)

    sortedKeys = sorted(date_price_f_dict)
    
    week_dict = defaultdict(list)
    i = 7
    sunday = ""
    for x in sortedKeys:
        if i == 7:
            i = 0
            sunday = x
        week_dict[sunday] += date_price_f_dict[x]
        i += 1
    
    nf = open("weekly_prices_sample.csv","w+")
    for x in week_dict:
        Max = max(week_dict[x])
        Min = min(week_dict[x])
        Mean = statistics.mean(week_dict[x])
        newline = x+","+str(Max)+","+str(Min)+","+str(Mean) + "\n"
        nf.write(newline)



if __name__ == "__main__":
    main()